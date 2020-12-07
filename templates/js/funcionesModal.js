
$(document).ready(function () {
    let boton = document.getElementById("botonActualizar");
    boton.addEventListener("click", function(e){
        console.log("click");
        //aqui se debe hacer la actualizacion en la base de datos
        $('#exampleModal').modal('hide');
    })
    
  });

