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
se conviertan en código máquina ejecutable por el ordenador,
cada lenguaje usa una de estas dos estrategias:

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
- Las **librerias estandard**, que són cosas que no hace falta que programes tú, porqué ya están programadas y vienen de serie:
	- Encontrarás informacion en la [referencia de la libreria estándard](https://docs.python.org/3/library/)
- Las **librerías no estándard**. Aunque no vengan por defecto algunas son de uso muy extendido.
	- Toda librería que se precie está incluida en el [índice de paquetes](https://pypi.python.org/pypi)
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

- Lo editamos con un editor de texto plano: kate, vim, gedit, nano, notepad++...
- La primera linea del fichero debe ser el _shebang_ que indica el interprete con el que se ejecuta el script.
  En `myscript.py` escribiriamos:

	~~~{.python}
	#!/usr/bin/env python3
	
	print('hola mundo')
	~~~

- Teniendolo así podemos ejecutarlo desde el shell con:

	~~~{.bash}
	$ ./miscript.py
	hola mundo
	~~~

- Alternativamente, si el script bien no lleva ni shebang o no tiene permisos,
podemos ejecutarlo pasandoselo como primer parámetro al intérprete:

	~~~{.bash}
	$ python3 miscript.py
	hola mundo
	~~~

# Calculando expresiones en Python

## Operadores numéricos

Podemos usar Python como una calculador escribiendo expresiones numéricas.

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

Cuando combinamos las expresiones,
se resuelven por prioridad.
Por ejemplo, la multiplicacion y división tienen mas prioridad que la suma y la resta
y la exponenciación más que la mutiplicación y la división.
Por eso:

~~~{.python}
>>> 2 * 3 + 4
10
>>> 2 + 3 * 4
14
~~~

Cuando combinamos operadores del mismo nivel, resuelven de izquierda a derecha (como se lee).

Si el orden no nos gusta podemos agrupar con paréntesis:

~~~{.python}
>>> 2 * (3 + 4)
14
>>> (2 + 3) * 4
20
~~~

A veces, los paréntesis son útiles
para que se entienda mejor una expresión compleja,
aunque por prioridad no se necesiten.

**Ejercicio:** Usa el ipython3 como calculadora para hacer algunos cálculos.


## Literales, valores, tipos y expresiones

Antes de seguir, un poquitín de vocabulario:

- Los datos que manejamos en el lenguaje son **valores**.
- Dichos valores pueden ser de muchos **tipos**.
	- Hasta ahora hemos visto números enteros (`int`), con decimales (`float`) y textos (`str`)
- La forma más directa de expresar un valor de un tipo son los **literales**. Cada tipo tiene su sintaxis:
	- Enteros: `4`, `0`, `-5234`, `0xF4` (notación hexadecimal), `0b10010` (notación binaria)...
	- Coma flotante (decimales): `3.1416`, `1.3e-13` (notacion científica)
	- Textos (strings): `'Hola mundo'`
	- ...
- Usamos **expresiones** para obtener nuevos valores a partir de otros valores existentes.

Ahora sigamos viendo más tipos de valores, literales y expresiones.


## Trabajando con texto

El tipo `str` sirve para representar texto.
Podemos construir literales de texto delimitando el texto entre comillas dobles o simples.

~~~{.python}
>>> "hola"
'hola'
>>> 'hola'
'hola'
~~~

Tener dos tipos de comillas va bien cuando el texto
contiene una de ellas, usamos la otra:

~~~{.python}
>>> print('Me dijo: "Adios" y me fuí')
Me dijo: "Adios" y me fuí
>>> print("Castellar de N'Hug")
Castellar de N'Hug
~~~

Pero, si el texto contiene ambas, tenemos otras soluciones:

~~~{.python}
>>> print('Usando sequencias de \'escape\'')
Usando sequencias de 'escape'
>>> print('''Usando las "triples" 'comillas'.''')
Usando las "triples" 'comillas'.
>>> print("""Que tambien pueden ser "dobles" 'triples'.""")
Que tambien pueden ser "dobles" 'triples'.
~~~

Las secuencias de escape con la contrabarra `\` tambien sirven para
insertar saltos de linia (`\n`), tabuladores (`\t`)...
De hecho para incluir una contrabarra hay que poner dos `\\`.
Si un literal de texto contiene muchas contrabarras,
igual nos combiene deshabilitar las secuencias de escape
prefijando una `r` de 'raw' (crudo) al literal.

Un uso común, por ejemplo, los ficheros en Windows:

~~~{.python}
>>> print("c:\temp\newitem")  # Las contrabarras se convierten en un tab y un salto de linia
c:	emp
ewitem
>>> print("c:\\temp\\newitem")   # Escapando contrabarras
c:\temp\newitem
>>> print(r"c:\temp\newitem")    # Deshabilitando secuencias de escape con el prefijo 'r'
c:\temp\newitem
~~~

Podemos usar algunos operadores numéricos tambien con texto:

~~~{.python}
>>> "Hola" + "mundo"  # juntamos los dos textos (sin espacio!)
'Holamundo'
>>> 'hola'*4    # Multiplicar por un numero, repite el texto
'holaholaholahola'
~~~

Y tenemos algunas funciones _built-in_ que podemos usar con ellas:

~~~{.python}
>>> len('hola')   # longitud de un texto
4
~~~


## Variables

Una **variable** nos permite volver a referenciar un **valor** que hemos construido antes.

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
> que son fáciles de entender por sus compañeros
> (o por él mismo, cuando pase el tiempo).»
>
>> Martin Fowler (parafraseado)

Así que para dar a entender el significado de una variable
en vez de llamarla `a`, la llamaremos `anguloRecorrido`.
Los nombres de variables no pueden contener espacios,
pero para que sea explicativa una variable suele necesitar
mas de una palabra.

- **Plain**: `sinningunadiferenciaentrepalabras`
- **Camel Case**: `alteramosLasMayusculasAlInicioDePalabra`
- **Underscore**: `separamos_las_palabras_con_subrayados`

La primera estrategia es bastante ilegible aunque para nombres cortos funciona.
La segunda es más legibles sobretodo cuando te acostumbras.
Y la tercera aunque parezca mas legible,
confunde cuando lo mezclas con otros operadores.

Se suele escoger una de las dos últimas estrategias.
Ninguna es mejor que la otra pero, dentro de un proyecto,
hay que unificar la forma de llamar a las cosas.


## Indexando y recortando (slices)

La indexacion con los simbolos `[ ]` nos permiten selecionar letras de un texto.
En general, el enésimo elemento de una secuencia.

Los índices empiezan por el cero.

~~~{.python}
>>> a = 'murcielago'
>>> a[1]   # ¡ojo! ¡La primera letra es la 0!
'u'
>>> a[0]
'm'
>>> len(a)
10
>>> a[10] # ¡ojo! el ultimo es el 9, si nos salimos, error
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
IndexError: string index out of range
>>> a[9]   # así sí
'o'
~~~

Si usamos índices negativos, empezamos por el final.
El último es el -1, el penúltimo el -2.

~~~{.python}
>>> a[-1]  # Con índices negativos empezamos por el final
'o'
>>> a[-2]
'g'
~~~

También podemos sacar rebanadas (_slices_)
usando inicio y final separado por dos puntos.
El final no se incluye.

~~~{.python}
>>> a[2:6] # de la tercera (2) a la sexta letra (5)
'rcie'
>>> a[:6] # Si no ponemos el inicio se deduce desde el principio
'murcie'
>>> a[2:] # si no pones el final se deduce que hasta el fin
'rcielago'
>>> a[:5] + a[5:]  # ¿porque el índice 5 no esta repetido?
'murcielago'
~~~

**Ejercicio:** ¿Porque en la ultima expresión no se repite el índice 5?

Un tercer elemento en el _slice_ es el paso;
cuantas casillas saltamos.
Normalmente es 1, pero si lo especificamos...

~~~{.python}
>>> a[::2]  # saltamos las letras de dos en dos
'mrilg'
>>> a[1::2]  # si le damos un offset
'uceao'
>>> a[6:2] # si inicio y fin no estan ordenados, retorna texto vacío
''
>>> a[6:2:-1]  # pero con un paso negativo, va hacia atrás
'leic'
~~~

**Pregunta:** ¿Porqué en la última expresión no son las mismas letras invertidas que con `a[2:6]`?

**Pregunta:** ¿Qué retornaria a[5:5]? ¿Porqué?


> **¿Porque la complicación de que se empiece por cero y que el índice del final no se incluya?**
>
> Algunos lenguajes lo intentaron, pusieron al 1 como primer índice, pretendiendo ser más simples.
> Parece que fuera a ser mas simples así.
> Pero, por las operaciones que se suelen hacer cuando programas,
> que los índices empiecen por 1 acaba siendo un incordio.
> **Esos lenguajes que lo intentaron perecieron o malviven siendo muy odiados.**


## Llamando funciones

Otro elemento que podemos usar en una expresión son las funciones.
Las **funciones** retornan valores calculados a partir de los parámetros que les enviamos con el operador paréntesis.

Por ejemplo, la función `max`, incluida en el lenguaje,
retorna el mayor de los valores que le pasemos como parámetros.

~~~{.python}
>>> a = 100
>>> b = 200
>>> c = max(50,a,b)  # El máximo de 3 valores: 50, 100 y 200
>>> print(c)
200
~~~

Observa que `print`, que hemos usado antes,
también es una función que llamamos con el operador paréntesis.

El tutorial oficial de Python tiene una
[lista de las funciones incluidas](https://docs.python.org/3/library/functions.html)
en el lenguaje (_built-in_).


## Definiendo funciones

Para definir una nueva función lo hacemos de la siguiente manera:

~~~{.python}
>>> def media(a, b):
...     suma = a+b
...     return suma/2
...
>>> media(3, 1)
2.0
>>> media(4, 5)
4.5
~~~

- La definición de una función comienza con la palabra reservada `def`.
- Le sigue el nombre que daremos a la función, `media` en este caso.
	- El nombre sigue las mismas normas que para las variables.
- Después, entre parentesis y separados por comas, la lista de parámetros.
	- Los parametros son variables que existiran sólo mientras se ejecute la función
	- Se les asignan los valores que pasamos entre paréntesis
		- En la primera llamada a=3. En la segunda llamada a=4.
		- En la primera llamada b=1. En la segunda llamada b=5.
- Todas las sentencias que finalizan con `:`, van seguidas de un conjunto de sentencias indentadas un nivel más.
	- Decimos que estas sentencias indentadas están dentro de la sentencia que les da paso con los dos puntos.
	- En el caso de una función son las sentencias que se ejecutarán cuando la llamemos.
	- Los puntos suspensivos los escribe el interprete para indicar que aun tenemos que acabar la sentencia.
	- Para salir de los puntos suspensivos dejamos una linea en blanco
- La primera sentencia de dentro crea una variable `suma`
	- Las variables que creemos dentro de una función solo existen mientras la función se ejecuta.
	- En jerga se dice que es una variable _local_, en contraposicion de las variables que se definen fuera de funciones que se les llama _globales_
	- Que las variables tengan un ámbito local nos ayuda a no tener que buscar nombres que no colisionen con los de otras funciones
- La ultima sentencia es una sentencia especial `return`
	- Una sentencia `return` sale de la función y devuelve el control al llamante
	- Ademas el llamante recibirá el valor resultante de la expresión que va después del `return`
	- Si hubiera sentencias después del return, no se seguirían ejecutando

## No valor, `None`

¿Qué pasaría si se llega al final de la función y no encuentra ningún return?

Pues que el llamante retornaría un no-valor. También llamado `None`.
Cuando no ponemos ninguna expresión en el return tambien se retorna `None`.

Hay un valor especial para indicar el concepto de _ningún valor_.

- Cuando una función no retorna nada, retorna `None`.
- Cuando no le queremos asignar nada a una variable, le asignamos `None`.

~~~{.python}
>>> None # El interprete no muestra resultado si una sentencia resulta en None
>>> print(None)  # Pero lo podemos imprimir explícitamente
None
>>> a = print("hola")  # La funcion print tampoco retorna nada
hola
>>> a   # Lo dicho
>>> print(a)
None
>>> def noReturnFunction():
...     2+2
...
>>> noReturnFunction()
>>> print(noReturnFunction())
None
~~~


# Empezando a programar, tomando decisiones

Programar es dejar que el ordenador tome sus decisiones.
Nosotros le decimos en el programa como las tiene que tomar.
Cuando el se encuentre con la disyuntiva, tomará,
según lo que le digamos, una opción o otra.

Para programar decisiones es necesario entender bien los booleanos.

## Tipos booleanos

Los booleanos son valores representan condiciones, cosas que pueden ser bien ciertas o bien falsas.

A pesar de su simplicidad son la base de la programación, puesto que nos sirven para tomar decisiones.

El tipo booleano (`bool`) solo tiene dos valores posibles representados por los literales `True` y `False`.

## Operadores de comparación

Una forma de obtener booleanos es comparando valores.

Los **operadores relacionales** devuelven `True` o `False` dependiendo de la .
(`<`, `>`, `<=`, `>=`, `<`, `==`, `!=`)

~~~{.python}
>>> 1<3
True
>>> 10<3
False
>>> 'alfredo' < 'benito'  # orden alfabético
True
>>> 'alfredo' == 'alfredo' # igualdad
True
>>> 'alfredo' != 'alfredo' # desigualdad
False
>>> a = 3
>>> 1 <= a <= 10    # ¿es a un numero del 1 al 10, ambos incluidos?
True
~~~

**Operadores de identidad:** Son los que comparan si un valor es el mismo que otro. (`is`, `is not`)
Para los tipos básicos que han salido hasta ahora, son equivalentes a igualdad y desigualdad.
Pero veremos objetos más adelante, las estructuras, que aunque contengan los mismos valores,
mantienen 'identidades' diferentes porque los podemos modificar de forma independiente.
Por eso se les llama **mutables**.

El caso es que para los tipos básicos los operadores de identidad
también nos sirven porque son más expresivos que los de igualdad.

~~~{.python}
>>> guy = 'alf' + 'redo'
>>> guy is 'alfredo' # identidad 
True
>>> guy is not 'alfredo' # no identidad
False
~~~

## Sentencia condicional `if`

Una de las utilidades de los booleanos es la capacidad
de ejecutar o no código dependiendo de una condición.

La sentencia `if` nos permite ejecutar una serie de comandos solo si se cumple una condición:

~~~{.python}
if name is 'Aitor':
	print ('Hola Aitor, bienvenido a casa')
if name is not 'Aitor':
	print ('Hola, desconocido, ya te puedes pirar')
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


## Alternativas

Es frecuente que después de evaluar una condición para ver si tenemos que hacer algo,
tengamos que evaluar lo contrario para hacer otra cosa alternativa.
Para ello es muy util el `else`.
Hay que ponerlo al nivel del `if` y contiene su bloque de sentencias alternativas.

Reescribiendo el ejemplo anterior solo evaluando una condicion:

~~~{.python}
if name is 'Aitor':
	print ('Hola Aitor, bienvenido a casa')
else:
	print ('Hola, desconocido, ya te puedes pirar')
~~~

Está bien, pero tambien podemos tener mas de una alternativa.
Para eso sirve la sentencia `elif` (viene de _else if_).

~~~{.python}
if name is 'Aitor':
	print ('Hola Aitor, bienvenido a casa')
elif name is 'David':
	print ('Hola David, Aitor llegará en un momento.')
else:
	print ('Hola, desconocido, ya te puedes pirar')
~~~


## Decisiones complejas, operadores booleanos

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

La regla es:

- el `or` es cierto si cualquier operando es cierto.
- el `and` es cierto si todos los operandos son ciertos.


## Evalua con cortocircuito o muere

Otra forma de ver los operadores `and` y `or` es la siguiente:

- Si los operandos son el mismo valor, retornar ese valor
- Si son distintos:
	- en el `or`, el `True` es dominante sobre el `False`
	- en el `and`, el `False` es dominante sobre el `True`

Así pues, en una expresion `or` o `and`,
cuando evaluamos el primer operando
y nos da el valor dominante,
Python no evalua el segundo operando porque ya sabe el resultado.
Es lo que se llama evaluación por cortocircuito,
y se hace para que el programa vaya más rápido.

~~~{.python}
>>> pi = 3.1416
>>> r = 10
>>> # Como la primera parte ya es cierta, la segunda no se llegara a evaluar
>>> (2*r*pi > 3)  or   (3*r**2*pi>10)
True
~~~

Y pasa lo de siempre:
haces algo por algún motivo y sale alguien que lo utiliza para otro.
Mucha gente aprovecha los cortocircuitos para construcciones
condicionales que la verdad es que quedan
bastante expresivas (y barriobajeras) como:

~~~{.python}
# Barriobajeras? claro:
giveMeTheMoney or die("you sucker")
touchMe and die("you dared shit")

# En realidad se usan asi:

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

## Condiciones anidadas

Podemos anidar un `if` dentro de otro formando un árbol de decisión:

~~~{.python}
if meGustaElFutbol :
	if miEquipo is 'Real Madrid':
		print("Merenge!")
	elif miEquipo is 'Barça':
		print("Cules!")
	else:
		print("whatever")
else
	print("Mejor pensemos en otras cosas mas productivas")
~~~

Observa que los `else`s y `elif`s estan al mismo nivel que el `if`
al que se corresponden y que los bloques de sentencias estan
indentados aún más adentro.



# Estructuras de datos

Hasta ahora hemos visto valores muy simples.
Una de las potencias de Python es la facilidad con la que se manejan estructuras de datos mas complejas.

## Listas

Las listas (tipo `list`) son sequencias ordenadas de valores.

Los literales de las listas se construyen incluyendo los valores entre corchetes `[]` y separados por comas.
Podemos acceder a los elementos con indices y rebanadas igual que con los textos `str`.

~~~{.python}
>>> l = [1,2,3,4,5]
>>> l[3]
4
>>> l[-1]
5
>>> l[2::2]
[3,5]
~~~

Los valores pueden ser de tipos diferentes. Incluso pueden ser otras listas.

~~~{.python}
>>> # Una lista que contiene listas
>>> l = [[11,12],[21,22],'ultimo']
>>> l[-1]
'ultimo'
>>> l[1]
[21,22]
>>> l[1][1]
22
~~~

Podemos usar los operadores numericos como con los textos:

~~~{.python}
>>> [1,2,3] + [4,5,6] # Uniendo dos listas
[1,2,3,4,5,6]
>>> [0]*10  # creando una lista de 10 ceros
[0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
~~~

Cuando trabajamos con textos, siempre creamos
nuevos valores a partir de los anteriores.
En cambio las listas las podemos modificar
y mantienen su identidad aunque cambien su valor.

~~~{.python}
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
~~~




## Bucles

La sentencia `for` permite repetir la ejecución de sus subsentencias,
para una serie de valores en una secuencia (es como se llaman los tipos que tienen items).
Define una variable que va adoptando cada vez un valor de la secuencia.

~~~{.python}
>>> l = [1,2,3,4]
>>> for item in l :
...     doble = item*2
...     print(doble)
2
4
6
8
~~~

En este código, la variable `item` va adoptando los valores
incluidos en la lista y ejecuta las sentencias de dentro.

A diferencia de las funciones, aquí las variables como `doble` o `item` no se limitan al `for`.


## Uniendo y separando (`split` y `join`)

Dos operaciones muy comunes son dividir un texto usando
un separador obteniendo una lista de textos,
o al revés, dada una lista juntarla con un separador.

Para ello usaremos los métodos `join` y `split`.
Un método es una función que estan ligadas a un objeto.
Se llaman con la sintaxis del punto (`.`).

~~~
objeto.metodo(parametros)
~~~

Cada tipo de objeto tiene sus propios métodos.
`join` y `split` son métodos de los objetos de tipo `str`.

La ventaja de los métodos respecto a las funciones es que
el método no contamina el espacio de nombres.
Objetos de tipos diferentes pueden tener métodos con el mismo nombre,
lo cual tiene sentido si hacen cosas conceptualmente similares.
Si tuvieramos que buscar un nombre para la funcion que hace
lo mismo para cada tipo acabariamos con funciones llamadas
`hazlo_texto`, `hazlo_lista`...


~~~{.python}
>>> l = ['a','b','c']
>>> s = '-'.join(l) # Las juntamos con el '-'
>>> s
'a-b-c'
>>> s.split('-') # Usamos el '-' como separador
['a','b','c']
~~~



El constructor de lista recibe un iterable.
Como los textos son iterables, crea una lista con cada letra como elemento.

~~~{.python}
>>> list('abc') # Separamos por letras
['a','b','c']
>>> ''.join(['a','b','c']) # Juntarlas con la cadena vacia como separador
'abc'
~~~


**Ejercició:** Haz un script que dada una lista de listas,
que representa lineas de columnas,
imprima por pantalla un CSV con el tabulador como separador.


~~~{.python}
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
for linia in tabla:
	print('\t'.join(linia))
~~~

## Listas del tirón

Si quisieramos crear una nueva lista con los valores que antes hemos imprimido:

~~~{.python}
>>> l = [1,2,3,4]
>>> l2 = []
>>> for item in l:
...     l2.append(item*2)
>>> l2
[2,4,6,8]
~~~

Python ofrece una forma directa de crear listas a partir de otras listas,
las _comprehension lists_, o listas creadas del tirón.

~~~{.python}
>>> l = [1,2,3,4]
>>> l2 = [ item*2 for item in l ]
>>> l2
[2,4,6,8]
~~~

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


~~~{.python}
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
~~~

Problema la linea vacia del final.
Las _comprehension lists_ tienen una parte opcional que les permite
filtrar los items del iterable de entrada.


~~~{.python}
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
~~~

## Empaquetando y despempaquetando valores, las tuplas `tuple`

En python podemos asignar a dos variables a la vez:

~~~{.python}
>>> a, b = 1, 2
>>> a
1
>>> b
2
~~~

Por eso no hay la funcion de `swap`, típica de otros lenguajes,
para intercambiar los valores de dos variables.
En Python se hace simplemente así:

~~~{.python}
a, b = b, a
~~~

A sentencias como las de arriba se les llama desempaquetar una tupla.
Por tupla nos referimos a la parte derecha:
Dos valores separados por una coma.

Una tupla de hecho es otro tipo de dato (`tuple`),
muy parecido a una lista, pero no permite modificar su contenido.
Como con los textos, podemos generar una a partir de otra, pero no modificar la existente.
Sus literales son como las listas pero sin corchetes.
A menudo se necesitan paréntesis cuando se usan en sitios donde podría haber comas:
como parámetro de una funcion, dentro de un literal de lista...
Así que por si acaso siempre se ponen los paréntesis,
al menos que como en la expresión de arriba sea muy claro.

Tambien podemos desempaquetar listas:

~~~{.python}
>>> a, b = [3, 4]
>>> a
3
>>> b
4
~~~

Podemos crear una lista, a partir de una tupla y al revés usando los constructores:

~~~{.python}
>>> t = 2, 4, 6
>>> t
(2,4,6)
>>> t1,t2,t3 = t   # desempaquetando
>>> list(t)
[2,4,6]
>>> list( (2,4,6) )   # el literal requiere parentesis si es un parámetro
[2,4,6]
>>> tuple(list( (2,4,6) ) )
(2,4,6)
~~~

Las tuplas son muy útiles cuando funciones retornan más de un valor.
Por ejemplo la funcion _built-in_ `divmod` retorna la división entera
y el resto a la vez evitando tener que calcular dos veces la división.

~~~{.python}
>>> div, mod = dm = divmod(30,7)
>>> dm
(4,2)
>>> div
4
>>> mod
2
~~~

Tambien podemos desempaquetar en un `for`:

~~~{.python}
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
~~~

**Ojo:**
El desempaquetado debe hacerse solo cuando estamos seguros de que
el numero de valores que aceptamos coincide con el que desempaquetamos.
Si no, veremos errores. Familiaricemonos con ellos, que saldrán:

~~~{.python}
>>> a,b = 1,2,3  # Nos sobran valores
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
ValueError: too many values to unpack (expected 2)
>>> a,b,c = 1,2  # Nos faltan valores
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
ValueError: need more than 2 values to unpack
~~~

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

~~~{.python}
>>> t = 1,2
>>> t2 = t
>>> t += 3,4
>>> t # Apunta a un valor distinto
(1,2,3,4)
>>> t2 # Aun apunta al anterior valor
(1,2)
~~~

Es decir, pasa igual que con los textos.
En cambio con listas, como habíamos visto:

~~~{.python}
>>> l = [1,2]
>>> l2 = l
>>> l += [3,4]
>>> l
[1,2,3,4]
>>> l2
[1,2,3,4]
~~~



## Conjuntos `set`

Un `set` es un contenedor, como lo es una lista, pero con las siguientes diferencias.

- No mantiene un orden entre los elementos
	- no podemos indexarlos, ni slices
	- no nos asegura un orden cuando iteramos en él
- No acepta duplicados
	- Insertar un valor que ya està, no tiene efecto

Los literales del set son como los de las listas, pero usan los corchetes rizados `{}`.

~~~{.python}
>>> { 1, 2, 3, 1 }  # El 1 esta duplicado
{1,2,3}
>>> set([1,2,3])  # con el constructor lo podemos crear a partir de una lista
{1,2,3}
>>> list({1,2,3})  # y al reves
[1,2,3]
>>> ''.join(set('abracadabra')) # cuantas letras diferentes usa un texto?
'rcabd'
>>> ''.join(sorted(set('abracadabra'))) # no nos aseguran orden, usamos la funcion sorted
'abcdr'
~~~

Es muy práctico para algunas cosas:

- Comprobar si un valor esta incluido con el operador `in` o `not in` (la lista también lo tiene pero es más lenta)
- Calcular intersecciones, uniones, y todas aquellas cosas de teoría de conjuntos que hicimos en mates

~~~{.python}
>>> s1 = set(range(3,9))
>>> s1
{3,5,6,7,8}
>>> 3 in s1  # Comprobando pertenencia
True
>>> 10 in s1
False
>>> 3 not in s1
False
>>> s1 + set(range(4,12)) # Union
{3,4,5,6,7,8,20,21,22,23,24}
~~~









