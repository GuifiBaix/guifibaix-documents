# Programación: El lenguaje Python 3

## Lenguajes de programación

Un lenguaje de programación es la forma en que las personas
indicamos al ordenador como se tiene que comportar.
Hay muchos lenguajes de programación.
Cada uno tiene sus puntos fuertes
o es más expresivo para según que tareas.
Por eso hay una miriada de lenguajes.

El ordenador solo entiende de instrucciones en código máquina.
Dicho código no está pensado para que lo entiendan las personas,
es una secuencia de números sin sentido,
en la que cada número codifica
algo que tiene que hacer el ordenador.

Los lenguajes de programación son más cercanos a algo que una
persona puede entender,
haciendo de puente entre las personas y el ordenador.
Los programas se escriben en archivos de texto,
con unas reglas bastante rígidas, la sintaxis,
que es lo que determina el lenguaje.

Para pasar un programa escrito en un lenguaje de programación
a código máquina ejecutable hay dos estrategias:

Un __compilador__ convierte el programa en lenguaje y genera
un archivo ejecutable/binario que incluye el código máquina.
Ese archivo binario lo podremos ejecutar aunque ya no tengamos
el compilador a mano.

![Proceso de compilación](TODO)

Un __interprete__, en cambio, decide que código máquina
ejecutar a medida que lee el programa,
sin que haya que generar el archivo binario intermedio.
En este caso, el interprete ha de estar disponible siempre
para poder ejecutar el programa.

![Proceso de interpretación](TODO)

En general, un lenguaje interpretado se ejecutará más
lento que uno compilado, puesto que tiene que interpretar
el texto antes de decidir que código máquina ejecutar.
Por otro lado, un lenguaje interpretado tiene un ciclo
de desarrollo más ágil al ahorrarnos el paso de compilación,
y el coste de interpretación es asumible con los ordenadores
modernos.

## Python

Python es un lenguaje interpretado que
se caracteriza por tener una sintaxis muy limpia y expresiva.

Nos centraremos en la version 3 (3.4.3 en el momento de escribir esto).

- [La documentación del lenguaje](https://docs.python.org/3/)
- Para aprender Python hay tres elementos:
	- El **lenguaje**, que son las reglas de como decir las cosas.
		- Encontraras informacion en la [referencia del lenguaje](https://docs.python.org/3/reference/index.html)
	- Las **librerias estandard**, que són cosas que no hace falta que programes tú, porqué ya están programadas:
		- Encontrarás informacion en la [referencia de la libreria estándard](https://docs.python.org/3/library/index.html)
	- Las librerías no estándard. Aunque no vengan por defecto algunas son de uso muy extendido.
		- Cada una tiene su propia documentación. Normalmente con formato similar al de las librerías estándard.


Hay dos formas de ejecutar código Python:

- tecleando sentencias en el interprete interactivo (python3 o, mejor, ipython3)
- escribiendo las sentencias en un archivo de texto (script) y lanzándolas de golpe

### Intérprete interactivo

- El interprete interactivo te permite escribir código Python y ver los resultados de forma inmediata
- Es ideal para probar cosas cortas
- El intérprete clásico es `python3`.
	- Instalación: `sudo apt-get install python3`
	- Seguramente ya lo tendrás instalado
	- Sales con Control+D
- Recomendamos el intérprete con esteroides llamado `ipython3`
	- Instalación: `sudo apt-get install ipython3`
	- Tienes historial de lo que has escrito, que puedes recuperar con la tecla del cursor hacia arriba.
	- Te completa expresiones con la tecla del tabulador
	- Puedes ejecutar comandos del shell precediendolos con `!`
	- Si le pones un signo `?` a una expresion te muestra ayuda sobre el objeto resultante
	- Te enseña el resultado de la expresión escrita aunque no lo imprimas explicitamente

Cuando digamos de ejecutar algo en un interprete lo solemos escribir así:

~~~{.python}
>>> print("hola mundo")
hola mundo
~~~

- El `>>>` indica el símbolo que el interprete pone para decirte que puedes escribir.
- Lo que has de escribir es lo que va despues, del `print` en adelante.
- La segunda linea es lo que ha imprimido por la pantalla.

**Nota:** Si has programado en Python 2, ojo que en Python 3, la instrucción `print` requiere paréntesis.



### Scripts

Un script es un fichero de texto que contiene
las instrucciones de un programa escrito
en un lenguaje interpretado (bash, python, perl, php...).

Para que se pueda ejecutar sin problemas en Unix:

- Necesitan permisos de escritura

	~~~{.bash}
	$ touch miscript.py
	$ chmod +x miscript.py
	~~~

- La primera linea debe ser el _shebang_ que indica el interprete con el que se ejecuta el script.
  En `myscript.py` escribiriamos:

	~~~{.python}
	#!/usr/bin/env python3
	
	print('hola mundo')
	~~~

- Teniendolo así podemos ejecutarlo con:

	~~~{.bash}
	$ ./miscript.py
	hola mundo
	~~~

- Alternativamente, si el script no lleva ni shebang o no tiene permisos,
podemos ejecutarlo pasandoselo como primer parámetro al intérprete:

	~~~{.bash}
	$ python3 miscript.py
	hola mundo
	~~~

## Variables, valores, literales

Una **variable** es un nombre por el cual referenciamos a un **valor**.

~~~{.python}
>>> a = 23
>>> print(a)
23
>>> b = 10
>>> print(b)
10
~~~

En Python, una misma variable en un script puede ir apuntando a valores diferentes.
De hecho, puede apuntar incluso a valores de diferente tipo.

Los **literales** son la forma en que expresar en un lenguaje
los valores de un tipo concreto: `12`, `'hola'` y `0.31416`.

~~~{.python}
a = 12        # tipo entero (int)
a = 'hola'    # tipo texto (str)
a = 0.31416   # tipo coma flotante (float)
~~~

Consejos de programador abuelete:

- Aunque puedas, no es recomendable reusar las variables.
  Si en un punto la variable se refiere a una cosa,
  confunde que después se refiera a otra.
- Usar nombres de variables de una letra tampoco es bueno,
  **los nombres de las variables tienen que recordarnos a que se refieren**.

En los ejemplos, normalmente se abusa de los nombres tontos de variables.
No uses nombres tontos cuando estés programando de verdad.

> «Cualquier programador escribe un programa que entienda la máquina.
> Un buen programador se reconoce por escribir programas
> que otros programadores entienden fácilmente.»
>
>> Martin Fowler (parafraseado)

## Expresiones

Una **expresión**
combina variables y literales con **operadores**
para obtener un valor diferente.

~~~{.python}
>>> a = 23
>>> b = a+10
>>> print(b)
33
~~~

Observa, en el ejemplo anterior, la diferencia entre valor y literal:
El programa no usa el literal `33`, sin embargo acaba obteniendo ese valor mediante una expresión.

En resumen:

- Un literal es una forma de representar un valor concreto
- Una variable es un nombre que referencia a un valor
- Una expresión combina valores para obtener un valor nuevo

### Operadores numéricos

**Operadores numéricos:** Són los que operan con números y obtienen números (floats, ints...).

~~~{.python}
>>> print(10+3, 10-3, 10*3, 10/3)  # Suma, resta, multiplicación, división
13 7 30 3.3333333333333335
>>> print(10//3, 10%3)  # Division entera y resto
3 1
>>> print(10**3)  # Potencia
1000
~~~

**Ejercicio:** Usa el ipython3 como calculadora.
En ipython no necesitas `print`,
cada vez que escribes una expresión, el valor resultante se imprime.

~~~{.python}
In [1]: 10/3
Out [1]: 3.3333333333333335
~~~

### Operadores con texto

Algunos operadores numéricos tambien tienen sentido con texto:

~~~{.python}
>>> print( "Hola" + "mundo" )  # juntamos los dos textos (sin espacio!)
Holamundo
>>> print("hola"*4)    # Multiplicar por un numero, repite el texto
holaholaholahola
~~~


### Valores y operadores booleanos

Los booleanos representan condiciones, cosas que pueden ser bien ciertas o bien falsas.

- Nos sirven para tomar decisiones.
- El tipo booleano (`bool`) solo tiene dos valores posibles representados por los literales `True` y `False`.
- Se pueden combinar en expresiones mediante los operadores booleanos `or`, `and` y `not`.

~~~{.python}
annaQuiereConducir = True
toniQuiereConducir = False

annaConduce = annaQuiereConducir and (not toniQuiereConducir)
toniConduce = toniQuiereConducir and (not annaQuiereConducir)
losDosQuieren = annaQuiereConducir and toniQuiereConducir
ningunoQuiere = (not annaQuiereConducir) and (not toniQuiereConducir)
loEchamosASuerte = losDosQuieren or ningunoQuiere
~~~

Los valores resultantes de los operadores
se indican esta tabla de verdad:

`a`         `b`       `a or b`     `a and b`    `not a`
--------- - ------- - ---------- - ---------- - ---------
`True`      `True`    `True`       `True`       `False`
`True`      `False`   `True`       `False`      `False`
`False`     `True`    `True`       `False`      `True`
`False`     `False`   `False`      `False`      `True`

### Sentencia condicional `if`

Una de las utilidades de los booleanos es la capacidad
de ejecutar o no código dependiendo de una condición.

La sentencia `if` nos permite ejecutar una serie de comandos solo si se cumple una condición:

~~~{.python}
if toniConduce:
	print ('Que conduzca Toni')
if annaConduce:
	print ('Que conduzca Anna')
if loEchamosASuerte :
	print('Mejor tira una moneda, cara anna, cruz toni')
~~~






### Operadores de comparación

**Operadores de comparacion:** Son los que comparan dos valores y devuelven un valor booleano `True` o `False`.

- De magnitud: `<`, `>`, `<=`, `>=`, `<`, `==`, `!=`

	~~~{.python}
	>>> print(1<3)
	True
	>>> print(10<3)
	False
	>>> print('alfredo' < 'benito')  # orden alfabético
	True
	~~~

- De identidad: `is`, `is not`
	~~~{.python}
	
	~~~



#### La diferencia entre la igualdad y la identidad

Hasta ahora hemos visto tipos inmutables,
`str`, `float`, `int`, `bool`...
son tipos inmutables, quiere decir que son tan básicos
que lo único que puedes hacer es cambiar un valor por otro.
En esos casos, podemos usar indistintamente igualdad e identidad.

Más adelante veremos valores como las listas, los diccionarios o los objetos,
de los cuales puedes cambiar su contenido pero manteniendo su identidad como objeto.
En esos casos, los operadores de igualdad mirarán si tienen **el mismo contenido**,
mientras los de identidad mirarán **si se trata del mismo objeto**.


## Llamando funciones

Otro elemento que podemos usar en una expresión son las funciones.
Las **funciones** retornan valores calculados a partir de los parámetros que les enviamos con el operador paréntesis.

Por ejemplo, la función `max` retorna el mayor de los valores que le pasemos como parámetros.

~~~{.python}
>>> a = 100
>>> b = 200
>>> c = max(50,a,b)  # El máximo de 3 valores: 50, 100 y 200
>>> print(c)
200
~~~

Observa que `print` también es una función que llamamos con el operador paréntesis.


## Sentencias condicionales

Las sentencias condicionales permiten que 

~~~{.python}
a = 30
b = 50
if a < b:
	print("Es menor")
else:
	print("Es mayor")
~~~




Un principio básico de la sintaxis de Python:

> Siempre que una construcción del lenguaje acaba en dos puntos,
> le sigue un bloque de instrucciones indentadas un nivel.

## Definiendo funciones

Para definir una nueva función lo hacemos de la siguiente manera:

~~~{.python}
>>> def suma(a,b):
... 	resultado = a+b
... 	return resultado
>>> print(suma(1,1))
2
>>> print(suma(3,5))
8
~~~


## Tipos básicos


### Booleanos

- Tienen dos literales `True` y `False`.
- Ojo con la primera letra en mayúscula (otros lenguajes usan minúscula)
- Se pueden combinar con los operadores `and`, `or` y `not`.
- La expresión se evalua con cortocircuito:
	- Si la izquierda de un `and` es `False` ya no se evalua la expresión de la derecha, y se retorna `False`
	- Si la izquierda de un `or` es `True` ya no se evalua la expresión de la derecha, y se retorna `True`

Los cortocircuitos se usan a menudo con idiomas como:

~~~{.python}
condicionNecesaria or die("No se ha dado la condicion necesaria para seguir!!")
condicionDeError and die("Se ha dado la condicion de error!!")
~~~

### No valor, `None`

Hay un valor especial para indicar el concepto de _ningún valor_.

Cuando una función no retorna nada, retorna `None`.

Cuando no le queremos asignar nada a una variable, le asignamos `None`.

Para comprobar si una variable es `None`, usamos los operadores de identidad.

~~~{.python}
>>> a = 3
>>> b = None
>>> print(a is None)
False
>>> print(b is None)
True
>>> print(a is not None)
True
>>> print(b is not None)
False
~~~











