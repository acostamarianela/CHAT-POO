# Importar las bibliotecas necesarias
from flask import Flask, redirect, url_for, render_template, request, make_response
from flask_socketio import SocketIO
from claseUsuario import Usuario # Importar la clase Usuario desde claseUsuario.py
from claseMensaje import Mensaje # Importar la clase Mensaje desde claseMensaje.py

# Crear la aplicación Flask, establecer como determinada la carpeta de los templates a renderizar en "templates"
app = Flask(__name__, template_folder='templates')

# Configurar una clave secreta para la aplicación (necesaria para las sesiones)
app.config['SECRET_KEY'] = 'tu_clave_secreta'
# Inicializar SocketIO y permitir solicitudes desde cualquier origen
socketio = SocketIO(app, cors_allowed_origins="*")


# Ruta para manejar la solicitud POST de enviar un mensaje
@app.route('/enviarMensaje', methods=['POST'])
def enviarMensaje():
    if request.method == 'POST':
        infoMensaje = request.get_json()  # Obtener los datos en formato JSON desde la solicitud POST
        nombre = infoMensaje.get('nombre') # Obtener el nombre de usuario del JSON
        mensajeTexto = infoMensaje.get('mensaje') # Obtener el texto del mensaje del JSON

        usuario = Usuario(nombre) # Crear una instancia de Usuario con el nombre
        # Crear una instancia de Mensaje, con el contenido del texto obtenido y con el estado de que se encuentra en el servidor
        mensaje = Mensaje(mensajeTexto, 'en servidor') 
        # Envía el mensaje a través del usuario
        usuario.enviarMensaje(mensaje, socketio)
    response = make_response(redirect(url_for('chat')))
    response.headers['Access-Control-Allow-Private-Network'] = 'true'
    return response


# Ruta principal que renderiza la página de chat
@app.route('/')
def chat():
    return render_template('chat.html', ) # Renderizar la plantilla 'chat.html'

# Ejecutar la aplicación Flask con SocketIO
if __name__ == '__main__':
    socketio.run(app, debug=True)
