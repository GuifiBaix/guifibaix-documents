
- Conecta el dispositivo a una red con DHCP
- Ver la IP que se le ha dado, mirar la MAC que corresponda con la de la caja
- Apuntamos el navegador a la IP
- Login 'admin'

- Basic Settins
	- Language: Spanish IVR (cambia las grabaciones del interfaz de voz a español)
- FXS Port:
	- Primary SIP Server: extensiones.nubip.com  (Nos lo pasan como 'dominio')
	- Outbound Proxy: 94.23.81.212:55698 (Nos lo pasan como 'proxy')
	- SIP Transport: UDP
	- NAT Traversal: STUN
	- SIP User ID: XXXXXX (Lo que nos pasen como 'user')
	- Authenticate ID: XXXXX (El mismo que nos pasan como 'user')
	- Authenticate Password: XXXXXXXX (Lo que nos pasan como 'pass')
	- Name: guifibaix-<idexpediente>
	- Lista Codecs: G729, PCMU, PCMA, G723, G726-32, iLBC (Hay que cambiar el orden importa)
		- Orden de negociacion del metodo de codificado de audio
		- Depende la calidad y el caudal utilizado
	- Jitter Buffer Type: Fixed
	- Jitter Buffer Length: High
		- Jitter es la variacion del tiempo de llegada de los fragmentos de sonido que se van enviando por internet
		- El buffer sirve para compensar esas diferencias acomulando los fragmentos y retrasando la salida por el altavoz
		- Si el buffer es adaptativo adapta su longitud al retardo detectado, no funciona bien asi que lo ponemos fijo y maxima longitud.
- Advanced:
	- Password: Se cambia y se aplica
	- STUN Server: stun.l.google.com:19302
	- Use STUN to detect network connectivity: Yes
- Status
	- Comprobar que:
		-  NAT:  Full Cone NAT (STUN)
- Conectar un telefono y llamar para comprobar cosas:
	- Si el numero que llama es el que toca
	- si hay microcortes
- Ya en el cliente
	- Comprobar llamar desde voip (igual que en guifibaix)
	- Comprobar tambien las llamadas entrantes cuando este la portabilidad






