# Material didáctico

Podeis encontrar unos videos muy bien explicados en ingles:

- [Lista de reproduccion](http://www.youtube.com/watch?v=Tahfluke6cU&list=PL08C86258934DD006)
	- [Introduction to Telephone Systems](http://www.youtube.com/watch?v=Tahfluke6cU)
	- [Telephone system call routing](http://www.youtube.com/watch?v=tsWvJTgN15M)
	- [Introduction to Voice over IP](http://www.youtube.com/watch?v=2x3Ie6VZ_sg)
- [Cisco: Fundamentals of SIP](http://www.youtube.com/watch?v=lvLwcARHFoY)a
- [SIP Training](http://www.youtube.com/watch?v=RWggp5zHop8)
- [VoIP Codecs](http://www.youtube.com/watch?v=pfahWL5z5rU)

Lo que siguen son apuntes tomados de los videos anteriores

# Sistemas de telefonía

## Red Telefónica Conmutada (RTC)

En inglés: PSTN (Public Switch Telephone Network)

- Línea física (trunk line):
	- Conecta el edificio con la centralita (central office)
	- Tiene espacio para una llamada entrante o saliente
- Las centralitas (central office) estan interconectadas entre ellas
- El ''plan de marcado'' (Dialing plan) determina como enrutan las llamadas entre ellas basándose en el número de destino
- Demarcation point: La caja que separa la instalación de la compañia de la instalación interior
- En el interior del edificio puede haber un Conmutador del Ramal Privado (PBX, Private Branch Exchange)
- El PBX controla como se encaminan las llamadas internamente

## Trabajando con múltiples lineas

- Cuantas líneas físicas (trunk lines) tengas determina cuantas llamadas entrantes o salientes puedes hacer simultáneamente.
- Cada línea tiene su número propio
- Normalmente, se cogen menos líneas de los puesto de telefonía que necesitas
- Se arbitran con un PBX en el edificio

Cada línea tiene su propio número.
Entonces, como podemos hacer que siempre llamando a un solo numero tener varias lineas disponibles?

- Se programa en la centralita pública
- Se asignan diversas lineas cada una con su número
- Se suelen asignar números correlativos
- Se publica el primer número como número al que llamar
- Se programa en la centralita pública un ''Grupo de caza'' (Hunt group)
	- Si la primera linea y esta ocupada, se redirige a la segunda, la segunda a la tercera y así.
- Internamente el PBX puede encaminar la llamada, al terminal interno (operador) disponible.

¿Y las llamadas salientes?

- Se programa en el PBX, un ''Grupo de llamada'' (Call group)
	- la primera linea disponible, si esta ocupada la segunda...
	- Se suele usar el orden inverso del hunt group
- Se suele liberar alguna linea para que siempre haya llamadas entrantes disponibles
- Podemos priorizar unas lineas o otras según el tipo de llamada (internacional, urgencia...)

## Elementos del ramal privado

- PBX: Encaminado de llamadas
- VoiceMail: Contesta con audio y graba o entiende audio
	- No solo es contestador automatico, también 
	- Dispone de buzones de voz (MailBoxes) numerados
	- El PBX puede redirigir a esos 
- Estaciones (Stations): Terminales. Pueden ser telefonos, interfonos, megafonía...
	- Pueden conectarse analógicamente o digitalmente (tambien ip, pero ignoremoslas de momento)
	- Los telefonos de casa suelen ser analógicos
	- Las digitales tienen más funcionalidades
	- Son compatibles entre ellos, un PBX tendrá un número de lineas de cada tipo

- Subscriptores (Subscribers): Usuarios del sistema
	- No tienen porque ser una estación asociada
	- No tienen porque ser una persona

- Ports:
	- Caminos disponibles de encaminamiento interno entre el PBX y el VoiceMail

- Call groups
- Hunt groups

## Encaminado de llamadas

- Extensión: Cada cosa que puede hacer el PBX es una extensión
	- Redirigir a otra extension
	- Redirigir a una estacion
	- Redirigir a un buzon de voz
	- Redirigir a una linea externa
	- Redirigir a un intercomunicador
	- Auto-atención
	- Hunt groups
	- Call groups
	- ...

- Planificación del ramal interno:
	- Cuantos dígitos identifican la extensión
	- Extensiones de servicio: Se pueden marcar y dirigen a estaciones o voice mails
	- Extensions administrativas: Internas, no se pueden marcar, se usan para los grupos, auto-atencion...

- Ruta de llamada (Call path)
	- Secuencia de acciones que se hacen cuando llamas a una extension
	- Ejemplo: Suena en el telefono tres veces, despues redirige a la recepcionista, si tampoco lo cogen al buzon de voz

- Outcalling
	- Redirigir las llamadas entrantes como una llamada saliente
	- Ojo: normalmente se bloquea porque:
		- coste para la empresa
		- ocupa dos lineas

- Grupo de lineas físicas (Trunk group)
	- Se agrupan para que puedan pasar diferentes cosas
	- Cada grupo se asigna a una extensión

- __Autoattención:__ (Auto-attendant) Lanza un mensaje de voz del MailVoice y deriva según el numero que se marque
	- "Si quiere cagarse en mi madre, pulse 0"
	- Los mensajes se especifican especificando un mailbox
	- Se mapea cada número a otra extensión
	- Siempre tener un time out, porque se dan situaciones en las que no es posible marcar
	- Programar horas de atencion para que si no hay nadie de otro mensaje

- __Hunt group:__ Camino que redirigiendo sucesivamente a una serie de extensiones si no se contesta.
- __Weighted hunt group:__ Permite priorizar los han recibido menos llamadas para repartirlas mejor.
- __Call groups:__ Camino que llama __A la vez__ a una serie de extensiones. El que descuelga se queda la llamada.


## Llamadas de salida

- Dependiendo de el telefono de destino podemos controlar por que trunk group salir.
	- Número de dígitos
	- Prefijos
- Podemos separar, por ejemplo, en Trunk Groups las líneas que permiten internacionales baratas y las que no.
	- Es útil tener solo una linea que tenga llamadas internacionales incluidas (mas caro el mes)

# Voice over IP

## VoIP Servers

VoIP: Comunicacion de audio en tiempo real entre dispositivos de datos (IP).

- Terminales de datos conectados al switch
- Terminales a estaciones digitales o analogicas.
- Trunk Lines
- VoIP Trunk Line (via Internet)

- El servidor VoIP
	- substituye el PBX.
	- se puede tener fisicamente fuera del edificio
		- centralizar servicios en múltiples sedes
		- externalizar servicios
	- no necesitan cacharrería específica (un ordenador conectado a la red)

## VoIP Clients

- Hard phones: Cacharreria especifica para llamar (parece un teléfono)
- Soft phones: Software que instalas en el ordenador para que funcione como un teléfono

Cada teléfono tiene:

- Extension
- Usuario
- Password

- El teléfono se regisra en el servidor
- Apartir de ahí todas las llamadas a dicha extension se dirigen a ese dispositivo


## VoIP Gateways (puertas de enlace)

- Un Gateways conecta una red VoIP con una red RTC.
- Tambien entre diferentes tipos de redes: SIP, XMPP, Skype...
- Si tienes sedes distribuidas, tener un gateway RTC en cada sede permite hacer llamadas locales desde cualquier sede

## VoIP Protocols

- SIP: Session Initiation Protocol. Es el estandar común.
- Hay protocolos privativos, pero te obligan a tenerlo todo de una marca.
	- Skype, Viacom, Cisco...


## VoIP Codecs

- Como se digitalizan la voz como datos
- Determinan:
	- Calidad del sonido
	- Uso del ancho de banda
- Normalmente es un compromiso entre ambas.
- Algunos codecs son propietarios y no se pueden usar en instalaciones open source

- Codecs
	- PCM Pulse Code Modulacion
		- 8bits Unsigned 0 a 255  127
		- 8bits Signed -126 127 0
		- 92K 48K 44.100 22.050
	- ulaw
	- float
	- compresion



## Calidad de servicio (QoS) y latencia de red

- Las aplicaciones de datos están normalmente en competencia perfecta por el recurso del ancho de banda.
- QoS permite priorizar trafico basado en su contenido
- Se tiene que programar en Switches y Routers

- Latencia: Cuanto tarda la informacion en llegar de un lado al otro
	- Importante sobretodo si tenemos un servidor hospedado remotamente
	- No importa para otros usos de datos
	- En RTC, la tatencia suele ser de 45ms
	- Si llega a 100ms empieza a ser problematico
		- Nos atropellemos hablando

# SIP

Protocolo de inicio de sesión (SIP, Session Initiation Protocol)

Funcionalidades:

- Localizar usuarios relacionando una direcion sip con una direccion IP
- Negociar capacidades y funcionalidades entre los participantes en una sesión
- Cambiar parametros de sesión durante la llamada
- Manejar las inicios y finales de llamada para los participantes

- User Agent: Dispositivo de usuario final que inicia una sesión

- Registrar servers: Base de datos de usuarios en un dominio

- Proxy server:
	- Call routing
	- Autentificacion
	- Detencion de bucles
	- A nivel 


# Servidores SIP libres

- Asterisk
- Kamailio (antiguo OpenSER)








