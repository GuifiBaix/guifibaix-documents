---
title: 'Programación: El lenguaje Python 3'
author: David García Garzón
copyright: 2015 Guifibaix SCCL
documenclass: book
---

# Introducción

> «Para un programador es necesaria la habilidad
> de escribir código que entienda el ordenador.
> Pero acaba siendo una habilidad inútil si no tiene
> también la habilidad de escribir código
> que entiendan con facilidad otras personas...
> (o uno mismo, cuando pase el tiempo)»
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
definimos el comportamiento de los programas informáticos.
Hay muchos lenguajes de programación.
Cada lenguaje tiene sus puntos fuertes
o está más adaptado a según que tareas,
o a las preferencias de cada persona.
Por eso existen una miriada de lenguajes.

Al final, el ordenador solo entiende de código máquina.
El codigo máquina no está pensado para que lo entiendan las personas;
es una secuencia de números sin sentido aparente,
en la que cada número codifica
algo que tiene que hacer el ordenador:
Cargar un número en el procesador desde una posición de memoria,
operar con ese número,
colocar el resultado en otra posición de memoria,
enviar un código a un dispositivo...
Cosas de muy de tocar el hierro.

Los lenguajes de programación son más cercanos
a algo que una persona puede entender,
haciendo de puente entre las personas y el ordenador.
Nos permiten abstraernos de las interioridades del ordenador,
y pensar en términos más cercanos al problema que queremos resolver.

Los programas se escriben en archivos de texto,
con unas reglas bastante rígidas, lo que se llama **sintaxis**,
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


En general, un lenguaje interpretado se ejecutará más
lento que uno compilado, puesto que, a parte de la tarea que haya que hacer,
tiene el trabajo extra de interpretar el texto para
decidir que código máquina ejecutar.

Con los rápidos ordenadores actuales,
el tiempo de interpretación dejó de ser un problema.
Y se prefiere en muchos casos un lenguaje interpretado porque,
al no requerir el paso de compilación,
el proceso de desarrollo es mucho más rápido y simple.

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
	- Encontrarás informacion en la [referencia de la libreria estándard](https://docs.python.org/3/library/)
- Las **librerías no estándard**. Aunque no vengan por defecto algunas son de uso muy extendido.
	- Toda librería que se precie está incluida en el [índice de paquetes](https://pypi.python.org/pypi)
	- Cada una tiene su propia documentación.
	Normalmente con un formato similar a la documentación de las librerías estándard.
- Si necesitas algo más, esta es [toda la documentación del lenguaje](https://docs.python.org/3/)

Hay dos formas de ejecutar código Python:

- tecleando sentencias en el intérprete en modo interactivo (python3 o, mejor, ipython3),
para experimentar y probar cosas.
- escribiendo las sentencias en un archivo de texto (script) y lanzándolas de golpe con el intérprete,
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
	- Si le pones un signo `?` a una expresion te muestra ayuda sobre el objeto resultante
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

**Nota:** Si has programado en Python 2, ojo que en Python 3, la instrucción `print` requiere paréntesis.

**Nota:** En modo interactivo, siempre nos imprimira el resultado de la expresion que hayamos introducido.
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
  En `myscript.py` escribiriamos:

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

El primer tipo de sentencia que veremos será la expresión.
Una **expresión** es una construcción del lenguaje que resulta en un **valor**.
Por ejemplo: `3+4` es una expresión que resulta en el valor `7`.

Las expresiones se usan en muchos sitios pero también son sentencias de pleno derecho.
Así que podemos introducir expresiones en el intérprete interactivo de Python y usarlo de calculadora.


## Tipos de datos y literales

Decíamos que  `3+4` es una expresión que da el valor `7`.
De hecho, `3`, `4` y `7` son expresiones también, de las que llamamos literales.
Los **literales** son la forma más directa de representar un valor de un tipo concreto.

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
- Las tuplas (`tuple`) son parejas, trios... de valores que juntamos para pasarlos como un solo valor.
- Las listas (`list`) son como las tuplas pero podemos insertar y eliminar elementos.
- Los conjuntos (`set`) son como las listas,
  pero no guarda el orden entre los elementos,
  y no tienen repetidos
  (por eso, en el ejemplo, uno de los dos `1` desaparece).
- Los diccionarios (`dict`) contienen parejas clave-valor, en los que se puede acceder al valor mediante la clave.
- El no-valor `None` (`NoneType`) representa el concepto de _ningún valor_, más útil de lo que parece.
- Los valores lógicos (`bool`) representan una condición que puede ser cierta o falsa, y sirven para tomar decisiones.


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
Por ejemplo, la multiplicacion y división tienen más prioridad que la suma y la resta.
La exponenciación tiene más prioridad que la mutiplicación y la división.
Por eso:

```python
>>> 2*3+4  # se resuelve como (2*3)+4
10
>>> 2+3*4  # se resuelve como 2+(3*4)
14
```

Sí, cuando el orden que sale de la prioridad de operadores no nos gusta,
podemos agrupar con paréntesis:

```python
>>> 2 * (3 + 4)
14
>>> (2 + 3) * 4
20
```

Los paréntesis aunque no sean necesarios porque la prioridad ya lo ejecuta como queremos,
también ayudan a leer y entender la expresión.

Recuerda que no solo escribimos código para el ordenador.
También escribimos código para el siguiente programador que tenga
que revisarlo, que podemos ser nosotros mismos de aquí a un tiempo
cuando ya apenas recordemos como iba el programa.
Si vemos los paréntesis no tendremos que pensar en cual es la
prioridad o sospechar si cuando lo escribimos la teníamos clara.

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
generan valores que una vez los hemos hecho servir desaparecen de la memoria del ordenado.

Las **variables** nos permiten mantener una referencia a un **valor**,
para volverlo a usar después.
La sentencia en la asociamos un valor a un nombre se llama *sentencia de asignación*.
Decimos que *asignamos un valor a la variable*.

```python
>>> a = 23  # sentencia de asignacion
>>> a       # uso de la variable
23
>>> b = 10*a
>>> b
230
```

En Python, una misma variable en un script puede ir apuntando a valores diferentes.
De hecho, puede apuntar incluso a valores de diferente tipo,
cosa que no permiten otros lenguages como C o Java.

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

Todos los operadores con signo tienen su versión de actualización
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

Otro elemento que podemos usar en una expresión son las funciones.
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
hay que llamar a la funcion `print`.

Por ejemplo, para ver el resultado de llamar a la funcion `max`:
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
cuando el texto contiene una de ellas, usamos la otra.

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

Y tenemos algunas funciones _built-in_ que podemos usar con secuencias:

```python
>>> len('hola')   # longitud de un texto
4
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

Un tercer elemento en el _slice_ es el paso;
cuantas casillas saltamos.
Normalmente es 1, pero si lo especificamos...

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



## Definiendo funciones

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
	- Los parámetros en las subsentencias se usan como variables
	- Se les asignan los valores que pasamos entre paréntesis cuando llamamos la función
		- En la primera llamada a=3. En la segunda llamada a=4.
		- En la primera llamada b=1. En la segunda llamada b=5.
	- Existirán sólo mientras se ejecute esa llamada a la función
- La sentencia `def` acaba con dos puntos (`:`), siguen subsentencias indentadas un nivel
	- Las sentencias de dentro son las que se ejecutarán cada vez que llamemos la función.
	- Los tres puntos los escribe el intérprete, en vez de los `>>>` para indicar que aun tenemos que acabar la sentencia.
	- Para salir de los tres puntos en el intérprete dejamos una linea en blanco
- La primera sentencia de dentro crea una variable `suma`
	- Las variables que creemos dentro de una función solo existen mientras la función se ejecuta.
	- En jerga se dice que es una _variable local_, en contraposicion de las variables que se definen fuera de funciones que se les llama _globales_
	- Que las variables tengan un ámbito local nos ayuda a no tener que buscar nombres que no colisionen con los de otras funciones
- La ultima sentencia es una sentencia especial `return`
	- Una sentencia `return` sale de la función y devuelve el control al llamante
	- Además el llamante recibirá el valor resultante de la expresión que va después del `return`
	- Si hubiera más sentencias después del return, no se seguirían ejecutando

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
...     2+2  # ojo, error típico queriamos retornar algo y nos dejamos el return
...
>>> noReturnFunction()
>>> print(noReturnFunction())
None
```
Una función retorna `None` 

- Porque explícitamente hace un `return None`
- Porque hace un return sin expresión: `return`
- Porque se le acaban las sentencias de la función sin haber hecho un `return`


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
De esta forma, el intérprete puede ir asignando valores a los parámetros sin problemas.



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

Se pueden combinar parámetros posicionales con nombrados.
La regla es que primero se especifican los posicionales
y luego van los nombrados.
Los posicionales se reparten en orden tal i como están en la definición de la funcion (`def`).

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

Para programar decisiones es necesario entender bien los booleanos.

## Tipos booleanos

Los booleanos son valores representan condiciones,
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
Estos dos operadores son equivalentes al operador de igualdad `==` y desigualdad `!=` para los tipos básicos:
numéricos, textos...
Eso sí, son mucho más expresivos porque conseguimos frases casi en inglés como estas:

```python
>>> guy = 'alf' + 'redo'
>>> guy is 'alfredo'
True
>>> guy is not 'alfredo'
False
```

La diferencia la encontraremos con
los valores tipo estructura, como las listas, los diccionarios...
cuyo contenido puede variar mantieniendo la identidad.
De hecho dos objetos pueden tener el mismo contenido y no compartirían identidad.

```python
>>> l1 = [1,2,3]
>>> l2 = l1       # l1 y l2 apuntan al mismo objeto
>>> l3 = [1,2,3]  # l3 es un objeto con el mismo contenido que l1
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
que después de evaluar una condición para ver si tenemos que hacer algo,
tengamos que evaluar lo contrario para hacer otra cosa alternativa.
Para ello es muy util la sentencia `else`.
Hay que ponerlo al nivel del `if` y contiene su bloque de sentencias alternativas.

Reescribiendo el ejemplo anterior solo evaluando una condición:

```python
if name is 'Aitor':
	print ('Hola Aitor, bienvenido a casa')
else:
	print ('Hola, desconocido, ya te puedes pirar')
```

Está bien, pero tambíén podemos tener más de una alternativa.
Para eso sirve la sentencia `elif` (viene de _else if_).

```python
if name is 'Aitor':
	print ('Hola Aitor, bienvenido a casa')
elif name is 'David':
	print ('Hola David, Aitor llegará en un momento.')
else:
	print ('Hola, desconocido, ya te puedes pirar')
```

## Condiciones anidadas

Podemos anidar un `if` dentro de otro formando un árbol de decisión:

```python
if meGustaElFutbol :
	if miEquipo is 'Real Madrid':
		print("Merenge!")
	elif miEquipo is 'Barça':
		print("Cules!")
	else:
		print("whatever")
else
	print("Mejor pensemos en otras cosas más productivas")
```

Observa que los `else`s y `elif`s estan al mismo nivel que el `if`
al que se corresponden y que los bloques de sentencias estan
indentados aún más adentro.


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

TODO: Ejercicio para reforzar


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

> **Ejercicio:**
> Todos los operadores relacionales que vimos se pueden expresar
> combinando uno solo de ellos con operadores lógicos.
> Expresa todos los operadores relacionales usando solo el 'menor que' y operaciones lógicas.
> Ejemplos:
> 
> ```python
> >>> (a > b) is (b < a)
> True
> >>> (a >= b) is not(a < b)
> True
> >>> (a != b) is ((a < b) or (b < a))
> True
> ```
> Faltan `<=` y `==`.


> **Ejercicio:**
> Comprueba con una tabla de verdad que estas expresiones son equivalentes (Remember Abelians):
> 
> - `not not a == a` (Doble negación)
> - `not(a and b) == (not a or not b)` (De Morgan)
> - `not(a or b) == (not a and not b)` (De Morgan)
> - `(a and b) == (b and a)`  (Conmutativa)
> - `(a or b) == (b or a)`  (Conmutativa)
> - `a or (b and c) == (a or b) and (a or c)` (Distribuitiva)
> - `a and (b or c) == (a and b) or (a and c)` (Distribuitiva)
> - `a and (b and c) == (a and b) and c` (Asociativa)
> - `a or (b or c) == (a or b) or c` (Asociativa)

Las equivalencias del anterior ejercicio
nos van de coña para simplificar las condiciones
y mejorar la calidad del código.

> **Ejercicio:**
> De Morgan se resume como: negar un operador booleano,
> equivale a usar el otro operador con los operandos negados.
> 
> - Aplica DeMorgan a las expresiones que usamos para calcular:
> `annaConduce`, `toniConduce`, `losDosQuieren` y `ningunoQuiere`.
> - Elimina las dobles negaciones resultantes.
> - Lee las expresiones a ver si aún tienen sentido.
> - Quédate con las reescrituras que simplifiquen la expresión.


Otra forma de ver los booleanos es como numeros con dos únicos valores 0 (`False`, nada) y 1 (`True`, algo, cualquier número positivo diferente de cero).
El `and` es la multiplicación y el `or` es la suma.

- `1 + 1 = 1`  (algo más algo, da algo)
- `1 + 0 = 1`  (algo más nada, da algo)
- `0 + 0 = 0`  (nada más nada, da nada)
- `1 * 1 = 1`  (algo por algo, da algo)
- `1 * 0 = 0`  (algo por nada, da nada)
- `0 * 0 = 0`  (nada por nada, da nada)

Otra forma de ver los booleanos, como interruptores de un circuito eléctrico
que a su vez estan activados o no por otros circuitos eléctricos:

- Una `or` son interruptores en paralelo. Con que uno este encendido pasa la luz.
- Una `and` son interruptores en serie. Los dos tiene que estar encendidos para que pase la luz.
- Un `not` es un interruptor que se apaga cuando le llega corriente, al revés que los normales.


## Evalua con cortocircuito o muere

Otra forma más de ver los operadores `and` y `or` es la siguiente:

- Si los operandos son el mismo valor, retornar ese valor
- Si son distintos:
	- en el `or`, el `True` es dominante sobre el `False`
	- en el `and`, el `False` es dominante sobre el `True`

Así pues, en una expresion `or` o `and`,
cuando evaluamos el primer operando
y nos da el valor dominante,
Python ya no evalua el segundo operando porque ya sabe el resultado.
Solo evalua el segundo operando si el primero es el no dominante.
Es lo que se llama evaluación por cortocircuito,
y se hace para que el programa vaya más rápido.
Optimizamos el programa si ponemos primero el operando
que con más frecuencia evalue al valor dominante.

```python
>>> pi = 3.1416
>>> r = 10
>>> # Como la primera parte ya es cierta, la segunda no se llegara a evaluar
>>> # Intentaremos poner a la izquierda la condición que sea cierta más veces para optimizar
>>> (2*r*pi > 3)  or   (3*r**2*pi>10)
True
```

Cuando alguien hace algo por algún motivo,
siempre sale alguien que lo utiliza para otra cosa.
Mucha gente aprovecha los cortocircuitos para construcciones
condicionales que la verdad es que quedan
bastante expresivas (y barriobajeras) como:

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

En cualquier caso, hay que tener cuidado cuando usemos expresiones booleanas
porque puede que una parte de los operandos, no se lleguen a evaluar.
Si la expresion del segundo operando tiene efectos colaterales necesarios,
no se ejecutarían.

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

# Repitiendo cosas, los bucles

## Bucles condicionales, sentencia `while`

La sentencia `while` ejecuta las subsentencias mientras que una condición sea cierta.

El siguiente código imprime las potencias de 2 menores que 50:

```python
>>> a = 1
>>> while a < 50:
...     print(a)
...     a *= 2   # equivalente: a = a*2
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
- Antes de entrar en las sub-sentencias del while, se evalua la condición `a<50`
- Como es cierta se procede a ejecutar las subsentencias
- La primera sentencia del bucle imprime el valor actual de `a`
- La segunda sentencia del bucle actualiza `a` multiplicando el valor por 2
- Cuando se acaban las subsentencias se vuelve a evaluar la condición con el nuevo valor de `a`.
- Después de la vuelta en que `a` pasa a valer `64`, la condición evalua `False`, y se sale de la sentencia `while`
- Fuera de la función `a` valdra `64` aunque no se haya llegado a imprimir ese valor.

Cada vez que la ejecución entra en las subsentencias se llama una **iteración**.
Diremos pues que el **bucle** ha ejecutado 6 iteraciones.


## Llamándose a sí mismo, recursividad

La recursividad es otra forma de repetir las cosas,
de basar un caso en un caso más simple.

El ejemplo típico es una funcion factorial.
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
Hacer que la funcion retorne algo basado en el resultado de llamarse a si misma con otros paràmetros:

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


## Bucles sobre iterables: sentencia `for`

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
Clásicamente se considera que usar este tipo de sentencias es una abobinación para la programación formal.
**Bien usadas, ayudan a que el código sea mucho más entendible.
Mal usadas, sí, pueden complicarlo abovinablemente.**

La sentencia `continue`, sirve para saltar a la siguiente iteración.
Si se ejecuta una sentencia `continue`, lo que quede de sentencias de esa iteración, ya no se ejecutará.

Volviendo al ejemplo de las animadoras.
Las animadoras francesas saben que la gente se rie cuando pronuncian la 'r',
así que directamente se la cuelan:

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


## Intérvalos de números, tipo `range`

Una fuente muy usada de elementos iterables son los intervalos o `range`.

Un intérvalo es un objeto que genera números.
Lo creamos con la función _built-in_ `range`.

```python
>>> for i in range(6):
>>> 	print(i)
0
1
2
3
4
5
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

Y como en las rebanadas podemos especificar un paso.

```python
>>> for i in range(1,6,2):
>>> 	print(i)
1
3
5
```


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



## Uniendo y separando (`split` y `join`)

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
>>> ''.join(['a','b','c']) # Juntarlas con la cadena vacia como separador
'abc'
```


**Ejercició:** Haz un script que dada una lista de listas,
que representa lineas de columnas,
imprima por pantalla un CSV con el tabulador como separador.


```python
#!/usr/bin/env python3

tabla = [
	[
		'11',
		'12',
		'13',
		'14',
	],
	[
		'21',
		'22',
		'23',
		'24',
	],
]
for linea in tabla:
	print('\t'.join(linea))
```

## Listas del tirón

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

## Empaquetando y despempaquetando valores, las tuplas `tuple`

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

Que se puede hacer con una tupla igual que con una lista:

- Iterar sobre ella
- Desempaquetar
- Acceder a índices y rebanadas
- Métodos `index(value)` y `count(value)`
- Multiplicar por un entero
- Sumarse con otro del mismo tipo para obtener un tercero

Que se puede hacer en una lista que no se pueda en una tupla.
En general modificaciones en el mismo objeto, sin generar un tercero:

- Añadir elementos al mismo objeto: `append`, `extend`, `insert`...
- Eliminar elementos con `del`
- Modificar un elemento del objeto `t[2] = valor`

Que se puede hacer pero tienen resultados distintos:

- `+=` en la lista modifica la lista original.

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







## Usando generadores

Un generador es un objeto que retorna objetos en los que iterar.
La diferencia con una lista sería que el generador no construye la lista en memória pero si que ofrece los items.

### Generando secuencias de números, el generador `range`

Uno de los generadores más usado es el _built-in_ `range`, genera enteros y 
sus tres parámetros son equivalentes a los de un slice: inicio, fin y paso.

```python
>>> for i in range(3,20,3):
... 	print(i)
...
3
6
9
12
15
18
>>> print(range(3,20,3)) # No es una lista es otro tipo de objeto
range(3,20,3)
>>> list(range(3,20,3))  # como es iterable lo podemos pasar al constructor de list
[3,6,9,12,15,18]
>>> tuple(range(3,20,3)) # o al constructor de tuple
(3,6,9,12,15,18)
```
**Ejercicio:**

- Prueba que pasa si recibe solo dos argumentos `range(2,10)`
- Prueba que pasa si recibe solo un argumento `range(10)`
- Prueba como funcionan los numeros negativos para cada parámetro.
- Escribe una _comprehension list_ en la que esten los cuadrados de los números del 1 al 10
	- Pista, código en el camino pero erróneo:

		```python
		[ n*n for n in range(1,10) ]
		```

### Expresiones generadoras

Las expresiones generadoras son muy parecidas a las _comprehension lists_:

- Usan la misma sintaxis pero en vez de usar corchetes usan paréntesis, como si fueran tuplas.
- En vez de crear una lista en memoria, crean un 'generador'

La principal ventaja de usarlos es con volúmenes grandes de datos,
evitando que se creen grandes listas intermedias en memoria.

```python
# Busca los cuadrados de los numeros hasta 999 que acaben en 5
[
	square
	for square in [n*n for n in range(1000)]
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


### Enumerando elementos, `enumerate`

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


### Emparejando secuencias, `zip`

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
Reimplementa `enumerate` como una funcion `enumerate2`
que use `zip`, `range` y `len`.



### Nuestras propias funciones generadoras, `yield`

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



## Conjuntos `set`

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
>>> set(range(1,5)).differenc(set(range(3,8))  # Diferencia
{1,2}
```

# Temas pendientes TODO's

- Diccionarios
- Desempaquetando parámetros, llamadas con `*` y `**`
- Parámetros abiertos, declaraciones con `*` y `**`
- Manejando exepciones, `try`-`except`
- Lanzando exepciones, `raise`
- Leyendo ficheros, `open`, `read`, `close`
- Controlando cierre de recursos `with`
- Escribiendo ficheros, `write`
- Usando modulos `import`
- Instalando librerías
- Entornos virtuales
- Manejando fechas, `datetime` y `dateutils`
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


