$(document).ready(function() {

    $("form#formLogin").submit(function(event) {
        Loader.start();
        var url = "/auth/ajax/connexion/";
        var formData = new FormData($(this)[0]);
        $.post({ url: url, data: formData, processData: false, contentType: false}, function(data){
            if (data.status) {
                if (data.new) {
                    Loader.stop();
                    localStorage.setItem("user_id", data.user_id)
                    $("#modal-newUser").modal();
                }else{
                    window.location.href = "/main/dashboard";
                }
            }else{
                Loader.stop();
                Alerter.error('Erreur !', data.message);
            }
        });
        return false;
    });



    $("form#formNewUser").submit(function(event) {
        Loader.start();
        var url = "/auth/ajax/first_user/";
        var formData = new FormData($(this)[0]);

        $.post({url: url, data: formData, processData: false, contentType: false}, function(data){
            if (data.status) {
                window.location.href = "/main/dashboard";
            }else{
                Alerter.error('Erreur !', data.message);
            }
        });
        return false;
    });


});