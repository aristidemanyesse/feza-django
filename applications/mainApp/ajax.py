from django.contrib.auth.models import User
from django.http.response import HttpResponse
from django.shortcuts import render
from django.contrib.auth import authenticate, login
from django.http import  JsonResponse
import uuid, datetime
from django.contrib.sessions.backends.db import SessionStore
# Create your views here.
from django.utils.translation import gettext as _

from officineApp.models import ResponsableOfficine



def connexion(request):
    if request.method == "POST":
        datas = request.POST
        print(datas)
        user = authenticate(request, username=datas["identifiant"], password=datas["password"])
        if user is not None:
            try:
                if user.is_superuser:
                    request.session["user_id"] = user.id
                else:
                    respo = ResponsableOfficine.objects.get(pk = user.id)
                    if respo.is_never_connected:
                        request.session["respo_id"] = respo.id
                        return JsonResponse({"status":True, "new":True})
                login(request, user)
                return JsonResponse({"status":True})
            except Exception as e:
                print("**----------------------------------", e)
                return JsonResponse({"status":False, "message":_("Une erreur s'est produite lors de l'opération, veuillez recommencer !")})
        else:
            return JsonResponse({"status":False, "message":_("Login et/ou mot de passe incorrect !")})



def unlocked(request):
    if request.method == "POST":
        datas = request.POST
        user = authenticate(request, username=datas["username"], password=datas["password"])
        if user is not None:
            try:
                login(request, user)
                url = request.session['last_url']
                if 'locked' in request.session:
                    del request.session['locked']
                    del request.session['last_url']
                return JsonResponse({"status":True, "url":url})
            except Exception as e:
                print("-----------------------------------", e)
                return JsonResponse({"status":False, "message":_("Une erreur s'est produite lors de l'opération, veuillez recommencer !")})
        else:
            return JsonResponse({"status":False, "message":_("Mot de passe incorrect !")})



def unlocked(request):
    if request.method == "POST":
        datas = request.POST
        user = authenticate(request, username=datas["username"], password=datas["password"])
        if user is not None:
            try:
                login(request, user)
                url = request.session['last_url']
                if 'locked' in request.session:
                    del request.session['locked']
                    del request.session['last_url']
                return JsonResponse({"status":True, "url":url})
            except Exception as e:
                print("-----------------------------------", e)
                return JsonResponse({"status":False, "message":_("Une erreur s'est produite lors de l'opération, veuillez recommencer !")})
        else:
            return JsonResponse({"status":False, "message":_("Mot de passe incorrect !")})




def first_user(request):
    if request.method == "POST":
        datas = request.POST
        if len(datas["password"]) >= 6:
            if datas["password2"] == datas["password"]:
                try:
                    if ResponsableOfficine.objects.filter(deleted=False, username=datas["identifiant"]).exclude(pk = request.session["respo_id"]).count() > 0:
                        raise Exception(_("Vous ne pouvez pas utiliser ce nom d'utilisateur, veuillez le changer !"))
                    
                    respo = ResponsableOfficine.objects.get(pk = request.session["respo_id"])
                    if User.objects.filter(username=datas["identifiant"]).exclude(pk = respo.user_ptr_id).count() > 0:
                        raise Exception(_("Vous ne pouvez pas utiliser ce nom d'utilisateur, veuillez le changer !"))
                    
                    respo.username = datas["identifiant"]
                    respo.set_password(datas["password"])
                    respo.is_never_connected = False
                    respo.save()

                    respo = authenticate(request, username=datas["identifiant"], password=datas["password"])
                    login(request, respo)
                    res = JsonResponse({"status":True})

                except Exception as e:
                    print("++++----------------------------------", e)
                    res = JsonResponse({"status":False, "message": str(e)})
            else:
                res = JsonResponse({"status":False, "message":_("Les mots de passe ne correspondent pas !")})
        else:
            res = JsonResponse({"status":False, "message":_("Le nouveau mot de passe est trop court, minimum 8 caractères !")})

        return res





def forgetpassword(request):
    if request.method == "POST":
        datas = request.POST
        try :
            user = User.objects.get(email = datas["email"])
            ForgotPassword.objects.create(
                    email = datas["email"]
                )
            return JsonResponse({"status":True, "url":"/auth/reset/"})
        except Exception as e:
            print(e)
            return JsonResponse({"status":False, "message":_("Désolé, cette adresse email n'est pas connu par le ssytème !")})




def reset(request):
    if request.method == "POST":
        datas = request.POST
        if datas["password"] == datas["confirm"]:
            try :
                fp = ForgotPassword.objects.get(pk = id, is_validate = False)
                if fp.finished_at >= datetime.datetime.now():
                    user = User.objects.get(email = fp.email)
                    user.set_password(datas["password"])
                    user.save()

                    fp.is_validate = True
                    fp.save()
                    return JsonResponse({"status":True, "url":"/auth/login/"})
                else:
                    return JsonResponse({"status":False, "message":_("La période pour changer le mot de passe avec ce mail a expiré, veuillez recommencer la procédure !")})
            except Exception as e:
                print(e)
                return JsonResponse({"status":False, "message":_("Une erreur s'est produite lors del'opération, veuillez recommencer !")})
        else:
            return JsonResponse({"status":False, "message":_("Les mots de passe ne correspondent pas !")})




def logout(request):
    return render(request, "login.html")



# def forgetpassword(request):
#     if request.method == "POST":
#         datas = request.POST
#         try :
#             user = User.objects.get(email = datas["email"])
#             ForgotPassword.objects.create(
#                     email = datas["email"]
#                 )
#             return JsonResponse({"status":True, "url":"/auth/reset/"})
#         except Exception as e:
#             print(e)
#             return JsonResponse({"status":False, "message":_("Désolé, cette adresse email n'est pas connu par le ssytème !")})




# def reset(request):
#     if request.method == "POST":
#         datas = request.POST
#         if datas["password"] == datas["confirm"]:
#             try :
#                 fp = ForgotPassword.objects.get(pk = id, is_validate = False)
#                 if fp.finished_at >= datetime.datetime.now():
#                     user = User.objects.get(email = fp.email)
#                     user.set_password(datas["password"])
#                     user.save()

#                     fp.is_validate = True
#                     fp.save()
#                     return JsonResponse({"status":True, "url":"/auth/login/"})
#                 else:
#                     return JsonResponse({"status":False, "message":_("La période pour changer le mot de passe avec ce mail a expiré, veuillez recommencer la procédure !")})
#             except Exception as e:
#                 print(e)
#                 return JsonResponse({"status":False, "message":_("Une erreur s'est produite lors del'opération, veuillez recommencer !")})
#         else:
#             return JsonResponse({"status":False, "message":_("Les mots de passe ne correspondent pas !")})




def logout(request):
    return render(request, "login.html")