<meta http-equiv="Content-Type" content="text/html; charset=utf-8">

* Todas las antenas tienen una IP4 de mesh y una IP4 de LAN.
* La IP4 de mesh es 10.139.81.xx/24 donde xx es el número de antena
* La IP4 de LAN es normalmente 172.30.22.1
	* Por condiciones de la red interna puede cambiarse
* La IP de rescate es 169.254.232.1
* Las antenas tambien tienen un nombre de antena SJDxx-CalleNum-
	* Por ejemplo SJD14-Major22-
	* El guion final es para separar los dos ultimos digitos de la MAC que se añaden automaticamente
	* Quedaria SJD14-Major22-0f


= Estando en dos redes a la vez

Si un DHCP nos ha asignado direccion (digamos 172.33.22.44)
y hay un dispositivo físicamente conectado a nosotros
que esta en otra red (192.168.1.1) al que queremos acceder,
podemos añadir un interfaz virtual con el comando:

	sudo ifconfig eth0:1 192.168.1.33

El interfaz real es eth0.









