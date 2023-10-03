
$(function(){


    modal = function(modal){
        $(modal).modal("show")
    }


    //mettre en session par ajax
    session = function(name, value){
    	var url = "../../../core/ajax/session/";
    	$.post(url, {name:name, value:value});
    }

    //supprimer en session par ajax
    delete_session = function(name){
    	var url = "../../../core/ajax/delete_session/";
        $.post(url, {name:name});
    }


});