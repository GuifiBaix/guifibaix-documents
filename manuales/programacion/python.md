---
title: 'Programación: El lenguaje Python 3'
---

# Introducción

## Lenguajes de programación

Un lenguaje de programación es la forma en que las personas
indicamos al ordenador como se tiene que comportar.
Hay muchos lenguajes de programación.
Cada uno tiene sus puntos fuertes
o es más expresivo para según que tareas.
Por eso hay una miriada de lenguajes.

El ordenador solo entiende de instrucciones en código máquina.
El codigo máquina no está pensado para que lo entiendan las personas;
es una secuencia de números sin sentido,
en la que cada número codifica
algo que tiene que hacer el ordenador.

Los lenguajes de programación son más cercanos a algo que una
persona puede entender,
haciendo de puente entre las personas y el ordenador.
Los programas se escriben en archivos de texto,
con unas reglas bastante rígidas, la sintaxis,
que es lo que determina el lenguaje.

Para que esos ficheros de texto,
escritos en un lenguaje de programación,
se conviertan en código máquina ejecutable por el ordenador
usamos dos estrategias:

- ![Proceso de compilación](TODO)

	Un __compilador__ hace la traducción una vez,
	generando un archivo ejecutable/binario que incluye el código máquina.
	Ese archivo binario lo podremos ejecutar sin necesitar el compilador
	ni el texto original.

	Ejemplos: C++, Java, Pascal... son lenguajes compilados.

- ![Proceso de interpretación](TODO)

	Un __interprete__, en cambio, traduce el programa a código máquina
	a la vez que lo ejecuta.
	No genera el archivo binario intermedio
	y necesitaremos tanto el texto (script) como el interprete
	cada vez que lo queramos ejecutar.

	Ejemplos: Bash, Python, Perl, PHP... son lenguajes interpretados.

En general, un lenguaje interpretado se ejecutará más
lento que uno compilado, puesto que tiene que interpretar
el texto antes de decidir que código máquina ejecutar.
Esto, con los ordenadores actuales, cada vez es menos problema.
Por otro lado, un lenguaje interpretado tiene un ciclo
de desarrollo más ágil al ahorrarnos el paso de compilación.

## Buscando más cosas sobre Python

Python es un lenguaje interpretado que
se caracteriza por tener una sintaxis muy limpia y expresiva.

Nos centraremos en la version 3 (3.4.3 en el momento de escribir esto).

Para aprender Python hay tres elementos:

- El **lenguaje**, que son las reglas de como decir las cosas.
	- La descripción formal de la sintaxis la puedes encontrar en la [referencia del lenguaje](https://docs.python.org/3/reference)
	- Un poco más explicado, aunque en inglés, lo tienes en el [tutorial](https://docs.python.org/3/tutorial)
- Las **librerias estandard**, que són cosas que no hace falta que programes tú, porqué ya están programadas:
	- Encontrarás informacion en la [referencia de la libreria estándard](https://docs.python.org/3/library/)
- Las **librerías no estándard**. Aunque no vengan por defecto algunas son de uso muy extendido.
	- La mayoría de librerías no estándard, todas las decentes, están en el [Índice de paquetes](https://pypi.python.org/pypi)
	- Cada una tiene su propia documentación. Normalmente con formato similar a la de las librerías estándard.
- Si necesitas algo más, esta es [toda la documentación del lenguaje](https://docs.python.org/3/)

Hay dos formas de ejecutar código Python:

- tecleando sentencias en el interprete interactivo (python3 o, mejor, ipython3)
- escribiendo las sentencias en un archivo de texto (script) y lanzándolas de golpe con el intérprete

## Usando el intérprete interactivo

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

Cuando digamos de ejecutar algo en un interprete lo solemos escribir así:

~~~{.python}
>>> print("hola mundo")
hola mundo
~~~

- El `>>>` indica el símbolo que el interprete pone para decirte que puedes escribir.
- Lo que has de escribir es lo que va despues, del `print` en adelante.
- La segunda linea es lo que ha imprimido por la pantalla.

**Nota:** Si has programado en Python 2, ojo que en Python 3, la instrucción `print` requiere paréntesis.



## Escribiendo y ejecutando scripts

Un script es un fichero de texto que contiene
las instrucciones de un programa escrito
en un lenguaje interpretado (bash, python, perl, php...).

Para que se pueda ejecutar sin problemas en Unix:

- Necesitan permisos de escritura

	~~~{.bash}
	$ touch miscript.py   # Crea un archivo si no existe
	$ chmod +x miscript.py  # Activa los permisos de ejecución
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

# Calculando expresiones en Python

## Variables, valores, literales

Una **variable** es un nombre por el cual referenciamos a un **valor**.

~~~{.python}
>>> a = 23
>>> a
23
>>> b = 10
>>> b
10
~~~

En Python, una misma variable en un script puede ir apuntando a valores diferentes.
De hecho, puede apuntar incluso a valores de diferente tipo.

Los **literales** son la forma en que expresar en un lenguaje
los valores de un tipo concreto: `12`, `'hola'` y `3.1416`.

~~~{.python}
a = 12        # tipo entero (int)
a = 'hola'    # tipo texto (str)
a = 3.1416   # tipo coma flotante (float)
~~~

Consejos del programador abuelete:

- Aunque puedas, no es recomendable reusar las variables.
  Si en un punto una variable se refiere a una cosa,
  confunde que después se refiera a otra.
- Usar nombres de variables de una letra tampoco es bueno,
  **los nombres de las variables tienen que recordarnos a que se refieren**.

En los ejemplos, normalmente se abusa de los nombres tontos de variables.
**No uses nombres tontos cuando estés programando de verdad.**

> «Cualquier programador escribe un programa que entienda la máquina.
> Un buen programador se reconoce por que escribe programas
> que son fáciles de entender para sus compañeros (o el mismo, después).»
>
>> Martin Fowler (parafraseado)

Así que para dar a entender el significado de una variable
en vez de llamarla `a`, la llamaremos `anguloRecorrido`.
Podríamos usar muchas nomenclaturas las mas comunes son:

- **Camel Case**: `alteramosLasMayusculasAlInicioDePalabra`
- **Underscore**: `separamos_las_palabras_con_subrayados`

Ninguna es mejor que la otra pero, dentro de un proyecto,
hay que unificar la forma de llamar a las cosas.


## Expresiones

Una **expresión**
combina variables y literales con **operadores**
para obtener un valor diferente.

~~~{.python}
>>> a = 23
>>> b = a+10
>>> b
33
~~~

Observa, en el ejemplo anterior, la diferencia entre valor y literal:
El programa no usa el literal `33`, sin embargo acaba obteniendo ese valor mediante una expresión.

En resumen:

- Un literal es una forma de representar un valor concreto
- Una variable es un nombre que referencia a un valor
- Una expresión combina valores para obtener un valor nuevo

## Operadores numéricos

**Operadores numéricos:** Són los que operan con números y obtienen números (floats, ints...).

~~~{.python}
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
~~~

**Ejercicio:** Usa el ipython3 como calculadora para hacer algunos cálculos.

## Operadores con texto

Algunos operadores numéricos tambien tienen sentido con texto:

~~~{.python}
>>> "Hola" + "mundo"  # juntamos los dos textos (sin espacio!)
'Holamundo'
>>> 'hola'*4    # Multiplicar por un numero, repite el texto
'holaholaholahola'
~~~

Para delimitar los literales de texto podemos usar indistintamente comillas simples o dobles.
Esto nos da la posibilidar de usar una o otra si el texto contiene una de las dos.


## Tipos booleanos

Los booleanos representan condiciones, cosas que pueden ser bien ciertas o bien falsas.

- Nos sirven para tomar decisiones.
- El tipo booleano (`bool`) solo tiene dos valores posibles representados por los literales `True` y `False`.

## Operadores de comparación

**Operadores de comparacion:** Son los que comparan dos valores y devuelven un valor booleano `True` o `False`.

- De magnitud: `<`, `>`, `<=`, `>=`, `<`, `==`, `!=`

	~~~{.python}
	>>> 1<3
	True
	>>> 10<3
	False
	>>> 'alfredo' < 'benito'  # orden alfabético
	True
	>>> 'alfredo' == 'alfredo' # igualda
	~~~

- De identidad: `is`, `is not`
	~~~{.python}
	# Tienen algo más de sentido con objetos
	~~~

## Operadores booleanos

Los booleanos se pueden combinar en expresiones mediante los operadores booleanos `or`, `and` y `not`.

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

`a`       | `b`     | `a or b`   | `a and b`  | `not a`
--------- | ------- | ---------- | ---------- | ---------
`True`    | `True`  | `True`     | `True`     | `False`
`True`    | `False` | `True`     | `False`    | `False`
`False`   | `True`  | `True`     | `False`    | `True`
`False`   | `False` | `False`    | `False`    | `True`

## Sentencia condicional `if`

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

Un principio básico de la sintaxis de Python:

> Siempre que una construcción del lenguaje acaba en dos puntos,
> le sigue un bloque de instrucciones indentadas un nivel.

~~~{.python}
if condicion:
	sentencia1   # estas dos sentencias solo se ejecutan si la condicion es cierta
	sentencia2
sentencia3       # Esta sentencia en el nivel superio se ejecutaria siempre
~~~


## Evalua con cortocircuito o muere

La evaluación de las expresiones booleanas se hace con cortocircuito.
Eso quiere decir que si evaluamos la izquierda del operador y por la tabla
de verdad ya sabemos el resultado, no evaluamos el otro lado.

- Si la izquierda de un `and` es `False` ya no se evalua la expresión de la derecha, y se retorna `False`
- Si la izquierda de un `or` es `True` ya no se evalua la expresión de la derecha, y se retorna `True`

Esto no solo hace que la 

Así que a menudo se usa `and` y `or` para ejecutar condicionalmente la segunda expresion.

Los cortocircuitos se usan a menudo con idiomas bastante expresivos (y barriobajeros) como:

~~~{.python}
condicionNecesaria or die("No se ha dado la condicion necesaria para seguir!!")
# equivalente a:
if not condicionNecesaria :
	die("No se ha dado la condicion necesaria para seguir!!")

condicionDeError and die("Se ha dado la condicion de error!!")
# equivalente a:
if condicionDeError:
	die("Se ha dado la condicion de error!!")
~~~

Donde `die` es una funcion que imprime el mensaje y sale del programa.
El cortocircuito de evaluación hace que la funcion `die` no se ejecute
si `condicionNecesaria` es `True` o si `condicionDeError` es `False`.

En cualquier caso, hay que tener cuidado cuando usemos expresiones booleanas
porque puede que una parte de los operandos, no se lleguen a evaluar.
Si la expresion en los operandos tiene efectos colaterales necesarios,
no se ejecutarán.


## Alternativas




### La diferencia entre la igualdad y la identidad

Hasta ahora hemos visto tipos inmutables,
`str`, `float`, `int`, `bool`...
son tipos inmutables, quiere decir que son tan básicos
que lo único que puedes hacer es cambiar un valor por otro.
En esos casos, podemos usar indistintamente igualdad e identidad.

Más adelante veremos valores como las listas, los diccionarios o los objetos,
de los cuales puedes cambiar su contenido pero manteniendo su identidad como objeto.
En esos casos, los operadores de igualdad mirarán si tienen **el mismo contenido**,
mientras los de identidad mirarán **si se trata del mismo objeto**.


# Llamando funciones

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


# Sentencias condicionales

Las sentencias condicionales permiten que 

~~~{.python}
a = 30
b = 50
if a < b:
	print("Es menor")
else:
	print("Es mayor")
~~~





# Definiendo funciones

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


# Tipos básicos


## Booleanos

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

## No valor, `None`

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











