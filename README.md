## Creación de una API con Flask + Python para exponer un modelo de ML 

Este proyecto consiste en crear un servidor web utilizando Flask y Python para exponer un modelo de aprendizaje automático a través de un endpoint REST. 

## Requisitos 

Antes de comenzar, asegúrate de tener instalado lo siguiente: 
 - [x] Python 3.x  
 - [x] Docker (opcional para empaquetamiento)

## Instalación  

1. Clona este repositorio en tu máquina local: 
	`git clone https://github.com/FelipeGarcia911/ml-model-docker`
2. Navega al directorio del proyecto: 
	`cd ml-model-docker`

### Configuración del Entorno Python en Windows
Asegúrate de cumplir con los siguientes requisitos:
 - [x] Windows 10 o superior. 
 - [x] Python 3.x instalado.

 - #### Instala Python 3.x:
	Si aún no tienes Python instalado, puedes descargar la última versión de Python para Windows desde el [sitio web oficial de Python](https://www.python.org/downloads/windows/). Asegúrate de seleccionar la opción "Agregar Python a PATH" durante la instalación para que Python sea accesible desde la línea de comandos.
	    
	Para verificar que Python se ha instalado correctamente, abre una ventana de comandos (cmd) y ejecuta el siguiente comando: `python --version`  Debería mostrar la versión de Python instalada.
 
 - #### Crea un entorno virtual (opcional, pero recomendado):
	Los entornos virtuales son una buena práctica para mantener las dependencias de tus proyectos separadas. Abre una ventana de comandos en la ubicación de tu proyecto y ejecuta los siguientes comandos:

	`python -m venv venv`
	`venv\Scripts\activate` 
	 
	 Esto activará el entorno virtual. Puedes desactivarlo más tarde con el comando `deactivate`.
 

 - #### Instala las dependencias del proyecto:

	Asegúrate de estar en el directorio de tu proyecto y con el entorno virtual activado si lo estás utilizando. Luego, ejecuta el siguiente comando para instalar las dependencias:
	 
	 `pip install -r requirements.txt` 
	 
	 Esto instalará todas las bibliotecas y paquetes necesarios para ejecutar tu proyecto Flask. Con esto, habrás configurado correctamente tu entorno Python en Windows y estarás listo para ejecutar tu aplicación Flask en modo de desarrollo local.

### Configuración del Entorno Python en macOS
Asegúrate de seguir estos pasos para configurar el entorno Python en macOS antes de ejecutar tu proyecto Flask:

 - #### Instala Python 3.x (si no está instalado)

	MacOS generalmente incluye una versión de Python preinstalada, pero se recomienda utilizar Python 3.x para este proyecto. Puedes descargar la última versión de Python desde el sitio web oficial de Python ([https://www.python.org/downloads/](https://www.python.org/downloads/)) o utilizando un administrador de paquetes como Homebrew.

	Para instalar Python 3.x con Homebrew, abre una terminal y ejecuta los siguientes comandos:

	`/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
	brew install python@3.9  # Cambia la versión según tus preferencias`

 - #### Configura un entorno virtual (recomendado)

	Un entorno virtual te permite aislar las dependencias de tu proyecto Python del sistema global, lo que facilita la gestión de paquetes y evita conflictos entre proyectos. Puedes usar la herramienta `venv` que viene con Python.

	Para crear un entorno virtual:

	1.  Navega al directorio de tu proyecto:    
	`cd cd ml-model-docker` 

	2.  Crea un entorno virtual:
	`python3 -m venv venv` 

	3.  Activa el entorno virtual:
	`source venv/bin/activate` 
    

 - #### Instala las dependencias del proyecto
	Dentro del entorno virtual, puedes instalar las dependencias del proyecto ejecutando:
	`pip install -r requirements.txt`

## Modo desarrollo local

Para ejecutar la aplicación Flask en tu entorno de desarrollo local, sigue estos pasos:
1.  Asegúrate de que estás en el directorio del proyecto y con el entorno virtual activado (si lo estás utilizando).
2.  Ejecuta la aplicación Flask:
    `yarn dev` 
3.  La aplicación estará disponible en [http://localhost:10000](http://localhost:10000/). 
4. Puedes acceder al endpoint de prueba de ML en la ruta `/api/v1/hello`.
5. Realiza pruebas y desarrollos locales según tus necesidades.

## Empaquetamiento con Docker

Si deseas empaquetar la aplicación en un contenedor Docker, sigue estos pasos:
1.  Asegúrate de tener Docker instalado en tu máquina.
2.  Desde el directorio del proyecto, crea una imagen Docker:
	`yarn docker:build` 
3.  Ejecuta el contenedor:   
	`yarn docker:run`
4. Puedes acceder al endpoint de prueba de ML en la ruta `/api/v1/hello`.
5. Realiza pruebas y desarrollos locales según tus necesidades.
6.  El contenedor se ejecutará en segundo plano. Para detenerlo, utiliza el comando 
	`docker stop`.

## Contribución

Si deseas contribuir a este proyecto, ¡estamos abiertos a colaboraciones! Siéntete libre de enviar pull requests y reportar problemas.

## Licencia

Este proyecto está bajo la licencia [Licencia MIT](https://chat.openai.com/c/LICENSE).
