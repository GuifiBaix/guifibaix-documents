#!/usr/bin/python3
# -*- coding: utf-8 -*-

import sys

with open("00-content.md") as f :
	template = f.read()

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


dummyEve = conf(
	nombre = "Alberta Gijón",
	dni = "12345678V",
	telefono = "93-111-2222",
	email = "email@usuario.test",
	domicilio =  conf(
		direccion = "C/Rue Percebe, 13, 4o 3a",
		municipio = "Sant Joan Despí",
		codigopostal = "08970"
		),
	genero = femenino,
	)


def load(filename) :
	import yaml, sys
	result = conf.wrap(yaml.load(stream=open(filename)))
	return result



vars = conf(
	fecha = conf(
		any = 2014,
		mes = "febrero",
		dia = 20,
		),
	lugar = "Sant Joan Despí",
	cliente = load(sys.argv[1]),
	proveedor = conf(
		nombre = "AT2, Acció Transversal per la Transformació Social",
		cif = "G64922131",
		telefono = "93-164-0492",
		email = "soporte"+ "@"+ "guifibaix.coop",
		emailcontacto = "contacto"+ "@"+ "guifibaix.coop",
		domicilio = conf(
			direccion = "C/Riu Llobregat, 47, Bxos",
			municipio = "El Prat de Llobregat",
			codigopostal = '08820',
			),
		representante = conf(
			nombre = "Ramón Álvarez",
			dni = "12345678C",
			),
		),
)

vars.genero = femenino if vars.cliente.genero.lower() == 'femenino' else masculino

print ( template.format(**vars) )




