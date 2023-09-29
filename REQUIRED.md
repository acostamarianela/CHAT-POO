Aplicación de chat en tiempo real desarrollada con Python utilizando el framework Flask y Socket.IO que permite a los usuarios enviar y recibir mensajes en tiempo real.

## Características

- Envío y recepción de mensajes en tiempo real.
- Registro de nombres de usuario.
- Interfaz de chat fácil de usar.

Para ejecutar la aplicación, se deben tener instalados los siguientes componentes:

- Python: [Descargar Python](https://www.python.org/downloads/)
- Flask: Instalar usando pip (`pip install Flask`)
- Flask-SocketIO: Instalar usando pip (`pip install Flask-SocketIO`)

⚠️IMPORTANTE⚠️
Si se desea utilizar la aplicación utilizando localhost, se debe copiar el link de 'http://localhost:5000' en
la linea 10 'socket = io.connect("https://m51ghldl-5000.brs.devtunnels.ms/");' del archivo chat.js que se encuentra en la carpeta static/js.
Si se desea realizar una conexión con la nube a través de los puertos (la opción de PORTS de VSC), se debe cambiar el enlace de localhost por el enlace generado, en el parámetro de io.connect. 

El proyecto se organiza de la siguiente manera:

- `app`: Contiene la lógica principal de la aplicación de chat.
- `claseMensaje`: Plantilla para crear un mensaje, con sus correspondientes atributos.
- `claseUsuario`: Plantilla para los usuarios que utilizan la aplicación, además de sus atributos y métodos propios.
- `templates/`: Almacena la plantilla HTML utilizada.
- `static/`: Contiene archivos estáticos como hojas de estilo (CSS), JavaScript, para dar estilo y funcionalidad a la aplicación.


