$(document).ready(function() {
    $('select.sl_productos').change(function (e) { 
        e.preventDefault();
        let v = $('option:selected').val();
        console.log(v);
    });
    $("#buscar").keyup(function (e) {
        _this = this;

        $.each($("#table tbody tr"), function (index) {
            if($(this).text().toLowerCase().indexOf($(_this).val().toLowerCase()) !== -1) {
                $(this).show();
            } else { 
                $(this).hide();
            }
        })
        document.getElementById("buscar").addEventListener("click", function (e) {
            $(this).empty();
        })

        e.preventDefault();
    });

    $('.producto').on('click', (e) => {
        const element = $(this)[0].activeElement.parentElement.parentElement;
        // console.log($(element).find("td").eq(5).text());
        const precio = parseFloat($(element).find("td").eq(5).text().split(" ")[1].replace(',', ''));
        // console.log(precio);
        console.log($(element).find("th").text());
        $("input[name='id_producto']").val($(element).find("th").text());
        $("input[name='producto']").val($(element).find("td").eq(0).text());
        $("input[name='descripcion']").val($(element).find("td").eq(1).text());
        $("input[name='precio']").val(precio);
        $("#BtnGuardar").val("Modificar").addClass("btn-success");
        $("#BtnGuardar").removeClass("btn-primary");
        if(!document.getElementById('cancelar')) {
            // $("#form-pro div:last").append(
            //     $(document.createElement('input')).prop({
            //         type: 'button',
            //         value: 'Cancelar',
            //         class: 'btn btn-danger form-control',
            //         name: 'btncancelar',
            //         id: 'cancelar'
            //     })
            // );
            $(this).val("Cancelar");
            $("#form-pro").attr('action', "modificar_producto");
        }

        e.preventDefault();
    });
});