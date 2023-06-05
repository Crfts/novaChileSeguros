
var rut = document.getElementById('id_rut')
var correo = document.getElementById('id_correo')
var telefono = document.getElementById('id_telefono') 
var fecha = document.getElementById('id_fecha_nacimiento')
var marca

var dominio = document.domain

rut.placeholder = 'Ej: 10123567-k'
correo.placeholder = 'Ingresa tu correo electronico'
telefono.placeholder = '(+56):'


document.getElementById('id_modelo').disabled = true
document.getElementById('id_ano').disabled = true

$("#id_patente").change(function(){
  if($('id_patente').val() != " "){
    $('#botonPatente').prop('disabled', false);
  }else{
    $('#botonPatente').prop('disabled', 'disabled');
  }
})

//Inicio Funcion validar select
$("#id_marca").change(function() {
    if($("#id_marca").val() != ""){
  
      $('#id_modelo').prop('disabled', false);
    }
    else {
      $("#id_modelo").prop('disabled', 'disabled')
      $("#id_ano").prop('disabled', 'disabled')
     
    };

    $("#id_modelo").change(function() {

      if($("#id_modelo").val() != ""){
        $('#id_ano').prop('disabled', false)
      }else{
        $('#id_ano').prop('disabled', 'disabled');
      }
    });

    $("id_ano").change(function(){
      if($("id_ano").val() != ""){
        $("#boton").prop('disabled', true)
      }else{
      
      }
    })
})
//Fin Funcion validar select

//Inicio Funcion pop 
function paso(){
  var con = document.getElementById('patente');
  var con3 = document.getElementById('cor');
  con.style.visibility = 'hidden';  
  con3.style.visibility = 'visible';
  //Esconder patente y mostrar auto
}

function hola(){
    var con1 = document.getElementById('cor');
    var con2 = document.getElementById('cor2');
    con1.style.visibility = 'hidden';
    con2.style.visibility = 'visible';
    //Esconder auto y mostrar datos personales
}

//Fin Funcion pop

//Inicio Funcion masDetalles
function masdetalles(){
  alert("hola como estas")
}
//Fin Funcion masDetalles