$(document).ready(function () {

    /* FORMULARIO CONTACTO */
    $("#formularioContacto").validate({
        rules: {
            txtRut: {
                required: true,
                minlength: 8,
                maxlength: 9
            },
            txtNombre: {
                required: true,
                minlength: 3,
                maxlength: 50
            },
            txtAsunto: {
                required: true,
                minlength: 5,
                maxlength: 80
            },
            Mensaje: {
                required: true,
                minlength: 10,
                maxlength: 200
            }
        }
    });


    $("#btnGuardar").click(function () {
        if ($("#formularioContacto").valid() == false) {
            return;
        }
        else {
            let nombre = $("#txtRut").val();
            let rut = $("#txtNombre").val();
            let asunto = $("#txtAsunto").val();
            let mensaje = $("#Mensaje").val();
            let avisos = $("#avisos").is(":checked");
            console.log(nombre);
        }
    });

    /* FORMULARIO INGRESO */
    $("#formularioIngreso").validate({
        rules: {
            txtName: {
                required: true,
                minlength: 3,
                maxlength: 50
            },
            txtPass: {
                required: true,
                minlength: 3,
                maxlength: 50
            },
        }
    });
    

    $("#btnIngre").click(function () {
        if ($("#formularioIngreso").valid() == false) {
            return;
        }
        else {
            let name = $("#txtName").val();
            let pass = $("#txtPass").val();
            let avisos = $("#avisos").is(":checked");
            console.log(nombre);
        }
    });

    /* FORMULARIO REGISTRO */
    $("#formularioRegistro").validate({
        rules: {
            txtNomb: {
                required: true,
                minlength: 3,
                maxlength: 50
            },
            txtApe: {
                required: true,
                minlength: 3,
                maxlength: 50
            },
            txtRuta: {
                required: true,
                minlength: 8,
                maxlength: 9
            },
            txtFecha: {
                required: true,
            },
            txtUse: {
                required: true,
                minlength: 3,
                maxlength: 50
            },
            txtContr: {
                required: true,
                minlength: 3,
                maxlength: 50
            },
            txtContra: {
                required: true,
                minlength: 3,
                maxlength: 50
            },
        }
    });


    $("#btnReg").click(function () {
        if ($("#formularioRegistro").valid() == false) {
            return;
        }
        else {
            let nomb = $("#txtNomb").val();
            let ape = $("#txtApe").val();
            let ruta = $("#txtRuta").val();
            let fecha = $("#txtFecha").val();
            let use = $("#txtUse").val();
            let contr = $("#txtContr").val();
            let contra = $("#txtContra").val();
            let avisos = $("#avisos").is(":checked");
            console.log(nombre);
        }
    });


});