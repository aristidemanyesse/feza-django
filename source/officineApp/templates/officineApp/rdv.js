

valider_rdv = function(id){
    url = "/officines/demandes/rdv/valider_rdv/";
    alerty.confirm("En validant, nous signalerons au demandeur que le médicament dont il est question est maintenant disponible dans votre officine.", {
        title: "Relance de demandeur",
        cancelLabel : "Annuler",
        okLabel : "OUI, relancer le client",
    }, function(){
        Loader.start()
        var formData = new FormData();
        formData.set("id", id);
        $.post({ url: url, data: formData, processData: false, contentType: false}, function(data){
            if (data.status) {
                window.location.reload()
            }else{
                Alerter.error('Erreur !', data.message);
            }
        },"json");
    })
}
