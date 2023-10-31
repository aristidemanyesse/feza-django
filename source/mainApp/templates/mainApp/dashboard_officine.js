
window.OneSignalDeferred = window.OneSignalDeferred || [];
OneSignalDeferred.push(function(OneSignal) {
    OneSignal.init({
        appId: "9e13458a-372b-4387-b193-c6f81b625bec",
    });
});

data = {}
fetch('../../../static/administrations/medicaments.json')
.then(response => {
    if (!response.ok) {
        throw new Error('Network response was not ok');
    }
    return response.json();  // Convertir la réponse en JSON
})
.then(result => {
    data = result
})

$(function () {
    alerty.confirm("Activer le son de l'alerte ?", {
        title: "Alerte Son...",
        cancelLabel: ".",
        okLabel: "Oui, activer !",
    })
})


timer = setInterval(()=>{
    var url = "/main/dashboard/check_demande/";
    $.post({ url: url, processData: false, contentType: false}, function(data){
        if (data.status){
            var bipAudio = new Audio("../../../static/dist/sounds/bip.mp3");
            bipAudio.play();
            bipAudio.addEventListener('ended', function() {
                setTimeout(function() {
                    bipAudio.play();
                }, 3000);// Jouer à nouveau le bip lorsque le son se termine
            }, false);

            stopAudioTimeout = setTimeout(function() {
                bipAudio.pause();
            }, 5 * 60 * 1000);
            
            Alerter.success('Nouvelle demande !', "Vous avez reçu une nouvelle demande.\n Veuillez actualiser la page pour repondre à cette demande.", 15 * 60 * 7 * 1000);
            clearInterval(timer);
        }else{
            Alerter.error('Erreur !', data.message);
        }
    }, "json");
}, 1000 * 20);    


$(".panel-body").find("input[type='checkbox']").prop('checked', false);
$(".panel-body").find("textarea").val('');



ajouter = function(id){
    var url = "/main/dashboard/ajouter/";
    var formData = new FormData();
    var produit = $(".panel-body#"+id).find("select.produits").val()
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
                Loader.stop()
            }
        }, "json");
    })     
}
    