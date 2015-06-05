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
- Finalmente, plantearemos paso a paso un refactoring pendiente, para que las fechas de los yaml de las facturas sean fechas y no textos, incluyendo el refactoring en sí y la migración de los datos.


## Base teòrica

### El módulo `datetime`

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

> **Ejercicio:**
> Prueba replicar el ejemplo anterior expresando el `timedelta` en horas.


> **Ejercicio:**
> Intenta crear una fecha con parámetros incorrectos y observa el resultado.
> Así te familiarizarás con los errores cuando te los encuentres inexperadamente.
> Algunos casos de error a probar:
> 
> - uno de ellos no sea un entero, por ejemplo un texto o un `float`
> - falte o sobre uno
> - Que uno de ellos (mes o día) este fuera de rango
> - En orden inverso (no iso)

> **Ejercicio:**
> Crea una funcion para calcular la fecha de vencimiento a partir de una fecha
> de emisión de la factura, sabiendo que son 15 días.
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
Esto lo podemos hacer con los llamados **métodos de clase**
que no necesitan una instancia para poder ser llamados.
En la documentación de las clases se suele indicar cuando lo son.

Ademas este método es lo que llamamos un **método factoría**.
Es decir un método cuyo propósito es crear, _fabricar_, objetos.

> **Ejercicio:**
> Averigua tu edad en días restándole tu fecha de nacimiento a `date.today()`.
> Obtendras un objeto tipo intervalo con tu edad en dias.

Otra cosa interesante del ejemplo anterior es que,
cuando enviamos una fecha al `print`, ya no nos devuelve
el texto de una llamada al constructor `datetime.date(2016,6,2)`
sino una fecha en formato ISO 8601 (YYYY-MM-DD).
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

Una refactorización es una modificación del código que no tiene impacto en el comportamiento externo.

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
de forma que cada receta (extraer una funcion, añadir un parámetro...)
tienen recetas con un listado de cosas, de sentido común,
a comprobar para asegurarnos de que modificando el código
no se modifica el comportamiento.

Es muy importante no mezclar refactorings con cambios en el comportamiento.
Todo es mucho más sencillo si cuando refactorizas, esperas que todo funcione igual.
Si algo cambia, no has refactorizado bien.
Cuando cambias comportamiento, que sea porque añades o has modificado un test,
y que ese test refleje ese cambio de comportamiento.


- Pequeños pasos
- No han de añadir funcionalidad
- Nos apoyamos en los tests que tenemos (¿no tenemos? ya sabemos lo que toca)

¿Hemos dicho test? ¿De donde salen los tests?

- Los tests han de comprobarse muy a menudo.
- Comprobar a ojo que el resultado es el que toca es una tarea muy pesada.
- Si lo tenemos que hacer a ojo, no lo vamos a hacer o no vamos a prestar la atención necesaria.
- **Solucion:** Hagamos que el ordenador compruebe los resultados por nosotros.
	- Si funciona no nos marea
	- Si algo no funciona entonces grita y nos enseña la salida no esperada comparada con la esperada.


> **Ejercicio:**
> Construye un script en bash (usando entre otros el comando `diff`)
> que compare la salida estandard del script anterior
> contra una salida esperada.
> Si es igual no muestra nada, si muestra algo

> Una forma de testear de forma automática es el test de espalda contra espalda (back-to-back o b2b).
> Es práctica si ya tenemos algo que funciona pero no tenemos tests unitarios.


## Un caso real

### Centralizando el formateo de fechas

Desarrollando nuestro programa de gestión, pasó que las llamadas a `strftime`
empezaron a pulular por todo el código.
A veces nos equivocabamos al escribir el formato,
a veces simplemente emborronaban el código.

> **Máxima: Don't Repeat Yourself, DRY, No te repitas.**
> Si estás escribiendo el mismo código una y otra vez, busca la forma de no repetirlo.
> El código repetido,
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
> datetime.date.strptime('%Y-%m-%d')
datetime.date(2015,6,2)
```

Claro que esto funciona porque sabemos que formato nos va a llegar,
y esto era así la mayoria de las veces, pero a veces no y ese día el programa fallaba.
Así que, si queremos que nuestro programa se sepa adaptar a la mayoría de casos,
debemos detectar el formato y generar la fecha.

Así que para eso creamos la funcion `dateutils.date`, que transparentemente convertía,
si es posible, lo que sea a un objeto `datetime.date`.

Por ejemplo:

```python
>>> dateutils.date(2015, 6, 2)
datetime.date(2015,6,2)
>>> dateutils.date((2015, 6, 2))
datetime.date(2015,6,2)
>>> dateutils(datetime.date(2015,6,2))
datetime.date(2015,6,2)
>>> dateutils.date("2015-06-02")
datetime.date(2015,6,2)
>>> dateutils.date("02-06-2015")
datetime.date(2015,6,2)
>>> dateutils.date("02/06/2015")
datetime.date(2015,6,2)
>>> dateutils.date("02062015")
datetime.date(2015,6,2)
>>> dateutils.date("20150602")
datetime.date(2015,6,2)
```

Implementada en un solo sitio y cubierta por tests, nos da la
seguridad de que si falla es porque no es una fecha.

> **Ejercicio:**
> Usa la función `dateutils.date` e intenta putearla.
> Si encuentras un caso que no funcione, implementa el test y hazlo pasar.

Haciendo que todas las funciones de formateo lo primero que hagan
es llamar a date sobre lo que sea que le pasemos por parámetro,
las funciones de formato se vuelven muy versátiles:

```python
>>> def slashDate(arg):
... 	adate = date(arg)
...	return adate.strftime('%d/%m/%Y')
>>> slashDate('20150602')
'02/06/2015'
```


### Formateando fechas en los templates

En las librerías propias de GuifiBaix tenemos utilidades para coger un yaml
y rellenar una plantilla con `format`.

Cuando leemos un `namespace` de un YAML,
la librería `python-yaml` detecta los campos que son fechas ISO
y las devuelve como `datetime.date`.
El problema es que si rellenamos una plantilla con ese campo,
siempre lo va a representar como fecha ISO y no suele ser lo que necesitamos.

```python
>>> import namespace
>>> date = namespace.namespace(today = datetime.today())
>>> "Hoy es {today}".format(date)
'Hoy es 2015-06-02'
```

Pero el método `format` nos permite acceder a partes del dato:
atributos (con la sintaxis de punto) y indices (con la sintaxis de `[]`).

Lo que se hizo fue crear una clase, `dateutils.Date`,
que extiende la clase `dateutils.date` y además:

- su constructor acepta todo lo que acepta la funcion `dateutils.date`.
- tiene atributos (calculados) `compact`, `slashDate`, `catalanDate`...

> **Detalle avanzado:**
> En la clase `dateutils.Date`, `catalanDate` y compañía son **atributos calculados**, o **properties**,
> son métodos que llevan delante de su definición `@property`,
> se accede a ellos como si fueran atributos,
> pero estás llamando a un método.
> `format` no nos deja llamar métodos, pero si son properties, no hay problema porque no usamos el operador llamada (paréntesis).


```python
>>> import namespace
>>> date = namespace.namespace(today = dateutils.Date(datetime.today()))
>>> "Hoy es {today.slashDate}".format(date)
'Hoy es 02/06/2015'
```

El módulo `namespace` ya tunea la librería de YAML para que cuando
encuentra una iso, devuelva un `dateutils.Date` en vez de un `datetime.date`.

Para no duplicar código, al principio `Date` delegaba en las funciones que
habíamos ido haciendo, pero en un refactoring posterior, invertimos la dependencia,
y ahora son las funciones las que crean un objeto `Date` y delegan en él,


## La misión, refactorizar fechas de facturas

Hay sitios donde las fechas aún son textos.
En el YAML de las facturas dos campos, `dataEmisió` y `dataVenciment`, están formateados como `slashDate` y no en iso.
Eso implica que cuando lo cargamos, python no lo maneja como una fecha sino como un texto.
En su día ya nos iba bien porque solo la usabamos para generar la factura,
y la factura usaba ese formato, por lo que simplemente poniamos la cadena y ya está.

Pero ahora usamos ese dato en más sitios, asi que tenemos que usar la función `date`
para generar.

Además, posiblemente en un futuro tengamos que integrarlo en una base de datos
y para ello combiene que las fechas sean fechas y no textos.

- Sitúate:
	- Usa el comando `grep` para buscar donde se usan los campos `dataEmisió` y `dataVenciment`.
	- Localizados los ficheros abrelos para ver que uso se hace del campo:
		- Se usa para una salida, formateados o tal cual
		- Lo usamos para obtener otro dato
		- Le damos un valor
		- ...
	- Piensa para cada uso como sería si usamos `dateutils.Date`
	- Aquí analizaríamos si es conveniente o no usarlo


- Crea un script para migrar los datos, que lea el YAML, y añada un atributo en inglés `issueDate` y `dueDate`






