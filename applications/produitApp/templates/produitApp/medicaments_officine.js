$(function(){

    changeState = function(item, state){
        Loader.start();
        var url = "/produits/ajax/changeState/";
        var formData = new FormData();
        formData.set("item", item);
        formData.set("state", state);
        $.post({ url: url, data: formData, processData: false, contentType: false}, function(data){
            if (data.status) {
                $("ul#"+item+" li").removeClass("hide")
                $("btn-group a.btn").addClass("hide")

                $("ul#"+item).find("li#"+state).addClass("hide")
                $("btn-group").find("a.btn#"+state).removeClass("hide")

                console.log("ul#"+item+" li#"+state)
                Loader.stop();
            }else{
                Loader.stop();
                Alerter.error('Erreur !', data.message);
            }
        });
        return false;
    }
    
})