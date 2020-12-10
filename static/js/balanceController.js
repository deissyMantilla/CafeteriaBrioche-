var ventasDia;

window.onload = function() {
  let hoy = new Date();
  let fechaString = formatearFecha(hoy);
  document.getElementById('fechaBalance').value = fechaString;
  ventasDia = [
    {
      "id" : "415",
      "total" : "$25.000",
      "productosVendidos" : [
        {
          "id" : "45",
          "nombre" : "Café",
          "precioUnitario" : "$2.500",
          "cantidad" : "2"
        },
        {
          "id" : "23",
          "nombre" : "Torta Chocolate",
          "precioUnitario" : "$5.000",
          "cantidad" : "4"
        }
      ]
    },
    {
      "id" : "416",
      "total" : "$7.250",
      "productosVendidos" : [
        {
          "id" : "10",
          "nombre" : "Malteada Chocolate",
          "precioUnitario" : "$5.500",
          "cantidad" : "1"
        },
        {
          "id" : "10",
          "nombre" : "Tinto Mediano",
          "precioUnitario" : "$2.000",
          "cantidad" : "1"
        }
      ]
    },
    {
      "id" : "417",
      "total" : "$2.250",
      "productosVendidos" : [
        {
          "id" : "11",
          "nombre" : "Tinto Grande",
          "precioUnitario" : "$2.250",
          "cantidad" : "1"
        }
      ]
    }
  ];

  document.getElementById('ventaID1').innerHTML = ventasDia.find(element => element.id == 415).id;
  document.getElementById('ventaTotal1').innerHTML = ventasDia.find(element => element.id == 415).total;

  document.getElementById('ventaID2').innerHTML = ventasDia.find(element => element.id == 416).id;
  document.getElementById('ventaTotal2').innerHTML = ventasDia.find(element => element.id == 416).total;

  document.getElementById('ventaID3').innerHTML = ventasDia.find(element => element.id == 417).id;
  document.getElementById('ventaTotal3').innerHTML = ventasDia.find(element => element.id == 417).total;

  let mydate = window.document.getElementById("fechaBalance");
  let olddate = mydate.value;
  let isChanged = function(){
    if(mydate.value!== olddate){
      olddate=mydate.value;
      return true;
    };
    return false;
  };
  mydate.addEventListener("change", function(){
    if(isChanged())
      alert("Consultando el balance del día " + mydate.value + " en la base de datos...");
  });

};

let mostrarDetalles = function(ventaID) {
  let ventaSeleccionada = ventasDia.find(element => element.id == ventaID);
  document.getElementById('total').innerHTML = ventaSeleccionada.total;
};

let formatearFecha = function(date) {
  var year = date.getFullYear().toString();
  var month = (date.getMonth() + 1).toString();
  var day = date.getDate().toString();
  if(month.length == 1)
    month = "0" + month;
  if(day.length == 1)
    day = "0" + day;
  return year + "-" + month + "-" + day;
};