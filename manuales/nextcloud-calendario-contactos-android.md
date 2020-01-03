# Guardar los contactos y la agenda de Android en NextCloud

## Propósito

Las apps por defecto de Android para los contactos y el calendario
sincronizan los datos con tu cuenta de Google Accounts.
Eso permite que todos tus dispositivos compartan contactos y eventos
aun si pierdes el móvil.

Si prefieres que Google no tenga esa información,
puedes usar el NextCloud de GuifiBaix (o el tuyo propio si te lo montas)
para tener los datos sincronizados ahí en vez de en Google.

## Requisitos

Primero asegurate que puedes entrar en el [NextCloud de guifibaix](https://nextcloud.guifibaix.net).
Deberías poder entrar con el mismo usuario y contraseña que usas en la mediateca.

Después deberías instalarte dos aplicaciones.
Están disponibles en el Google Play pero como estás desconectando de Google
igual te interesa mas bajarlas con la applicacion [F-Droid](https://f-droid.org/).
Las aplicaciones de F-Droid, como las dos que hay que instalar son todas open source.

Las aplicaciones son:

[DAVx5](https://www.davx5.com/):
Que sirve para sincronizar recuros de contactos y calendarios via WebDav.

[NextCloud Client](https://f-droid.org/es/packages/com.nextcloud.client/)
Es el cliente oficial de NextCloud.
Añadira un nuevo tipo de cuenta de usuario.
También te permite usar las otras funcionalidades de NextCloud como archivos en la nube.


## Configuración

Configurar el cliente Nextcloud para definir la cuenta.

- Abre la aplicacion NextCloud
- Clica en Abrir session
- Como dirección pon http://nextcloud.guifibaix.net
- Proceder a dar acceso a la aplicacion
- Escoger un método de validación (da igual cual)
- Poner usuario y contraseña
- Dar al botón para dar permiso a la app del mobil para acceder a la web.
- Decir si quieres que la app NextCloud acceda los ficheros del dispositivo para compartirlos cuando digas (puedes poner que no)

La aplicación a parte de configurar la cuenta te da acceso a los ficheros que tienes almacenados en el Servidor.

- Ves a la configuracion de NextCloud
- Seleccionar "Sincronizar contactos y calendario con DAVx5
- Proceder otra vez con el login igual que antes.
- Cuando acabas sale la pantalla de crear cuenta
- le das al boton para hacerlo


Configurar el DAVx5 para que sincronice los contactos

- Abrir la aplicacion DAVx5
- Si hemos procedido a lo anterior deberia salir un boton grande con tu usuario de guifibaix
- Lo pulsamos.
- Pedira permisos para que davx5 pueda acceder a los recursos del dispositivo que tiene que actualizar (calendario, contactos, tareas...)
- En la pestala CARDCAV (contactos) marcar el recurso remoto y dar al boto para actualizar.
- En la pestala CALCCAV (calendario) marcar el recurso remoto que quieres ver en local y dar al boto para actualizar.


## Copiando los contactos

Al principio, normalmente, tendremos en los contactos tres cuentas:
La del dispositivo, la de google y la de DAVx5.
Las podemos ver en el menu de los contactos, seleccionando 'Cuentas'.
Todos los contactos estaran en la de google seguramente.

Para realmente tener los contactos sincronizados en el NextCloud hay que moverlos.

- Desde 'Contactos', vamos al menu, y seleccionamos 'Importar/Exportar'
- Seleccionar la cuenta en la que estan los contactos (gmail?)
- Seleccionamos la cuenta donde los queremos copiar (nextcloud)

Algunas versiones de Android no tienen para pasar entre cuentas directamente.
Habria que exportar a un fichero ICS y despues importarlo a la cuenta de DAVx5.

En cualquier caso, esto duplicara todos los contactos.
Bien borramos la cuenta original o hacemos un merge/mezclado de los contactos (no en todos los androids esta la opcion).

## Traspaso de contactos

Desde la aplicacion de contactos:

- clickar el menu de la derecha.
- Opción "Importar/Exportar".
- "Exporta un archivo .vcx".
- Te sale la lista de contactos a marcar.
- Clickas en "0 Selected" y aparecerá un pop-up, clica en "Selecciona todos".
- Clickas al boton "Ok"
- Indicar el fichero de salida. Yo suelo incluir la fecha (2020-02-29) en el nombre.

Este fichero contiene todos los contactos actuales.
Los contactos ahora siguen en la cuenta que tuvieras: Telefono, google accounts...
Hay que traspasarlos a la cuenta DAVx5/NextCloud.

- Opción "Importar/Exportar".
- "Importa un archivo .vcx".
- Especifica el fichero que has guardado antes
- Indica la cuenta de DAVx5










