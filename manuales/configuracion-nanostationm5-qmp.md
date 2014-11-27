TODO: Explicar context

## Instal·lar el programari requerit

Per configurar una antena cal un navegador, un client ssh i un client tftp.

En Ubuntu:

	$ sudo apt-get install tftp openssh-client


## Seleccionar i baixar la imatge a instal·lar

Les darreres imatges que hem testejat son:

TODO: Canviar a fw.guifibaix.coop quan estigui disponible

Per a les XW (fabricació 2014 o posterior):

- http://canvoki.net/fw/NanoStationM5-XW-qMp_kalimotxo-factory-20141105_1622.bin  (configuració de fabrica)
- http://canvoki.net/fw/NanoStationM5-XW-qMp_kalimotxo-sysupgrade-20141105_1622.bin (actualització, mantenint configuració)

Per a les velles:

- http://canvoki.net/fw/NanoStationM5-qMp_kalimotxo-factory-20141105_1617.bin (configuració de fabrica)
- http://canvoki.net/fw/NanoStationM5-qMp_kalimotxo-sysupgrade-20141105_1617.bin (actualització, mantenint configuració)

A GuifiBaix guardem les imatges que anem provant i funcionen,
perquè a http://fw.qmp.cat van esborrant les imatges antigues
i sovint passa que les que hi ha pujades no funcionen.

Si voleu provar una nova versió no testada:

- Aneu a http://fw.qmp.cat/kalimotxo
	- Encara que no les necessiteu, baixeu-vos les quatre versions: XW i no XW, factory/sysupgrade
		- XW (per antenes >= 2014), o sense XW (per antenes <2014)
		- factory (per instal·lacions inicials) i sysupgrade (per quan necessitem actualitzar la resta d'antenes a la mateixa versió mantenint la configuració)
	- Per NanostationM5 (ni M2 ni LocoM5)
	- SENSE l'infix 'Guifi'. No ens funciona.
	- Ara mateix funcionem amb la versió 'kalimotxo', pero això va canviant
- Total encara que només feu servir una, per que sigui útil pel grup cal baixar-se les quatre
	- Les imatges de qmp.cat
- Si les proveu i funcionen:
	- Pujeu-les al servidor
	- Si no teniu accés al servidor envieu-les a la llista d'**equip** amb `[firmware qmp]` al subject per que les pujin els companys

TODO: Criteris per identificar una XW

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

	```bash
	$ tftp 192.168.1.20
	tftp> bin
	tftp> trace
	tftp> put NanoStationM5-XW-qMp_kalimotxo-factory-20141105_1622.bin
	tftp> quit
	```

- Les llums de l'antena faran el cotxe fantàstic fins que actualitzi el firmware
- Un cop s'instala es reinicia un parell de vegades per reconfigurar-se,
	- Cal esperar fins que el DHCP ens doni una IP a 172.30.X.X
	- Si tens connexió automàtica (DCHP) es posible que durant aquestes reconfiguracions et doni IP en l'interval 192.168.1.X
		- Si passa això torna a reconnectar fins que et doni una IP bona a 172.30.X.X
- Un cop ens dona IP bona, connectar-se a http://172.30.22.1  root 13f

TODO: Coses que poden anar malament


## Configuració bàsica (agafar internet d'altres antenes)


- NOTA: A les versions noves (novembre 2014) l'opció per per cambiar entre el menu qmp y el menu administracio, està abaix de tot de cada pàgina.
- Canviar la contrasenya a Administration/System/Administration/Router Password
	- Nota: amb return no hi ha prou, ves avall i dona-li a "Save & Apply"
- qMp/Node configuration/qmp Easy SetUp
	- En principio solo hay que cambiar la IP de MESH
	- Network Mode: Roaming
	- IP address: La que toqui a la zona mesh
	- Interface Modes (Nuevas XW):
		- eth0.2: wan
		- eth0.1: lan
		- wlan: mesh
	- Interface Modes (Antiguas):
		- eth1: wan
		- eth0: lan
		- wlan: mesh
	- Save and Apply
- qMp/Node configuration/Basic Settings
	- Node name: GuifiBaix-Proves   (o el de la zona mesh que toque)
	- Latitude: el primer numero del expediente.coords
	- Longitude: el segundo numero del expediente.coords
	- Altitude: Calcular aproximado segun el numero de pisos
	- Contacte: nodes at guifibaix.coop
	- Save and Apply
- Hay un bug en algunas versiones (2014-11-05) en que no se guardan bien las coordenadas (concretamente la longitud)
	- Si que se guardan en `/etc/config/qmp` pero no en `/etc/config/libremap`
	- Entrar en la antena con `ssh root@172.30.22.1`
	- Copiamos el valor de un fichero a otro con:

		```bash
		$ sed -i 's/.*longitude.*/'"$(grep longitude /etc/config/qmp)"'/' /etc/config/libremap
		```

- qMp/Node configuration/Wireless Settings
	- Country code: ES
	- BSSID: 02:CA:FF:EE:BA:BE (es el que pone por defecto)
	- Channel: 140-  (el - es importante)
	- Power: 17dB (se puede ajustar a mas o menos si vamos teniendo buena señal)
	- Save and Apply
- Comprobar que a partir de aqui vemos a las otras antenas
	- Con esto configurado podremos conectarnos a la antena por radio si tocando los interfaces la perdemos
- qMp/Mesh/Configuration/Advanced
	- tunOutTimeout: 0 (por defecto estaria en blanco)
	- Save and Apply
- Hay un bug que vuelve a vaciar el tunOutTimeout cada vez que reiniciamos la antena.
  Desde el portatil ejecutamos el siguiente 

	```bash
	$ ssh root@172.30.22.1  '(crontab -l; echo '\''* */1 * * bmx6 --runtimeDir /var/run/bmx6 -c -p | grep tunOutTime && echo Parameter tunOutTimeout already set  || (echo Setting tunOutTimeOut; bmx6 --runtimeDir /var/run/bmx6 -c --tunOutTimeout 0)'\'') | crontab - && echo done || echo failed' 

	```

## Si estarà a la mateixa xarxa que els servidors de Sant Joan Despí

Si la antena estarà connectada als servidors de Sant Joan Despí convé configurar-la perque faci servir els DNS interns.
D'aquesta manera resoldrà adreces com http://mediateca.guifibaix.net, no disponibles als DNS convencionals.

- Per defecte els DNS que estan posats son els de opendns:
	- 208.67.222.222 208.67.220.220 209.244.0.3
- Els de GuifiBaix son:
	- 10.1.40.8 10.1.40.7 10.1.40.132

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

- Hay que configurar los cacharros internos para que quien acabe resolviendo dns sea la antena
- Si no hay posibilidad, hay que configurar los DNS de guifibaix contra mas lejos de los dispositivos finales posible
	- Antena
	- Router
	- Dispositivos


## Si volem que l'antena ofereixi Internet

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

- La antena ha de tenir connectivitat a Internet perque funcioni
- Suposem que la antena és 172.30.22.1 (no ho sera si s'accedeix via mesh)
- Copiem l'script de tunelat `crear_tunnels.sh` i li donem permisos

		```bash
		$ scp crear_tunels.sh root@172.30.22.1:/etc/
		$ ssh root@172.30.22.1 "chmod +x /etc/crear_tunels.sh"
		```

- Canviem els ports (777 establirà 77780 per luci i 77722 per ssh, de fet serian ports invalids)
	- De fet 777 genera ports invàlids, han d'estar entre 1024 i 65535
	- Aixi que les xifres superiors han d'anar entre 11 (1022 estaria fora)  i 654 (65588 estaria fora)

		```bash
		$ ssh root@172.30.22.1  'sed -i s/111/777/ /etc/crear_tunels.sh'
		```

- Ens copiem al portatil la clau publica de l'antena

	$ ssh root@172.30.22.1 "dropbearkey -y -f /etc/dropbear/dropbear_rsa_host_key | grep ssh-rsa" > /tmp/pubkey

- La fiquem com clau autoritzada al servidor de tunels.

	- Si estem a la xarxa de Sant Joan Despi

		$ ssh root@10.1.40.14 'echo "'$(cat /tmp/pubkey)'" >> /home/tunel/.ssh/authorized_keys

	- Si no hi som podem intentar fer-ho amb el dyndnsa

		```bash
		$ ssh root@tunel.guifibaix.coop -p 2222 'echo "'$(cat /tmp/pubkey)'" >> /home/tunel/.ssh/authorized_keys
		```

	- Para comprobar la lista de claves:

		```bash
		$ ssh root@10.1.40.14 'cat /home/tunel/.ssh/authorized_keys'
		```

- Programem el cron

	```bash
	$ ssh root@172.30.22.1  '(crontab -l; echo '\''*/5 * * * /etc/crear_tunels.sh  > /tmp/log/tunels_guifibaix.log'\'') | crontab -'
	```


TODO: Hay que activar los Gateway Ports? Parece no necesario, es el -g el que se requiere

	ssh root@10.1.47.201 "grep GatewayPorts /etc/config/dropbear || echo -e '\toption GatewayPorts on' > /etc/config/dropbear"








