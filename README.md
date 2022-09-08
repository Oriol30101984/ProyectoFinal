# ProyectoFinal
#### Tabla de contenido

- [1. Descripción y funcionamiento](#0-descripción-y-funcionamiento)
- [2. Tecnologías usadas](#2-tecnologías-usadas)
- [3. Como usar la aplicación](#3-como-usar-la-aplicación)
- [4. Licencia](#4-licencia)
- [5. Créditos](#5-créditos)

## 1. Descripción y funcionamiento

Api creada como proyecto final del curso de Python. Esta api se ha creado para una empresa tecnológica que ha estado trabajando en remoto desde marzo de 2020. Esto ha implicado que los trabajadores hayan perdido el contacto humano que tenían y la empresa quiere dar un impulso a la manera que tienen los trabajadores de relacionarse, permitiendo que contacten entre ellos creando grupos de interés.

Esta api ha de permitir a los empleados que puedan contactar con otros compañeros para formar grupos para jugar a un videojuego, con el objetivo de poder compartir un rato de ocio _afterwork_.

El funcionamiento de la aplicación és:

1. Los usuarios se tienen que poder registrar a la aplicación, estableciendo un usuario/contraseña.
2. Los usuarios tienen que autenticarse a la aplicación haciendo login.
3. Los usuarios tienen que poder crear Parties (grupos) por un determinado videojuego.
4. Los usuarios tienen que poder buscar Parties seleccionando un videojuego.
5. Los usuarios pueden entrar y salir de una Party.
6. Los usuarios tienen que poder enviar mensajes a la Party. Estos mensajes tienen que poder ser editados y borrados por su usuario creador.
7. Los mensajes que existan a una Party se tienen que visualizar como un chat común.
8. Los usuarios pueden introducir y modificar sus datos de perfil, por ejemplo, su usuario de Steam.
9. Los usuarios tienen que poder hacer logout de la aplicación web.


[⬆ Volver al índice](#tabla-de-contenido)

## 2. Tecnologías usadas
- PostgreSQL.
- Python (3.9 o superior).
- VirtualEnv propio.
- Django para la estructura de proyecto.
- Django Rest Framework encargado de la serialización de objetos JSON.
- JWT.
- Git como Sistema Control de Versiones

[⬆ Volver al índice](#tabla-de-contenido)

## 3. Como usar la aplicación

### Ejecutar la aplicación

```shell
python  mysite/manager.py runserver
```

### Desde la web

El superusuario es:

- **user**: Oriol
- **pass**: 1234

### Desde la API

Una vez iniciada la aplicación con `... runserver`

`http://localhost:8000/{entidad}`

[⬆ Volver al índice](#tabla-de-contenido)

## 4. Licencia

El proyecto utiliza la licencia MIT.

[⬆ Volver al índice](#tabla-de-contenido)

## 5. Créditos

Proyecto hecho por Oriol Luis Boiria para GeeksHubsAcademy como proyecto final de Python
# [⬆ Volver arriba ⬆](#ProyectoFinal)