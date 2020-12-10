

function abrirModalProductos(id){

    //Se traen los valores del producto seleccionado
let nombre = document.getElementById("nombre"+id).textContent;
let precio = document.getElementById("precio"+id).textContent;
let cantidad = document.getElementById("cantidad"+id).textContent;
let imagen = document.getElementById("imagen"+id).scr;

//Se traen los campos del promularios
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