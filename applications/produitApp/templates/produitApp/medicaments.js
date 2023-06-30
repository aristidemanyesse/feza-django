$(function(){

    get = function(id){
        Loader.start();
        var url = "/produits/ajax/get/";
        var formData = new FormData();
        formData.set("id", id);
        $.post({ url: url, data: formData, processData: false, contentType: false}, function(data){
            if (data.status) {
                var data = JSON.parse(data.data)[0]
                var fields = data["fields"];

                $("#modal-modifier-medicament").find("form").find("input[name=id]").val(data["pk"]);
                $("#modal-modifier-medicament").find("form").find("input[name=name]").val(fields["name"]);
                $("#modal-modifier-medicament").find("form").find("textarea[name=description]").val(fields["description"]);
                $("#modal-modifier-medicament").find("form").find("input[name=codebarre]").val(fields["codebarre"]);
                $("#modal-modifier-medicament").find("form").find("input[name=voies]").val(fields["voies"]);
                $("#modal-modifier-medicament").find("form").find("input[name=forme]").val(fields["forme"]);
                $("#modal-modifier-medicament").find("form").find("input[select=only_ordonnance]").val(fields["only_ordonnance"]);
                $("#modal-modifier-medicament").find("form").find("img").attr("src", "/"+fields["image"]);
                Loader.stop();
            }else{
                Loader.stop();
                Alerter.error('Erreur !', data.message);
            }
        });
        return false;
    }
    
})