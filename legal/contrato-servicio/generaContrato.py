#!/usr/bin/python3
# -*- coding: utf-8 -*-

# Dependencias Ubuntu:
# sudo apt-get install pandoc texlive-lang-spanish pdftk
# sudo pip3 install pypandoc

import sys, os
import argparse, datetime

def sourceRelative(path) :
	"""Returns files relative this source"""
	return os.path.join(
		os.path.dirname(
		os.path.relpath(
			__file__, os.curdir)), path)


def parseDate(v) :
	import re
	if not re.match('^20[0-9][0-9]-(0[1-9]|10|11|12)-[0-3][0-9]$', v) :
		raise ValueError
	year, month, day = (int(x) for x in v.split('-'))
	if day<1 or day > 31 : raise ValueError
	return year, month, day

def isodate(value) :
	try : return parseDate(value)
	except ValueError: raise argparse.ArgumentError()
	
parser = argparse.ArgumentParser(
	description="Genera el contracte de servei de GuifiBaix")
parser.add_argument(
	'user',
		help='YAML file containing user personal info',
		metavar='USER.yaml'
	)
parser.add_argument(
	'provider',
		help='YAML file containing provider info',
		nargs='?',
		metavar='PROVEEDORA.yaml'
	)
parser.add_argument(
	'--md',
		action='store_true',
		dest='generateMarkdown',
		help='Dumps intermediate markdown content on stderror.',
	)
parser.add_argument(
	'-o', '--output',
		dest='output',
		help='specifies an output file. '
			'Format is deduced from the  extension. '
			'If not specified, markdown is dumped on stdout',
		metavar='OUTPUT',
	)
parser.add_argument(
	'-d', '--data',
		dest='data',
		type=isodate,
		help='Contract date in ISO format YYYY-MM-DD',
		default=parseDate(datetime.date.today().isoformat()),
		metavar='ISODATE',
	)
args = parser.parse_args()

from yamlns import namespace as ns

female = ns(
	quotedElCliente = "la \"CLIENTA\"",
	cliente = "CLIENTA",
	elCliente = "la CLIENTA",
	delCliente = "de la CLIENTA",
	ELCLIENTE = "LA CLIENTA",
	ElCliente = "La CLIENTA",
	alCliente = "a la CLIENTA",
	DelCliente = "De la CLIENTA",
	AlCliente = "A la CLIENTA",
	)

male = ns(
	quotedElCliente = "el \"CLIENTE\"",
	cliente = "CLIENTE",
	elCliente = "el CLIENTE",
	delCliente = "del CLIENTE",
	ELCLIENTE = "EL CLIENTE",
	ElCliente = "El CLIENTE",
	alCliente = "al CLIENTE",
	DelCliente = "Del CLIENTE",
	AlCliente = "Al CLIENTE",
	)

proveedora = ns.load(args.provider) if args.provider else ns(
	name = "GUIFIBAIX SCCL",
	nif = "F66576380",
	contact = ns(
		phone = [
			"93-164-0492",
		],
		email = [
			"contacto@guifibaix.coop",
			"soporte@guifibaix.coop",
		],
	),
	email = "soporte"+ "@" + "guifibaix.coop",
	emailcontacto = "contacto"+"@"+"guifibaix.coop",
	address = "C/Major 22, 3",
	city = "Sant Joan Despí",
	postalcode = '08970',
	proxy = ns(
		name = "David García Garzón",
		nif = "36517097C",
		genre = male,
	),
)


meses="enero febrero marzo abril mayo junio julio agosto septiembre octubre noviembre diciembre".split()
data = ns(
	fecha = ns(
		any = args.data[0],
		mes = meses[args.data[1]-1],
		dia = args.data[2],
		),
	lugar = "Sant Joan Despí",
	client = ns.load(args.user),
	proveedor = proveedora,
)

data.genre = female if data.client.genre.lower() == 'female' else male
data.imagepath = sourceRelative('')


with open(sourceRelative("00-content.md"),encoding="utf8") as f :
	template = f.read()
filled = template.format(**data)

if args.generateMarkdown :
	print(filled)
	sys.exit(0)

outputfile = args.output or (
	"contrato-guifibaix-{}-{}-{}.pdf".format(
		datetime.date(*args.data).isoformat(),
		data.client.nif,
		''.join(data.client.name.split())
	))

import pypandoc
pypandoc.convert(filled,
	format='markdown',
	to='latex',
	extra_args=[
		'-o', outputfile,
		'--template',sourceRelative('default.latex'),
		]
	)

if __name__ == '__main__' :
	pass


