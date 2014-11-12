
TODO: Explicar context

TODO: Baixar les imatges que toquen

TODO: Instal·lar TFTP

## Pujar la imatge

- Connecta el portàtil a connector 'LAN' del PoE
- Connecta el RJ45 etiquetat 'PoE' del PoE al RJ45 amb etiqueta 'Main' de l'antena.
- Desconnecta l'antena com et vagi millor per reconnectar-la després
	- Si la tens connectada amb un endoll amb interruptor
	- Desendollant el cable d'alimentació del PoE
	- Desconectant RJ45 que va del PoE a l'antena
- Pressiona amb un clip el botó que hi ha al forat de darrera del PoE
	- A l'antena tambe té un botó de reset al costats dels RJ45 que fa el mateix
- Torna a engegar l'antena sense alliberar el boto de reset
- I espera a que els leds de nivell de wifi s'alternin intermitentment (~18s)
- En aquest moment hem posat l'antena en mode TFTP per aceptar una imatge a flashejar

- La antena en aquest mode té l'adreça 192.168.1.20 pero no dona DHCP
- Per poder accedir-hi, posem l'ordinador amb una ip statica de la xarxa 192.168.1.X
- Canviant el nom de la imatge el procediment seria:

	$ tftp 192.168.1.20
	tftp> bin
	tftp> trace
	tftp> put NanoStationM5-XW-qMp_kalimotxo-factory-20141105_1622.bin
	tftp> quit

- Quan acabi de fer pampallugues els leds podem accedir a http://192.168.1.20  root 13f

TODO: Coses que poden anar malament

## Configuració bàsica (agafar internet d'altres antenes)


- A les versions noves (novembre 2014) per cambiar del menu qmp al menu administracio, els botons estan abaix de tot.
- Canviar la contrasenya a Administration/System/Administration/Router Password
	- Nota: amb return no hi ha prou, ves avall i dona-li a "Save & Apply"
- qMp/Node configuration/qmp Easy SetUp
	- En principio solo hay que cambiar la IP de MESH
	- Network Mode: Roaming
	- IP address: La que toqui a la zona mesh
	- Interface Modes:
		eth0.2: wan
		eth0.1: lan
		wlan: mesh
	- Save and Apply
- qMp/Node configuration/Basic Settings
	- Node name: GuifiBaix-Proves   (o el de la zona mesh que toque)
	- Latitude: el primer numero del expediente.coords
	- Longitude: el segundo numero del expediente.coords
	- Altitude: Calcular aproximado segun el numero de pisos
	- Contacte: nodes at guifibaix.coop
	- Save and Apply
- qMp/Node configuration/Wireless Settings
	- Country code: ES
	- BSSID: 02:CA:FF:EE:BA:BE (es el que pone por defecto)
	- Channel: 140-  (el - es importante)
	- Power: 17dB (se puede ajustar a mas o menos si vamos teniendo buena señal)
	- Save and Apply
- qMp/Mesh/Configuration/Advanced
	- tunOutTimeout: 0 (por defecto estaria en blanco)
	- Save and Apply
- Hay un bug que vuelve a vaciar el tunOutTimeout cada vez que reiniciamos la antena.
  Desde el portatil ejecutamos el siguiente 

	$ ssh root@172.30.22.1  '(crontab -l; echo '\''* */1 * * bmx6 --runtimeDir /var/run/bmx6 -c -p | grep tunOutTime && echo Parameter tunOutTimeout already set  || (echo Setting tunOutTimeOut; bmx6 --runtimeDir /var/run/bmx6 -c --tunOutTimeout 0)'\'') | crontab - && echo done || echo failed' 


## Si tenemos connectividad con los servidores de Sant Joan Despí

Hay que reconfigurar los DNS locales para poder acceder a los servicios adicionales.

- qMp/Node configuration/Network Settings/Advanced network Settings
	- DNS Nameservers: 10.1.40.8 10.1.40.7 10.1.40.132
		- Por defecto apuntarian a los de opendns:
			- 208.67.222.222 208.67.220.220 209.244.0.3
	- Si la antena da DHCP a los clientes directamente, para que el DNS Forwarding funcione, desde el meu de OpwenWRT > Network > DHCP and DNS, deshabilitar las opciones "Domain Required" y "Rebind Protection", además de añadir la lista de los servidores DNS a los cuales realizaremos el forward de las peticiones DNS.
	
	- Nota: Revisar, no funciona
		- Tampoco configurando en Administration/Network/DHCP and DNS/DNS Forwardings
		- Ambos funcionan desde la antena, pero la antena por DHCP da de DNS ella
		- Tampoco configurandolo en Administration/Network/Interfaces/LAN/Use Custom DNS servers
		- Tampoco configurandolo en Administration/Network/Interfaces/LAN/DHCP/DHCP Options


## Si queremos que la antena ofrezca internet

- qMp/Node Configuration/Easy Setup
	- eth0.2 Wan -> Lan
	- eth0.1 Lan -> Wan
	- Nos aseguramos mucho de que todo es correcto porque podemos perder la antena por cable
	- Save and Apply
- Connectem el cable del portatil que teniem al 'Lan' del PoE, ara a 'Secondary' de l'antena
- Ens hauria de donar DHCP a la xarxa




## Si queremos establecer un tunel















