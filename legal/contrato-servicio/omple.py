#!/usr/bin/python3
# -*- coding: utf-8 -*-

with open("00-content.md") as f :
	template = f.read()

class conf : 
	def __init__(self, **keyw) :
		for k,v in keyw.items() :
			setattr(self, k, v)


vars = conf(
	fecha = conf(
		any = 2014,
		mes = "febrero",
		dia = 20,
		),
	periodo = "un año",
	cliente = conf(
		nombre = "Alberto Gijón",
		dni = "12345678V",
		telefono = "93-111-2222",
		email = "email@usuario.test",
		domicilio =  conf(
			direccion = "C/Rue Percebe, 13, 4o 3a",
			municipio = "Sant Joan Despí",
			codigopostal = "08970"
			),
		),
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


print ( template.format(**vars.__dict__) )






