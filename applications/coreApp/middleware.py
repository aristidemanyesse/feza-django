
import datetime
import uuid, pytz
from django.shortcuts import redirect
from django.utils.timezone import make_aware
from UserApp.models import Utilisateur
from officineApp.models import ResponsableOfficine, Officine
from coreApp.models import Etat
from django.utils import translation
from django.shortcuts import redirect, get_object_or_404



class LockoutMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        response = self.get_response(request)
        return response     

    def process_view(self, request, view_func, view_args, view_kwargs):
        if '/admin/' not in request.path_info and '/auth/' not in request.path_info and '/graphql/' not in request.path_info and '/media/' not in request.path_info:
            if 'locked' in request.session:
                if request.session['locked'] :
                    return redirect("mainApp:locked")

            if not request.user.is_authenticated:
                return redirect("mainApp:login")



class  AccessCheckMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        response = self.get_response(request)
        return response    

    def process_view(self, request, view_func, view_args, view_kwargs):
        if len(request.path_info.split("/")) >= 2:
            request.module_name = request.path_info.split("/")[1]
            request.base_template = "layout/base_sidebar_"+request.module_name+".html"
            
            if len(request.path_info.split("/")) >= 3:
                try:
                    test = uuid.UUID(request.path_info.split("/")[3], version=4)
                except:
                    test = False
                if len(request.path_info.split("/")) >= 4 and request.path_info.split("/")[3] != "" and not test:
                    request.page_name = request.path_info.split("/")[3]
                else:
                    request.page_name = request.path_info.split("/")[2] if request.path_info.split("/")[2] != "" else "dashboard_"+request.module_name

            
            if not request.path_info.startswith('/admin/') and not request.path_info.startswith('/auth/expiration/') :
                request.now = datetime.datetime.now()
                request.etat = Etat
                request.uuid = uuid.uuid4()



class ChangeLanguage:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        response = self.get_response(request)
        return response     

    def process_view(self, request, view_func, view_args, view_kwargs):
        print(request.session.get("language", "fr"), "----------------------")
        translation.activate(request.session.get("language", "fr"))
        pass
    
    
    


class InjectMyAppDataMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        response = self.get_response(request)
        return response

    def process_view(self, request, view_func, view_args, view_kwargs):
        # request.languages_available = LANGUAGES

        if "date1" not in request.session:
            request.session["date1"] = str((datetime.datetime.now() - datetime.timedelta(days=3)).date())
            request.session["date2"] = str((datetime.datetime.now()).date())
            
        request.date1 = datetime.date.fromisoformat(request.session["date1"])
        request.date2 = datetime.date.fromisoformat(request.session["date2"])
        
        if not request.path_info.startswith('/admin/') and not request.path_info.startswith('/graphql/') and not request.path_info.startswith('/media/'):
    
            request.officine = None
            if request.user.is_authenticated:
                request.menu = "./partials/menu_admin.html"
                request.respo = request.user
                if not request.user.is_superuser:
                    respo = ResponsableOfficine.objects.get(user_ptr = request.user)
                    request.respo = respo
                    request.officine = respo.officine
                    request.menu = "./partials/menu_officine.html"
                    
                                
         

