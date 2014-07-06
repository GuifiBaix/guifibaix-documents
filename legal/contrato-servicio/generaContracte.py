#!/usr/bin/python3
# -*- coding: utf-8 -*-

import sys
import argparse, datetime

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
	'--user-template',
	action='store_true',
	dest='userTemplate',
	help='dumps a template for a user YAML file on standard output',
	)
parser.add_argument(
	'user',
	help='YAML file containing user personal info',
	nargs='?',
	metavar='USER.yaml')
parser.add_argument(
	'provider',
	help='YAML file containing provider info',
	nargs='?',
	metavar='PROVEEDORA.yaml')
parser.add_argument(
	'-o', '--output',
	dest='output',
	help='specifies an output file. '
		'Format is deduced from the  extension. '
		'If not specified, markdown is dumped on stdout',
	metavar='OUTPUT')
parser.add_argument(
	'-d', '--data',
	dest='data',
	type=isodate,
	help='Contract date in ISO format YYYY-MM-DD',
	default=parseDate(datetime.date.today().isoformat()),
	metavar='ISODATE')
args = parser.parse_args()

class conf(dict) :
	def __init__(self, *args, **keyw) :
		super(conf,self).__init__(*args, **keyw)
		self.__dict__ = self

	@classmethod
	def wrap(cls, data) :
		if type(data) is dict :
			return conf({
				k: cls.wrap(v)
				for k,v in data.items()
				})
		return data

	@classmethod
	def load(cls, filename) :
		import yaml
		result = cls.wrap(yaml.load(stream=open(filename)))
		return result

if args.userTemplate :
	print("""\
nombre: Pepe Gotera
dni: 12345678A
telefono: 93-111-2222
email: email@usuario.coop
genero: masculino
domicilio:
    direccion: C/Rue Percebe, 13, 4o 3a
    municipio: Sant Joan Despí
    codigopostal: 08970
""")
	sys.exit()


femenino = conf(
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

masculino = conf(
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

proveedora = conf.load(args.provider) if args.provider else conf(
	nombre = "AT2, Acció Transversal per la Transformació Social",
	cif = "G64922131",
	telefono = "93-164-0492",
	email = "soporte"+ "@" + "guifibaix.coop",
	emailcontacto = "contacto"+"@"+"guifibaix.coop",
	domicilio = conf(
		direccion = "C/Riu Llobregat, 47, Bxos",
		municipio = "El Prat de Llobregat",
		codigopostal = '08820',
	),
	representante = conf(
		nombre = "Paco Ibàñez",
		dni = "52623709P",
		genero = masculino,
		cargo = "Dibujante oficial de AT2",
	),
)


meses="enero febrero marzo abril mayo junio julio agosto septiembre octubre noviembre diciembre".split()
vars = conf(
	fecha = conf(
		any = args.data[0],
		mes = meses[args.data[1]-1],
		dia = args.data[2],
		),
	lugar = "Sant Joan Despí",
	cliente = conf.load(args.user),
	proveedor = proveedora,
)

vars.genero = femenino if vars.cliente.genero.lower() == 'femenino' else masculino


with open("00-content.md") as f :
	template = f.read()
filled = template.format(**vars)

if args.output :
	import pypandoc
	pypandoc.convert(filled,
		format='markdown',
		to='latex',
		extra_args=[
			'-o', args.output,
			'--template','default.latex',
			]
		)
else :
	print(filled)

if __name__ == '__main__' :
	pass


