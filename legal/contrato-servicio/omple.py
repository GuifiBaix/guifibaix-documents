#!/usr/bin/python3

with open("00-content.md") as f :
	template = f.read()

class conf : 
	def __init__(self, **keyw) :
		for k,v in keyw.items() :
			setattr(self, k, v)


vars = conf(
	fecha = conf(
		año = 2014,
		mes = "febrero",
		dia = 20,
		),
	cliente = conf(
		nombre = "Alberto Gijón",
		dni = "12345678V",
		domicilio =  conf(
			dirección = "C/. Trece Rue Percebe, 34, 4o 3a",
			municipio = "Sant Pere de Rivas",
			codigopostal = "08970"
			),
		),
	proveedor = conf(
		nombre = "AT2, Acció Transversal per la Transformació Social",
		cif = "G123345566",
		domicilio = conf(
			dirección = "C/. Trece Rue Percebe, 34, 4o 3a",
			municipio = "Sant Pere de Rivas",
			codigopostal = '23414',
			),
		representante = conf(
			nombre = "Alberto Gijón",
			dni = "12345678C",
			),
		),
)


print ( template.format(**vars.__dict__) )






