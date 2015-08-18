---
title: 'Programación: El lenguaje Python 3'
author: David García Garzón
copyright: 2015 Guifibaix SCCL
documenclass: book
---

# Introducción

> «Los programadores escriben código para comunicarse con el ordenador.
> Un buen programador escribe código que además le sea fácil de entender 
> a los programadores que tendrán que leerlo después,
> incluyendo uno mismo, cuando pase el tiempo.»
>
> Martin Fowler (parafraseado)

Este manual explica las bases del lenguaje de programación Python.
Su propósito es formar a algunos compañeros de Guifibaix,
pero es extendible a lectores con un perfil similar:
que no hayan programado nunca
aunque con nociones básicas de la consola Linux:
como manejar ficheros desde línia de comandos,
instalar programas, o hacer un script de `bash`.

A lo largo del manual identificarás las ordenes que hay
que ejecutar desde el terminal porque van precedidas de un signo `$`.
Así:

```bash
$ echo hola mundo
```

Para algunos ejemplos y ejercicios,
también es aconsejable conocer
el uso del sistema de control de versiones `git`.


## Lenguajes de programación

Un lenguaje de programación es la forma en que las personas
definimos el comportamiento de las aplicaciones.
Existen muchos lenguajes de programación.
Cada lenguaje tiene sus puntos fuertes
o está más adaptado a según que tareas,
o a las preferencias de cada persona.
Por eso hay tantos lenguajes.

Al final, el ordenador solo entiende de código máquina.
El codigo máquina no está pensado para que lo entiendan las personas;
es una secuencia de números sin sentido aparente,
en la que cada número codifica
algo que tiene que hacer el ordenador:
Cargar en el procesador un número contenido en una posición de memoria,
operar con ese número,
colocar el resultado en otra posición de memoria,
enviar un código a un dispositivo...
Cosas de muy de tocar el hierro.

Los lenguajes de programación son más cercanos
a algo que una persona puede entender,
haciendo de puente entre las personas y el ordenador.
Nos permiten abstraernos de las interioridades del ordenador,
y pensar en términos más cercanos al problema que queremos resolver.

Los programas se escriben en archivos de texto plano,
con unas reglas bastante rígidas.
Las reglas conforman lo que se llama **sintaxis**,
que es lo que es propio de cada lenguaje.

Esos ficheros de texto,
escritos en un lenguaje de programación,
tienen que ser traducidos a
código máquina ejecutable por el ordenador.
Según la estrategia que se use para hacerlo
hablamos de _lenguajes compilados_ o
de _lenguajes interpretados_.

Un __compilador__ hace la traducción una vez,
generando un archivo ejecutable/binario que incluye el código máquina.
Ese archivo binario, una vez generado, lo podremos ejecutar sin necesitar ya
ni el compilador ni el texto del programa original.

- Ejemplos: C++, Java, Pascal... son lenguajes compilados.

Un __interprete__, en cambio, traduce el programa a código máquina
a la vez que lo ejecuta.
No genera el archivo binario intermedio
y, cada vez que lo queramos ejectuar,
necesitaremos tanto el texto del programa (script) como el intérprete.

- Ejemplos: Bash, Python, Perl, PHP... son lenguajes interpretados.

Haciendo la analogía en terminos de lenguages humanos,
un intérprete sería la traducción simultánea,
el intérprete tiene que ir buscando la traducción al vuelo,
mientras que un compilador seria como el traductor de un libro,
puede dedicar tiempo en encontrar la mejor traducción
porque una vez traducido el libro traducido queda ahí para quien lo lea.

En general, un lenguaje interpretado se ejecutará más
lento que uno compilado, puesto que, el ordenador tiene que
ejecutar, a parte de la tarea que indica el programa,
la traduccion a cógigo máquina.

Con los rápidos ordenadores actuales,
el tiempo de interpretación dejó de ser un problema.
Y se prefiere en muchos casos un lenguaje interpretado porque,
al no requerir el paso de compilación,
el proceso de desarrollo es mucho más rápido y simple.

Si te lo puedes permitir es más flexible viajar al extrangero
con un traductor simultáneo, que
salir con un papelito en el que tienes escrito en guirilandés lo que debes decir.

> **Ejercicio:**
> En Linux la mayoría de programas (archivos ejecutables) se encuentran en `/usr/bin/`.
> El comando `file` identifica tipos de ficheros.
> Mira que tipo de ejecutables tienes ahí con:
>
> ```bash
> $ file /usr/bin/*
> ```
>
> Verás que la mayoría de ejecutables que aparecen tienen formato `ELF`.
> Es el formato que generan los compiladores en Linux y contiene el código máquina del programa.
> Estos programas se escribieron seguramente en C, C++... pero ya no nos importa para ejecutarlo.
> Si miramos su contenido, solo veremos basura digital, por ejemplo:
>
> ```bash
> $ cat /usr/bin/man
> ```
>
> Junto con los ELF también aparecen un montón de archivos que identificados como de _texto ejecutable_ (o scripts)
> escritos en Python, Perl, Bash, Ruby, Javascript...
> Si haces un `cat` de uno de estos, verás el código fuente tal cual.
> Es texto que podríamos incluso editar:
>
> ```bash
> $ cat /usr/bin/rgrep
> ```


## Buscando más cosas sobre Python

Python es un lenguaje interpretado de propósito general que
se caracteriza por tener una sintaxis muy limpia y expresiva.

Nos centraremos en la version 3 (3.4.3 en el momento de escribir esto).

Para aprender Python hay tres elementos:

- El **lenguaje**, que son las reglas de como decir las cosas.
	- La descripción formal de la sintaxis la puedes encontrar en la [referencia del lenguaje](https://docs.python.org/3/reference)
	- Un poco más explicado, aunque en inglés, lo tienes en el [tutorial](https://docs.python.org/3/tutorial)
- Las **librerias estándard**, que són cosas que no hace falta que programes tú, porqué ya están programadas y vienen de serie:
	- Encontrarás informacion en la [referencia de la librería estándard](https://docs.python.org/3/library/)
- Las **librerías no estándard**. Aunque no vengan por defecto algunas son de uso muy extendido.
	- Toda librería que se precie está incluida en el [índice de paquetes](https://pypi.python.org/pypi)
	- Cada librería tiene su propia documentación.
	Normalmente con un formato similar a la documentación de las librerías estándard.
- Si necesitas algo más, esta es [toda la documentación del lenguaje](https://docs.python.org/3/)

Hay dos formas de ejecutar código Python:

- tecleando sentencias en el **intérprete en modo interactivo** (python3 o, mejor, ipython3),
para experimentar y probar cosas.
- escribiendo las sentencias en un archivo de texto, que llamamos **script**, y lanzándolas de golpe con el intérprete,
cuando estemos evolucionando un código o queremos que quede para la posteridad.

## Usando el intérprete interactivo

- El intérprete interactivo te permite escribir código Python y ver los resultados de forma inmediata
- Es ideal para probar cosas cortas, lo usaremos sobre todo al principio del tutorial
- El intérprete clásico es `python3`.
	- Instalación en Ubuntu: `sudo apt-get install python3`
	- Seguramente ya lo tendrás instalado
	- Sales con Control+D
- Recomendamos el intérprete con esteroides llamado `ipython3`
	- Instalación en Ubuntu: `sudo apt-get install ipython3`
	- Tienes historial de lo que has escrito, que puedes recuperar con la tecla del cursor hacia arriba.
	- Te completa expresiones con la tecla del tabulador
	- Puedes ejecutar comandos del shell precediendolos con `!`
	- Si le añades un signo `?` a una expresion te muestra ayuda sobre el objeto resultante
- Nota: Las ultimas versiones del intérprete clásico, tiene ya historial y completa expresiones.

Cuando digamos de ejecutar algo en un intérprete lo solemos escribir así:

```python
>>> print("hola mundo")
hola mundo
```

- El `>>>` indica el símbolo que el intérprete pone para decirte que puedes escribir.
	- En ipython3 es algo como `In [1]:`
- Lo que has de escribir es lo que va después, del `print` en adelante.
- La segunda linea es el resultado, lo que ha imprimido por la pantalla el intérprete.

**Nota:** Si has programado antes en Python 2, ojo que en Python 3, la instrucción `print` requiere paréntesis.

**Nota:** En modo interactivo, siempre nos imprimirá el resultado de la expresion que hayamos introducido.
No necesitamos el `print`, para verlo.


## Escribiendo y ejecutando scripts

Un **script** es un fichero de texto que contiene
las instrucciones de un programa escrito
en un lenguaje interpretado (bash, python, perl, php...).

Para que se pueda ejecutar sin problemas en Unix:

- Necesitan permisos de escritura

	```bash
	$ touch miscript.py   # Crea un archivo si no existe
	$ chmod +x miscript.py  # Activa los permisos de ejecución
	```

- Lo editamos con un editor de texto plano: kate, vim, gedit, nano, notepad++...
Asegúrate de que el editor usa el juego de carácteres UTF-8.

- La primera linea del fichero debe ser el _shebang_ que indica al shell con qué intérprete se ejecuta el script.
  En `myscript.py` escribiríamos:

	```python
	#!/usr/bin/env python3
	
	print('hola mundo')
	```

- Teniendolo así podemos ejecutarlo desde el shell con:

	```bash
	$ ./miscript.py
	hola mundo
	```

- Alternativamente, si el script bien no lleva shebang o no tiene permisos,
podemos ejecutarlo pasandoselo como primer parámetro al intérprete:

	```bash
	$ python3 miscript.py
	hola mundo
	```

- La extension `.py` del fichero no es necesaria para ejecutarlo en Linux.
Aunque puede serlo para ejecutarlo en otros sistemas
También sirve para que los editores con resaltado de sintaxis
detecten que es un fichero escrito en Python y lo coloreen adecuadamente.

## Reglas generales de sintaxis

La sintaxis de Python sigue unos principios generales bastante homogéneos:

- Un script en Python se compone de una serie de **sentencias**.
Esas sentencias, las podemos escribir directamente en el intérprete
o en un fichero script como hemos visto antes.

- Normalmente, se escribe una sentencia por línea

	```python
	print("hola")
	print("mundo")
	```

- Todo lo que haya a la derecha de una almohadilla es un **comentario**.
Es ignorado por el intérprete y se usa para explicar el código a los otros humanos.

	```python
	# esto es un comentario
	print("hola mundo")  # y esto otro
	```

- Hay sentencias especiales que acaban en dos puntos (`:`).
Los dos puntos indican que se da paso a una serie de **subsentencias**,
que van **indentadas a un nivel más adentro**.

	```python
	# Repetición infinita
	while True :  # Repite las subsentencias mientras... siempre
		print("hola")
		print("mundo")
	```

- Las subsentencias se acaban cuando aparece una sentencia en el anterior nivel de indentación

	```python
	while False :    # repite las subsentencias mientras... nunca
		print("hola") # esta sentencia pertenece al while
		print("mundo") # esta también
	print("¡Acabé!")  # esta sentencia se ejecuta cuando se sale del while
	```

- Cada sentencia con dos puntos, inicia un nivel de indentación nuevo

	```python
	while False :
		print("hola")
		while True:
			print("que tal") # esta pertenece al segundo while
		print("mundo") # esta vuelve a ser del primero
	print("¡Acabé!") # y esta cuando sale del primer while
	```

- Tanto si se incrementa la indentación sin que haya una sentencia con dos puntos que lo justifique,
  como si se reduce sin llegar al nivel de indentación de una de las sentencias superiores,
  el intérprete nos lanzará un `Indentation Error: unexpected indent`.

	```python
	while False :
	    print("hola") # la primera subsentencia del grupo define el nivel
	    print("mundo") # esta lo sigue
	     print("sobrada")  # ¡¡¡esta se ha pasado!!!
	  print("oops")  # ¡¡¡esta se ha quedado corta!!!
	print("al nivel del while, correctamente fuera del while")
	```

- Dada la importancia de la indentación para estructurar el código,
  es importante ser cuidadoso.
  No hay que mezclar, en un fichero, indentación con tabuladores y indentación con espacios
  y, si es con espacios, usar consistenemente el mismo número de espacios para cada nivel.
  Es decir, que en todo el proyecto cada nivel sea 1, 2, 4, o 8 espacios.

	- Aunque a Guido, el autor de Python, odia los tabuladores, personalmente, los prefiero por:
		- Con espacios aun tenemos la guerra de cuantos espacios usar
		- En cambio, los tabuladores cada uno puede ajustarlos en el editor al tamaño que le gusten.
		- Con espacios es más fácil visualmente que te dejes un espacio de más o de menos.
	- En cualquier caso, si no empezamos proyecto nuevo, hay que ajustarse a lo que use el proyecto.
	  Peor que tener tabuladores o espacios, es tener una mezcla de ellos.

- Si abrimos un símbolo que haya que cerrar, como, por ejemplo, los paréntesis,
  podemos extendernos varias lineas y despreocuparnos por la indentación,
  hasta que lo cerremos.

	```python
	print(
		'Hola mundo'
		)
	```

- Otros elementos que se abren y se cierran
y que permiten extender la sentencias en varias líneas hasta cerrarlos son:
	- Paréntesis: `( )`
	- Corchetes planos: `[ ]`
	- Corchetes rizados: `{ }`
	- Comillas: `" "`
	- Comillas simples: `' '`
	- Comillas triples: `""" """`
	- Comillas simples triples: `'''  '''`

- Si el último caracter de una línea es una contrabarra (`\`),
  el intérprete **ignora el salto de línea como si no estuviera**.
  **No hay que abusar de ello**, pero es la opción de último recurso
  cuando una sentencia se nos hace larga (80 caracteres es lo máximo recomendado),
  y no tenemos un paréntesis o similar para cortar.

	```python
	print \
		("hola mundo")
	```

- Al revés, se puede **juntar sentencias en una sola línea**
  si las separamos con un punto y coma (`;`).
  **No es recomendable hacerlo porque suele ofuscar el código**.
  Lo hace más difícil de leer.

	```python
	print("hola"); print("mundo")
	```

- Cuando una sentencia compuesta solo tiene una subsentencia,
  se puede poner en la misma línea.
  Tampoco es recomendable hacerlo,
  y sólo con subsentencias realmente cortas.

	```python
	while True: print("hola mundo")
	```

Sabiendo todo esto, aprendamos a escribir todas esas sentencias mágicas.



# Calculando expresiones en Python

Escribamos nuestro primer código con sentido.

El primer tipo de sentencia que veremos será la expresión.
Una **expresión** es una construcción del lenguaje que resulta en un **valor**.
Por ejemplo: `3+4` es una expresión que resulta en el valor `7`.

Las expresiones se usan en muchos sitios pero también son sentencias de pleno derecho.
Así que podemos introducir expresiones en el intérprete interactivo de Python y usarlo de calculadora.


## Tipos de datos y literales

Decíamos que  `3+4` es una expresión que da el valor `7`.
De hecho, `3`, `4` y `7` son expresiones también, de las que llamamos literales.
Los **literales** son la forma más directa de representar un valor.
Los valores pueden ser de diferentes **tipos** y cada tipo de dato tiene su forma de expresar sus literales.

A continuación, vemos ejemplos de literales de los tipos de dato más comunmente usados.
Entre paréntesis, en el comentario, el nombre que se le da al tipo en Python.

```python
>>> -12     # un número entero (int)
-12
>>> 12.34   # un número con decimales (float)
12.34
>>> 2+3j    # un número complejo (complex)
(2+3j)
>>> 'un texto'  # un texto (str)
'un texto'
>>> 12, 23  # una tupla (tuple) con dos enteros
(12, 23)
>>> [1, 2, 3, 1]  # una lista (list) con 4 enteros
[1, 2, 3, 1]
>>> {1, 2, 3, 1} # un conjunto (set) con 4... ops, 3 enteros
{1, 2, 3}
>>> # un diccionario (dict) 2 con parejas clave: valor
>>> { 'David': 40, 'Aitor': 25 }
{ 'David': 40, 'Aitor': 25 }
>>> None   # el no-objeto (NoneType), el intérprete ni lo imprime
>>> True   # un valor lógico (bool), su antitesis es False
True
```

A lo largo del tutorial iremos explicando como trabajar con estos tipos de objetos.
Un aperitivo:

- Con los tipos numéricos (`int`, `float`,`complex`) podemos hacer operaciones aritméticas.
- Con los textos (`str`) podemos concatenarlos, substituir, partir, buscar...
- Las tuplas (`tuple`) son parejas, trios... de valores que juntamos para pasarlos juntos como un solo valor.
- Las listas (`list`) son como las tuplas pero podemos insertar y eliminar elementos.
- Los conjuntos (`set`) son como las listas,
  pero no guarda el orden entre los elementos,
  y descarta los valores repetidos
  (por eso, en el ejemplo, uno de los dos `1` desaparece).
- Los diccionarios (`dict`) contienen parejas clave-valor, en los que se puede acceder al valor indicando la clave.
- El no-valor `None` (`NoneType`) representa el concepto de _ningún valor_, más útil de lo que parece.
- Los valores lógicos (`bool`) representan una condición que puede ser cierta o falsa, y sirven para tomar decisiones.

A continuación, veremos estos tipos más en detalle.

## Trabajando con números, tipos `int` y `float`

Podemos usar Python como una calculadora.
Combinando literales y operadores obtenemos expresiones numéricas.

```python
>>> 10+3  # suma
13
>>> 10-3  # resta
7
>>> 10*3  # multiplicación
30
>>> 10/3  # división con decimales
3.3333333333333335
>>> 10//3  # división entera
3
>>> 10%3  # resto de la división entera
1
>>> 10**3  # potencia
1000
```

Cuando combinamos varios operadores en una expresión,
se resuelven por prioridad.
Por ejemplo, la multiplicación y división tienen más prioridad que la suma y la resta.
La exponenciación tiene más prioridad que la mutiplicación y la división.
Por eso:

```python
>>> 2*3+4  # se resuelve como (2*3)+4
10
>>> 2+3*4  # se resuelve como 2+(3*4)
14
```

Igual que en mates, podemos alterar esa prioridad, usando paréntesis:

```python
>>> 2 * (3 + 4)    #  = 2 * 7 = 14
14
>>> (2 + 3) * 4    #  = 5 * 4 = 20
20
```

Los paréntesis aunque no sean necesarios porque la prioridad ya lo ejecuta como queremos,
también ayudan a leer y entender la expresión.

Recuerda que no solo escribimos código para el ordenador.
También escribimos código para el siguiente programador que tenga
que revisarlo, que podemos ser nosotros mismos de aquí a un tiempo
cuando ya apenas recordemos como iba el programa.
Si vemos los paréntesis no tendremos que pensar en cual es la
prioridad o sospechar que cuando lo escribimos no la teníamos clara.

Cuando combinamos operadores del mismo nivel,
se resuelven de izquierda a derecha,
es decir, tal y como se lee.

```python
>>> 2 + 3 + 4 + 5 # se resuelve ((2+3)+4)+5
14
```

> **Ejercicio:** Usa el ipython3 como calculadora para hacer algunos cálculos.

A parte de los literales que hemos visto,
podemos usar otras notaciones para los literales numéricos:

```python
>>> # Notaciones alternativas para int
>>> 0xF0  # notacion hexadecimal, con 0x delante
240
>>> 0b10010  # notacion en binario, con 0b delante
18
>>> # Notaciones alternativas para float
>>> 1.3e-5  # notación científica, equivale a 1.3*(10**(-5))
1.3e-5
```

> **Ejercicio:**
> Experimenta con las notaciones
> [hexadecimales](http://es.wikipedia.org/wiki/Sistema_hexadecimal),
> [binarias](http://es.wikipedia.org/wiki/Sistema_binario) y
> [científica](https://es.wikipedia.org/wiki/Notaci%C3%B3n_cient%C3%ADfica).


## Reusando resultados: variables y la sentencia de asignación

Todas las  expresiones que hemos visto anteriormente,
incluyendo las que forman parte de otras expresiones,
generan valores que, una vez los hemos hecho servir,
desaparecen de la memoria del ordenador.

Las **variables** nos permiten conservar un **valor**, dándole un nombre,
para volverlo a usar después.
La sentencia en la que asociamos un valor a un nombre se llama *sentencia de asignación*.
Decimos que *asignamos un valor a la variable*.
Una vez asignada, en adelante,
podemos usar la variable como si fuera un literal más.

```python
>>> a = 23  # sentencia de asignacion
>>> a       # uso de la variable
23
>>> b = 10*a  # 'a' en una expresión, el resultado de la expresión a 'b'
>>> b
230
```

En Python, una misma variable en un script puede ir apuntando a valores diferentes.
De hecho, puede apuntar incluso a valores de diferente tipo,
cosa que no se permite en otros lenguages como C o Java.

```python
a = 12       # tipo entero (int)
a = 'hola'   # tipo texto (str)
a = 3.1416   # tipo coma flotante (float)
```

Consejos del programador abuelete:

- Aunque puedas, no es recomendable reusar las variables.
  Si, en un punto, una variable se refiere a una cosa,
  confunde que después se refiera a otra cosa.
- Usar nombres de variables de una letra, como `a`, tampoco es bueno,
  **los nombres de las variables tienen que recordarnos a que se refieren**.

En los ejemplos, normalmente se abusa de los nombres tontos de variables.
**No uses nombres tontos cuando estés programando de verdad.**
Martin Fowler vendrá por la noche, matará tus procesos y violará a tus segmentos.

Así que para dar a entender el significado de una variable
en vez de llamarla `a`, la llamaremos `anguloRecorrido`.

Para que el nombre de una variable sea explicativo
se suele necesitar más de una palabra,
pero los nombres de variables no pueden contener espacios,
así que se usan diferentes nomenclaturas:

- **Lower Case**: `sinningunadiferenciaentrepalabras`
- **Camel Case**: `alteramosLasMayusculasAlInicioDePalabra`
- **Underscore**: `separamos_las_palabras_con_subrayados`

La primera estrategia es bastante ilegible aunque para nombres cortos funciona.
La segunda es más legibles sobretodo cuando te acostumbras.
Y la tercera aunque parezca más legible,
confunde cuando se mezcla con otros operadores que se parecen al guión bajo,
como el punto, la coma o el guión normal.

Como con el estilo de indentación, cada uno tiene sus preferencias y motivos,
pero conviene que el criterio sea coherente dentro de cada proyecto.


## Operadores de actualizacion (`+=`, `*=`...)

Muy a menudo queremos actualizar el valor de una variable
en base al valor anterior. Por ejemplo:

```python
saldo = 0
# aqui hago una venta, incremento el saldo
saldo = saldo + 200
```

Todos los operadores numéricos tienen su versión de actualización
que actualizan la variable en base al antiguo valor,
añadiendo un `=` al operador original.

Usando esos operadores, la última línea del ejemplo anterior quedaría así:

```python
saldo += 200
```

Otro ejemplo con mas operadores:


```python
costeAntena = 100
costeSwitch = 45
descuento = 20
factorIva = 0.21

costeFactura = 0
costeFactura += costeAntena
costeFactura += costeSwitch
costeFactura -= descuento
costeFactura *= 1 + factorIva
print(costeFactura)
```



## Llamando funciones

Otro elemento útil que podemos usar en una expresión son las funciones.
Las **funciones** retornan valores calculados a partir de los parámetros que les enviamos con el operador paréntesis.

Por ejemplo, la función `max`, incluida en el lenguaje,
retorna el mayor de los valores que le pasemos como parámetros.

```python
>>> max(50,200)  # El máximo de 2 valores: 50 y 200
200
```
Como una función retorna un valor,
podemos usar el resultado de esa función dentro de otra expresión más compleja.

```python
>>> max(50,200) + 4
204
```

Las funciones pueden ser _built-in_, si, como `max`,
están siempre disponibles en el lenguaje.
También podemos definirlas nosotros,
o importarlas de librerías existentes,
pero eso lo veremos más adelante.

Te habrás dado cuenta que desde el primer ejemplo
hemos estado usando una de estas funciones _built-in_, la función `print`.
`print` es una función que no devuelve nada (un objeto `None`)
pero tiene el efecto lateral
de mostrar por el terminal los valores que le pasamos.

Cuando usamos el intérprete interactivo,
es el intérprete el que nos va enseñando los resultados de las expresiones.
Pero cuando ejecutamos un script,
si queremos ver algo por consola,
hay que llamar a la función `print`.

Por ejemplo, para ver el resultado de llamar a la función `max`:
```python
print(max(50,200))
```

Fíjate que hemos usado la salida de una función, `max`,
como parámetro (entrada) de otra, `print`.


## Trabajando con texto, tipo `str`

El tipo `str` sirve para representar texto.
Podemos construir literales de texto delimitando el texto entre comillas dobles o simples.

```python
>>> "hola"
'hola'
>>> 'hola'
'hola'
```

Tener dos tipos de comillas va bien:
Si el texto contiene una de ellas, usamos la otra.

```python
>>> print('Me dijo: "Adios" y me fuí')
Me dijo: "Adios" y me fuí
>>> print("Castellar de N'Hug")
Castellar de N'Hug
```

Si el texto contiene ambas, tenemos otras soluciones:

```python
>>> print('Usando la contrabarra para \'escapar\' la comilla')
Usando la contrabarra para 'escapar' la comilla
>>> print('''Usando las "triples" 'comillas'.''')
Usando las "triples" 'comillas'.
>>> print("""Que tambíén pueden ser "dobles" 'triples'.""")
Que tambíén pueden ser "dobles" 'triples'.
```

Las secuencias de escape con la contrabarra `\` tambíén sirven para
insertar saltos de línea (`\n`), tabuladores (`\t`)...
De hecho para incluir una contrabarra en un texto
hay que _escaparla con contrabarra_, es decir, poner dos `\\`.
Si un literal de texto contiene muchas contrabarras,
igual nos combiene deshabilitar las secuencias de escape
prefijando una `r` de 'raw' (en crudo) al literal.

Un uso común, por ejemplo, los ficheros en Windows:

```python
>>> # Las contrabarras se convierten en un tab y un salto de línea
>>> print("c:\temp\newitem")
c:	emp
ewitem
>>> print("c:\\temp\\newitem")   # Escapando contrabarras
c:\temp\newitem
>>> print(r"c:\temp\newitem")    # Texto 'en crudo', prefijo 'r'
c:\temp\newitem
```

Podemos usar algunos operadores numéricos tambíén con texto:

```python
>>> "Hola" + "mundo"  # juntamos los dos textos (sin espacio!)
'Holamundo'
>>> 'hola'*4    # Multiplicar por un numero, repite el texto
'holaholaholahola'
```

De hecho si tenemos literales, sumarlos es una perdida de CPU.
Python considera los literales seguidos como un solo literal
lo que nos permite escribir texto como éste:

```python
print(
	"No es verdad, angel de amor\n"
	"que aquella apartada parrilla\n"
	"estan friendo morcillas\n"
	"y hasta aquí llega el olor?\n"
	)
```

Tenemos algunas funciones _built-in_ que podemos usar con secuencias:

```python
>>> len('hola')   # longitud de un texto
4
```

Y algunos operadores específicos tambien para sequencias como son el operador `in` y su complementario `not in`.

```python
>>> 'ol' in 'hola'
True
>>> 'lo' in 'hola'
False
>>> 'lo' not in 'hola'
True
>>> 'ol' not in 'hola'
False
```


## Indexando y rebanando (slices)

La indexacion con los simbolos `[ ]` nos permite selecionar letras de un texto por su posición.
En general, nos permiten acceder al enésimo elemento de una secuencia,
siendo una **secuencia** cualquier estructura que contenga elementos en un orden determinado.
La única secuencia que hemos explorado en profundidad es el texto,
así que para los ejemplos usaremos textos,
pero también podremos hacer lo mismo con tuplas y listas, que también son secuencias.

**¡Ojo! ¡Los índices empiezan siempre por el cero!**

```python
>>> a = 'murcielago'
>>> a[1]   # ¡ojo! ¡La primera letra es la 0!
'u'
>>> a[0]   # Ahora sí
'm'
>>> len(a)
10
>>> a[10] # ¡ojo! el ultimo es el 9, si nos salimos, error
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
IndexError: string index out of range
>>> a[9]   # así sí
'o'
```

Si usamos índices negativos, empezamos por el final.
El último es el -1, el penúltimo el -2.

```python
>>> a[-1]  # Con índices negativos empezamos por el final
'o'
>>> a[-2]
'g'
```

También podemos sacar rebanadas (_slices_)
usando inicio y final separado por dos puntos.
**El índice final no se incluye.**

```python
>>> a[2:6] # de la tercera (2) a la sexta letra (5)
'rcie'
>>> a[:6] # Si no ponemos el inicio se deduce desde el principio
'murcie'
>>> a[2:] # si no pones el final se deduce que hasta el fin
'rcielago'
>>> a[:5] + a[5:]  # ¿porque el índice 5 no esta repetido?
'murcielago'
```

> **Pregunta:** ¿Porque en la ultima expresión no se repite el índice 5?

Un tercer elemento que se le puede añadir al _slice_ es el paso;
cuantas casillas saltamos.
Cuando no lo especificamos el salto es 1, pero si lo especificamos...

```python
>>> a[::2]  # saltamos las letras de dos en dos
'mrilg'
>>> a[1::2]  # si le damos un offset
'uceao'
>>> a[6:2] # si inicio y fin no estan ordenados, retorna texto vacío
''
>>> a[6:2:-1]  # pero con un paso negativo, va hacia atrás
'leic'
>>> a[::-1]  # guárdate esta, sirve para voltear cualquier secuencia
'ogaleicrum'
```

> **Pregunta:** ¿Porqué `a[6:2:-1]` no son las mismas letras invertidas que con `a[2:6]`?

> **Pregunta:** ¿Qué retornaria a[5:5]? ¿Porqué?

**Reflexión:**

> **¿Porqué lo complican todo empiezando los índices por cero y haciendo que el final de los intervalos no se incluya?**
>
> Es heréncia de cuando se trabajaba con el hardware.
> El texto está en una posición de memoria,
> para acceder a la segunda letra hay que saltar 1 posicion, para acceder a la primera, cero posiciones.
> Hubo una ola de lenguajes que intentaron usar el 1 como primer índice, pretendiendo ser más naturales.
> Resultó que todo el código acabo siendo más complicado.
> Las operaciones con índices basados en 0 son mucho más simples.
> Que los índices empiecen por 1 acaba siendo un incordio.
>
> **Esos lenguajes que intentaron empezar los índices con 1 perecieron o malviven siendo muy odiados.**



## Definiendo funciones, sentencia `def`

En nuestro script podemos definir nuestras propias funciones.

```python
>>> def media(a, b):
...     suma = a+b
...     return suma/2
...
>>> media(3, 1)
2.0
>>> media(4, 5)
4.5
```

- La definición de una función comienza con la palabra reservada `def`.
- Le sigue el nombre que daremos a la función, `media` en este caso.
	- El nombre sigue las mismas normas que para las variables.
	- De hecho compiten por el mismo espacio de nombres:
		- si declaramos después una variable llamada `media` perderemos nuestra función.
- Después, entre paréntesis y separados por comas, la lista de parámetros.
	- Los parámetros se pueden usar en las subsentencias como si fueran variables
	- Se les asignan los valores que pasamos entre paréntesis cuando llamamos la función
		- En la primera llamada `a=3`. En la segunda llamada `a=4`.
		- En la primera llamada `b=1`. En la segunda llamada `b=5`.
	- La asociación de los parámetros existe sólo mientras se ejecute esa llamada a la función
- La sentencia `def` acaba con dos puntos (`:`), siguen subsentencias indentadas un nivel
	- Las sentencias de dentro son las que se ejecutarán cada vez que llamemos la función.
	- Los tres puntos los escribe el intérprete, en vez de los `>>>` para indicar que aun tenemos que acabar la sentencia.
	- Para salir de los tres puntos en el intérprete dejamos una linea en blanco
- La primera sentencia de dentro crea una variable `suma`
	- Las variables que creemos dentro de una función, igual que los parámetros, solo existen mientras la función se ejecuta.
	- En jerga se dice que es una _variable local_, en contraposicion de las variables que se definen fuera de funciones que se les llama _globales_
	- Que las variables tengan un ámbito local nos ayuda a no tener que buscar nombres que no colisionen con los de otras funciones
	- Los paràmetros `a` y `b` también se consideran variables locales.
- La ultima sentencia es una sentencia especial `return`
	- Una sentencia `return` sale de la función y devuelve el control al llamante
	- Además el llamante recibirá el valor resultante de la expresión que va después del `return`
	- Si hubiera más sentencias después del return, no se seguirían ejecutando (se _sale_ de la función)

## El no-valor `None`

¿Qué pasaría si se llega al final de la función y no encuentra ningún return?

Pues que el llamante recibiría un valor especial que representa el _no-valor_.
Se trata del `None` que es el único valor del tipo `NoneType`.

```python
>>> None # El intérprete no muestra resultado si una sentencia resulta en None
>>> print(None)  # Pero lo podemos imprimir explícitamente
None
>>> a = print("hola")  # La función print tampoco retorna nada
hola
>>> a   # Lo dicho
>>> print(a)
None
>>> def noReturnFunction():
...     2+2  # ojo, error típico queríamos retornar algo y nos dejamos el return
...
>>> noReturnFunction()
>>> print(noReturnFunction())
None
```
Una función retorna `None` 

- Porque explícitamente hace un `return None`
- Porque hace un return sin expresión: `return`
- Porque se acaban las sentencias de la función sin haber llegado un `return`


## Parámetros opcionales, valores por defecto

Se puede indicar que, para una función,
algunos parámetros son opcionales.
Lo hacemos indicando el valor por defecto
que adoptará el parámetro si no lo pasamos.

En el siguiente ejemplo definimos una función
para aplicar el iva a una base imponible.
Como el IVA típico ahora mismo es del 21%,
para no tener que especificarlo siempre,
lo ponemos como parámetro opcional,
y en el caso de que no se lo pasemos,
lo ponemos a `0.21`.

```python
>>> def aplicaIva(baseImponible, factorIva=0.21):
... 	return baseImponible + baseImponible*factorIva
...
>>> aplicaIva(100, 0.07)
107
>>> aplicaIva(100)
121
```

Fíjate que, en la declaración de los parámetros,
hemos igualado el `factorIva` al valor que adoptará
en el caso que el llamante no lo proporcione, `0.21`.

La declaración de parámetros opcionales tiene una restricción importante:
**Todos los parámetros obligatorios han de ir delante de los opcionales.**
De esta forma, el intérprete puede ir asignando valores a los parámetros
hasta que se acaban y completar el resto con los valores por defecto.

> **Exercicio:**
> Define una función con dos parámetros obligatorios y dos opcionales
> que imprima los valores para ver que le llega.
> Llámala con 1, 2, 3, 4 y 5 valores a ver que dice en cada caso.




## Parámetros por clave

Otra virguería que podemos hacer con las funciones
es especificar los parámetros por su nombre
cuando llamamos a una función.

```python
>>> aplicaIva(factorIva=0.07, baseImponible=100)
107
```

Como se ve en el ejemplo,
si indicamos el nombre de los parámetros,
podemos colocarlos en el orden que queramos.

Pero no sólo sirve para desordenar los parámetros.
Cuando las funciones tienen muchos parámetros,
determinar por posición qué parámetro corresponde con cual es muy dado a errores.
No sólo genera errores si no que a alguien que está leyendo el código,
le cuesta seguirlo.
Así que especificar el nombre del parámetro ayuda a esa lectura.

Otro caso en que es útil especificar los nombres:
Si, durante la evolución del script,
decidimos alterar los parámetros de la función,
hay que actualizar también las llamadas.
En este caso especificar el nombre también facilita
la detección de errores en el proceso de migración.

En resumen, se recomienda explicitar los nombres de paràmetros:

- Cuando alteremos el orden en los parámetros de llamada
- Cuando haya muchos parámetros, para no liarnos
- Cuando preveamos una evolución en los parámetros
- Cuando hay varios opcionales de los que normalmente queremos especificar pocos (si los llamaramos po

Se pueden combinar parámetros posicionales con nombrados.
La regla es que primero se especifican los posicionales
y luego van los nombrados.
Los posicionales se reparten en orden tal i como están en la definición de la función (`def`).

```python
>>> aplicaIva(100, factorIva=0.07)
107
```

Si después de repartir los parámetros,
hay algun parámetro, que no se le haya asignado valor y tampoco tenga uno por defecto,
el intérprete se quejará:

```python
>>> aplicaIva(factorIva=0.07)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: aplicaIva() missing 1 required positional argument:
'baseImponible'
```


## Llamando a métodos

El espacio de nombres es un recurso escaso cuyo abuso puede afectar a nuestra salud mental.
Cuantos menos nombres tengas que tener en cuenta cuando te metes en un código en concreto, mejor.
Normalmente, los lenguajes aportan herramientas
para partir ese espacio de nombres en trocitos aislados.
Es el caso que vimos antes con las variables locales,
las que se definen dentro de una función y no son visibles desde fuera.

El hecho es que las funciones compiten por el mismo espacio de nombres que las variables.
Una solución para definir funciones que no colisionen son los **métodos**.
Un método es una función que está ligada a un tipo de objeto/valor.
Se llaman con la sintaxis del punto (`.`) a partir del objeto/valor.

```python
objeto.metodo(parámetros)
```

El intérprete interactivo nos deja explorar los métodos disponibles
si tecleamos un literal o una variable, un punto y damos al tabulador
y lo autocompleta si lo empezamos a teclear y le damos al tabulador.

Los textos `str` tienen varios métodos disponibles:

```python
>>> s = 'abracadabra'
>>> s.count('bra')  # Cuantas veces contiene el parámetro en el receptor
2
>>> s.count('a')
5
>>> s.index('b') # En que posicion esta la primera 'b'
1
>>> s.index('b',2)  # ...a partir de la posicion 2
8
>>> s.startswith('abra')
True
>>> s.endswith('abra')
True
>>> s.capitalize() # primera letra mayúscula
'Abracadabra'
>>> 'ábrete sésamo'.title() # primera letra de cada palabra mayúscula
'Ábrete Sésamo'
>>> 'ábrete sésamo'.title().swapcase() # invierte mayúsculas y minúsculas
'áBRETE sÉSAMO'
>>> s.upper() # todo a mayusculas
'ABRACADABRA'
>>> 'AbRaCaDaBra'.lower() # todo a minúsculas
'abracadabra'
>>> 'abracadabra'.split('a')
['', 'br', 'c', 'd', 'br', '']
>>> 'hola tu que tal'.split()
['hola', 'tu', 'que', 'tal']
>>> '-'.join(['hola', 'tu', 'que', 'tal'])
'hola-tu-que-tal'
>>>  s.replace('a', 'o')
'obrocodobro'
>>>  s.replace('ab', 'XXX')
'XXXracadXXXra'
```

Objetos de tipos diferentes pueden tener métodos con el mismo nombre,
lo cual tiene sentido si hacen cosas conceptualmente similares
aunque la implementación sea distinta para cada tipo.

Por ejemplo, los métodos `count` y `index`, que tiene `str`,
también los tienen los otros tipos secuencia, `tupla` y `list`.
Tienen el mismo nombre y se usan igual,
facilitando así el aprendizaje por analogía.
Como estan definidos en clases distintas pueden tener el mismo nombre
y tener implementaciones distintas.


## Rellenando textos con valores, el método `format`

Un método muy usado del `str` es el metodo `format`.
Permite rellenar un texto con valores del programa como si fuera una plantilla.
El texto tiene que marcar los sitios donde introducir
los valores con corchetes `{}`.

```python
>>> 'El resultado es {}'.format(4)
'El resultado es 4'
>>> '{} tiene {} puntos'.format('Aitor', 14)
'Aitor tiene 14 puntos'
```

Dentro de los corchetes podemos especificar que y como queremos rellenar.
Por ejemplo, poniendo un número, podemos alterar el orden,
o repetir un valor.

```python
>>> '{0} tiene {1} puntos. ¡Felicidades, {0}!'.format('Aitor', 14)
'Aitor tiene 14 puntos. ¡Felicidades, Aitor!'
```

Usar los índices es muy práctico cuando la cadena a rellenar viene de una traducción.
Idiomas diferentes pueden tener los huecos en ordenes diferentes.

Cuando tenemos muchos parámetros que rellenar,
seguirle la pista a cual es cual se vuelve complicado.
Por eso, a menudo es util usar claves para rellenarlo.
Fíjate en este ejemplo como le estamos pasando los parámetros.

```python
>>> '{nombre} tiene {puntos} puntos. ¡Felicidades, {nombre}!'.format(
... 	nombre='Aitor', puntos=14)
'Aitor tiene 14 puntos. ¡Felicidades, Aitor!
```

Una segunda parte del indicador es el formato.
Podemos hacer virguerias decidiendo como se representan los números.
Por ejemplo, dos decimales rellenados por la derecha con ceros,
y todo el numero ocupando mínimo de 8 posiciones rellenadas por la izquierda con 0:

```python
>>> 'El saldo al dia de hoy es {saldo:08.02f}€'.format(saldo=34.2)
'El saldo al dia de hoy es 00034.20€'
```

**Ojo:**
Cuando formatees dinero de esta manera.
El redondeo no se hace como debería de hacerse a ley:
un 5 hacia arriba.
Aquello típico de aplicar el IVA a una cantidad con 50 céntimos:

```python
>>> '{saldo:.02f}€ {saldo:.04f}€'.format(saldo=2.50*1.21)
'3.02€ 3.0250€'
```

Sobre el problema de representar dinero, hablaremos más adelante.

Puedes encontrar más detalles sobre el mini lenguaje de formateo en el
[manual de referencia](https://docs.python.org/3/library/string.html#format-specification-mini-language)


# Tomando decisiones

Programar es dejar que el ordenador tome sus decisiones.
El programa define que acciones tomar según lo que
se encuentre en cada momento.
Es lo que dota de inteligencia al ordenador.
Según los parámetros que le llegan al programa,
calcular un _sí_ o un _no_ a cada acción posible.

En esta unidad,
veremos como obtener y manipular valores booleanos, síes y noes,
y como hacer depender el curso del programa de dichos valores.

## Tipos booleanos

Los booleanos son valores que representan condiciones,
cosas que pueden ser bien ciertas o bien falsas.

El tipo booleano (`bool`) solo tiene dos valores posibles
representados por los literales `True` y `False`.

## Operadores de comparación

Una forma de obtener booleanos es comparando valores.

Los **operadores relacionales**
(`<`, `>`, `<=`, `>=`, `==`, `!=`)
devuelven `True` o `False`
dependiendo de la relación de menor a mayor que tengan.

```python
>>> a = 3
>>> 1<a  # operador de inequalidad 'menor que'
True
>>> 10<a
False
>>> 1 <= a <= 10    # ¿es a un numero del 1 al 10, ambos incluidos?
True
>>> 'alfredo' < 'benito'  # orden alfabético
True
>>> 'alfredo' == 'alfredo' # igualdad
True
>>> 'alfredo' != 'alfredo' # desigualdad
False
```

**Operadores de identidad:**
`is` y `is not` deciden si un objeto es el mismo o no.
Para los tipos básicos (numeros, textos...),
estos dos operadores serían equivalentes al operador de igualdad `==` y desigualdad `!=`.
Eso sí, son mucho más expresivos porque conseguimos frases casi en inglés como estas:

```python
>>> guy = 'alf' + 'redo'
>>> guy is 'alfredo'
True
>>> guy is not 'alfredo'
False
```

La diferencia ente igualdad e identidad la encontraremos con
los valores tipo estructura, como las listas, los diccionarios...

- Dos estructuras pueden contener los mismos valores (serían iguales) pero cada una mantendría su identidad independiente.
- Una estructura puede cambiar de valor (su contenido no sería igual en el tiempo) pero mantendría su identidad.

```python
>>> l1 = [1,2,3]
>>> l2 = l1       # l1 y l2 apuntan al mismo objeto
>>> l3 = [1,2,3]  # l3 es un objeto distinto con el mismo contenido que l1
>>> l1 == l2  # Son el mismo objeto, así que tienen el mismo contenido
True
>>> l1 == l3  # No son el mismo objeto, pero aun tienen el mismo contenido
True
>>> l1 is l2  # Son de hecho el mismo objeto
True
>>> l1 is l3  # No son el mismo objeto, aunque tengan el mismo contenido
False
```

## Tomando decisiones, la sentencia condicional `if`

Una de las utilidades de los booleanos es la capacidad
de ejecutar o no código dependiendo de una condición.

La sentencia `if` nos permite ejecutar una serie de subsentencias
solo si se cumple una condición:

```python
if name is 'Aitor':
	print ('Hola Aitor, bienvenido a casa')
if name is not 'Aitor':
	print ('Hola, desconocido, ya te puedes pirar')
```


## Considerando alternativas, `else` y  `elif`

Es frecuente, como en el ejemplo anterior,
que, después de evaluar una condición para ver si tenemos que hacer algo,
tengamos que evaluar lo contrario para hacer otra cosa alternativa.
Para ello es muy útil la sentencia `else`.
Hay que ponerla al nivel del `if` y contiene su bloque de sentencias
que se ejecutarán si la condición del if no se cumple, la alternativa.

Reescribiendo el ejemplo anterior solo evaluando una condición:

```python
if name is 'Aitor':
	print ('Hola Aitor, bienvenido a casa')
else:
	print ('Hola, desconocido, ya te puedes pirar')
```

También es común que haya más de una alternativa.
Para elegir entre ellas podríamos anidarlas así:


```python
if name is 'Aitor':
	print ('Hola Aitor, bienvenido a casa')
else:
	if name is 'David':
		print ('Hola David, Aitor llegará en un momento.')
	else:
		print ('Hola, desconocido, ya te puedes pirar')
```

Pero el código acaba quedando bastante rockambólico.
Para ordenar mejor este tipo de código
sirve la sentencia `elif` (viene de _else if_).

```python
if name is 'Aitor':
	print ('Hola Aitor, bienvenido a casa')
elif name is 'David':
	print ('Hola David, Aitor llegará en un momento.')
else:
	print ('Hola, desconocido, ya te puedes pirar')
```

Podemos poner los `elif` que queramos antes del `else` final
e incluso no poner el `else`.

> **Ejercicio:**
>
> - Añade una condición más al ejemplo anterior.
> - Prueba que pasa si le quitamos el `else`, ¿se lo traga? ¿qué hace?



## Expresiones condicionales, `if` en modo expresión

A menudo usamos el if para decidir un valor.
Por ejemplo:

```python
if condicion:
	valor = valor1
else:
	valor = valor2
```

Sin embargo hay una construcción del lenguaje que nos permite
crear una expresión cuyo valor depende de la condicion.
Se hace así:

```python
valor = valor1 if condicion else valor2
```

> **Ejercicio:**
> Construye una sola expresion que dependiendo de el tipo de producto (una variable dada `esPrimeraNecesidad`)
> llame a la función `aplicaIva` con el porcentaje de IVA que toca (7% o 21%).
> Es decir, el resultado de la expresion `if-else` no se va asignar a una variable
> sino que lo vas a pasar directamente como parámetro a una función.


## Decisiones complejas, operadores booleanos

Los booleanos se pueden combinar en expresiones mediante los operadores booleanos `or`, `and` y `not`.

```python
annaQuiereConducir = True
toniQuiereConducir = False

annaConduce = annaQuiereConducir and (not toniQuiereConducir)
toniConduce = toniQuiereConducir and (not annaQuiereConducir)
losDosQuieren = annaQuiereConducir and toniQuiereConducir
ningunoQuiere = (not annaQuiereConducir) and (not toniQuiereConducir)
loEchamosASuerte = losDosQuieren or ningunoQuiere
```

Los valores resultantes de los operadores
se indican esta tabla de verdad:

`a`       | `b`     | `a or b`   | `a and b`  | `not a`
--------- | ------- | ---------- | ---------- | ---------
`True`    | `True`  | `True`     | `True`     | `False`
`True`    | `False` | `True`     | `False`    | `False`
`False`   | `True`  | `True`     | `False`    | `True`
`False`   | `False` | `False`    | `False`    | `True`

La regla es:

- el `or` es cierto si cualquier operando es cierto.
- el `and` es cierto si todos los operandos son ciertos.

o al revés:

- el `and` es falso si cualquiera de los operandos es falso.
- el `or` es falso si todos los operandos son falsos.

Vemos que para el `or`, `True` es dominante:
Con que solo alguno de los operandos fuera `True`,
el resultado es `True`.
Y que para que el débil, `False`, acabe ganando, por decirlo así,
los dos operadores han de ser `False`.

Lo contrario pasa con el `and` que tiene como dominante el `False`.
Basta con que uno de los operadores sea `False`, el resultado es `False`.
Para obtener el resultado débil, `True`, los dos han de ser `True`.

Quédate con el concepto de dominancia que lo recuperaremos después.

## Equivalencias lógicas

Es muy importante que conozcamos equivalencias,
de cara a manipular el código.
A veces, podemos simplificar el código aplicándolas
y conociéndolas podremos saber que podemos cambiar y lo que no.

Todos los operadores relacionales que vimos se pueden expresar
en términos de un solo operador de inequalidad (`<`, `<=`, `>` o `>=`)
combinados mediante operadores lógicos.
Algunos ejemplos expresados en términos del `<`:

```python
# Para qualquier número como a o b
>>> (a > b) is (b < a)  # invertimos el orden de los operandos
True
>>> (a >= b) is not(a < b) # es el complementario, negamos
True
>>> (a != b) is ((a < b) or (b < a)) # si es mayor o menor no es igual
True
```
> **Ejercicio:**
> Faltan `<=` y `==`. ¿Te atreves?

Cuando manipulamos expresiones booleanas,
también hay algunas equivalencias.

- `not not a == a` (Doble negación)
- `not(a and b) == (not a or not b)` (De Morgan)
- `not(a or b) == (not a and not b)` (De Morgan)
- `(a and b) == (b and a)`  (Conmutativa)
- `(a or b) == (b or a)`  (Conmutativa)
- `a or (b and c) == (a or b) and (a or c)` (Distribuitiva)
- `a and (b or c) == (a and b) or (a and c)` (Distribuitiva)
- `a and (b and c) == (a and b) and c` (Asociativa)
- `a or (b or c) == (a or b) or c` (Asociativa)


> **Ejercicio:**
> Comprueba con una tabla de verdad que estas expresiones son equivalentes

Las equivalencias del anterior ejercicio
nos van de coña para simplificar las condiciones
y mejorar la calidad del código.
Es decir, hacer un refactoring, que veremos más adelante.

> **Ejercicio:**
> De Morgan se resume como: negar un operador booleano,
> equivale a usar el otro operador con los operandos negados.
>
> - Aplica DeMorgan a las expresiones que usamos para calcular:
> `annaConduce`, `toniConduce`, `losDosQuieren` y `ningunoQuiere`.
> - Elimina las dobles negaciones resultantes.
> - Lee las expresiones a ver si, por lógica, aún tienen sentido.
> - Quédate con las reescrituras que simplifiquen la expresión.

Es notable las diferentes formas de entender los booleanos.

Una forma de verlos es como numeros con dos únicos valores:
0 (`False`, nada) y
1 (`True`, algo, cualquier número positivo diferente de cero).
El `and` es la multiplicación y el `or` es la suma.

- `1 + 1 = 1`  (algo más algo, da algo)
- `1 + 0 = 1`  (algo más nada, da algo)
- `0 + 0 = 0`  (nada más nada, da nada)
- `1 * 1 = 1`  (algo por algo, da algo)
- `1 * 0 = 0`  (algo por nada, da nada)
- `0 * 0 = 0`  (nada por nada, da nada)

Y otra forma de verlos: como interruptores de un circuito eléctrico
que a su vez estan activados o no por otros circuitos eléctricos.

TODO: Diagramas

- Una `or` son interruptores en paralelo: Con que uno de los dos esté encendido pasa la luz.
- Una `and` son interruptores en serie: Los dos tiene que estar encendidos para que pase la luz.
- Un `not` es un interruptor que se apaga cuando le llega corriente, al revés que los normales.

De hecho esta idea se parece mucho a la implementación electrónica
de los ordenadores.

## Evalua con cortocircuito o muere

Cuando hablabamos del valor dominante de un operador booleano,
dijimos que es un concepto que nos iba a ser útil.
Veamos porqué.

Cuando Python evalúa una expresion `or` o `and`,
listo y vago como él solo,
si ve que el primer operando evalúa al valor dominante del operador,
se escaquea y ya no calcula el segundo operando.
Total, ya sabe lo que va a dar, ¿no?

Por ejemplo:

```python
>>> a=3; b=6; c=9
>>> (a < b) or (c > a)
```

La primera expresión `a < b` es `True`,
que es el valor dominante para `or`.
Así que, Python, sin llegar a calcular el segundo operando,
dice que toda la expresión es `True`, y no se come la olla.
Lo que fuera a dar la segunda parte, `True` o `False`,
no le quita el sueño.
No lo calcula, finito.

Esto se llama _evaluación por cortocircuito_,
y se hace para acelerar la ejecución de los programas.

Si además lo sabemos, podemos aprovecharlo:

- Se puede poner primero
la expresión más barata de calcular para ahorrarnos
evaluar la más cara en algunos casos,
cuando la barata evalúe a dominante.

	```python
	>>> noCuestoMuchoYAVecesSoyFalso() and cuestoMuchoDeCalcular()
	```

- O si las dos son más o menos igual de caras,
pero una sabemos que evalua dominante más a menudo,
ponemos esa primero para la mayor parte de las veces
ahorrarnos evaluar una de las dos.

	```python
	>>> evaluoMuchoACierto() or yoNoTanto()
	```

En los ejemplos anteriores los operandos son llamadas a funciones,
dando a entender que
_'vete a a saber qué cálculos más complejos hacen'_.

**¡Ojo si en esas funciones tienen efectos
laterales que sean necesarios!**

Un bug frecuente y difícil de encontrar,
es que hayamos colocado en el segundo operando de un operador booleano
una llamada a función que haga algo que necesitamos hacer siempre,
evalúe el primer operando a `True` o a `False`.


Suele pasar que, cuando alguien hace algo por algún motivo,
por ejemplo, que el programa vaya más rápido evaluando en cortocircuto,
siempre sale alguien que lo utiliza para otra cosa.
Mucha gente aprovecha los cortocircuitos 
para como construcciones condicionales.
Normalmente los abusos del lenguaje suelen ser feos,
pero la verdad es que estos abusos quedan bastante expresivos (y barriobajeros):

```python
# Barriobajeras? claro:
giveMeTheMoney or die("you sucker")
touchMe and die("you dared shit")

# En realidad se usan asi:

condicionNecesaria or die("No se ha dado la condición necesaria para seguir!!")
# equivalente a:
if not condicionNecesaria :
	die("No se ha dado la condición necesaria para seguir!!")

condicionDeError and die("Se ha dado la condición de error!!")
# equivalente a:
if condicionDeError:
	die("Se ha dado la condición de error!!")
```

Donde `die` es una función que imprime el mensaje y sale del programa.
El cortocircuito de evaluación hace que la función `die` no se ejecute
si `condicionNecesaria` es `True` o si `condicionDeError` es `False`.

En resumen:

- La evaluación por cortocircuito deja de evaluar el segundo operando, si evaluando el primero ya se conoce el resultado.
- Se hace para optimizar, y podemos potenciar su efecto escogiendo el orden de los operandos.
- Es fuente frecuente de errores, si ponemos un segundo operando con efectos laterales necesarios. Porque se nos olvide que se ejecuta con cortocircuito, o porque se nos olvide que tiene dichos efectos.
- También se (ab)usa la evaluación por cortocircuito como alternativa _expresiva_ a los `if`.


## Operadores booleanos con operandos no booleanos

Los operadores booleanos también se usan con valores no booleanos.
Cuando los usamos así en cada tipo, ciertos valores que se evaluan como `False`
y el resto como `True`.

Los valores que se consideran `False` son:

- `False` (¡Por su puesto!)
- `None`
- Los ceros de los tipos numéricos: `0`, `0.0`, `0j`
- Los valores vacíos: `""`, `[]`, `()`, `{}`, `set()`

A menudo se usa este hecho
combinado con los cortocircuitos lógicos
para hacer expresiones condicionales más sencillas.
Por ejemplo, se usan mucho expresiones como la siguiente
para dar valores por defecto en caso de que no haya:

```python
miApellido = apellidoPaterno or 'Expósito'
```

Si `apellidoPaterno` es un texto no vacío por cortocircuito
`miApellido` adoptará ese valor.
En cambio, si soy huérfano y `apellidoPaterno` está vacío o es `None`,
me llamaré `Expósito`.

Cabe destacar que aquí no se está convirtiendo los otros tipos a tipos `bool`.
Simplemente los operadores booleanos usan la lógica por cortocircuito
para escoger que operando eligen:

- Si el primer operando es el dominante para el operador, escógelo
- Si no, escoge el segundo (sea o no dominante)

> **Ejercicio:**
> Piensa los resultados de estas expresiones y compruébalas luego con el intérprete:
> 
> ```python
> 'algo' or 'otro'
> [] or (3,3)
> [] or {}
> '' and 5
> 5 and 'algo'
> 5 and None
> ```

## Recopilando

Hemos visto que:

- La sentencia `if` (con ayuda de `else` y `elif`) permiten tomar la decisión de si ejecutar un grupo de sentencias o otro dependiendo de valores booleanos.
- Cuando de la decisión solo depende un valor, podemos usar una expresión `if-else` en vez de una sentencia.
- Podemos obtener booleanos comparando valores entre sí.
- Podemos combinar booleanos con `not`, `and` y `or` para tomar decisiones más complejas.
- Podemos reescribir expresiones complejas usando equivalencias
- Los operadores booleanos se evaluan por cortocircuito. Explotamos este hecho para optimizar, para ir de barriobajero o para generar bugs difíciles de encontrar (ejem).
- Tambien podemos usar otros valores no booleanos como si fueran booleanos dando pie a algunas fórmulas expresivas más.


# Repitiendo cosas, los bucles

En tomar decisiones, no lo tengo claro,
pero si hay algo en lo que los ordenadores
son unos machacas es en repetir cosas.

En esta unidad veremos diferentes formas de repetir cosas.
Con `while`, con `for`, con llamadas recursivas...
También veremos como controlar el flujo del bucle
en casos excepcionales.


## Bucles condicionales, sentencia `while`

La sentencia `while` ejecuta las subsentencias
mientras que una condición sea cierta.

El siguiente código imprime las potencias de 2 menores que 50:

```python
>>> a = 1
>>> while a < 50:
...     print(a)
...     a *= 2
...
1
2
4
8
16
32
```

Este código se ejecuta de la siguiente manera:

- La variable `a` se inicializa a `1`
- Se evalua la condición `a<50`
- Como es cierta se procede a ejecutar las subsentencias
- La primera sentencia del bucle imprime el valor actual de `a`
- La segunda sentencia del bucle actualiza `a` multiplicando el valor por 2
- Cuando se acaban las subsentencias se vuelve a evaluar la condición con el nuevo valor de `a`.
- Como la expresión, con el nuevo valor actualizado, sigue siendo `True`, sigue.
- Después de la vuelta en que `a` pasa a valer `64`, la condición evalua `False`, y se sale de la sentencia `while`
- Fuera de la función `a` valdra `64` aunque no se haya llegado a imprimir ese valor.

Cada vez que la ejecución entra en las subsentencias se llama una **iteración**.
Diremos pues que el **bucle** ha dado 6 iteraciones.


## Llamándose a sí mismo, recursividad

La recursividad es otra forma de repetir las cosas,
de basar un caso en un caso más simple.

El ejemplo típico es una función factorial.
El factorial de 5 se puede resolver multiplicando 5 por el factorial de 4,
el de 4 multiplicando 4 por el factorial de 3,
y así hasta que llegamos al factorial de 0 que es 1.

En un bucle normal lo podemos calcular así:

```python
def factorial(n) :
	f = 1
	while n>0
		f *= n
		n -= 1
	return f

>>> factorial(5)
120
```

Otra forma de hacerlo es la recursividad.
Hacer que la función retorne algo basado en el resultado de llamarse a si misma con otros paràmetros:

```python
def factorial(n)
	if n is 0 : return 1
	return n*factorial(n-1)
```

A menudo la recursión es mucho más simple.
Solo hay que tener en cuenta que siempre hay que tener un caso,
el caso básico, que no se resuelve por recursión
y al que siempre acabamos llegando.
En este caso, cuando llegamos al 0, retornamos 1.

> **Ejercicio:**
> Prueba quitarle el caso base y ejecutarlo, ¿que pasa?

> **Ejercicio:**
> Vuelve a ponerle el caso base y pruébalo con un número negativo.
> ¿Como arreglarías la función para estos casos?

Cualquier iteración se puede resolver de forma recursiva y al revés.
En cada caso hay que evaluar cual es la versión más sencilla, de escribir y de entender.


## Bucles sobre iterables: sentencia `for`-`in`

La verdad es que la sentencia `while` apenas se usa,
porque en Python la verdadera reina es la sentencia `for`.
La sentencia `for` permite repetir sentencias para cada
uno de los elementos de un texto, o una lista o...
cualquier cosa que tenga elementos en los que iterar.

Por ejemplo, el algoritmo de las animadoras,
itera sobre las letras de una palabra:

```python
>>> def animadora(palabra):
... 	for letra in palabra:
... 		print("¡Dame una {}!".format(letra))
... 	print("¡{}!".format(palabra))
...
>>> animadora("abracadabra")
¡Dame una a!
¡Dame una b!
¡Dame una r!
¡Dame una a!
¡Dame una c!
¡Dame una a!
¡Dame una d!
¡Dame una a!
¡Dame una b!
¡Dame una r!
¡Dame una a!
¡abracadabra!
```

La sentencia `for`, tiene la estructura:

```python
for variable in expresion:
	sentencias
```

Si la _expresión_ resulta en algo que contenga elementos,
las _sentencias_ se ejecutan para cada elemento,
asignado dicho elemento a la _variable_.

Otro ejemplo con una lista de textos:

```python
>>> for nombre in ['Aitor', 'Victor', 'Raúl', 'David']:
... 	print("{} es socio de GuifiBaix".format(nombre))
Aitor es socio de GuifiBaix
Victor es socio de GuifiBaix
Raúl es socio de GuifiBaix
David es socio de GuifiBaix
```

La potencia del `for` radica en que se puede aplicar
a cualquier cosa que nos ofrezca elementos en los que iterar.
Y eso son muchas cosas en Python, como veremos.



## Salidas prematuras: sentencias `break` y `continue`

Las sentencias `break` y `continue` sirven para alterar la ejecución normal de un bucle.
Clásicamente se considera que usar este tipo de sentencias es una abominación para la programación formal.
**Bien usadas, ayudan a que el código sea mucho más entendible.
Mal usadas, sí, pueden complicarlo abominablemente.**

La sentencia `continue`, sirve para saltar a la siguiente iteración.
Si se ejecuta una sentencia `continue`, lo que quede de sentencias de esa iteración, ya no se ejecutará.

Volviendo al ejemplo de las animadoras.
Las animadoras francesas saben que la gente se rie cuando pronuncian la 'r',
así que directamente se la cuelan y dejan que las demas animadoras la digan:

```python
>>> def animadoraFrancesa(palabra):
... 	for letra in palabra:
... 		if letra is 'r':
... 			continue
... 		print("¡Dame una {}!".format(letra))
... 	print("¡{}!".format(palabra.replace('r','g')))
...
>>> animadoraFrancesa("rabo")
¡Dame una a!
¡Dame una b!
¡Dame una o!
¡gabo!
```

La otra sentencia corta rollos es `break`.
Es más contundente que `continue`,
pues no solo corta la iteración en curso,
sinó para todas las iteraciones siguientes.


```python
>>> def animadoraFrancesaEscarmentada(palabra):
... 	for letra in palabra:
... 		if letra is 'r':
... 			print("Basta ya de greigos, ¡me vuelvo a mi país!")
... 			break
... 		print("¡Dame una {}!".format(letra))
... 	print("¡{}!".format(palabra.replace('r','g')))
...
>>> animadoraFrancesaEscarmentada("abracadabra")
¡Dame una a!
¡Dame una b!
Basta ya de greigos, ¡me vuelvo a mi país!
¡abgacadabga!
```

De hecho no tiene sentido que si salimos por un `break` despues diga la palabra.
El `else` en una iteración se ejecuta cuando se sale normalmente del bucle.
Es decir, cuando no hacemos un `break`.

```python
>>> def animadoraFrancesaEscarmentada(palabra):
... 	for letra in palabra:
... 		if letra is 'r':
... 			print("Basta ya de greigos, ¡me vuelvo a mi país!")
... 			break
... 		print("¡Dame una {}!".format(letra))
... 	else:
... 		print("¡{}!".format(palabra.replace('r','g')))
...
>>> animadoraFrancesaEscarmentada("casa")
¡Dame una c!
¡Dame una a!
¡Dame una s!
¡Dame una a!
¡casa!
>>> animadoraFrancesaEscarmentada("abracadabra")
¡Dame una a!
¡Dame una b!
Basta ya de greigos, ¡me vuelvo a mi país!
```


Hay una tercera forma de abortar la ejecución de un bucle si estamos dentro de una función o método.
De hecho ya la hemos visto: la sentencia `return`.
Al salir de la función, interrumpe cualquier tipo de iteración.
Es una buena estrategia para funciones y métodos de búsqueda.

```python
>>> def animadoraFrancesaPerspicaz(palabra) :
... 	for letra in palabra.lower():
... 		if letra is 'g':
... 			print("Ey, peña, no nos cachondeemos de los acentos")
... 			return
... 	for letra in palabra:
... 		print("¡Dame una {}!".format(letra))
... 	print("¡{}!".format(palabra))
```

> **Ejercicio:**
> Reescribe la función `animadoraFrancesaPerspicaz`
> sustituyendo el primer bucle por una expresión con el operador `in`.


## Intérvalos numéricos, tipo `range`

Una fuente muy usada de elementos iterables para los bucles
son los intervalos o `range`.
Un intérvalo es un objeto que genera números.
No los contiene físicamente, como una `list` o una `tuple`.
Simplemente los genera cuando se los pide un `for`.

Lo creamos con la función _built-in_ `range`.

```python
>>> for i in range(4):
>>> 	print(i)
0
1
2
3
```

Vemos que, igual que las rebanadas,
empieza en el 0 y no incluye el último.

Podemos indicar un inicio diferente de 0.

```python
>>> for i in range(3,6):
>>> 	print(i)
3
4
5
```

Y, como en las rebanadas, podemos especificar un paso.

```python
>>> for i in range(1,6,2):
>>> 	print(i)
1
3
5
```

Lo bueno de los `range` es que, como hemos dicho,
no contienen los números físicamente.
Así que podrías hacer un `range` de 4 millones de números
y ocuparía tanto como uno de 10.

Ahora, si queremos tener los números,
solo hay que pasarle el `range` al constructor
de `list`, `tuple` o `set`:

```python
>>> list(range(10))
[0,1,2,3,4,5,6,8,9]
>>> set(range(10))
{0,1,2,3,4,5,6,8,9}
>>> tuple(range(10))
(0,1,2,3,4,5,6,8,9)
```

> **Ejercicio:**
> ¿Que pasa si aplicamos un slice (`[ ]`) a un range como haciamos con los textos?
>
> - Haz una hipótesis
> - Comprueba lo que pasa realmente
> - Experimenta hasta que tengas claro el comportamiento
> - Complica los casos de prueba, introduciendo, tanto en el _slice_ como en el `range`, cosas mas complicadas como _pasos_, indices negativos...


> **Ejercicio:**
> ¿Que le pasa a un `range` cuando lo usamos con la función `len`, o el operador `in`?

> **Ejercicio avanzado:**
> Piensa como debe funcionar el objeto range por dentro.
> Sin crear un objeto `range`:
> 
> - Implementa una función `inrange(n, inicio, final, paso)`
>   que devuelva si `n` esta incluido.
> - Implementa una función `rangelen(inicio, final, paso)`
>   que devuelva el número de items.
> - Implementa una función `rangeslice(inicio, final, paso, inicioSlice, finalSlice, stepSlice)`
>   que devuelva el rango resultante de aplicar la rebanada.


> **Ejercicio:**
> ¿Qué pasa si sumas dos `range`?
> ¡Ojo! en este caso no retorna otro `range`.
> ¿Qué retorna? ¿Qué pasa si los intervalos se solapan?
> ¿Qué pasa si multiplicas el `range` por un entero? ¿Te lo esperabas?



# Estructuras de datos

Hasta ahora hemos visto valores muy simples.
Una de las potencias de Python es la facilidad con la que se manejan estructuras de datos más complejas.


## Usando listas, tipo `list`

Las listas (tipo `list`) son secuencias ordenadas de valores.

Los literales de las listas se construyen incluyendo los valores entre corchetes `[]` y separados por comas.
Podemos acceder a los elementos con indices y rebanadas igual que con los textos `str`.

```python
>>> l = [1,2,3,4,5]
>>> l[3]
4
>>> l[-1]
5
>>> l[2::2]
[3,5]
```

Los valores incluidos en la lista pueden ser de tipos diferentes.
Incluso pueden ser otras listas.

```python
>>> # Una lista que contiene listas y algo más
>>> l = [[11,12],[21,22],'ultimo']
>>> l[-1]
'ultimo'
>>> l[1]
[21,22]
>>> l[1][1]
22
```

Podemos usar los operadores numericos como hacíamos con los textos:

```python
>>> [1,2,3] + [4,5,6] # Uniendo dos listas
[1,2,3,4,5,6]
>>> [0]*10  # creando una lista de 10 ceros
[0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
```

Cuando trabajamos con textos, siempre creamos
nuevos valores a partir de los anteriores.
En cambio las listas las podemos modificar
y mantienen su identidad aunque cambien su valor.

```python
>>> l = [1,2,3,4]
>>> l2 = l   # l2 apunta a la misma lista
>>> l.append(5)  # añadir un elemento
>>> l2   # el cambio afecta a l2
[1,2,3,4,5]
>>> l.extend([6,7]) # le añadimos los elementos de otra lista
>>> l2
[1,2,3,4,5,6,7]
>>> del l[::3] # borra un elemento cada 3
>>> l2
[2,3,5,6]
>>> l.insert(0,1) # en la posicion 0 inserta un 1
>>> l.insert(3,6) # en la posicion 3 inserta un 4
>>> l2
[1,2,3,6,5,6]
>>> l[3] = 4  # modificar directamente un valor
>>> l2
[1,2,3,4,5,6]
>>> l3 = [1,2,3,4,5,6]  # Una lista diferente con los mismos valores
>>> l is l3 # No son la misma lista
False
>>> l == l3 # pero tienen los mismos valores
True
>>> l is l2  # estas dos si que apuntan a la misma lista
True
>>> l4 = l[:]  # Un slice es una copia, aunque sea entera
>>> l is l4
False
>>> # Atencion a los problemas de alias
>>> l += [7]   # la suma asignada afecta a l2
>>> l2
[1,2,3,6,5,6,7]
>>> l = l + [8,9]  # en cambio si asignamos a la suma
>>> l
[1,2,3,6,5,6,7,8,9]  # creamos una lista nueva diferente
>>> l2
[1,2,3,6,5,6,7]  # y dejamos la original como estaba, aun accedible desde l2
```


## Uniendo y separando, métodos `split` y `join`

Dos operaciones muy comunes son dividir un texto usando
un separador obteniendo una lista de textos,
o al revés, dada una lista juntarla con un separador.

Para ello usaremos los métodos `join` y `split` del tipo `str`.


```python
>>> l = ['a','b','c']
>>> s = '-'.join(l) # Las juntamos con el '-'
>>> s
'a-b-c'
>>> s.split('-') # Usamos el '-' como separador
['a','b','c']
```


El constructor de lista recibe un iterable.
Como los textos son iterables, crea una lista con cada letra como elemento.

```python
>>> list('abc') # Separamos por letras
['a','b','c']
>>> str(['a','b','c'])   # Lo contrario no funciona igual
"['a', 'b', 'c']"
>>> print(['a', 'b', 'c']) # str esta pensado para el print
['a', 'b', 'c']
>>> ''.join(['a','b','c']) # Para juntarlas, con la cadena vacia como separador
'abc'
```

> **Ejercició:** Haz un script que dada una lista de listas,
> que representa lineas de columnas,
> imprima por pantalla un CSV con el tabulador como separador.
>
> ```python
> #!/usr/bin/env python3
>
> tabla = [
> 	[
> 		'11',
> 		'12',
> 		'13',
> 		'14',
> 	],
> 	[
> 		'21',
> 		'22',
> 		'23',
> 		'24',
> 	],
> ]
> for linea in tabla:
> 	print('\t'.join(linea))
> ```

> **Ejercició:** Haz un script que dado un texto CSV,
> Obtenga una tabla de filas y columnas
>
> ```python
> #!/usr/bin/env python3
>
> csv = (
> 	"11\t12\t13\t14\n"
> 	"21\t12\t13\t14\n"
> 	)
> tabla = []
> for linea in csv.split('\n'):
> 	columnas = linea.split('\t')
> 	tabla.append(columnas)
> print(tabla)
> ```
>
> La solución anterior tiene un problema, la ultima linea vacia, fíltrala con un `continue`.




## Listas del tirón, _comprehension lists_

Si quisieramos crear una nueva lista con los valores que antes hemos imprimido:

```python
>>> l = [1,2,3,4]
>>> l2 = []
>>> for item in l:
...     l2.append(item*2)
>>> l2
[2,4,6,8]
```

Python ofrece una forma directa de crear listas a partir de otras listas,
las _comprehension lists_, o listas creadas del tirón.

```python
>>> l = [1,2,3,4]
>>> l2 = [ item*2 for item in l ]
>>> l2
[2,4,6,8]
```

La mayoría de lenguajes no tienen construcciones como esta.
Si es la primera vez que ves una de estas, mejor que la expliquemos.

- Una _comprehension list_ es una expresión que genera una lista.
- Empieza y acaba con `[]` como los literales de la lista.
- Tiene la estructura: `[` _expresion_ `for` _variable_ `in` _iterable_ `]`
	- _iterable_ es una fuente de items (una lista, un texto...)
	- _expresion_ se evaluará para generar los elementos de la nueva lista a partir de cada elemento del iterable
	- esa expresion puede usar la _variable_ que contendrá el correspondiente elemento del iterable

**Ejercicio:**
A partir de un texto CSV con tabuladores, genera una tabla.


```python
#!/usr/bin/env python3

csv = """\
11\t12\t13\t14
21\t22\t23\t24
31\t32\t33\t34
"""

tabla = [
	line.split('\t')
	for line in csv.split('\n')
	]
print tabla
```

Problema la linea vacia del final.
Las _comprehension lists_ tienen una parte opcional que les permite
filtrar los items del iterable de entrada.


```python
#!/usr/bin/env python3

csv = """\
11\t12\t13\t14
21\t22\t23\t24
31\t32\t33\t34
"""

tabla = [
	line.split('\t')
	for line in csv.split('\n')
	if line != ''  # filtro
	]
print tabla
```

## Valores empaquetados o tuplas, tipo `tuple`

En python podemos asignar a dos variables a la vez:

```python
>>> a, b = 1, 2
>>> a
1
>>> b
2
```

Por eso no hay la función de `swap`, típica de otros lenguajes,
para intercambiar los valores de dos variables.
En Python se hace simplemente así:

```python
a, b = b, a
```

A sentencias como las de arriba se les llama desempaquetar una tupla.
Por tupla nos referimos a la parte derecha:
Dos valores separados por una coma.

Una tupla de hecho es otro tipo de dato (`tuple`),
muy parecido a una lista, pero no permite modificar su contenido.
Como con los textos, podemos generar una a partir de otra, pero no modificar la existente.
Sus literales son como las listas pero sin corchetes.
A menudo se necesitan paréntesis cuando se usan en sitios donde podría haber comas:
como parámetro de una función, dentro de un literal de lista...
Así que por si acaso siempre se ponen los paréntesis,
al menos que como en la expresión de arriba sea muy claro.

Tambien podemos desempaquetar listas:

```python
>>> a, b = [3, 4]
>>> a
3
>>> b
4
```

Podemos crear una lista, a partir de una tupla y al revés usando los constructores:

```python
>>> t = 2, 4, 6
>>> t
(2,4,6)
>>> t1,t2,t3 = t   # desempaquetando
>>> list(t)
[2,4,6]
>>> list( (2,4,6) )   # el literal requiere paréntesis si es un parámetro
[2,4,6]
>>> tuple(list( (2,4,6) ) )
(2,4,6)
```

Las tuplas son muy útiles cuando funciones retornan más de un valor.
Por ejemplo la función _built-in_ `divmod` retorna la división entera
y el resto a la vez evitando tener que calcular dos veces la división.

```python
>>> div, mod = dm = divmod(30,7)
>>> dm
(4,2)
>>> div
4
>>> mod
2
```

Tambien podemos desempaquetar en un `for`:

```python
>>> edades = [
...     ('Antonio', 35),
...     ('Pedro', 15),
...     ('Enrique', 55),
...     ]
...
>>> for nombre, edad in edades:
...     print("La edad de", nombre, "es",edad)
...
La edad de Antonio es 35
La edad de Pedro es 15
La edad de Enrique es 55
```

**Ojo:**
El desempaquetado debe hacerse solo cuando estamos seguros de que
el numero de valores que aceptamos coincide con el que desempaquetamos.
Si no, veremos errores. Familiaricemonos con ellos, que saldrán:

```python
>>> a,b = 1,2,3  # Nos sobran valores
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
ValueError: too many values to unpack (expected 2)
>>> a,b,c = 1,2  # Nos faltan valores
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
ValueError: need more than 2 values to unpack
```

Qué se puede hacer con una tupla igual que con una lista:

- Iterar sobre ella
- Desempaquetar
- Acceder a índices y rebanadas
- Métodos `index(value)` y `count(value)`
- Multiplicar por un entero
- Sumarse con otro del mismo tipo para obtener un tercero

Qué se puede hacer en una lista que no se pueda en una tupla.
En general modificaciones en el mismo objeto, sin generar un tercero:

- Añadir elementos al mismo objeto: `append`, `extend`, `insert`...
- Eliminar elementos con `del`
- Modificar un elemento del objeto `t[2] = valor` o `t[3:6]= valor1, valor2`

Qué se puede hacer pero tienen resultados distintos:

- `+=` en la lista modifica la lista original a la que apunta la variable.
- `+=` en la tupla genera una tupla nueva y la asigna a la variable.

```python
>>> t = 1,2
>>> t2 = t
>>> t += 3,4
>>> t # Apunta a un valor distinto
(1,2,3,4)
>>> t2 # Aun apunta al anterior valor
(1,2)
```

Es decir, pasa igual que con los textos.
En cambio con listas, como habíamos visto:

```python
>>> l = [1,2]
>>> l2 = l
>>> l += [3,4]
>>> l
[1,2,3,4]
>>> l2
[1,2,3,4]
```


## Diccionarios, tipo `dict`

Un diccionario de Python es una estructura que nos permite acceder a valores a partir de una clave.

Para acceder a los valores usamos la sintaxis de indexación (`[ ]`) con la clave entre los corchetes.

Veamos ejemplos de su uso:

```python
>>> saldos = {
... 	'David': 200,
... 	'Aitor': 500,
... 	}
>>> saldos['David']
200
>>> saldos['Aitor'] += 300
>>> saldos['Aitor']
800
>>> saldos
>>> del saldos['David']  # borramos la clave 'David'
>>> saldos
{'Aitor': 800}
>>> 'Aitor' in saldos  # ¿Tiene la clave 'Aitor'?
True
>>> 'David' in saldos
False
>>> saldos['Victor']  # Accediendo a una clave que no está
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
KeyError: 'Victor'
>>> # El método get permite cogerlo de forma segura
>>> saldos.get('Aitor',0) # Coge el valor y si no está, 0
800
>>> saldos.get('Victor',0)
0
```

Igual que con las listas podemos iterar sobre un diccionario.

```python
>>> for nombre in saldos:
... 	print(nombre)
... 
David
Aitor
```

Observamos dos cosas:

- Iteramos sobres las claves del diccionario, nos faltan los valores
- El orden es indefinido (a ti te saldrá este como podria salir otro)

Si queremos obtener parejas clave-valor, tenemos que usar el método `items`.
Devuelve tuplas clave-valor así que usamos la sintaxis de desempaquetado.

```python
>>> for nombre, saldo in saldos.items():
... 	print(nombre,saldo)
... 
David 200
Aitor 800
```

> **Ejercicio:**
> Modifica el código usando `format` para que diga _El saldo de menganito son XXXX€_.


## Conjuntos, tipo `set`

Un `set` es un contenedor, como lo es una lista, pero con las siguientes diferencias.

- No mantiene un orden entre los elementos
	- no podemos indexarlos, ni slices
	- no nos asegura un orden cuando iteramos en él
- No acepta duplicados
	- Insertar un valor que ya està, no tiene efecto

Los literales del set son como los de las listas, pero usan los corchetes rizados `{}`.

```python
>>> { 1, 2, 3, 1 }  # El 1 esta duplicado
{1,2,3}
>>> set([1,2,3])  # con el constructor lo podemos crear a partir de una lista
{1,2,3}
>>> list({1,2,3})  # y al reves
[1,2,3]
>>> ''.join(set('abracadabra')) # cuantas letras diferentes usa un texto?
'rcabd'
>>> ''.join(sorted(set('abracadabra'))) # no nos aseguran orden, usamos la función sorted
'abcdr'
```

Es muy práctico para algunas cosas:

- Comprobar si un valor esta incluido con el operador `in` o `not in` (la lista también lo tiene pero es más lenta)
- Calcular intersecciones, uniones, y todas aquellas cosas de teoría de conjuntos que hicimos en mates

```python
>>> s1 = set(range(3,9))
>>> s1
{3,5,6,7,8}
>>> 3 in s1  # Comprobando pertenencia
True
>>> 10 in s1
False
>>> 3 not in s1
False
>>> set(range(1,5)).union(range(3,8))  # Union
{1,2,3,4,5,6,7}
>>> set(range(1,5)).intersection(range(3,8))  # Intersección
{3,4}
>>> set(range(1,5)).difference(set(range(3,8))  # Diferencia
{1,2}
```

TODO: Diagramas de conjuntos


## Diccionarios y conjuntos _del tirón_

Vimos que teníamos la sintaxis _del tiron_ para construir listas
en la que obteniamos los elementos de la lista nueva a partir de una expresión
calculada en base de los elementos de otro iterable.

También existe una sintaxis para crear diccionarios y conjuntos del tiron.
Por analogía, si para la lista usabamos los corchetes planos (`[ ]`),
para los conjuntos usaremos corchetes rizados (`{ }`).

```python
>>> firstSquares = { x*x for x in range(1,10) }
>>> firstSquares
{1,4,9,16,25,36,49,64,81}
```

Si queremos tener parejas de raiz y quadrado, con un diccionario del tirón:

```python
>>> firstSquares = { x : x*x  for x in range(1,10) }
>>> firstSquares
{1:1,2:4,3:9,4:16,5:25,6:36,7:49,8:64,9:81}
>>> firstSquares[3]
9
```
> **Pregunta:**
> En el código anterior usamos enteros como índices en vez de textos que hemos usado en otros ejemplos.
> En las listas también indexamos con enteros.
> ¿Qué podemos hacer con una lista que no podemos hacer con un diccionario indexado por enteros y al revés?
> Pistas: Rebanadas, orden, huecos en los indices...


> **Ejercicio:**
> Tenemos que retribuir un 2% del saldo de cada socio.
> Calcula _del tirón_ un diccionario con las retribuciones a partir del diccionario de los saldos.
> Ayuda: Dado que el iterable en el que nos basamos tambien es un diccionario,
> hay que usar el método `items` y desempaquetar clave y valor.
> Es decir, dentro de los corchetes habrá algo como: `for nombre, saldo in saldos.items()`

> **Ejercicio:**
> Hay ciertos socios que han renunciado a cobrar retribución.
> Pon a esos socios en un conjunto `antiIntereses`.
> Añade un filtro `if` que filtre los socios que estan en el grupo.


## Llenando parámetros con estructuras (`*` y `**` en llamada)

Recuperemos por un momento uno de los ejemplos del método `format`:

```python
>>> '{nombre} tiene {puntos} puntos.'.format(
... 	nombre='Aitor', puntos=14)
'Aitor tiene 14 puntos.'
```

Imagina que ya disponemos de un diccionario como el siguiente:

```python
>>> data = { 'nombre': 'Aitor', 'puntos': 14 }
```

Para usarlo en esa misma plantilla deberíamos hacer:

```python
>>> '{nombre} tiene {puntos} puntos.'.format(
... 	nombre=data['nombre'], puntos=data['puntos'])
'Aitor tiene 14 puntos.'
```

Existe el operador unario `**`
que permite desempaquetar un diccionario como parámetros por clave
en una llamada a función (o método).

```python
>>> '{nombre} tiene {puntos} puntos.'.format(**data)
'Aitor tiene 14 puntos.'
```


Análogamente, al operador `**`, 
existe el operador unario `*` permite desempaquetar,
en una llamada a función,
listas o tuplas como parámetros posicionales.

```python
>>> # Si tenemos
>>> data = [ 'Aitor', 14 ]
>>> # En vez de hacer
>>> '{0} tiene {1} puntos. ¡Felicidades {0}!'.format(data[0], data[1])
'Aitor tiene 14 puntos. ¡Felicidades Aitor!'
>>> # Podemos hacer
>>> '{0} tiene {1} puntos. ¡Felicidades {0}!'.format(*data)
'Aitor tiene 14 puntos. ¡Felicidades Aitor!'
```

Se puede combinar distintos modos de introducir parámetros en la llamada,
pero siempre, hay que cumplir ciertas normas:

- Los posicionales siempre al principio
- Los de clave y el argumento con `*`, en cualquier orden, en medio.
- El argumento con `**` siempre el último


## Definiendo funciones con parámetros abiertos (`*` y `**` en definición)

Las funciones que hemos definido hasta ahora,
tenian unos parámetros definidos.
Podían ser opcionales, pero eran definidos.
Había unos nombres de parámetros definidos para rellenarlos con claves
y un número mínimo y máximo de parametros para rellenar posicionalmente.

¿Cómo debe estar definida la función `format`
para recibir cualquier número de parámetros posicionales,
y cualesquiera claves en los parámetros con clave?

En una función se pueden definir dos parámetros especiales:

- uno precedido de `*` en la definicion,
  que recibe, en una lista,
  el exceso de parámetros posicionales.
  Por convención llamado `args`, 
- otro precedido de `**` en la definición,
  que recibe, en un diccionario,
  el exceso de parámetros por clave.
  Por convención llamado `kwds`.


```python
>>> def aceptoTodo(estoSiempre, estoAVeces='default', *args, **kwds):
... 	print("estoSiempre:", estoSiempre)
... 	print("estoAVeces:", estoAVeces)
... 	print("args:", args)
... 	print("kwds:",kwds)
>>> aceptoTodo(1)
estoSiempre: 1
estoAVeces: default
args: []
kwds: {}
>>> aceptoTodo(1, 2, 3, 4, 5)
estoSiempre: 1
estoAVeces: 2
args: [3, 4, 5]
kwds: {}
>>> aceptoTodo(1, otro=5, estoAVeces=6)
estoSiempre: 1
estoAVeces: 6
args: []
kwds: {'otro': 5}
```

Como en la llamada, en la definición tambien hay un orden,
más estricto si cabe.

- Primero los parámetros no opcionales
- Después los opcionales
- Después el parámetro con `*`
- Por último, el parámetro con `**`


# Usando generadores

Un generador es un objeto que retorna objetos en los que iterar.
La diferencia con una estructura como la lista
sería que los valores del generador no existen en memoria,
sino que los genera a medida que se los van pidiendo.
De hecho ya hemos visto un tipo de generador, `range`.

En esta unidad vamos a ver unas cuantas maneras de generar valores,
o de modificar los valores provenientes de otros iterables.


## Expresiones generadoras

Hemos visto como las listas tenian las _comprehension lists_,
o listas _del tirón_,
que introducían un `for` dentro de los mismos corchetes planos (`[ ]`)
que usan las listas para los literales.

Análogamente, los `set` y los `dict`, tenían su expresion _del tirón_
con los corchetes rizados (`{ }`).

Sin embargo, si intentamos hacer una tuplas _del tirón_,
con paréntesis el objeto que obtenemos no es una tupla.
Es un generador.

La principal ventaja de usarlos es con volúmenes grandes de datos,
evitando que se creen grandes listas intermedias en memoria.

Analicemos, por ejemplo, este código:

```python
# Busca los cuadrados de los números hasta 999 que acaben en 5
[
	square
	for square in [n*n for n in range(10000)]
	if square % 10 == 5
]
```

En el código de arriba estamos generando una lista de mil cuadrados,
iteramos sobre ella y seleccionamos aquellos que el numero anterior
sea divisible por 10.

El problema es para que generar una lista intermedia, la de los 1000 cuadrados,
que no vamos a usar más.
Ocupamos memoria y hacemos que todo vaya más lento.

En canvio si convertimos la lista interna en una expresion generadora
cambiando los corchetes por paréntesis:

```python
# Busca los cuadrados de los numeros hasta 999 que acaben en 5
[
	square
	for square in (n*n for n in range(1000))
	if square % 10 == 5
]
```

La lista interna de 1000 elementos no se generará, solo la final filtrada de 100 elementos.


## Enumerando elementos, función `enumerate`

Otro generador muy util es `enumerate`.
Dado un iterable, genera tuplas con la posicion y el valor de cada elemento del iterable.

```python
>>> list(enumerate([
... 	'perro',
... 	'gato',
... 	'raton',
... 	]))
...
[(0,'perro'), (1,'gato'), (2,'raton')]
```
Es tremendamente útil cuando en un bucle necesitamos saber la posición de cada elemento.

```python
top5 = [
	'Miguel Jacobez',
	'Los Gansos Rosas',
	'Francisco Ferdinando',
	'Pimientos rojos de chilly picantes',
	'Mermelada de Perlas',
	'',
	]

for i, nombre in enumerate(top5):
	print("En el puesto {}: {}".format(i+1, nombre))
```

**Ejercicio:**
Usa el generador `reversed`, para darle emoción a la lista y acabar por el ganador.
¿Que pasa si lo aplicas antes de `enumerate`?
¿Que pasa si lo aplicas después de `enumerate`?

**Ejercicio:**
Usa el generador `sorted` para ordenar una lista de nombres.
Investiga y experimenta los parámetros de `sorted` hasta que los entiendas.


## Emparejando secuencias, función `zip`

El generador `zip` toma varios iterables y empareja sus valores.

```python
>>> for a, b in zip(range(10), range(10,20)):
... 	print(a, b)
0 10
1 11
2 12
3 13
4 14
5 15
6 16
7 17
8 18
9 19
```

**Ejercicio:**
Reimplementa `enumerate` como una función `enumerate2`
que use `zip`, `range` y `len`.



## Nuestras propias funciones generadoras, sentencia `yield`

Podemos crear nuestros propios generadores con una expresión generadora que ya hemos visto.
Pero en las expresiones generadoras estamos limitados a una sola expresión.
Si queremos hacer algo más complejo tenemos que usar funciones generadoras.

Una función generadora no retorna un valor, retorna muchos,
y lo hace acordandose de por donde iba para cuando se le vuelva a necesitar.

```python
function squares(limit=None):
	n = 0
	while limit is None or n<limit:
		n += 1
		yield n*n
	return
```

La sentencia `yield` (igual que las señales de 'ceda el paso' en inglés)
es similar al `return` en el sentido que devuelve un valor.
Pero a diferencia del `return`, no abandona del todo la función,
solo devuelve el control al llamante temporalmente
y cuando el llamante pide el siguente valor
la función sigue ejecutándose por donde iba.



# Armando una aplicación de línea de comandos

Si has hecho una lectura lineal de este tutorial,
llegado a este punto tendrás un montón de bagaje
que estarás deseando aplicar para hacer algo útil.

Si has saltado directamente hasta aquí, también es correcto.
Hemos puesto enlaces a las anteriores secciones que son necesarias si algo no se entiende.

En esta unidad, vamos a reforzar todo lo anterior al mismo tiempo que
introduciremos conceptos claves para cualquier aplicación como
el uso de librerías,
la lectura y escritura de ficheros,
la toma de argumentos de la línia de comandos...
pero lo vamos a hacer ya desde el punto de vista de una tarea concreta.
Vamos a dejar el intérprete de línea de comandos,
y emprezaremos a armar un script.

Conceptos que introduciremos:

- Argumentos de línia de comandos
- Lectura y escritura de ficheros
- Entrada y salida estándard
- Uso y definición de librerías


## El script mínimo

Partiremos de un script _hola mundo_ como el que habíamos explicado
[en las primeras unidades](Escribiendo y ejecutando scripts).

Crearemos un script con el editor de texto llamado `miscript.py`.
Recuerda usar la codificación UTF-8,
y darle permisos de ejecucion en Linux.


```python
#!/usr/bin/env python3

print('hola mundo')
```

Comprobamos que lo podemos ejecutar desde una consola con:

```bash
$ ./miscript.py
hola mundo
```

## Leyendo un fichero, la función `open`

Creemos un fichero de texto con el editor de texto plano.
Pongamos varias líneas con varias palabras y guardémoslo como `entrada.txt`
en el mismo directorio que estamos trabajando.

Mi fichero `entrada.txt` tiene este contenido:

```
En un lugar de La Mancha cuyo nombre no quiero acordarme,
vivia un fidalgo de aspecto desaliñado que no paraba
de comer ganchitos.

```

El primer ejercicio será que el programa nos enseñe el texto por pantalla.
Como si fuera el comando `cat` de UNIX (o `type` de MSDOS).
Modificaremos nuestro script de la siguiente manera:


```python
#!/usr/bin/env python3
infile = open('entrada.txt')
contenido = infile.read()
print(contenido)
infile.close()
```

Puedes ejecutar el script para ver su resultado.
A la función _built-in_ `open` le pasamos el nombre del fichero a leer.
Retorna un objeto, que guardamos en la variable `infile`,
y que representa el fichero.
En este caso es un fichero de lectura,
del cual podemos leer.
Este objeto nos da métodos para manipular el fichero.
Por ejemplo, `read` nos retorna el contenido íntegro.
Y `close` libera el fichero para que otros usuarios lo usen.

Es muy importante llamar a `close`,
tanto que no lo volveremos a llamar sinó que,
siempre que abramos un archivo, lo vamos a hacer con la sentencia `with`.


## Controlando la vida de los recursos, la sentencia `with`

La sentencia `with` sirve para controlar la vida de los recursos.
Es tan importante llamar a métodos como el `close`
cuando acabamos de usar algun recurso, que no se nos puede olvidar.
Una sentencia `with` nos sirve para asegurar que
ciertas cosas se hacen al acabar.

Usando el `with` con un `open`, 
nos asegura que se llama al `close` cuando salimos del bloque de subsentencias.


```python
#!/usr/bin/env python3
with open('entrada.txt') as infile:
	contenido = infile.read()
	print(contenido)
```

Fíjate, ya no llamamos al `close` y la asignacion de `infile` la hacemos con `as`.
Después de ejecutar la sentencia `print`, el `with` llamará al `close`.
Incluso si alguna sentencia dentro del `with` falla, el `with` llamará al `close`.

Dado que queremos tener los ficheros bloqueados el menor tiempo posible,
una vez que hemos hecho el `read` podríamos ya cerrar el fichero.
Es decir, dejar el `print` fuera del `with`.

```python
#!/usr/bin/env python3
with open('entrada.txt') as infile:
	contenido = infile.read()
print(contenido) # Aquí el fichero ya estaria cerrado
```

## Interpretando la linea de comandos, la lista `sys.argv`

Hemos dicho antes que queríamos hacer un comando `cat`.
Pero al comando `cat` se le pasa el fichero por línia de comandos,
y ahora, si decimos:

```bash
$ ./miscript.py cualquierotrofichero.txt
```

nos ignora; siempre enseña `entrada.txt`.

Para acceder a la línea de comandos,
vamos a usar la librería estándard `sys`.

Hay que indicar que usamos la librería con una sentencia `import`.

```python
import sys
```

Cuando importamos una librería de este modo,
las cosas que estan dentro de la librería son accesibles
con la sintaxis de punto (`.`), por ejemplo,
si importamos `librería` podemos acceder a `librería.cosaDeDentro`.

Importamos `sys`, podemos acceder a la linea de comandos como `sys.argv`.
Es una lista con los elementos de la línea de comandos.
El primer elemento, el 0, siempre es el comando, en nuestro caso `./myscript.py`.
El resto de elementos son los diferentes argumentos que le pasamos.

> **Ejercicio:**
> Para acabar de entender `sys.argv`,
> comenta temporalmente el resto del código menos el `import sys`,
> añade una sentencia `print(sys.argv)`, y
> haz las siguientes pruebas para ver que devuelve:
> 
> ```bash
> $ ./miscript.py
> $ ./miscript.py uno dos tres
> $ ./miscript.py "uno dos" tres
> ```

Así que, si queremos coger el primer argumento de la línea de comandos,
tendremos que acceder a `sys.argv[1]`.
Recuerda que el `0` es el nombre del comando.
Substituimos en nuestro script:

```python
#!/usr/bin/env python3

import sys

with open(sys.argv[1]) as infile:
	contenido = infile.read()
print(contenido)
```

Y lo llamamos con:

```bash
$ ./miscript.py entrada.txt
```

Ahora ya tenemos un `cat`, bueno, casi.

## Gestionando errores de línea de comandos

¿Qué pasa ahora si no le pasamos parámetros a nuestro script?

```bash
$ ./myscript.py
Traceback (most recent call last):
  File "runme.py", line 5, in <module>
    with open(sys.argv[1]) as infile:
IndexError: list index out of range
```

Para nosotros que sabemos Python,
entendemos que estamos accediendo
a los argumentos más allá de los elementos que hay.
Es decir, que accedemos a un argumento 1 que no existe.
Y si no lo ves claro, 
`sys.argv` es una lista, así que repasa la [sección sobre listas](Usando listas, tipo `list`).

Al usuario incauto no le vas a pedir que aprenda Python
para descifrar este mensaje.
Vamos a interceptar el error antes de que pase
y le vamos a avisar como `$DEITY`
^[
Simulando otras variables de entorno configurables reales como `$LANGUAGE`, `$HOME`, `$USER`...
se usa `$DEITY` en coña en los foros de programacion
para de referirse deforma neutra a Dios, Ala, Buda, Ghanesha...
incluso algunos la tenemos definida como `None`.
] manda,
es decir, explicando que el script requiere un argumento.

Para detectar el error vamos a comprobar que la longitud de `sys.argv` sea 2 (el comando y un argumento).

```python
#!/usr/bin/env python3

import sys

if len(sys.argv) != 2 :
	print("Se esperaba un argumento")

with open(sys.argv[1]) as infile:
	contenido = infile.read()
print(contenido)
```

Ups, ahora en caso de error imprime el error pero, tambien el error antiguo.
Podemos poner el resto del código en un `else`:


```python
#!/usr/bin/env python3

import sys

if len(sys.argv) != 2 :
	print("Se esperaba un argumento")
else:
	with open(sys.argv[1]) as infile:
		contenido = infile.read()
	print(contenido)
```

¡Ya lo tenemos!


## Verificando que un fichero existe, función `os.access`

¿Qué pasa cuando el fichero no existe?

```bash
$ ./myscript.py dios.txt
Traceback (most recent call last):
  File "runme.py", line 5, in <module>
    with open(sys.argv[1]) as infile:
FileNotFoundError: [Errno 2] No such file or directory: 'dios.txt'
```

Otra vez hay que adelantarnos a los acontecimientos y detectar el error.
Usaremos la función `access` de la librería `os` (_operating system_)
que nos dice si podemos acceder a un fichero en un determinado modo.
Los modos son los de los permisos del `chmod`:

- `os.R_OK`: Podemos leerlo (_Reading is OK_)
- `os.W_OK`: Podemos escribir (_Writing is OK_)
- `os.X_OK`: Podemos ejecutarlo (_eXecuting is OK_), con los directorios, implica que podemos entrar
- `os.F_OK`: El fichero (_File is OK_) existe, tengamos o no permisos

En nuestro caso, no nos basta con que exista,
queremos poder leerlo, asi que usaremos
`os.R_OK`, (_Reading is OK_).

Antes de pringarnos metiéndolo en el código, un poco de previsión.
Como vamos a usar el nombre de fichero que sacamos de `argv`,
en varios sitios y `sys.argv[1]` es algo bastante ilegible,
primero vamos a reescribir el código anterior para introducir
una variable llamada `infilename`.
La introducimos una vez sabemos que el argumento existe,
es decir, en el `else`.

```python
#!/usr/bin/env python3

import sys

if len(sys.argv) != 2 :
	print("Se esperaba un argumento")
else:
	infilename = sys.argv[1]
	with open(infilename) as infile:
		contenido = infile.read()
	print(contenido)
```
Y ahora si, con la variable definida,
comprobemos que el fichero existe antes de abrirlo.

```python
#!/usr/bin/env python3

import sys
import os # libreria nueva

if len(sys.argv) != 2 :
	print("Se esperaba un argumento")
else:
	infilename = sys.argv[1]
	# condicion de error nueva 
	if not os.access(infilename, os.R_OK) :
		print("No se pudo leer el fichero '{}'".format(infilename))
	else:
		with open(sys.argv[1]) as infile:
			contenido = infile.read()
		print(contenido)
```


## Saliendo del script prematuramente, función `sys.exit`

El estilo de programación de la última versión es bastante... feo.
Más que nada porque si tienes unas cuantas condiciones de error
al final tu script parecerán las cataratas del Niagara
con tanto nivel.
Como siempre, el ordenador lo entenderá pero los humanitos y las humanitas
perderán su preciado tiempo resiguiendo los niveles de indentación.

Lo mejor es hacer una salida prematura.
Para salir prematuramente de una función lo hacíamos con `return`.
Para salir prematuramente de un bucle, lo hacíamos con `break`, o
de una iteración a la siguiente con `continue`.
Pero ¿cómo podemos salir prematuramente de un script?

Para salir prematuramente de un script, se usa la función `sys.exit`.

Reescribamos el script, pues:

```python
#!/usr/bin/env python3

import sys
import os

if len(sys.argv) != 2 :
	print("Se esperaba un argumento")
	sys.exit(-1)

infilename = sys.argv[1]

if not os.access(infilename, os.R_OK) :
	print("No se pudo leer el fichero '{}'".format(infilename))
	sys.exit(-1)

with open(infilename) as infile:
	contenido = infile.read()
print(contenido)
```

Ahora las condiciones de error nos han quedado bastante identificadas
y no tenemos la tensión cognitiva de estar dentro de un `if`-`else`
en el resto del código.
Detectamos una condición de error, la gestionamos y nos olvidamos de ella.

¿Qué quiere decir el -1?

Ese número que se le pasa es el _estado de salida_ o _exit status_ del programa.
Son códigos que pueden usar los llamantes de un programa
para saber si ha habido un error o si ha pasado algo anormal.
Si todo ha funcionado como toca, el código será `0`.
El resto de números sirven para codificar diferentes motivos,
y se suele usar el `-1` para indicar que es un error sin especificar cual.

De hecho, igual que pasaba en las funciones con el `return None`,
si las sentencias se ejecutan hasta la última y el script termina,
automáticamente es como si se ejecutara un `sys.exit(0)` al final.


> **Ejercicio:**
> ¿Quieres ver cual es el código que ha retornado un programa?
> En el mismo shell que lo ha lanzado, justo despues de terminar, lanza:
> 
> ```bash
> $ echo $?
> ```
> 
> Prueba con el `grep` o el `diff`,
> verás que es diferente dependiendo de si encuentran o no lo que buscan
> (que encuentre la palabra el primero, diferencias entre los ficheros el segundo),
> o de si alguno de los parámetros falta o es erróneo.


## La función `die`

Como comentamos cuando hablabamos de condicionales y booleanos,
para estos casos es muy práctico montarse una función `die`.
Hagámoslo:

```python
#!/usr/bin/env python3

import sys
import os

def die(message):
	print(message)
	sys.exit(-1)

if len(sys.argv) is not 2:
	die("Se esperaba un argumento")

infilename = sys.argv[1]

if not os.access(infilename, os.R_OK):
	die("No se pudo leer el fichero '{}'".format(infilename))

with open(infilename) as infile:
	contenido = infile.read()
print(contenido)
```

Es muy interesante tener esta función centralizada
en vez de tener los `print` y `exit` repartidos por todo el script.

Con todo el ruido fuera,
nos es más fácil hilar más fino y diferenciar el mensaje de error:

```python
if len(sys.argv) < 2:
	die("Se esperaba un argumento")
if len(sys.argv) > 2:
	die("Demasiados argumentos, se esperaba uno solo")
```

Ahora imagina que queremos que todos los mensajes de error del `die`
queremos que empiecen con `Error crítico`.
Si tuviéramos varias salidas como esta sin una función `die`,
tendriamos que añadir eso en cada sitio.
Pero con `die` solo tenemos que hacerlo en un punto y ya está.

```python
def die(message):
	print('Error crítico: ' + message)
	sys.exit(-1)
```

Todas las llamadas al `die` se beneficiarán de la mejora.


> **Ejercicio:**
> Otra mejora más llamativa que se le puede hacer es hacer que los mensajes de error se vean en color rojo.
> Hay que sumarle al mensaje delante `\033[31;1m` para activar el color
> y `\033[0m` al final para desactivarlo.
> El `\033` es un carácter especial (escape) y sirve para entrar
> las llamadas [secuencias ANSI de control de terminal](https://es.wikipedia.org/wiki/C%C3%B3digo_escape_ANSI).


El módulo `consoleutils` de GuifiBaix
tiene funciones para varios tipos de mensajes:
`error`, `fatal`, `warning`, `step`...
Si estás programando para la cooperativa,
no te construyas otra función `die`, usa las funciones de ese módulo.

## Salidas y entradas estandard

Sigamos mejorando la función `die`.
El mensaje de error se imprime con `print`.
En consola, esto hace que vaya a la salida estándard.

Recordemos lo que aprendimos en los tutoriales de `bash`
sobre lo que eran la salida estándard, y la salida de error.

En UNIX todo es un fichero.
El teclado es un fichero del cual podemos leer,
la pantalla es un fichero en el cual podemos escribir,
los ficheros de disco son ficheros en los que podemos leer y escribir...

Así que todos los programas de UNIX,
(por extension los de Linux y Mac, y por mala copia, los de Windows),
por el hecho de ejecutarse tienen siempre 3 ficheros abiertos:

0. La entrada estándard
1. La salida estándard
2. La salida de error

Por defecto, la entrada está conectada al teclado
y las dos salidas a la pantalla del terminal.
Pero, en el momento de llamar al script,
desde `bash`, podemos redirigirlas.
Por ejemplo:

```bash
$ # Enviamos la salida de nuestro script a un fichero 'salida.txt'
$ ./miscript.py entrada.txt > salida.txt
$ # Enviamos la salida de nuestro script como entrada del `grep`
$ # sustituyendo al teclado
$ ./miscript.py entrada.txt | grep ganchitos
de comer ganchitos.
```

En el primer caso enviamos la salida estándard al fichero `salida.txt`.
En el segundo conectamos, con lo que se llama una tuberia,
la salida de nuestro script con la entrada del comando `grep`,
que filtra las líneas que contengan la palabra _ganchitos_.
El comando `grep` en vez de leer su entrada del teclado la lee de la salida de nuestro script.

Debido a este tipo de uso, es importante que los mensajes de error no se mezclen
con la salida esperada del comando y por eso hay dos ficheros diferenciados
aunque a veces los dos se envien al mismo destino.
Al estar separados, aunque redirigamos la salida estándard,
los errores aún apareceran por pantalla.

Estos tres ficheros estan disponibles como `sys.stdin`, `sys.stdout` y `sys.stderr`.
Son objetos parecidos al objeto `infile` que nos devolvía `open`,
que usamos para leer el fichero `entrada.txt`.

La función `print`, trabaja normalmente con `sys.stdout`,
si queremos cambiarlo, podemos especificar la salida con el parámetro `file`.

Modifiquemos la función `die` para que no nos mezcle los errores con nuestra salida:


```python
def die(message):
	print(
		'\033[31;1m' +
		'Error crítico: ' + message +
		'\033[0m',
		file=sys.stderr)
	sys.exit(-1)
```

> **Culturilla:**
> Sin exagerar, en UNIX todo es un fichero.
> La entrada y salida de una consola, el teclado y la pantalla de texto, estan abstraidos en el fichero especial `/dev/tty`.
> Si redirijes texto a ese fichero, saldrá por el terminal,
> si lees de ese fichero, leeras lo que escribas en ese terminal.


## Los ficheros como iterables

El método `read` que estamos usando carga todo el fichero en memória a la vez.
Es bastante conveniente pero si el fichero es grande,
la aplicación empezará a ir lenta pues se nos llenará la memoria.

La solución es ir leyendo a trozos.
En el caso de los ficheros de texto, a líneas.
Y para ello, la función `read` ya no nos vale.

Lo bueno es que Python intenta ver todo como un iterable.
Es decir, como si fuera una lista.
Y si iteramos sobre un fichero de texto,
los items que nos va a ofrecer, son justamente, las líneas.

Modificamos nuestro `with` de esta manera:

```python
with open(infilename) as infile:
	for linea in infile:
		print(linea)
```

Si miramos la salida, veremos que algo esta pasando.
Hay una línea en blanco que antes no estaba.
Ese salto de línea nos lo introduce el `print`.
El método `write` de los ficheros no lo introduce,
así que lo usamos con `sys.stdout`.

```python
with open(infilename) as infile:
	for linea in infile:
		sys.stdout.write(linea)
```

Ya está, arreglado.

> **Ejercicio:**
> Modifica el script para que se convierta en una especie de `grep`
> sencillo, sin expresiones regulares, que simplemente filtre palabras.
>
> Claves:
>
> - Recibirá un parámetro extra por linea de comandos que será la palabra. Hay que ampliar los parámetros a recibir.
> - Dentro del `for` usaremos el operador `in` para saber si la línea contiene la palabra.


## Sofisticando la línea de comandos, librería `argparse`

¿Cómo sería el script para hacer que,
si recibe sólo un parámetro, se comporte como el `cat`
y si recibe un segundo, se comporte como el `grep`?


```python
#!/usr/bin/env python3

import sys
import os

def die(message):
	...

if len(sys.argv) < 2: 
	die("Se esperaba mínimo un argumento")

if len(sys.argv) > 3: 
	die("Se esperaban máximo dos argumentos")

infilename = sys.argv[1]

if not os.access(infilename, os.R_OK):
	die("No se pudo leer el fichero '{}'".format(infilename))

filtro = sys.argv[2] if len(sys.argv) is 3 else None

with open(infilename) as infile:
	for line in infile:
		if filtro and filtro not in line:
			continue
		sys.stdout.write(line)
```

Observa que, aunque las opciones son mínimas,
y hemos hecho algunos trucos para reducir la lógica relacionada ellas,
la gran parte del código aún tiene que ver con las opciones.

Las líneas de comandos se pueden complicar mucho más:
Parámetros opcionales y múltiples,
opciones (esas que empiezan con guion como `--force`),
subcomandos (como los `commit` y `push` del `git`)...

Podemos currárnoslo nosotros, trabajando con la lista `sys.argv`.
Pero, cuando ya tienes varios parámetros y alguna opción,
combiene usar la libreria estándard
[`argparse`](https://docs.python.org/3/library/argparse.html).

Esa libreria, no solo nos recogerá apropiadamente
los valores de las opciones,
sino que nos dará mensajes de error apropiados cuando no se especifiquen correctamente.
Y, como extra, añade la opción `--help`, que los usuarios agradecen.
Saca por pantalla una ayuda de como usar el script,
aprovechando la descripción que le damos de las opciones.

Cuando usamos `argparse`, lo hacemos en dos pasos:

- Creamos un objeto analizador (_parser_)
- Añadimos al parser las opciones y argumentos que queremos recibir
- Le decimos al parser que procese `sys.argv`, llamando al método `parse_args`
- Nos devuelve un segundo objeto con las opciones como atributos que podemos acceder con la sintaxis de punto (`.`).
- Si hay un error o llaman a la opción `--help`, ya se encarga él.

```python
#!/usr/bin/env python3

import sys
import os
import argparse

def die(message):
	...

parser = argparse.ArgumentParser(
	description = "Muestra el fichero, opcionalmente filtrando lineas",
	)
parser.add_argument(
	'infilename',
	help="Fichero de entrada",
	)
parser.add_argument(
	'filter',
	help="Palabra por la que filtrar la salida",
	# Con nargs decimos que es opcional
	nargs='?',
	# Si no lo pasan, recibiremos el default
	default = None,
	)

options = parser.parse_args(sys.argv)

if not os.access(options.infilename, os.R_OK):
	die("No se pudo leer el fichero '{}'".format(options.infilename))

with open(options.infilename) as infile:
	for line in infile:
		if options.filter and options.filter not in line:
			continue
		sys.stdout.write(line)
```

Quizás es verdad que ahora nuestro script es más largo,
pero tenemos un monton de cosas nuevas gratis
que agradeceran nuestros usuarios.
Y cuando compliquemos de verdad las opciones no habrá color.

Hagámoslo.
Vamos a añadir una opción `--upper` 
para que convierta todo lo que salga en mayúsculas.
Añadamos en las opciones:

```python
parser.add_argument(
	'--upper',
	help = "Convierte la salida a mayúsculas",
	# si existe la opción, el atributo valdra True
	action = 'store_true',
	)
```

Y el bucle quedaría:

```python
with open(options.infilename) as infile:
	for line in infile:
		if options.filter and options.filter not in line:
			continue
		# código nuevo
		if options.upper:
			line=line.upper()

		sys.stdout.write(line)
```

> **Ejercicio:**
> Añade otra opción para que aplique algun otro método
> de los textos como `lower`, `capitalize`, `title`, `swapcase`,
> `lstrip`, `strip`, `rstrip`...

De los métodos de texto que devuelven otro texto,
algunos llevan un parámetro.
Es el caso de `center`, 
que centra el texto con espacios a un cierto ancho.

Vamos a ver como añadir una opción que lleve un parámetro:


```python
parser.add_argument(
	'--center',
	help = "Centra el contenido a WIDTH espacios",
	# el texto de la opción lo pasara por el constructor de int
	type=int,
	# en el ejemplo de uso el parámetro saldra como WIDTH
	metavar='WIDTH',
	)
```

Como no especificamos el `store_true`,
la opción tomará un parametro.

Observa que las opciones y argumentos son todos textos.
Ahora necesitamos un número entero.
El valor de `type` es una función que se llamará
para construir el valor del atributo a partir del texto.
Como le pasamos el tipo `int`, usado como función
interpreta el texto como entero, y si no lo es se queja.

> **Ejercicio:**
>
> - Comprueba que si le pasamos algo que no sea un entero, se nos queja.
> - Comprueba que si no le pasamos el parámetro, también se queja.

Dado que la opción lleva un parámetro, hemos indicado una `metavar`
que es como saldrá el parámetro en la descripción de uso.
Si no lo indicamos, cogería el nombre de la opción en mayúsculas.
Pero vemos que `CENTER` tiene menos sentido que `WIDTH`,
por eso lo indicamos.

Ataquemos ahora el bucle.
La implementación directa sería añadir:

```python
		if options.center:
			line=line.center(options.center)
```

Sin embargo, verás que el resultado no es el esperado.

> **Ejercicio:**
> Arregla el center para que funcione.
> Lo que hace `center` es añadir espacios
> a ambos lados del texto hasta que el numero de caracteres
> sea el especificado.
> El problema es que nuestro texto acaba con un `\n`.
> Una de las líneas es:
> 
> ```python
> 'de comer ganchitos.\n'
> ```
> 
> Si centramos a 30, añadiremos unos 5 espacios por cada lado, quedando:
> 
> ```python
> '      de comer ganchitos.\n     '
> ```
> 
> Fíjate que los espacios de la derecha se han añadido despues del `\n`,
> por lo que afectarán al alineamiento de la siguiente línea.
> Puedes usar `strip` o `rstrip` pero no te olvides volver a añadir el `\n`.


En este punto si usamos la opción `--help`, nos saldrá algo como:

```
usage: myscript.py [-h] [--upper] [--center WIDTH] infilename [filter]

Muestra el fichero, opcionalmente filtrando lineas

positional arguments:
  infilename      Fichero de entrada
  filter          Palabra por la que filtrar la salida

optional arguments:
  -h, --help      show this help message and exit
  --upper         Convierte la salida a mayúsculas
  --center WIDTH  Centra el contenido a WIDTH espacios
```




# Ficheros de texto tabulares, CSV

## El formato CSV

Vamos a crear un fichero `csv`.
CSV son las siglas de _comma separated values_,
es decir, valores separados por comas.
Es una forma de representar una tabla de valores
en que cada línea del fichero es una fila de la tabla
y los valores de cada columna de la fila, se separan entre ellos por una coma.

De hecho, la extensión `.csv` se usa de forma generalizada
para ficheros de texto que tengan datos tabulados,
se use o no la coma como separador.
Las aplicaciones de hoja de cálculo permiten
exportar e importar esos ficheros especificando
el caracter separador o otras convenciones.

Nosotros vamos a usar el caracter tabulador `'\t'` como separador de columnas.

## Convirtiendo una tabla en CSV

Imaginemos que tenemos los datos en una tabla.

```python
table = [
	[ 'valor 11', 'valor 12', 'valor 13', 'valor 14'],
	[ 'valor 21', 'valor 22', 'valor 23', 'valor 24'],
	[ 'valor 31', 'valor 32', 'valor 33', 'valor 34'],
	[ 'valor 41', 'valor 42', 'valor 43', 'valor 44'],
]
```

Y queremos representar esos valores en una fichero csv para abrirlos con nuestra aplicación de hoja de cálculo.
Tenemos que unir los valores de cada fila con el tabulador, y los de cada columna con el salto de línea, se encarga el `print`.

```python
for row in table:
	print('\t'.join(row))
```

Si quisieramos tener el texto en memoria o guardarlo en un segundo fichero
podemos hacer un doble `join`.

```python
csv = '\n'.join( '\t'.join(row) for row in table )
with open('tabla.csv', 'w') as outfile:
	outfile.write(csv)
```

Prueba de abrir el fichero generado con una suite de ofimática.
Con el LibreOffice, nos preguntará que tipo de CSV
estamos abriendo.
Hay que seleccionar que el separador es el tabulador,
que no estamos usando comillas
y que la codificacion de los caracteres es UTF-8.


## Conviertiendo un CSV en una tabla

¿Y al revés? ¿Como leemos un CSV?

Pues si para escribirlo usabamos `join`, para leerlo usaremos `split`.

```python
# Este texto lo podríamos obtener igual con un read de un fichero.

csv = """\
valor 11\tvalor 12\tvalor 13\tvalor 14
valor 21\tvalor 22\tvalor 23\tvalor 24
valor 31\tvalor 32\tvalor 33\tvalor 34
valor 41\tvalor 42\tvalor 43\tvalor 44
"""
# Componemos la tabla (lista de listas)
tabla = [
	row.split('\t')
	for row in csv.split('\n')
	]
```

Ojo, el `split` nos da una fila extra por la ultima línea vacía.
Hay un `'\n'` pero no hay fila después.
Para filtrarla, podemos usar un `if`.

```python
tabla = [
	row.split('\t')
	for row in csv.split('\n')
	if row.strip() # la función strip elimina caracteres blancos
	]
```

> **Ejercicio:**
> Crea con el LibreOffice una tabla con los datos de los socios:
> Nombre, apellidos, municipio...
> Grábala en formato CSV ("Guardar como" y cambia el tipo de archivo abajo).
> Te pedirá los parámetros del CSV, como siempre tabuladores, UTF-8 y sin comillas.
> Carga la tabla en Python.


## Usando las cabeceras para crear un diccionario

A menudo se reserva la primera fila para las cabeceras de las columnas.
Podemos aprovechar este hecho para en vez de una lista de listas,
usar una lista de diccionarios donde las claves sean el título de cada atributo.
Momento de revisar el capítulo sobre diccionarios y el de diccionarios _del tirón_.

```python
csv = """\
columna 1\tcolumna 2\tcolumna 3\tcolumna 4
valor 11\tvalor 12\tvalor 13\tvalor 14
valor 21\tvalor 22\tvalor 23\tvalor 24
valor 31\tvalor 32\tvalor 33\tvalor 34
valor 41\tvalor 42\tvalor 43\tvalor 44
"""
# Repetimos la operación anterior
tabla = [
	row.split('\t')
	for row in csv.split('\n')
	if row
	]
# Una vez tenemos la tabla en crudo,
# construyamos la lista de diccionarios.
objetos = [
	{
		key: value
		for key, value in zip(tabla[0], row)
	} for row in tabla[1:]
]
print(objetos[2]['columna 3']
# imprime: valor 23
print(objetos)
# imprime una lista de diccionarios:
#[
#	{
#		'columna1' : 'valor 11',
#		'columna2' : 'valor 12',
#		'columna3' : 'valor 13',
#		'columna4' : 'valor 14',
#	},{
#		'columna1' : 'valor 21',
#		'columna2' : 'valor 22',
#		'columna3' : 'valor 23',
#		'columna4' : 'valor 24',
#	},{
#		'columna1' : 'valor 31',
#		'columna2' : 'valor 32',
#		'columna3' : 'valor 33',
#		'columna4' : 'valor 34',
#	},{
#		'columna1' : 'valor 41',
#		'columna2' : 'valor 42',
#		'columna3' : 'valor 43',
#		'columna4' : 'valor 44',
#	},
#]
```

La función _built-in_ `zip` coge los dos iterables
y construye un iterable con tuplas de ambos.
Estamos cogiendo la primera fila que contiene las cabeceras
y las emparajamos con cada una de las siguentes filas.

Con columnas tan sosas como `columna 1`,
igual no tiene sentido.
Empezarás a verlo cuando tengas columnas que se llamen
`Nombre`, `Apellidos`, `DNI`...

La ventaja está en que dejamos de contar
y referenciamos las columnas por su nombre.
Imaginate que en nuestro csv añadimos una columna
deberíamos de revisar todos los índices.
Son números, así que un busca y sustituye
es bastante tedioso y tendiente a errores.

Accedemos por nombre y si no tenemos cabeceras para hacerlo
las deberiamos de inventar.
Es decir, es tan bueno referenciar las celdas por su
nombre que si no tenemos cabeceras, es bueno
definir una lista con los nombres de los campos,
y acceder por ellos.
¿Porqué?
Primero, el código se va a entender mejor y nos ahorramos
el estar contando todo el rato mientras escribimos o leemos el código,
para saber cual es la columna del nombre y la del apellido.
Segundo, si modificamos la estructura del csv,
si cambiamos el orden de las columnas o añadimos alguna, solo
tendremos que cambiar la lista de las cabeceras.



## La clase namespace

# Trabajando con rutas

## Manipulando rutas, el módulo `os.path`

Otro tipo de operaciones muy importantes cuando estamos manejando ficheros
es la manipulación de rutas de archivos.
La **ruta** (_path_) es la secuencia de cambios de directorio
que hay que hacer para llegar a un recurso en el sistema de ficheros.

En UNIX (e hijos, como Linux y Mac), la ruta se expresa
separando los pasos con una barra (`/`).
En Windows, se separan con contrabarras (`\`).
Para construir rutas sin ir preguntando en qué sistema estás,
Python proporciona la función `os.path.join`.

```python
>>> os.path.join('expedients', 'sjd-verdaguer42', 'contracte.yaml')
'expedients/sjd-verdaguer42/contracte.yaml'
```

Hablamos de **ruta absoluta** cuando se expresa a partir de la raiz.
En Unix las absolutas empiezan todas con la barra (`/`), por ejemplo, `/home/aitor`.
En contraste, hablamos de **ruta relativa** cuando se expresa a partir de otro directorio.
Las rutas relativas se identifican (en UNIX) porque no llevan la barra inicial, por ejemplo, `Documents/guifibaix/suro`.

Normalmente el directorio de referencia para las rutas relativas es el llamado **directorio de trabajo**.
El directorio de trabajo es el que cambiamos en linea de comandos con `cd`.
Desde Python podemos cambiarlo con la función `os.chwd(directorio)`.
Pero una ruta relativa sirve también para aplicarse a otro directorio base,
por ejemplo, combinándolos con la función `os.path.join`.

```python
>>> miCasa = '/home/aitor'
>>> suro = 'Documents/guifibaix/suro'
>>> os.path.join(miCasa, suro)
'/home/aitor/Documents/guifibaix/suro'
```

De hecho esta suele ser una buena estrategia para localizar los recursos de un programa.
Combinar un directorio absoluto que puede cambiar,
con las rutas a los recursos a partir de ese punto base.
De esta manera evitamos tener que cambiar todas las localizaciones en el código.
Las rutas relativas dependen solo de nuestro programa,
y la base dependerá de a donde se vaya a vivir
finalmente nuestro programa,
sea un path de instalación o el directorio del usuario que sea.


## Rutas estándard, la librería externa `appdirs`

De hecho, existen estándares que especifican donde tienen que ir
cada tipo de fichero de una aplicacion.
Dichos estándares dependen del sistema,
pero afortunadamente hay una librería externa (que hay que instalar)
que nos dice, estemos en el sistema que estemos, cuales son.

Es una librería externa, así que hay que instalarla.

En Ubuntu/Debian, está disponible como paquete así que podemos instalarla en el sistema con:

```bash
$ sudo apt-get install python3-appdirs
```

Si no estuviera como paquete en la distribución,
también podríamos instalarla desde el Package Index, PyPI:

```bash
$ sudo pip install appdirs
```

Una vez instalado, podemos hacer `import`
como hemos hecho con las librerías estándard.

La librería nos da varias localizaciones útiles.
No está de mas que con el `ipython3` exploraras
la librería con el tabulador y
consultaras su ayuda añadiendo el `?` a las funciones que ofrece.

Para nuestras aplicaciones, me centraría en estas:

- `appdirs.user_data_dir(appname, appauthor)`: Donde están los datos de aplicación para el usuario.
- `appdirs.user_config_dir(appname, appauthor)`: Donde están los ficheros de configuración de la aplicación, para el usuario.

## Comodines, la función `glob.glob`

En `bash` podemos expandir cosas con asteriscos `*` para que se expandan en varios nombres que coincidan con un patron.

Por ejemplo: `*.py` se expande con todos los ficheros Python del actual directorio de trabajo.

Python ofrece una librería estándard, `glob`, que nos hace esta expansión.

Le pasamos un string con los comodines y nos devuelve una lista con
los ficheros que coinciden.

> **Culturilla:**
> `glob` viene de _global match_.
> Era una función que tenía algún sistema Unix antiguo
> para hacer que un comando en vez de aplicarse a un fichero,
> se aplicara _globalmente_ a un conjunto de ficheros.
> 
> La expresión _global_ hoy en dia ha perdido mucho de su significado,
> pero se usa _glob_ (o _globear_ en castellano malo) como verbo,
> y globbing a las expresiones.




# Hasta aqui hemos llegado

A partir de aquí hay dragones.

...y capítulos muy en pañales.










# Temas pendientes TODO's

- Manejando exepciones, `try`-`except`
- Lanzando exepciones, `raise`
- ~~Leyendo ficheros, `open`, `read`, `close`~~
- ~~Controlando cierre de recursos `with`~~
- ~~Escribiendo ficheros, `write`~~
- ~~Usando modulos `import`~~
- ~~Instalando librerías~~
- Entornos virtuales
- ~~Manejando fechas, `datetime` y `dateutils`~~
- Manejando dinero, `decimal`
- Creando mòdulos
- Creando paquetes
- Definiendo proyectos
- Subiendo proyectos al PyPI
- Definiendo clases, `class`
- Definiendo atributos y métodos, `self`
- Usando herencia
- Propiedades `@property`
- Unit Testing `unittest`


# Manejando dinero

El dinero es una cantidad numérica,
y teniendo decimals, por los céntimos,
tendemos a representarlo con el tipo `float`.

El tipo `float` tiene el inconveniente de la precisión.
No se puede representar con `float` un número de N decimales de forma exacta.

```python
>>> '{saldo:.02f}€ {saldo:.06f}€'.format(saldo=2.50*1.21)
'3.02€ 3.025000€'
```

Esto pasa porque:

- La representación para números `float` en el ordenador no puede representar exactamente los números decimales.
- Por eso el número no es exactamente 3.025 sinó algo muy pegado por debajo
- Al representarlo con varios decimales, redondea por encima y llega al 3.025
- Al representarlo solo con dos decimales, ese 5 no llega al 5, por lo que se redondea a la baja.

Solución:

- **Para dinero no usar nunca `float`.**
- Usar ints contando en centimos o la clase `Decimal` del modulo `decimal` o una clase `money` de alguna librería que esté bien.
- Cuando apliques porcentajes por impuestos, augmenta la precisión dos dígitos (centésima de céntimo) o más si el porcentaje tambíén tiene decimales.
- Justo después de aplicar el porcentaje redondea al céntimo con el metodo de redondeo HALF_FROM_ZERO.

```python
from decimal import Decimal as D, ROUND_HALF_UP

>>> (D('2.50')*D('1.21')).quantize(D('0.01'), rounding=ROUND_HALF_UP)
Decimal('3.03')
```



