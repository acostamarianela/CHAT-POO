#La clase Usuario representa a un usuario en una aplicación de chat. 
#La relación entre la clase Usuario y la clase Mensaje es una ASOCIACIÓN, ya que el método
#enviarMensaje recibe una instancia de la clase Mensaje (mensajeParaEnviar), y utiliza el texto de ese mensaje para enviarlo al cliente.
#No existe dependencia de clases.
class Usuario:
    # Constructor de la clase Usuario que recibe el nombre de usuario como parámetro.
    def __init__(self, nombreUsuario):
        self.__nombreUsuario = nombreUsuario

    #ENCAPSULAMIENTO Y ABSTRACCION 
    # Método para obtener el nombre de usuario.
    def getNombreUsuario(self):
        return self.__nombreUsuario
    
    # Método para establecer el nombre de usuario.
    def setNombreUsuario(self, nombreUsuario):
        self.__nombreUsuario = nombreUsuario

    #Método para ingresar el nombre de usuario (destinado a futuras implementaciones).
    #Esta funcion será encargada de validar el nombre de usuario (que no posea números, por ejemplo)
    def ingresarNombreUsuario(self):
        pass

    #Método para enviar un mensaje al cliente a través de SocketIO.
    #Recibe la instancia del mensaje recibido en las routes, y una instancia de SocketIO para utilizar.
    def enviarMensaje(self, mensajeParaEnviar, socketio):
        #Obtiene el texto del mensaje que se va a enviar, a través del método getTexto() de la clase Mensaje.
        mensaje = mensajeParaEnviar.getMensaje()
        #Obtiene el nombre de usuario del remitente del mensaje.
        nombre = self.getNombreUsuario()
        #Emite un evento 'message' a través de SocketIO con el nombre del usuario y el mensaje.
        #Los eventos son una forma de comunicación bidireccional entre el servidor y el cliente en tiempo real,
        #permiten que el servidor y el cliente envíen y reciban datos de manera asincrónica.
        socketio.emit('message', {'nombre': nombre, 'mensaje': mensaje})
        #Enviar el mensaje a través del usuario y SocketIO
        mensajeParaEnviar.setEstado('Enviado')
    
    #POLIMORFISMO: en este caso se utilizan metodos con el mismo nombre(tambien en claseMensaje) pero que tienen distinto comportamiento. 
    #en claseUsuario si es que el usuario lo requiere, puede recuperar ambos atributos del mensaje
    def getMensaje(self, mensaje):
        return mensaje.getMensaje(), mensaje.getEstado()
