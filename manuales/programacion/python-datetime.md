# Manejo de fechas `datetime`, `dateutils`

## Objetivos de la unidad

- Conocer el módulo estándard `datetime` para el manejo de fechas y horas
- Conocer el módulo de GuifiBaix `dateutils` que extiende `datetime`
- Familiarizarse con el concepto de refactoring y el código como algo en evolución
- Ser capaz de hacer un pequeño refactoring en código real
- Ser capaz de hacer un script de migración de datos YAML
- Introducir algunos conceptos de orientación a objetos:
	- Métodos de clase vs métodos de instancia
	- Métodos factoría
	- Propiedades (las de Python, diferentes de las que vimos en la unidad de Qt)

Para ello:

- Veremos lo básico del módulo `datetime`
- Introduciremos el concepto de _refactoring_.
- Veremos un ejemplo de como sucesivos refactorings de código que usaba `datetime`, derivaron contenido actual del módulo `dateutils`
- Finalmente, plantearemos paso a paso un refactoring pendiente,
  para que las fechas de los yaml de las facturas sean fechas y no textos,
  incluyendo el refactoring en sí y la migración de los datos.


## El módulo `datetime`

El módulo `datetime` es el módulo estándard para representar tiempo.
Contiene cuatro clases importantes:

- `date`: fechas (hoy, mañana...)
- `time`: horas (las tres y media)
- `datetime`: fecha + hora (hoy a las tres y media)
- `timedelta`: intérvalos de tiempo (tres dias y cuatro horas)

Entendamos lo que es un `timedelta` con un ejemplo:

```python
>>> import datetime
>>> hoy = datetime.date(2016,6,15)    # year, month, day
>>> ayer = datetime.date(2016,6,14)
>>> hoy - ayer
datetime.timedelta(1)
>>> ayer + datetime.timedelta(days=2) # añadimos un intérvalo de dos dias
datetime.date(2016,6,17)
```

Repasando un poco como llamar a funciones y métodos:

- El constructor de `date`, requiere 3 parametros obligatorios: `year`, `month` y `day`
- Los parámetros del constructor de `timedelta`, en cambio, son opcionales,
  así que puedes escoger cuales usas para expresar el intervalo explicitando el nombre:
  `days`, `hours`, `minutes`, `seconds` y `microseconds`.
  Siendo `hours` el primer parámetro,
  podríamos haber usado `datetime.timedelta(2)` pero este es un ejemplo claro
  en el que explicitar el nombre del parámetro ayuda a entender que hacemos.

> **Ejercicio:**
> Prueba replicar el ejemplo anterior un `timedelta` de 48 horas.


> **Ejercicio:**
> Intenta crear una fecha con parámetros incorrectos y observa el resultado.
> Así te familiarizarás con los errores cuando te los encuentres inexperadamente.
> Algunos casos de error a probar:
> 
> - uno de ellos no sea un entero, por ejemplo un texto o un `float`
> - falte o sobre uno
> - Que uno de ellos (mes o día) este fuera de rango (0 o 100)
> - En orden inverso (no iso)

> **Ejercicio:**
> Crea una función dada una fecha de emisión de una factura,
> devuelva la fecha de vencimiento sumándole 15 días.
> Usa para ello un `timedelta`.

Las clases `date`, `datetime`, y `time` tienen métodos útiles como `today` y `now`
cuyo resultado depende del momento actual.

```python
>>> import datetime
>>> print(datetime.date.today())
2015-06-02
```

Fíjate que aquí llamamos a un método usando la sintaxis de punto (`.`)
con una clase y no con una instancia.
Llamar a un método sin instáncia, usando la clase directamente,
se puede hacer sólo si el método es de los llamados **métodos de clase**.
En la documentación de las clases se suele indicar cuando lo son.
En oposición los otros métodos, los normales, se llaman **métodos de instancia**.

Ademas este método es lo que llamamos un **método factoría**.
Es decir un método cuyo propósito es crear, _fabricar_, objetos.
Cuando el método factoria genera instancias de la misma clase
suele ser tambien método de clase como en este caso, pero
no tiene porqué.

> **Ejercicio:**
> Averigua tu edad en días restándole tu fecha de nacimiento a `date.today()`.
> Obtendras un objeto tipo intervalo con tu edad en dias.
> Averigua como extraer los dias como un entero y
> divídelo por `365.25` para conocer tus edad astronómica.

Otra cosa interesante del ejemplo anterior es que,
cuando enviamos una fecha al `print`, ya no nos devuelve
el texto de una llamada al constructor `datetime.date(2015,6,2)`
sino una fecha en formato ISO 8601 (YYYY-MM-DD) como `2015-06-02`.
Esta es una representación en texto de la fecha muy práctica,
pues en ella coinciden el orden cronológico (por fecha)
con el orden lexicográfico (alfabético) de la representación.

La representación por defecto de las fechas es en formato ISO 8601.
Si queremos obtener otro formato, por ejemplo el típico `DD/MM/YYYY`
o el anglosajón `MM/DD/YYYY`
tenemos que usar el método `strftime`.

```python
>>> fecha.strftime('%d/%m/%Y')
'02/06/2015`
>>> fecha.strftime('%m/%d/%Y')
'06/02/2015`
```

Los códigos con `%` estan documentados en la [referéncia de la librerias estándard](https://docs.python.org/3/library/time.html#time.strftime).

> **Ejercicio:**
> En algunos procedimientos administrativos, por ejemplo los ficheros SEPA,
> se tienen que generar fechas usando el que llamamos formato compacto
> que es igual que el ISO pero sin guiones, pe `20150602`.
>
> - Genera con el `strftime` ese formato YYYYMMDD
> - Genera tambien el formato iso con el strftime YYYY-MM-DD

## Refactorizar

Una **refactorización** (refactoring) es una modificación del código que no tiene impacto en el comportamiento externo.

El nombre viene del algebra, donde puedes alterar el orden de los factores sin alterar el producto.

### Ejemplo

Por ejemplo:

```python
print("Hola Aitor")
```

Lo puedo refactorizar como:

```python
print("Hola {}".format("Aitor"))
```

Y posteriormente en:

```python
nombre = "Aitor"
print("Hola {}".format(nombre))
```

En ningún momento hemos cambiado lo que hace el programa, pero:

- El primer código es mucho más sencillo y más veloz, poco flexible.
- El segundo es más complicado y hace mas operaciones. Pero me abre camino hacia el tercero.
- El tercero también es más complicado, pero me permite, en un futuro tomar esa variable y cambiarla.

Podemos llevarlo más allá extrayendo una función:

```python
def saluda(nombre) :
	print("Hola {}".format(nombre))

nombre = "Aitor"
print("Hola {}".format(nombre))
```

Y finalmente usando la función

```python
def saluda(nombre) :
	print("Hola {}".format(nombre))

saluda("Aitor")
```

Ahora que hemos refactorizado, podemos añadir la funcionalidad que queriamos añadir.
Aquí nos quitamos la gorra de refactor, y nos ponemos la gorra de añadir/modificar funcionalidad.

```python
def saluda(nombre) :
	print("Hola {}".format(nombre))

saluda("Aitor")
saluda("David")
```

Estos pequeños pasos estan sistematizados,
de forma que cada acción de refactoring (extraer una función, añadir un parámetro...)
tienen recetas con un listado de cosas, de sentido común,
a comprobar para asegurarnos de que modificando el código
no se modifica el comportamiento.

Fíjate que ponemos nuestra mente en dos modos:

- **Modo refactoring:** Ponemos toda nuestra atención en que las modificaciónes que hagamos no alteren el producto
- **Modo funcionalidad:** Nos centramos en alterar ese producto, cambiando lo mínimo posible el código, para pasar un test en concreto

Es muy importante no mezclar refactorings con cambios en el comportamiento.
Todo es mucho más sencillo si cuando refactorizas, esperas que todo funcione igual.
Si algo cambia, no has refactorizado bien.
Cuando cambias comportamiento, que sea porque añades o has modificado un test,
y que ese test refleje ese cambio de comportamiento.

Si tenemos que cambiar mucho el código para añadir una funcionalidad,
es señal de que nos hemos dejado refactorings por el medio.

En resumen, cuando refactorizamos:

- Pequeños pasos
- No han de añadir funcionalidad
- Nos apoyamos en los tests que tenemos (¿no tenemos? ya sabemos lo que toca)

### Refactorizando con tranquilidad: los tests

Para refactorizar con la conciencia tranquila
es importante tener una batería de tests que te avisen
cuando te sales del camino.

Los tests han de comprobarse muy a menudo y
comprobar a ojo que el resultado es el que toca es una tarea muy pesada.
Si lo tenemos que hacer a ojo, no lo vamos a hacer o no vamos a prestar la atención necesaria.

**Solucion:** Hagamos que el ordenador compruebe los resultados por nosotros.

- Si funciona, que no nos maree enseñándonos la salida, que simplemente nos diga que 'todo bien'.
- Si algo no funciona, que entonces grite y nos enseñe la salida errónea comparada con la esperada.

> **Ejercicio:**
> Construye un script en bash (usando entre otros el comando `diff`)
> que compare la salida estandard del script anterior
> contra una salida esperada.
>
> - Tenemos la salida esperada guardada en un fichero.
> - Redireccionamos la salida obtenida en un segundo fichero
> - Hacemos el `diff` entre los dos.
> - Si son iguales el diff no muestra nada y da un codigo de error 0.
> - Si son diferentes el diff muestra las diferencias y da un codigo de error distinto de 0.
> - Puedes usar `diff file1 file2 && echo Todo bien! || echo LOS TESTS FALLAN!!!


Normalmente, los tests se añaden son de los que se llaman _unitarios_,
testean una sola cosa.
Antes de cada modificación que no es un refactoring,
hay que hacer un test que la justifique.
Es decir, un test que falle mientras no añadamos la nueva funcionalidad.

Con esta _norma_ nos aseguramos
de que todas las funcionalidades estén cubiertas y
de que no hagamos tests innecesarios.

A menudo, encontramos código a refactorizar no está cubierto por tests unitarios.
Si queremos tener algo de confianza a la hora de refactorizar,
una solución pasable puede ser plantear tests de espalda contra espalda (back-to-back, b2b).
El tests que has hecho antes con el comando `diff` es un test b2b.
Un tests b2b, ve el programa como una caja negra,
dada una misma entrada compara una salida antigua con la actual con el código modificado.
No nos planteamos, si la salida es buena o mala, simplemente queremos que no cambie.
Si validamos la primera vez a ojo la salida, debería seguir siendo igual.

A diferencia de los unitarios que añadimos para cada variación de la funcionalidad,
los b2b no consideran todos los casos, así que son débiles:
Es posible que cambie la funcionalidad y no lo detectemos.
O, como veremos, si la salida depende de unos datos que evolucionan,
la salida podría variar sin que cambie el programa, solo el entorno o los datos.
Por eso decimos que son tests débiles.
Pero para tomar el pulso a unos cambios puntuales nos puede sacar del atolladero.

## Un caso real: el origen del modulo `dateutils`

### Centralizando el formateo de fechas

Desarrollando nuestro programa de gestión, pasó que las llamadas a `strftime`
empezaron a pulular por todo el código.
A veces nos equivocabamos al escribir el formato,
a veces simplemente emborronaban el código.

> **Máxima: Don't Repeat Yourself, DRY, No te repitas.**
> Si estás escribiendo el mismo código una y otra vez, busca la forma de no repetirlo.
> El código repetido,
> 
> - Es trabajo de más
> - Aunque para escribirlo podemos cortar y pegar y es fácil, para leerlo sigue estando ahi
> - Si tienes que corregir un error, tienes que arreglarlo en un monton de sitios ¡y acordarte!

Para solventar la repetición fuimos creando funciones
que dada una fecha retornaban un formato o otro:

```python
def slashDate(date):
	return date.strftime('%d/%m/%Y')
```

Como al final teniamos varias de estas y las usábamos en varios módulos,
acabamos creando un módulo llamado `dateutils` con ellas dentro.

- `catalanDate` para las fechas de inicio y fin de los periodos de facturación y descuentos en las facturas: `2 de Juny de 2015`
- `slashDate` para las fechas de las facturas, para adaptarnos al formato de factura de Gats.
- `compactDate` para los ficheros SEPA y algunos mas


### Parseando fechas

Otra cosa que teniamos que hacer en varios sitios es tomar algo que nos llega
y asegurar que lo que tenemos sea un `datetime`.
Por ejemplo, nos puede llegar un texto con la fecha en formato ISO,
o cualquier otro de los que teniamos arriba,
nos puede llegar un `datetime`, una tupla año-mes-día, o al reves una tupla de día-mes-año.

Las clases de `datetime`, tienen el inverso de `strftime` que es `strptime`.
Como `today` es un método de clase y factoria.

```python
> s = '2015-06-02'
> datetime.datetime.strptime(s,'%Y-%m-%d')
datetime.datetime(2015,6,2,0,0)
```

Claro que esto funciona porque sabemos que formato nos va a llegar,
y esto era así la mayoria de las veces.
Pero a veces no llegaba el formato esperado y ese día el programa fallaba.
Así que, si queremos que nuestro programa se sepa adaptar a la mayoría de casos,
debemos detectar el formato y generar la fecha.

Así que para eso creamos la función `dateutils.date`, que transparentemente convertía,
si es posible, lo que sea a un objeto `datetime.date`.

Por ejemplo:

```python
>>> dateutils.date(2015, 6, 2)  # tres enteros como el constructor de datetime.date
datetime.date(2015,6,2)
>>> dateutils.date((2015, 6, 2))  # Una tupla
datetime.date(2015,6,2)
>>> dateutils(datetime.date(2015,6,2)) # un datetime.date
datetime.date(2015,6,2)
>>> dateutils.date("2015-06-02")  # una fecha iso
datetime.date(2015,6,2)
>>> dateutils.date("02-06-2015")  # fecha tradicional con guiones
datetime.date(2015,6,2)
>>> dateutils.date("02/06/2015")  # fecha tradicional con barras
datetime.date(2015,6,2)
>>> dateutils.date("02062015")   # compacto orden tradicional
datetime.date(2015,6,2)
>>> dateutils.date("20150602")   # compacto orden iso
datetime.date(2015,6,2)
```

Implementada en un solo sitio y cubierta por tests,
la función nos da la seguridad de que si falla es porque no es una fecha.

> **Ejercicio:**
> Usa la función `dateutils.date` e intenta putearla.
> Si encuentras un caso que no funcione, implementa el test y hazlo pasar.
> Algún caso habrá.

Haciendo que todas las funciones de formateo lo primero que hagan
es llamar a date sobre lo que sea que le pasemos por parámetro,
las funciones de formato se vuelven muy versátiles:

```python
>>> def slashDate(*args):
... 	adate = date(*args)
... 	return adate.strftime('%d/%m/%Y')
>>> slashDate('20150602')
'02/06/2015'
```

### Rellenando plantillas con templates

Repasamos como rellenar plantillas con ficheros YAML.

Creamos datos YAML con los que rellenar plantillas con el modulo de GuifiBaix `namespace`.

```python
>>> from namespace import namespace as ns
>>> datos = ns()
>>> datos.nombre = "Perico"
>>> datos.apellido1 = "Palotes"
>>> datos.direccion = ns()
>>> datos.direccion.via = "Rue del Percebe"
>>> datos.direccion.numero = 13
>>> datos.direccion.municipio = "Villabotijo"
>>> datos.direccion.provincia = "Zamora"
>>> datos.fechaNacimiento = datetime.date(1988,3,20)
>>> datos.dump()
nombre: Perico
apellido1: Palotes
direccion:
	via: Rue del Percebe
	numero: 13
	municipio: Villabotijo
	provincia: Zamora
fechaNacimiento: 1988-03-20
>>> datos.dump("perico.yaml")
```

```python
plantilla = """\
Hola, me llamo {nombre} {apellido1}.
Nací el {fechaNacimiento}.
Vivo en {direccion.via}, número {direccion.numero}
de {direccion.municipio}
en la província de {direccion.provincia}.
"""

datos = ns.load('perico.yaml')
salida = plantilla.format(**datos)
print(salida)
```

**Nota:**
Hay un comando de GuifiBaix que permite,
desde línia de comandos,
aplicar un YAML a un fichero con la plantilla.

```bash
$ nstemplate.py apply datos.yaml plantilla.md salida.md
```

### Formateando fechas en los templates

La librería `python-yaml` que usamos para cargar los ficheros YAML
detecta los campos con fechas ISO y genera datos de tipo `datetime.data`.
Y cuando usamos una fecha `datetime.date` en un `format`
lo que se imprime es la fecha en formato ISO.

```python
>>> from namespace import namespace as ns
>>> datos = ns()
>>> datos.today = datetime.today()
>>> "Hoy es {today}".format(**datos)
'Hoy es 2015-06-02'
```
El problema llega si queremos obtener en una plantilla
algun formato diferente al ISO, que es lo que suele pasar.

El método `format` nos permite poder acceder a los attributos usando la sintaxis del punto.
Las fechas tienen atributos como `year`. `month`, `day`...
Así que podríamos hacer:

```python
>>> "Hoy es {today.weekday} y estamos en el mes de {today.month}".format(**datos)
```

> **Ejercicio:**
> Explora otros atributos de la fecha usando el tabulador.
> Algunos son atributos, que se pueden acceder sin paréntesis,
> otros son funciones y para acceder necesitaremos llamarlas.

Para poder escoger que formato imprimimos en una plantilla,
aplicándole un YAML directamente,
convendría tener nuestros formatos disponibles como atributos en las fechas.
Igual que estan disponibles `day`, `year`, `month` y `weekday`.

Con ese propósito,
lo que se hizo fue crear una clase, `dateutils.Date`,
que extiende la clase `dateutils.date` y además:

- su constructor acepta, no sólo tres parametros `year`, `month`, `date`,
  sinó también todo lo que acepta la función `dateutils.date`.
- tiene atributos (calculados) `compact`, `slashDate`, `catalanDate`...

> **Detalle avanzado:**
> En la clase `dateutils.Date`, `catalanDate` y compañía son **atributos calculados**, o **properties**,
> son métodos que llevan delante de su definición `@property`,
> se accede a ellos como si fueran atributos,
> pero estás llamando a un método.
> `format` no nos deja llamar métodos, pero si son properties, no hay problema porque no usamos el operador llamada (paréntesis).
> Son conceptos parecidos, pero no confundas estas _properties_ con las de Qt.

Con estos atributos podemos hacer código como:

```python
>>> from namespace import namespace as ns
>>> datos = ns()
>>> datos.today = dateutils.Date.today()
>>> "Hoy es {today.slashDate}".format(**datos)
'Hoy es 02/06/2015'
```

Los refactorings no se acabaron ahí.
¿Cómo siguió evolucionando el código?

- Primero `dateutils.Date`, delegaba en las funciones que habíamos hecho en `dateutils`
	- Si lo que recibía el constructor no era un `datetime.date` se llamaba a la función `dateutils.date` para obtenerlo.
	- Los atributos de formateo llamaban a las funciones `dateutils.slashDate` y compañía.
- En un refactoring posterior, se invirtió la delegación:
	- Primero se duplicaba el codigo de la función dentro de la clase
	- Después hacíamos que la función llamara a la clase, eliminando la duplicación

Y ese es el código que tenemos ahora.
Todas las funciones libres (`date`, `catalanDate`...)
crean un objeto `Date` y usan sus métodos y propiedades para obtener el resultado.

Echale un ojo al código.


## La misión, refactorizar fechas de facturas

Hemos visto todos los refactorings que hemos ido haciendo
para simplificar el código de manejo de fechas.

Aún hay sitios en el código de GuifiBaix donde las fechas son textos.
En el YAML de las facturas dos campos, `dataEmisio` y `dataVenciment`,
están formateados en formato `slashDate` y no en iso.
Eso implica que cuando lo cargamos, python no lo maneja como una fecha sino como un texto.
En su día ya nos iba bien porque solo la usabamos traspasar el texto al PDF de la factura,
con ese mismo formato.

Pero ahora usamos ese dato en más sitios,
así que tenemos que usar la función `date`
para generar una fecha manipulable como tal.

Además, posiblemente en un futuro tengamos que integrarlo en una base de datos
y para ello también combiene tener fechas reales y no textos.

El objetivo de este refactoring es:

- Substituir esos campos por otros en formato ISO y con nombres en inglés: `dueDate`, `issueDate`
- Simplificar el código que maneja estos datos explotando las utilidades de `dateutils`


### La esencia de los refactorings

Dijimos que los refactorings son recetas para cada tipo de accion.
Estas recetas estan escritas en un libro precioso de Martin Fowler.
Pero no es necesario que nos aprendamos los pasos de las recetas si nos quedamos con la fórmula general.

Normalmente tenemos un código existente,
una función, un método, una variable, un campo, un cacho de código...
que queremos substituir por otro.
¿Como procedemos?
Pues como procederíamos en una reforma,
construyendo andamiaje para que nada se caiga
hasta que tengamos lo nuevo funcionando.

- **Duplicar:** Crear la nueva estructura sin tumbar la que había
- **Rellenar:** Rellenar la nueva estructura para que en cada momento contenga lo mismo que la antigua
- **Usar:** Que el código que se basaba en la estructura vieja se base en la nueva.
- **Limpiar:** Eliminar los usos de la estructura antigua.

Si lo hacemos en este orden, podemos mantener el programa (¡y los tests!) funcionando en todo momento.

En nuestro caso, tendremos que:

- Añadir los campos nuevos donde se añaden los viejos
- Modificar el valor de los campos nuevos donde se modifican los viejos
- Hacer que el resto de código pase a depender de los atributos nuevos en vez de en los viejos
- Limpiar lo que quede de los campos viejos y el código relacionado

### Situémonos

Lo esencial pues es averiguar donde se usan esos campos.
Y donde se usan, identificar si se usan para darles valor (_set_) o para tomar su valor (_get_).
También si el hecho de tener un `dateutils.Date` da pie a simplificar el código.

Usa el comando `grep` para buscar donde se usan los campos `dataEmisio` y `dataVenciment`.

```bash
$ grep -rIn 'data\(Emisio\|Venciment\)'
```

Veremos que se usan en los siguientes ficheros de código:

- `gb_registrafactura.py`
	- Aqui usamos `dataVenciment` para generar un vencimiento en `cobraments.yaml`
	- Es un uso de tipo _get_
	- De hecho decodificamos a mano el slashDate, ni usamos las funciones de `dateutils`.
      Nos estamos repitiendo, seguramente no lo estamos haciendo tan correcto como en `dateutils` y eso se podría simplificar.
- `gb_remesasepa.py`
	- Aquí tomamos (_get_) `dataVenciment` i `dataEmisio` para usarlas en los ficheros de remesa
	- Hacemos conversión explicita a `dateutils.Date` que no haría falta
	- Hacemos `dateutils.slashDate(invoice.dataEmisio)`, bastaría con `invoice.issueDate.slashDate`
- `gb_facturamanteniment.py`
	- Usos de tipo _set_ en dos sitios:
		- Funcion `generateInvoice` donde tomamos algo que representa una fecha y lo convertimos en `slashDate`.
		  No haria falta convertirlo a `slashDate` pero si a `dateutils.Date`.
		- En los datos de test, donde lo asignamos a un texto literal con el _slashDate_.
- `gb_factura.py`
	- Un uso de tipo _set_ en `dummyInvoice`
	- Un uso de tipo _get_ cuando se rellena el valor de la fecha en la casilla de la factura correspondiente con el `slashDate`
	- Un uso de tipo _set_ cuando indicamos las fechas con la línea de comandos o sinó tomamos los que tengan sentido (emisión hoy, vencimiento en 15 días)
	- Un uso de tipo _get_ de `dataEmisio` cuando la usamos para deducir `dataVenciment` y el año del ejercicio (`year`)

Podríamos cambiarlo al tajo,
pero es improbable que salga bien a la primera,
si fallara algo nos costaría detectar que es,
y seguro que, una vez que pensemos que esta todo,
no tendremos paciencia para comprobar
que cada cosa que hemos cambiado funcione bien
y algo se nos quedaría sin funcionar.

Vamos a aprender como hacerlo bien,
para que no perder el control.

### Asegurando el suelo por el que pisamos

Para asegurarnos de que no la cagamos,
nos aseguraremos de que todo comportamiento
tenga un test unitario que falle si cambia.
y si no, como mínimo, crearemos un back-to-back.

Para ejecutar los tests unitarios tenemos el script `test_all.sh`.

Una forma rápida de tener un b2b funcionando
es usar un git temporal para poner las salidas de los comandos
y detectar cuando cambian.

Para crear un repositorio nuevo temporal
para los datos de referencia del b2b:

```bash
$ git init b2bdata
```

Las salidas de b2b las colocaremos en ese directorio.
La primera vez que ejecutemos los scripts,
añadiremos esas salidas al control del git y comitearemos.
Si las sucesivas ejecuciones varian, git lo detectará como cambio.

El script que ejecute los b2b:

- borrará todos los archivos de `b2bdata` para asegurarnos de que son los comandos que los generan
- ejecutará los comandos de b2b
- `git status` para detectar las diferencias y `git diff` para mostrarlas.
- Lo llamaremos temporalmente desde el `test_all.sh` que también ejecuta los unitarios

Veamos que necesidades de testing tenemos:

- `gb_factura.py`:
	No tiene tests unitarios, y la salida, un PDF es binária.
	No habrá más opción cuando modifiquemos este que comprobar visualmente el PDF.
	Si podemos hacer un b2b a la opción `--dump`:

	```bash
	$ gb_factura --dump b2bdata/factura-default.yaml
	$ gb_factura --dump b2bdata/factura-issue.yaml --issue 2010-09-08
	$ gb_factura --dump b2bdata/factura-due.yaml --due 2017-09-08
	```

- `gb_facturamanteniment.py`
	Este script está suficientemente cubierto por los tests unitarios.

- `gb_remesasepa.py`
	Esta cubierto por tests pero justamente el uso que hacemos de los atributos
	queda fuera, pues se usa en la función principal asi que también
	añadiremos un b2b:

	```bash
	$ gb_remesasepa.py --paid --reference 1234567890123 \
		--now 00:00:00 --today 2014-01-01
	```

	Genera dos ficheros con todos los vencimientos sobre el cual hacer b2b

	- `PRE-20140101-010203-00000-1234567890123.csv` y
	- `PRE-20140101-010203-00000-1234567890123.c19`.

	El script de b2b tendrá que moverlos al directorio `b2bdata`.
	De hecho hay que ejecutarlo desde `tresoreria`, 
	el script de b2b entrará y volverá a ese directorio.

- `gb_registrafactura.py`

	Podemos hacer el b2b con la salida de:

	```bash
	$ gb_registrafactura.py --all
	```

	También hay que ejecutarlo desde `tresoreria`.

El script de back2back quedaria como sigue:


```bash
#!/bin/bash

# Esto hay que cambiarlo para que apunte donde toca
TRESORERIA=path/to/tresoreria
# Obtenemos el path del propio script
BASEPATH=$(dirname $(realpath -s $0))
B2BDATA=$BASEPATH/b2bdata

# Crea el repositorio de b2bdata si no existe
[ -d "$B2BDATA" ] || git init "$B2BDATA"

# Borra las referencias, si no se generan no estarán
rm "$B2BDATA"/*

# Ejecutamos los comandos que queremos controlar
(
	gb_factura.py --dump $B2BDATA/factura-default.yaml
	gb_factura.py --dump $B2BDATA/factura-issue.yaml --issue 2010-09-08
	gb_factura.py --dump $B2BDATA/factura-due.yaml --due 2017-09-08
)
(
	cd $TRESORERIA
	gb_remesasepa.py --paid --reference 1234567890123 \
		--now 01:02:03 --today 2014-01-01

	mv PRE-20140101-010203-00000-1234567890123.csv $B2BDATA/
	mv PRE-20140101-010203-00000-1234567890123.c19 $B2BDATA/

	gb_registrafactura.py --all > $B2BDATA/cobraments.yaml
)

# Miramos que referencias han cambiado con el git
(
	cd $B2BDATA/
	git status --porcelain
	[ "$(git status --porcelain)" == "" ] &&
		echo -e '\033[32;1mTest passed!!\033[0m' ||
		echo -e '\033[31;1mTest failed!!\033[0m'
)

```

La primera vez que se ejecute, hay que entrar establecer la referencia:

```bash
cd b2bdata
git add *
git commit . -m 'first'
```


Ojo que la salida de estos comandos que usamos de b2b
cambia a la que cambien los datos (entren facturas, cobros...),
ya dijimos que los b2b son bastane débiles,
pero nos servirá mientras hacemos el refactoring.


### Creando los scripts de migración de datos

Una migración en informática es saltar de un sistema a otro.
Por ejemplo, se migra de Windows a Linux o de una versión de Ubuntu a otra.

Cuando hablamos de **migración de datos**,
lo que hacemos es actualizar los datos,
por ejemplo nuestros YAML,
para que funcionen con una versión del código diferente.

En nuestro caso lo que hay que hacer es
substituir los atributos viejos, con nombres en catalán y de tipo texto,
por los nuevos atributos, con nombres en inglés y de tipo `dateutils.Date`.
Pero como hemos dicho, en los refactorings, antes de quitar lo viejo
hay que tener lo nuevo funcionando, y, durante el transito,
hay que mantener las dos estructuras.
Asi que la migración la haremos en dos pasos:

1. Añadir los atributos nuevos basandonos en (y manteniendo) los viejos
1. Eliminar los atributos viejos para cuando se acabe el refactor.

El primer script lo podemos llamar `migration_01_addIssueDateAndDueDate.py`.
Leera ficheros YAML de las facturas y le añadirá dos atributos en inglés, `issueDate` y `dueDate`,
basándose en `dataEmisio` y `dataVenciment`.

- Crea el script, dale permisos y demás
- Lo mas práctico es pasarle el nombre del YAML por línea de comandos
	- Recuerda para acceder al primer parámetro de la línea de comandos: `sys.argv[1]` y necesita un `import sys`.
- Empezaremos las pruebas con una factura que esté controlada con el git
	- Si la fastidiamos: `git checkout factura.yaml`
- Usa el método (de clase!) `namespace.namespace.load` para cargar el fichero yaml como `namespace` en una variable, por ejemplo `factura`.
	- Si necesitas algun ejemplo haz un grep de `load`
- Para asegurarnos de que alcanzamos los datos imprime `factura.dataEmisio` y `factura.dataVenciment`

	```python
	invoice = ns.load(sys.argv[1])
	print(invoice.dataEmisio)
	print(invoice.dataVenciment)
	```

- Convierte la carga en un `for` para `file` en `argv[1:]`, de esta manera podemos aplicar el script a todas las facturas usando comodines.


	```bash
	$ ./migration_01_addIssueDateAndDueDate.py factura*.yaml
	```

	```python
	for yaml in sys.argv[1:]:
		invoice = ns.load(yaml)
		print(invoice.dataEmisio)
		print(invoice.dataVenciment)
	```

- Puedes usar la función `step` de `consolemsg.py` para ver por donde va

	```python
	from consolemsg import step
	...
	for yaml in sys.argv[1:]:
		step(yaml)
		...
	```

- En vez de imprimir los campos tal cual, prueba de convertirlo en `dateutils.Date`

	```python
		...
		print(dateutils.Date(invoice.dataEmisio))
		print(dateutils.Date(invoice.dataVenciment))
		...
	```
	- Si alguno falla, hemos detectado un error que podemos corregir a tiempo.

- Y finalmente podemos crear los atributos nuevos y sobreescribir el fichero

	```python
	...
	for file in sys.argv[1:]:
		step(file)
		invoice = ns.load(file)
		invoice.issueDate = dateutils.Date(invoice.dataEmisio)
		invoice.dueDate = dateutils.Date(invoice.dataVenciment)
		invoice.dump(file)
	```

- Si haces un `git diff` de las facturas podrás ver los cambios y si todos son buenos o no
- Seguro que hay alguna informacion que se ha perdido (comentarios, formatos...) edítalos a mano si hiciera falta.

No hemos borrado el atributo antiguo.
No lo queremos eliminar hasta que el código ya no lo use para nada.
Pero podemos preparar el script de migración que lo borra, para después.

Lo podemos llamar `migration_02_deleteDataEmisioVencimient.py`
y tendría una pinta como:

```python
import sys
from namespace import namespace as ns
from consolemsg import step

if __name__ == '__main__'
	step("Eliminant atributs 'dataEmisio' i 'dataVenciment'"))
	for file in sys.argv[1:]:
		step(file)
		invoice = ns.load(file)
		del invoice.dataEmisio
		del invoice.dataVenciment
		invoice.dump(file)
```

### Duplicando donde se da valor a los atributos ('setters')

En este caso vamos a hacer los pasos de 'Duplicar' y 'Rellenar' juntos.
De los sitios donde el `grep` decía que usabamos los atributos,
hay que identificar aquellos en los que se les da un valor (`set`, dar valor)
que son distintos en los que se toma el valor para hacer algo (`get`, coger).

Ejemplos de _set_:

```python
invoice.dataEmisio = '01/02/2015'
```

o

```python
invoice.dataEmisio = issueDate
```

Tenemos que mantener esas linias y añadir unas al lado. Para la primera sería:

```python
invoice.dataEmisio = '01/02/2015'
invoice.issueDate = dateutils.date('01/02/2015')
```

Si bien, a las apariciones de los atributos en ficheros YAML
ya les pasaremos nuestro script de migración de datos,
hay YAML que está escrito en el código como literales de texto,
por ejemplo para los tests.

```python
testData = """\
...
dataEmisio: 01/02/2015
...
"""
```

Como aquí no entra el script de migración, lo duplicaremos nosotros así:

```yaml
dataEmisio: 01/02/2015
issueDate: 2015-02-01
```

Atención:

**Pasamos los tests a cada modificación que hacemos.**
En teoría estas modificaciones no deberían tener consecuencias.
Pero si las tiene, algo hemos hecho mal y está bien darse cuenta
cuanto antes mejor.

**Comiteamos cada vez que pasamos los tests.**
Los tests nos dicen si vamos bien.
Pero cuando fallan, cada commit es un punto seguro al que volver.
Si tienes un punto de retorno cerca, mejor.

Nos podemos saltar, bajo nuestra responsabilidad,
lo de pasar tanto los tests o commitear tan amenudo,
pero contra más grandes hagamos los pasos,
más grande puede ser el cachiporrazo.


### Substituyendo donde se usan los valores ('getters')

Una vez que tenemos los atributos nuevos rellenados
y teoricamente, con un valor equivalente a los viejos,
toca substituir los _getters_,
es decir, donde no se da valor al atributo sino
que se usa dicho valor para hacer algo.
Por ejemplo usarlo en una plantilla,
imprimirlo por pantalla,
generar un nombre de fichero en base a él,
tranferirlo a otra estructura,
o hacer algún cálculo.

Esos usos, tenemos que irlos substituyendo y usar el nuevo atributo.
No duplicamos como con los _setters_.

Dado que el nuevo atributo tiene funcionalidad nueva,
es posible que podamos simplificar código de conversión de formatos.
Por ejemplo:

- Si se convertia a `datetime.date`, o a `dateutils.Date` o se llamaba a `dateutils.date`,
ahora ya no serà necesario.
- Si se usaba para imprimirlo tal cual, ahora hay que usar el atributo `slashDate`.

Es importante de hacerlo en dos pasos,
primero burda substitución, pasar los tests,
después el refactoring y volver a pasar los tests.

### Limpiando el atributo

En este punto, deberían de quedar sólo los usos _set_ de los atributos.
Los que le daban o actualizaban valor y que hemos duplicado al principio.

Puesto que dicho valor no se usa ya para nada,
pues estamos utilizando los atributos nuevos,
podemos ir eliminando.
Siempre un uso cada vez y siempre pasando los tests.

Finalmente podemos pasar el segundo script de migración,
el que elimina el atributo de los datos.

Y ya tenemos el refactoring hecho.
Échale un ojo lo que has modificado por si se te ocurriera
algún refactoring pendiente que simplificara el código.

Haz un diff con la revisión original y contempla tu obra.


### Reflexionando sobre lo hecho

Muchas veces nos parece tan obvio el cambio que vamos directamente a modificarlo todo a la vez.
Puede salir bien, pero, casi siempre que he hecho esto, he acabado metiéndome en camisa de once varas.

Fíjate que en ningún momento los programas han dejado de funcionar.

Esto es muy importante, porque a veces nos metemos en modificaciones
que duran más de lo previsto, y si, por el hecho de estar en medio
de un refactoring, el sistema no está listo, todo se para.

O, al revés, por miedo de que se pare,
no hacemos un refactoring que facilitaría la inclusión de nuevas funcionalidades.
Esta forma de trabajar nos permite coger al toro por los cuernos,
ser más valientes a la hora de modificar el código,
porque tenemos una red de tests que parará nuestra caída.





