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


# Estando en dos redes a la vez

Si un DHCP nos ha asignado direccion (digamos 172.33.22.44)
y hay un dispositivo físicamente conectado a nosotros
que esta en otra red (192.168.1.1) al que queremos acceder,
podemos añadir un interfaz virtual con el comando:

	sudo ifconfig eth0:1 192.168.1.33

El interfaz real es eth0.

# Resolucion de nombres de maquinas (DNS)

Los DNS internos son:

	* 10.1.40.7
	* 10.1.40.8

En caso de que no estuvieran operativos, se pueden poner estos otros externos

	* 8.8.8.8 (google)
	* 8.8.4.4 (google)

El servidor DNS és una maquina que tiene almacenados las correspondencias entre
el nombre de un servidor (pe. guifibaix.coop)
y su direccion IP, la numérica (pe. 32.23.110.30).

Cuando fallan lo sabemos porque podemos acceder a los servidores
mediante su direccion numerica pero no responden si usamos el nombre.

Los servidores DNS estan jerarquizados:
Cada servidor DNS le pide a su DNS superior las correspondencias que le hacen falta.
Hasta llegar a los servidores raiz, que sirven cada raiz .com, .es, .org...

GuifiBaix tiene un par de servidores DNS internos.
Estos DNS a parte de recibir los DNS normales tienen dos funciones extra:

	- Resolver los nombres internos de GuifiBaix que no están en DNS públicos
	- Sobreescribir los nombres de nuestros servidores para que desde dentro se acceda 


Los DNS externos no resuelven los nombres internos nuestros.
Y los nombres como owncloud.guifibaix.coop los resuelve con la ip externa del servicio,
por lo que salimos por el ADSL y volvemos a entrar por el ADSL del servidor y van mas lentos.








