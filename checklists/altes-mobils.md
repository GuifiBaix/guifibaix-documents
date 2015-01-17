
- Si el mòbil que te el client no es lliure
	- El client ha de sol·licitar codi d'alliberament a l'actual proveidor
		- Li demanaran l'IMEI que s'obte prement *#06#a
		- Alguns proveidors tenen condicions (acabar la permanència, primer any...)
	- Alternativament podria adquirir un terminal que ho fos
- Tipus de tarja SIM del telefon: Normal, Micro o Nano
- ¿Va a necesitar MULTISIM? (Mas de una sim con el mismo numero?)
- ¿Va a necesitar numeración corta? (Solo para empresas)
	Unificación de la telefonía móvil y fija mediante una numeración corta.
	Por ejemplo, extensión fija 4800 y extensión móvil 5800.
- Se pide a los clientes:
	- Datos:
		- name:
		- nif:
		- address:
		- city:
		- postalCode:
		- email:
		- phone:
		- iban/ccc:
	- Servei:
		- linesToPort:
		- multisim:
		- simType:
- S'envien les dades a Nubip demanant els contractes
- Nubip retorna els contractes emplenats
- Es demana als clients que ens enviin
	- Per cada titular de linia:
		- Fotocopia del DNI vigent dues cares
	- Si el titular es una empresa:
		- Fotocopia del DNI del representant
		- Fotocopia del CIF
		- Escrituras de apoderamiento (debe aparecer la persona titular del DNI, que será la misma que firme los contratos
	- Per cada titular de compte:
		- Mandat SEPA (Autorització bancària)
	- Per cada número:
		- Escan del Contracte de Servei signat
		- Escan del Contracte de Portabilitat signat

