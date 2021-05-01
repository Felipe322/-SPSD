function muestraModal(url, titulo) {
    document.getElementById('formEliminar').action = url;
    document.getElementById('modalCuerpo').innerHTML = `Deseas eliminar el videojuego ${titulo}?`;
}


function muestraModalCategoria(url, nombre) {
    document.getElementById('formEliminarCat').action = url;
    document.getElementById('modalCuerpoCat').innerHTML = `Deseas eliminar la categoria ${nombre}?`;
}

function muestraModalUsuario(url, first_name) {
    document.getElementById('formEliminarUser').action = url;
    document.getElementById('modalCuerpoUser').innerHTML = `Deseas eliminar el usuario: ${first_name}?`;
}

$("#id_estado").on('change', function(){ 
    var token = $('[name="csrfmiddlewaretoken"]').val();  
    $.ajax({
        type: "post",
        url: `/usuarios/municipios/`,
        data: {'id':this.value, 'csrfmiddlewaretoken': token},
        success: function (response) {
            var html = "";
            if (response[0].hasOwnProperty('error')){
                html+=`<option value="0">${response[0].error}</option>`;
            }
            else{
                $.each(response, function (llave, valor) { 
                    html+=`<option value="${valor.id}">${valor.nombre}</option>`;
                });
            }
            $("#id_municipio").html(html);
        },
        error: function (param) { 
            console.log('Error en la petición')
        }
    });
});
/*
//Por post Ejemplo 1
$("#id_estado").on('change', function(){ 
    var token = $('[name="csrfmiddlewaretoken"]').val();  
    $.ajax({
        type: "post",
        url: `/usuarios/municipios/`,
        data: {'id':this.value, 'csrfmiddlewaretoken': token},
        success: function (response) {
            var html = "";
            if (response.error)
            if (response[0].hasOwnProperty('error')){
                html+=`<option value="0">${response[0].error}</option>`;
            }
            else{
                $.each(response, function (llave, valor) { 
                    html+=`<option value="${valor.id}">${valor.nombre}</option>`;
                });
            }
            $("#id_municipio").html(html);
        },
        error: function (param) { 
            console.log('Error en la petición')
        }
    });
});
*/

//Por Get
/*
$("#id_estado").on('change', function () {
    $.ajax({
        type: "get",
        url: `/usuarios/municipios/${this.value}`,
        //data: {'id':this.value, 'csrfmiddlewaretoken': token},
        success: function (response) {  
            var html = "";
            $.each(response, function (llave, valor) { 
                 html+=`<option value="${valor.id}">${valor.nombre}</option>`;
            });
            $("#id_municipio").html(html);
            //console.log(response);
        }
    });

});
*/
/*
$("#id_estado").on('change', function(){
    var token = $('[name="csrfmiddlewaretoken"]').val();
    $.ajax({
        type: "post",
        url: `/usuarios/municipios/`,
        data: {'id':this.value, 'csrfmiddlewaretoken': token},
        success: function (response) {
            var html = "";
            if (response[0].hasOwnProperty('error')){
                html+=`<option value="0">${response[0].error}</option>`;
            }
            else{
                $.each(response, function (llave, valor) {
                    html+=`<option value="${valor.id}">${valor.nombre}</option>`;
                });
            }
            $("#id_municipio").html(html);
        },
        error: function (param) {
            console.log('Error en la petición')
        }
    });
});
*/
/*
$("#id_estado").on('change',function(){
        alert('Hola');
        alert(this.value);
    });
*/

/*
 var token = $('[name="csrfmiddlewaretoken"]').val();
 $.ajax({
     type: "post",
     url: `/usuarios/municipios/`,
     data: {'id':this.value, 'csrfmiddlewaretoken': token},
     success: function (response) {
         var html = "";
         if (response[0].hasOwnProperty('error')){
             html+=`<option value="0">${response[0].error}</option>`;
         }
         else{
             $.each(response, function (llave, valor) {
                 html+=`<option value="${valor.id}">${valor.nombre}</option>`;
             });
         }
         $("#id_municipio").html(html);
     },
     error: function (param) {
         console.log('Error en la petición')
     }
 });
});

*/