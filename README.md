# Cyclic Redundancy Check

_El siguiente proyecto muestra el desarrollo de un algoritmo de para comprender el funcionamiento del Cyclic Redundancy Check, el cual es usado en la industria con el fin de verificar si un mensaje que ha sido enviado por un medio fisico fue enviado correctamente o si por el contrario no fue asi.
Este algortimo no determina la ubicacion del error, unicamente permite corroborar si el mensaje presenta o no errores_

## Comenzando 🚀

El  cyclic redundancy check se basa en el uso de un generador que crea una sere de bits, esta se divide en una trama un mensaje agregandole r cantidad de 0 a la trama, donde r es la longitud del generador.
El residuo entre el generador y la trama se agrega al final de la trama, y este sera el mensaje a enviar, luego el receptor divide el mensaje recibido entre un generador del mismo valor, si el residuo de esta division es 0, el mensaje se envio correctamente, de lo contrario se determina que hubo un error en el mensaje.


### Pre-requisitos 📋

_Este programa fue desarrollado con las librerias de tkinter y numpy, las cuales puede instalar correctamente dirigiendote a la carpeta principal y usar el comando:_

```
pip install -r requirements.txt
```

### Inicializacion 🔧

_Para poder ejecutar este proyecto se recomienda tener una versin reciente de python3, y usar el comando:_


```
python3 main.py
```


## Construido con 🛠️

_Menciona las herramientas que utilizaste para crear tu proyecto_

* [tkinter] - Interfaz grafica de usuario
* [Numpy] - Procesamiento de arrays 

## Contribuyendo 🖇️

Por favor lee el [CONTRIBUTING.md](https://gist.github.com/villanuevand/xxxxxx) para detalles de nuestro código de conducta, y el proceso para enviarnos pull requests.

## Wiki 📖

Puedes encontrar mucho más de cómo utilizar este proyecto en nuestra [Wiki](https://github.com/tu/proyecto/wiki)

## Versionado 📌

Usamos [SemVer](http://semver.org/) para el versionado. Para todas las versiones disponibles, mira los [tags en este repositorio](https://github.com/tu/proyecto/tags).

## Autores ✒️

_Menciona a todos aquellos que ayudaron a levantar el proyecto desde sus inicios_

* **Yefferson Nunez** - *Pruebas unitarias* - [villanuevand](https://github.com/villanuevand)
* **Santiago Arias** - *Interfaz grafica de usuario* - [fulanitodetal](#fulanito-de-tal)
* **Hector Puentes** - *Trabajo inicial*

También puedes mirar la lista de todos los [contribuyentes](https://github.com/your/CRC_lab/contributors) quíenes han participado en este proyecto. 

## Licencia 📄

Este proyecto está bajo la Licencia (Tu Licencia) - mira el archivo [LICENSE.md](LICENSE.md) para detalles

## Expresiones de Gratitud 🎁

* Comenta a otros sobre este proyecto 📢
* Invita una cerveza 🍺 o un café ☕ a alguien del equipo. 
* Da las gracias públicamente 🤓.
* Dona con cripto a esta dirección: `0xf253fc233333078436d111175e5a76a649890000`
* etc.



---
⌨️ con ❤️ por [Villanuevand](https://github.com/Villanuevand) 😊
