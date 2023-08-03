    $(".panel-body").find("input[type='checkbox']").each(function(i, element){
        element.check = false;
    })



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



    $("td input[type='checkbox']").change(function(){
        var parent = $(this).parent().parent();
        var id = parent.attr("id");
        if(this.checked){
            parent.find("div.hidde").hide()
        }else{
            parent.find("div.hidde").show()
        }
    })
    


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
            var produits_qte = {};
            var substituts = {};
            var substituts_qte = {};
            var rdv = {};
            $(".panel-body#"+id).find("table tbody tr").each(function(i, element){
                produits[$(element).attr("id")]= $(element).find("td input[type='checkbox']").is(":checked");
                produits_qte[$(element).attr("id")]= $(element).find("td input[type='number'][name='qte']").val();
                substituts[$(element).attr("id")]= $(element).find("td select[name='substitut']").val();
                substituts_qte[$(element).attr("id")]= $(element).find("td input[type='number'][name='substitut_qte']").val();
                rdv[$(element).attr("id")]= $(element).find("td select[name='rdv']").val();
            })

            console.table(produits_qte);
            console.table(substituts);
            console.table(substituts_qte);
            console.table(rdv);

            formData.set("demande", id);
            formData.set("produits", JSON.stringify(produits));
            formData.set("produits_qte", JSON.stringify(produits_qte));
            formData.set("substituts", JSON.stringify(substituts));
            formData.set("substituts_qte", JSON.stringify(substituts_qte));
            formData.set("rdv", JSON.stringify(rdv));
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
    