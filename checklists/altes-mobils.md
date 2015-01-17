
- Es demana al client si el seu mobil és lliure. Si no ho es:
	- El client ha de sol·licitar codi d'alliberament a l'actual proveidor
		- Li demanaran l'IMEI que s'obte prement *#06#a
		- Alguns proveidors tenen condicions (acabar la permanència, primer any...)
	- O alternativament podria adquirir un terminal lliure
- Tipus de tarja SIM del telefon: Normal, Micro o Nano
- ¿Va a necesitar MULTISIM? (Mas de una sim con el mismo numero?)
- ¿Va a necesitar numeración corta? (Solo para empresas)
	Unificación de la telefonía móvil y fija mediante una numeración corta.
	Por ejemplo, extensión fija 4800 y extensión móvil 5800.
- Se pide a los clientes:
	- Dades:
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
			- ...
		- simType: # Normal, Micro o Nano
		- multisim: # True/False - Mas de una sim con el mismo numero?
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
- S'envia tota la info a nubip demanant a nubip que ens avisi a nosaltres i als clients
- Nubip eventualment ens notifica la finestra de portabilitat
- Avisem als clients
	- Explicar com funciona tot durant la finestra de portabilitat (TODO: Aclarar-ho amb Nubip)


