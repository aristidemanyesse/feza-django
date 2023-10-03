
$(function () {

    // Initialisation des plugins
    // $("select.select2").select2();



    //bouton principal de deconnexion
    $("a#btn-deconnexion").click(function (event) {
        alerty.confirm("Voulez-vous vraiment vous deconnecter ???", {
            title: "Deconnexion",
            cancelLabel: "Non",
            okLabel: "Oui, me deconnecter !",
        }, function () {
            window.location.href = "/auth/disconnect/";
        })
    });


    //filtre de la barre generale de recherche
    $("#top-search").on("keyup", function () {
        var value = $(this).val().toLowerCase();
        $("table.table-mise tr:not(.no), .item").filter(function () {
            $(this).toggle($(this).text().toLowerCase().indexOf(value) > -1)
        });
    });


    //selection des images
    $('body').on("click", "button.btn_image", function (event) {
        $(this).prev("input[type=file]").trigger('click');
    });
    $('body').on("change", ".modal input[type=file]", function (e) {
        var src = URL.createObjectURL(e.target.files[0])
        $(this).prev("img.logo").attr('src', src);
    });



});