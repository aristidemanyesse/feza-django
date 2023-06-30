


    ajouter = function(id){
        var url = "/main/dashboard/ajouter/";
        var formData = new FormData();
        var produit = $(".panel-body#"+id).find("select").val()
        var produits = [];
        $(".panel-body#"+id).find("table tbody tr").each(function(i, element){
            produits.push($(element).attr("id"));
        })
        formData.set("demande", id);
        formData.set("produit", produit);
        formData.set("produits", produits);
        $.post({ url: url, data: formData, processData: false, contentType: false}, function(content){
            $(".panel-body#"+id).find("table tbody").append(content)
        }, "html");
    }
    


    validerDemande = function(id){
        Loader.start()
        alerty.confirm("Voulez-vous vraiment valider cette demande ?", {
            title: "Validation...",
            cancelLabel: "Non",
            okLabel: "Oui, valider !",
        }, function () {
            var url = "/main/dashboard/valider_demande/";
            var formData = new FormData();
            var comment = $(".panel-body#"+id).find("textarea[name='comment']").val()
            var produits = {};
            $(".panel-body#"+id).find("table tbody tr").each(function(i, element){
                produits[$(element).attr("id")]= $(element).find("td input[type='checkbox']").is(":checked");
            })

            formData.set("demande", id);
            formData.set("produits", JSON.stringify(produits));
            formData.set("comment", comment);
            $.post({ url: url, data: formData, processData: false, contentType: false}, function(data){
                if (data.status){
                    window.location.reload()
                }else{
                    Alerter.error('Erreur !', data.message);
                }
                Loader.stop()
            }, "json"); 
        })     
    }
    