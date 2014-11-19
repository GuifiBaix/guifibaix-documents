TODO: Explicar context

## Instal·lar el programari requerit

Per configurar una antena cal un navegador, un client ssh i un client tftp.

En Ubuntu:

	$ sudo apt-get install tftp openssh-client


## Seleccionar i baixar la imatge a instal·lar

Les darreres imatges que hem testejat son:

Per a les XW (fabricació 2014 o posterior):
- http://fw.qmp.cat/kalimotxo/NanoStationM5-XW-qMp_kalimotxo-factory-20141105_1622.bin  (configuració de fabrica)
- http://fw.qmp.cat/kalimotxo/NanoStationM5-XW-qMp_kalimotxo-sysupgrade-20141105_1622.bin (actualització, mantenint configuració)

Per a les velles:
- http://fw.qmp.cat/kalimotxo/NanoStationM5-qMp_kalimotxo-factory-20141105_1617.bin (configuració de fabrica)
- http://fw.qmp.cat/kalimotxo/NanoStationM5-qMp_kalimotxo-sysupgrade-20141105_1617.bin (actualització, mantenint configuració)

A GuifiBaix guardem les imatges que anem provant i funcionen,
perquè a http://fw.qmp.cat van esborrant les imatges antigues
i sovint passa que les que hi ha pujades no funcionen.

- http://fw.guifibaix.net (TODO: No està funcionant encara)

Si cal escollir una imatge nova de qmp.cat:

### Testing, experimental o kalimotxo

- De moment estem fent servir les imatges de kalimotxo
- TODO: perque

### Model: NanoStationM5

- Ni M2, ni M4, ni LocoM5...

### XW o no

- Les noves NanoStationM5 (fabricades a partir del 2014) porten un chipset diferent, XW.
- Les imatges pel Xipset nou porten l'infix addicional 'XW'.
- TODO: Criteri per identificar les antenes XW.

### Factory o Sysupgrade

- Les ''factory'' son imatges complertes que serveixen per flashejar l'antena completament
- Les ''sysupgrade'' son imatges per actualitzar una antena ja flashejada mantenint la configuració existent
- Per instal·lar una antena nova necessitem la ''factory'', pero...
- Sempre que ens baixem una imatge ''factory'' de qmp.cat, baixem també la ''sysupgrade'' corresponent, per si hem d'actualitzar la resta d'antenes a la mateixa versió.

### Guifi o no Guifi

- De moment NO farem servir les imatges que porten l'infix 'Guifi'
- TODO: Explicar que vol dir


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


## Si volem que l'antena ofrezca internet

TODO: No estem segurs de que aquesta configuració sigui la correcta, hem provat diverses a diferents llocs i han donat diferents resultats

- Alternativa 1: Configurar el port primari com WAN
	- Aquesta configuració requereix que el dispositiu de sortida a internet (Router ADSL) estigui donant DHCP
	- qMp/Node Configuration/Easy Setup
		- eth0.2 Wan -> Lan
		- eth0.1 Lan -> Wan
		- Nos aseguramos mucho de que todo es correcto porque podemos perder la antena por cable
		- Save and Apply
	- Connectem el cable del portatil que teniem al 'Lan' del PoE, ara a 'Secondary' de l'antena
	- En teoria, el port secundari ens donaria DHCP al portatil i el primari esperaria que el RouterADSL li dongues DHCP a la Antena

- Alternativa 2: LAN amb adreces estatiques
	- Mantenir la configuració Wan/Lan per defecte
	- Canviar la configuració de l'interficie primaria per que tingui
		- TODO: Confirmar on cal fer-ho: a Admin/Network/Interface/LAN es correcte i prou o on cal fer cada cosa
		- IP de la xarxa que dona sortida a internet, que no estigui dintre del rang DHCP que es reparteix al router
		- Desactivem el DCHP server
		- Default Gateway la IP del router
	- TODO: Altres passes que cal fer (NAT...)
	- TODO: Como hacer check para comprobar el gateway esta activo y dejar de ofrecerlo a qMp cuando se corte internet.



## Si volem establir un tunel d'administració

















