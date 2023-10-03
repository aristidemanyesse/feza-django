$(function(){

    disponible = function(off, prod){
        Loader.start();
        var url = "/produits/ajax/disponible/";
        var formData = new FormData();
        formData.set("prod", prod);
        formData.set("off", off);
        $.post({ url: url, data: formData, processData: false, contentType: false}, function(data){
            if (data.status) {
                Loader.stop();
                Alerter.success('Succes !', "Votre stock a été mis a jour !");
            }else{
                Loader.stop();
                Alerter.error('Erreur !', data.message);
            }
        });
        return false;
    }


    indisponible = function(item){
        Loader.start();
        var url = "/produits/ajax/indisponible/";
        var formData = new FormData();
        formData.set("item", item);
        $.post({ url: url, data: formData, processData: false, contentType: false}, function(data){
            if (data.status) {
                Loader.stop();
                Alerter.success('Succes !', "Votre stock a été mis a jour !");
            }else{
                Loader.stop();
                Alerter.error('Erreur !', data.message);
            }
        });
        return false;
    }
    
    
    changePrice = function(id){
        var url = "/produits/ajax/change_price/";
        alerty.prompt("Saisissez le prix actuel de ce médicament dans votre officine (ces modifications ne s'appliqueront qu'aux nouvelles demandes)", {
            title: 'Changement de prix',
            inputType : "number",
            cancelLabel : "Annuler",
            okLabel : "Changer le prix"
        }, function(price){
            Loader.start();
            $.post(url, {id:id, price:price}, (data)=>{
                if (data.status) {
                    window.location.reload()
                }else{
                    Alerter.error('Erreur !', data.message);
                }
            },"json");
        })
    }
})