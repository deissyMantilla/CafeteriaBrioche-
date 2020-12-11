
function abrirModalProductos(id){

    //Se traen los valores del producto seleccionado
let nombre = document.getElementById("nombre"+id).textContent;
let precio = document.getElementById("precio"+id).textContent;
let cantidad = document.getElementById("cantidad"+id).textContent;
let imagen = document.getElementById("imagen"+id).scr;

//Se traen los campos del formulario
let idForm = document.getElementById("idForm");
let nombreForm = document.getElementById("nombreForm");
let precioForm = document.getElementById("precioForm");
let cantidadForm = document.getElementById("cantidadForm");
let imagenForm = document.getElementById("imagenForm");

//se asignan valores al formulario para actualizar productos
idForm.value = id;
nombreForm.value = nombre;
precioForm.value = precio;
cantidadForm.value = cantidad;
/* imagenForm.value = imagen;
console.log(imagenForm); */

 }


 function abrirModalCajeros(id){
 //Se traen los valores del cajero seleccionado
let nombre = document.getElementById("nombre"+id).textContent;
let apellido = document.getElementById("apellido"+id).textContent;
let edad = document.getElementById("edad"+id).textContent;
let correo = document.getElementById("correo"+id).textContent;
let identificacion = document.getElementById("identificacion"+id).textContent;

//Se traen los campos del formulario
let idForm = document.getElementById("idForm");
let nombreForm = document.getElementById("nombreForm");
let apellidoForm = document.getElementById("apellidoForm");
let edadForm = document.getElementById("edadForm");
let identificacionForm = document.getElementById("identificacionForm");
let direccionForm = document.getElementById("direccionForm");
let emailForm = document.getElementById("emailForm");
let generoForm = document.getElementById("generoForm");
let contrasenaForm = document.getElementById("contrasenaForm");

//se asignan valores al formulario para actualizar cajero
idForm.value = id;
nombreForm.value = nombre;
apellidoForm.value = apellido;
edadForm.value = edad;
emailForm.value =correo;
identificacionForm.value = identificacion;


 }

 function recuperarPass(){
     alert('Se ha enviado un correo con tu contraseña')
 }