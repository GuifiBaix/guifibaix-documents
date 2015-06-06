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
- El constructor de `timedelta`, puedes escoger como expresas el intervalo
  usando los nombres de los parámetros opcionales: `days`, `hours`, `minutes`, `seconds` y `microseconds`
  Siendo `hours` el primer parámetro,
  podríamos haber usado `datetime.timedelta(2)` pero este es un ejemplo
  de como especificar el nombre del parámetro ayuda a entender que hacemos.

> **Ejercicio:**
> Prueba replicar el ejemplo anterior expresando el `timedelta` en horas.


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
se puede hacer sólo si el método es de los llamados **métodos de clase**,
En la documentación de las clases se suele indicar cuando lo son.
En oposición los otros métodos se llaman **métodos de instancia**.

Ademas este método es lo que llamamos un **método factoría**.
Es decir un método cuyo propósito es crear, _fabricar_, objetos.

> **Ejercicio:**
> Averigua tu edad en días restándole tu fecha de nacimiento a `date.today()`.
> Obtendras un objeto tipo intervalo con tu edad en dias.
> Divídelo por `365.25` y tendrás tus años astronómicos.

Otra cosa interesante del ejemplo anterior es que,
cuando enviamos una fecha al `print`, ya no nos devuelve
el texto de una llamada al constructor `datetime.date(2015,6,2)`
sino una fecha en formato ISO 8601 (YYYY-MM-DD) como `2015-06-02`.
Esta es una representación en texto de la fecha muy práctica
pues el orden cronológico (por fecha) coincide
con el orden lexicográfico (alfabético) de la representación.

La representación por defecto de las fechas es en formato ISO.
Si queremos obtener otro formato, por ejemplo el típico `DD/MM/YYYY`
tenemos que usar el método `strftime`.

```python
>>> fecha.strftime('%d/%m/%Y')
'02/06/2015`
```

Los códigos con `%` estan documentados en la [referéncia de la librerias estándard](TODO).

> **Ejercicio:**
> En algunos procedimientos administrativos, por ejemplo los ficheros SEPA,
> se tienen que generar fechas usando el que llamamos formato compacto
> que es igual que el ISO pero sin guiones, pe `20150602`.
>
> - Genera con el `strftime` ese formato.
> - Genera tambien el formato iso con el strftime

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

- Modo refactoring: Ponemos toda nuestra atención en que las modificaciónes que hagamos no alteren el producto
- Modo funcionalidad: Nos centramos en alterar ese producto, cambiando lo mínimo posible el código

Es muy importante no mezclar refactorings con cambios en el comportamiento.
Todo es mucho más sencillo si cuando refactorizas, esperas que todo funcione igual.
Si algo cambia, no has refactorizado bien.
Cuando cambias comportamiento, que sea porque añades o has modificado un test,
y que ese test refleje ese cambio de comportamiento.

En resumen, cuando refactorizamos:

- Pequeños pasos
- No han de añadir funcionalidad
- Nos apoyamos en los tests que tenemos (¿no tenemos? ya sabemos lo que toca)

### Refactorizando con tranquilidad: los tests

Para refactorizar con la conciencia tranquila
es importante tener una batería de tests que te avisen
cuando te sales del camino.

- Los tests han de comprobarse muy a menudo.
- Comprobar a ojo que el resultado es el que toca es una tarea muy pesada.
- Si lo tenemos que hacer a ojo, no lo vamos a hacer o no vamos a prestar la atención necesaria.
- **Solucion:** Hagamos que el ordenador compruebe los resultados por nosotros.
	- Si funciona, que no nos maree enseñándonos la salida, que simplemente nos diga que 'todo bien'.
	- Si algo no funciona, que entonces grite y nos enseñe la salida errónea comparada con la esperada.

> **Ejercicio:**
> Construye un script en bash (usando entre otros el comando `diff`)
> que compare la salida estandard del script anterior
> contra una salida esperada.
> Si es igual no muestra nada; si cambia, enciende alarmas y muestra la diferencia

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
Un tests b2b, ve el programa como una caja negra,
dada una misma entrada compara una salida antigua con la actual con el código modificado.
No nos planteamos, si la salida es buena o mala, simplemente queremos que no cambie.

A diferencia de los unitarios que añadimos para cada variación de la funcionalidad,
los b2b no consideran todos los casos, así que son débiles:
Es posible que cambie la funcionalidad y no lo detectemos.
El tests que has hecho antes, es el típico b2b.

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
>>> def slashDate(arg):
... 	adate = date(arg)
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
Usa el comando `grep` para buscar donde se usan los campos `dataEmisio` y `dataVenciment`.

```bash
$ grep -rI 'data\(Emisio\|Venciment\)'
```

Veremos que se usan en ficheros de código y en ficheros de datos.

- `data/example-maintainment-invoice.yaml`
- `gb_registrafactura.py`
- `gb_remesasepa.py`
- `gb_facturamanteniment.py`
- `gb_factura.py`


Normalmente los usos son:

- Se le da un valor al campo
- Se usa el valor para:
	- formatear una salia
	- obtener otro dato

Piensa para cada uso como sería si usamos `dateutils.Date`.


## Asegurando el suelo por el que pisamos

Para asegurarnos de que no la cagamos,
nos aseguraremos de que todo cambio tiene un test unitario que lo hace fallar,
y si no, como mínimo crearemos un back-to-back.

Una parte importante de los scripts es el `gb_balance.py`
y no tiene tests unitarios para el conjunto.

Genera un script shell que haga un b2b sobre su resultado.
Añadelo a `test_all.sh` (no lo comitees).

La salida de este tests b2b cambiará cuando cambien los datos,
ya dijimos que los b2b son bastane débiles,
pero nos servirá mientras hacemos el refactoring.

Otros scripts susceptibles de plantear un b2b son:

- TODO: básate en el analisis que has hecho en el anterior punto


### Creamos un script de migración

Una migración en informática es saltar de un sistema a otro.
Por ejemplo, se migra de Windows a Linux o de una versión de Ubuntu a otra.

Cuando hablamos de **migración de datos**,
lo que hacemos es actualizar los datos,
por ejemplo nuestros YAML,
para que funcionen con una nueva versión del código diferente.

Pero como hemos dicho antes, antes de quitar lo viejo hay que crear lo nuevo.
Añadamos los dos campos nuevos a los datos existentes.

- Crea un script `migra_fechas_facturas.py` para migrar los datos, dale permisos y demás
- Este script leera ficheros YAML de las facturas y le añadirá dos atributos en inglés `issueDate` y `dueDate`
- Lo mas práctico es empezar con un fichero que le pasamos por línea de comandos
	- Recuerda `sys.argv[1]` y hay que hacer `import sys`.
- Empezaremos las pruebas con una factura que esté controlada con el git
	- Si la fastidiamos: `git checkout factura.yaml`
- Usa el método (de clase!) `namespace.namespace.load` para cargar el fichero yaml como `namespace` en una variable, por ejemplo `factura`.
	- Si necesitas algun ejemplo haz un grep de `load`
- Para asegurarnos de que alcanzamos los datos imprime `factura.dataEmisio` y `factura.dataVenciment`
- Convierte la carga en un `for` para `file` en `argv[1:]`, de esta manera podemos aplicar el script a todas las facturas usando comodines.


	```bash
	$ ./migra_dates_factura.py factura*.yaml
	```

- Puedes usar la función `step` de `consolemsg.py` para indicar el progreso.

	```python
	for file in sys.argv[1:]:
		step(file)
		invoice = ns.load(file)
		print(invoice.dataEmisio, invoice.dataVenciment)
	```

- En vez de imprimir los campos tal cual, prueba de convertirlo en `dateutils.Date`
	- Si alguno falla es que seguramente no contenga una fecha, lo resolvemos

	```python
		print(dateutils.Date(invoice.dataEmisio)
		print(dateutils.Date(invoice.dataVenciment)
	```

- Puedes usar la función `step` de `consolemsg.py` para indicar el progreso.

	```python
	for file in sys.argv[1:]:
		step(file)
		invoice = ns.load(file)
		invoice.issueDate = dateutils.Date(invoice.dataEmisio)
		invoice.dueDate = dateutils.Date(invoice.dataVenciment)
		invoice.dump(file)
	```

- Si haces un `git diff` podrás ver los cambios y si todos son buenos
- Seguro que hay algunos que se han perdido (comentarios, formatos...) edítalos a mano si hiciera falta.


No hemos borrado el atributo antiguo.
Es el último paso del refactoring,
para despues de que cambiemos todo el código,
pero podemos preparar el script de migración.

Tendrá una pinta así:

`migration_02_deleteDataEmisioVencimient.py`

```python
if __name__ == '__main__'
	step("Eliminant atributs 'dataEmisio' i 'dataVenciment'"))
	for file in sys.argv[1:]:
		step(file)
		invoice = ns.load(file)
		del invoice.dataEmisio
		del invoice.dataVenciment
		invoice.dump(file)
```

## Creando los atributos en código

Hay que localizar los puntos del código donde se crean o dan valor a los atributos antiguos.
En esos puntos, crearemos también los atributos nuevos, con el valor apropiado.

**Pasamos los tests a cada modificación que hacemos.**
En teoría esta modificación no debería de tener consecuencias.
Pero si las tiene, algo hemos hecho mal y está bien darse cuenta
cuanto antes mejor.

**Comiteamos cada vez que pasamos los tests.**
Los tests nos dicen si vamos bien.
Si fallan, cada commit es un punto seguro al que volver.

Nos podemos saltar lo anterior pero contra más grandes hagamos los pasos,
más grande puede ser el cachiporrazo.

## Substituyendo los usos

Los usos que no son para dar valor al atributo,
normalmente son para usarlo y transmitirlo a otra parte.
Por ejemplo usarlo en una plantilla,
imprimirlo por pantalla,
generar un nombre de fichero en base a el,
tranferirlo a otra estructura,
o hacer algún cálculo.

Esos usos, tenemos que irlos substituyendo y usar el nuevo atributo.
Dado que el nuevo atributo tiene funcionalidad nueva,
es posible que podamos simplificar código de conversión de formatos.

Es importante de hacerlo en dos pasos,
primero burda substitución, pasar los tests,
después el refactoring y volver a pasar los tests.

# Limpiando el atributo

En este punto, deberían de quedar sólo los usos de los atributos
que le daban o actualizaban valor.

Puesto que dicho valor no se usa ya para nada,
pues estamos utilizando los atributos nuevos,
podemos ir eliminando.
Siempre pasando los tests.

Finalmente podemos pasar el segundo script de migración,
el que elimina el atributo de los datos.







