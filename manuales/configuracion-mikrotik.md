
- La boca 1 no da DHCP, es cliente DHCP.
- En las otras bocas responden a la 192.168.88.1/24 y dan DHCP en la misma red
- Acceder con el firefox a http://192.168.88.1
- comprobar version del firmware en la esquina superior derecha, que no sea ya la 6.2. Si no lo es, hay que actualizarlo.
- Hay que actualizar el Firmware a la 6.2 (las mas nuevas a dia de hoy tienen problemas)
  - http://www.mikrotik.com/download
 
    :::bash
    $ unzip all_packages-mipsbe-6.2.zip

- Menu 'Files'
- Subir los ficheros descomprimidos picando al boton de al lado de 'Upload' y seleccionandolos uno a uno.
- Una vez subidos todos, reiniciar la maquina con el menu System/Reboot
- Esperar un ratin que deje de hacer el coche fantastico, ir cuando vuelva a dar connectividad recargar la pagina
- Esta vez te pide password esta vez pero por defecto usuario admin y password vacia


- Por defecto viene ether1 marcada como gateway a internele
- El resto de bocas como switch
- Hay una marca como master (ether2) que es la que tiene configurado como se comporta ella y sus slaves.

- Configuracion objetivo:
  - ether1 -> Antena
  - ether2 -> Master connexiones de usuario
  - ether3 -> Slave ether2 (connexiones usuario)
  - ether4 -> Slave ether2 (connexiones usuario)
  - ether5 -> ADSL

## Conexion a la Antena (ether1)

- Cambiar el nombre del interfaz: Click en la interfaz ether1, editar el "Name" poner "ether1-Antena" y Ok
- Deshabilitar cliente DHCP
  - Menu IP/DHCPClient
  - Boton con la 'D' en la unica linea que hay (Deshabilita pero no lo borra)
- Añadir la IP del rango de LAN de la antena
  - Suponiendo que la antena tiene 172.30.22.1, escogemos, por ejemplo 172.30.22.2
  - Menu IP/Addresses
  - Boton 'Add New'
  - Interface: ether1-Antena
  - Address: 172.30.22.2/16
  - El Comment va bien ponerlo porque separa visualmente las IP
  - Comment: Antena
  - Ok

## Conexion al ADSL (ether5)

- Primero hay que desvincularla del switch
  - Menu Interfaces
  - Click en la linea de ether5
  - La opcion de 'Master Port' que esta en el ether2, hay que ponerla a None (ninguno)
  - Name: ether5-Internet
- Asignar IP del rango del ADLS
  - Suponiendo que el ADSL tiene 192.168.1.1, escogemos, por ejemplo 192.168.1.2
  - Menu IP/Addresses
  - Boton 'Add New'
  - Address: 192.168.1.2/24
  - Interface: ether5-Internet
  - Comment: Internet
  - Ok

## Conexiones de usuarios (ether2 a ether4)

- No hace tocar nada porque ya tienen un servidor DHCP que reparte direcciones del tipo 192.168.88.XX


## Establecer rutas


- Lo que esta conectado directamente no necesita rutas
- Tenemos dos salidas a internet, priorizaremos el ADSL y en caso de caida, la antena
- Añadiremos una ruta extra para poder acceder a la red Guifi.net 10.X.X.X

- Menu IP/Routes
- Las lineas que se ven son las directas
- Ruta al ADSL (principal de salida a internet)
  - Boton "Add New"
  - Dest. Address: 0.0.0.0/0
  - Gateway: 192.168.1.1
  - Check Gateway: Ping
  - La última opcion lo que hace es comprobar el estado del router ADSL

- Ruta al ADSL (principal de salida a internet)
  - Boton "Add New"
  - Dest. Address: 0.0.0.0/0
  - Gateway: 172.30.22.1
  - Check Gateway: Vacío
  - Distance: 2
  - El ultimo parametro dice que es menos prioritario (por defecto es 1)

- Ruta a Guifi.net
  - Boton "Add New"
  - Dest. Address: 10.0.0.0/8  (Pone 10, no 0, y hay mascara de 8 no 0)
  - Gateway: 172.30.22.1
  - Lo demás, por defecto

  

  
  
  
  