// Declaración de variables
var socket; // Variable para mantener la conexión Socket.IO
var mensajes = ""; // Inicializa la variable 'mensajes' para almacenar el historial de mensajes

// Espera a que el documento HTML esté completamente cargado antes de ejecutar el código JavaScript
document.addEventListener("DOMContentLoaded", function () {
  // Establece la conexión Socket.IO al servidor en http://localhost:5000
  socket = io.connect("https://m51ghldl-5000.brs.devtunnels.ms/");

  // Escucha el evento 'message' emitido por el servidor Socket.IO
  socket.on("message", function (data) {
    console.log('Evento "message" recibido con datos:', data);
    var chat = document.getElementById("chat");
    mensajes += data.nombre + ": " + data.mensaje + "\n"; // Agregar el mensaje a la variable
    chat.value = mensajes; // Actualizar el contenido del elemento chat
    //chat.scrollTop = chat.scrollHeight; se utiliza para desplazar automáticamente la ventana de chat hacia abajo,
    //para que el mensaje más reciente sea siempre visible.
    chat.scrollTop = chat.scrollHeight;
  });

  // Obtener una referencia al formulario y sus elementos
  var form = document.getElementById("mensajeForm");
  var inputNombre = document.getElementById("nombre");
  var inputMensaje = document.getElementById("mensaje");

  //Se agrega un event listener para el 'submit' del formulario. Cuando el formulario se envía, esta función se ejecuta.
  form.addEventListener("submit", function (e) {
    e.preventDefault(); // Previene el envío por defecto del formulario
    var nombre = inputNombre.value;
    var mensaje = inputMensaje.value;
    // Realizar una solicitud POST al servidor sin recargar la página  en la ruta '/enviarMensaje'.
    //se envían los datos en formato JSON con dos campos: 'nombre' y 'mensaje', que provienen de las variables nombre y mensaje.
    axios
      .post(
        "/enviarMensaje",
        { nombre: nombre, mensaje: mensaje }, //se envian los datos de nombre y mensaje en formato JSON.
        { headers: { "Content-Type": "application/json",},}) // Configura el tipo de contenido como JSON

      //Define una función que se ejecutará cuando la solicitud POST sea exitosa y se reciba una respuesta del servidor.
      .then(function (response) {
        // Emitir el mensaje al servidor Socket.IO
        //implica mostrar el mensaje en la ventana de chat para que el usuario pueda ver su propio mensaje en tiempo real.
        socket.emit("text", { msg: mensaje });
        //console.log para verificar que funcionacorrectamente.
        console.log(response.data);
      })
      //Define una función que se ejecutará si ocurre un error durante la solicitud POST.
      .catch(function (error) {
        console.error(error);
      });

    // Limpiar el campo de mensaje después de enviarlo
    inputMensaje.value = "";
  });

  //Cuando ocurre una desconexión con el servidor, se ejecuta esta función y muestra un mensaje en la consola.
  socket.on("disconnect", function () {
    console.log("Desconectado del servidor de Socket.IO");
  });
});
