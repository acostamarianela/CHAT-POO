#Clase que representa un mensaje en la aplicación.
#La relación entre la clase Usuario y la clase Mensaje es una ASOCIACIÓN, ya que el método
#enviarMensaje recibe una instancia de la clase Mensaje (mensajeParaEnviar), y utiliza el texto de ese mensaje para enviarlo al cliente.
#No existe dependencia de clases.
class Mensaje:
    #Método constructor
    def __init__(self, texto, estado):
        #Posee dos atributos, el contenido del mensaje y el estado del mensaje (por ejemplo, "en servidor", "recibido", etc.).
        self.__texto = texto
        self.__estado = estado

    #POLIMORFISMO: en este caso se utilizan metodos con el mismo nombre(tambien en claseUsuario, 'getMensaje()') pero que tienen 
    #distintos comportamientos. 
    #Obtiene el contenido del mensaje.
    #Setters y Getters: ENCAPSULAMIENTO Y ABSTRACCION 
    def getMensaje(self):
        return self.__texto
    
    #Establece el contenido del mensaje.
    def setMensaje(self, texto):
        self.__texto = texto

    #Obtiene el estado del mensaje.
    def getEstado(self):
        return self.__estado
    
    #Establece el estado del mensaje.
    def setEstado(self, estado):
        self.__estado = estado