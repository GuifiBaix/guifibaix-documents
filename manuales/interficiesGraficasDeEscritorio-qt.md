# Programación: Interfícies gràficas de escritorio

## La libreria Qt

Qt es una [librería] de programación para hacer interficies gráficas.

- Programada en C++ pero existen adaptadores para usarla desde otros lenguajes
- Para Python hay dos adaptadores: PySide y PyQt
- Nosotros usamos PySide para el `suro` así que la formación la haremos con PySide
	- `sudo apt-get install python3-pyside`
- La ultima version de Qt es 5.x, pero usamos la 4.x porque no hay PySide para Qt5
- El codigo con PyQt es muy parecido al codigo con PySide, cambian los imports y poca cosa más
- Documentacion
	- Qt: http://docs.qt.io/
	- PySide: TODO
	- La documentacion de Qt explica mejor las clases, pero el codigo de ejemplo esta en C++

[librería]: código ya hecho, listo para usar y reusar en diversos programas

## Programa Python mínimo en Qt

Ejercicio: Crea este script y ejecutalo

	#!/usr/bin/env python3
	from PySide import QtGui
	
	app = QtGui.QApplication([])
	w = QtGui.QDialog()
	w.show()
	app.exec_()

En este programilla ya hay teca que explicar:

### Módulos y clases

- Se importa el módulo `QtGui` de dentro de la libreria `PySide`
	- Culturilla: Las Qt son extensas y los modulos sirven para que
	una applicación no tenga que arrastrarlas enteras,
	solo las pijadas que necesite:
		- Interficie gráfica
		- Multimedia
		- Animaciones
		- Graficos 3D
		- Redes
		- Sensores (GPS, acelerómetro...)
		- Navegacion web
		- ...
	- Culturilla2: GUI viene de ''Graphical User Interface''. En contraste a los GUI estan los CLI, los TUI y los WUI.
    	- Los CLI (Command line interface), pe. `git`, `grep`, estan pensado para su uso con tuberias y scripts,
	 	- Los TUI (Text User Interfaces), pe. `htop`, `tig`, `aptitude`, tambien son de consola pero estan pensados para su uso interactivo.
		- Los WUI (Web-based User Interface) pe. `github`, `bitbucket`, `gitlab`, `mediateca`, `facebook`...
		- Seguimos...
- `QApplication` y `QDialog` son [clases] definidas dentro del modulo `QtGui`
- Creamos instancias de esas clases llamándolas con los paréntesis como si fueran una función.
- Al `QApplication` le pasamos una lista vacía, nos lo creemos
	- Culturilla: normalmente se le pasa la linia de comandos (sys.argv)

### Orientacion a eventos

- Casi todo el tiempo la aplicacion pasa dentro del `exec_`
- El `exec_` es un bucle que espera eventos y, según el evento que suceda, llama a unas partes o otras de nuestro programa
- Antes de entrar en el `exec_` tenemos que haber definido como es nuestra interficie y como responder a esos eventos
	- Culturilla: Esto se llama 'Orientacion a eventos'
- En este caso hemos creado un dialogo vacio `QDialog`
- El dialogo ya sabe como responder a algunos eventos.
	- Por ejemplo si pulsamos a la tecla ESC, el dialogo se cierra.
	- Como es nuestra unica ventana, al cerrarse, se acaba la aplicacion.

## El Qt Designer

Designer: Herramienta gráfica para editar interfícies

- Instalacion: `sudo apt-get install qt4-designer`
- Construyes una interfície arrastrando elementos gráficos
- Graba un XML que describe la interficie
- Despues, hay utilidades que, a partir de ese XML, generan código C++, Python...
- pyside-uic: El generador de codigo python para PySide
	- `sudo apt-get install pyside-tools`
- Veremos como usar ese código más adelante

Ejercicio:

- Crea un dialogo en designer y arrastra elementos gráficos del panel izquierdo
- Puedes probar el dialogo con `Control+R`
- Selecciona algun elemento arrastrado y juega con las propiedades (panel derecho)

## Widgets y propiedades

Propiedades: atributos que podemos consultar y/o cambiar

- Widget: Elemento gràfico: boton, checkbox. radiobutton, campo de edicion, dialogo, listas...

TODO: Añadir imagenes (pero bueno, para eso tienes el designer)

- Color, numero de opciones, tamaño, si esta habilitado, tipo...
- Intenta volcar widgets en el designer y cambiar sus propiedades con el panel
- Via designer con el panel de propiedades
- Via programacion con funciones:
	- Si la propiedad se llama `unaPropiedad`
	- Se cambia con: `widget.setUnaPropiedad(nuevoValor)`
	- Se consulta con: `valor = widget.unaPropiedad()`

## Composicion y layouts

- Composición: Unos elementos contienen a otros formando un arbol
- Widgets contenedores: los que pueden contener a otros
	- Raiz, acaban siendo una ventana: QDialog, QMainWindow...
	- Intermedios, sirven para agrupar: QFrame, QWidget...
- Layout (Distribuidor espacial): Politica de reparto del espacio del contenedor entre los widgets hijos
	- QHBoxLayout: Apilan los widgets horizontalmente
	- QVBoxLayout: Apilan los widgets verticalmente
	- QGridLayout: Distribuye en forma de tabla en filas y columnas
	- QFormLayout: Distribuye verticalmente filas de etiqueta y editor tipico de los formularios

- Ejercicio:
	- Selecciona varios widgets y clicka a los distintos botones de layout
	- Previsualiza el dialogo con control+R y cambia el tamaño de la ventana
	- Rompe el ultimo layout (el boton con el prohibido encima de un layout)
	- Selecciona el fondo del dialogo y clicka a esos mismos botones
	- Previsualiza el dialogo con control+R y cambia el tamaño de la ventana

- Moraleja: Es distinto
	- asignar un layout a un contenedor
	- que agrupar hijos en un layout
	- lo segundo no se expande con el contenedor.
	- Asigna siempre un layout a los contenedores

- Con código (ignoro la parte de crear la QApplication al principio y llamar `exec_` al final):

		contenedor = QDialog()
		l = QHBoxLayout()
		contenedor.setLayout(l)
		contenedor.setLayout(l)
		button1 = QPushButton('Hola')
		button2 = QPushButton('Mundo')
		for b in button1, button2:
			l.addWidget(b)
		l2 = QVBoxLayout()
		l.addLayout(l2)
		button3 = QPushButton('Chao')
		button4 = QPushButton('Chochin')
		for b in button3, button4:
			l2.addWidget(b)

		contenedor.show()


## Signals y slots

- Signals: la forma que tienen los widgets de notificar cosas que les pasan al resto del programa
	- Boton: he sido pulsado!
	- Ventana: Me han cambiado de tamaño!
	- Campo texto: Me han editado!
	- Editor: Me han dejado caer un icono!
	- Mapa: Me han hecho el gesto de zoom!
	- Lista: La seleccion ha cambiado!
- Los podemos conectar a funciones o metodos (slots) que se ejecutan cuando pasan esas cosas
- Con el designer con la herramienta "Editor de signal/slot"
	- Solo se pueden conectar a slots predefinidos en los otros widgets
	- Arrastra un widget a otro y despues especificas que signal conectas con que slot
	- Ejercicio:
		- Arrastra un QCheckBox, un QPushButton y un QLineEdit a un dialogo vacio
		- Conecta el CheckBox con el LineEdit para que el LineEdit no sea editable (disable) cuando el checkbox este checkeado (checked)
		- Conecta el push button para que cuando se pulse (triggered) el LineEdit se vacie (clear)
	- Con código:


			check = QCheckBox("Deshabilita")
			lineEdit = QLineEdit("Valor inicial")
			button = QPushButton("Limpia")
			for child in check, lineEdit, button:
				l.addWidget(child)
			
			check.toggled.connect(lineEdit.setDisabled)
			button.triggered.connect(lineEdit.clear)

	- Nota: No llamamos a clear con (), le pasamos la funcion al signal para que la llame ella cuando toque
	- Si lo hacemos con codigo, no estamos limitados a los slots predefinidos
	- Podemos hacer que disparen nuestros metodos o funciones:
		- button.triggered.connect(miSlot) <- a una funcion libre
		- button.triggered.connect(miInstancia.miSlot) <- a un metodo de un objeto python

- Herencia: El comportamiento compartido de los widgets esta definido en clases base
	- Arbol de herencia, las propiedades, funciones, 
- Propiedades: atributos que podemos cambiar:
	- Visibles desde el designer




