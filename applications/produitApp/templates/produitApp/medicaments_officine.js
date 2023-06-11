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

    
})