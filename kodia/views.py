from webbrowser import get
from django.shortcuts import redirect, render
from django.views import View
from django.http import HttpResponse
from django.utils.crypto import get_random_string
from .models import Kufa
# Create your views here.

class Home(View):
    def get(self, request):

        lang=request.COOKIES.get('lang')
        if lang is None or lang=='ar': 
            
            r = render(request, "homear.html")
            r.set_cookie('lang', 'ar')
        else:
            r = render(request, "homefr.html")
            
        
        
        user=request.COOKIES.get('user')
        
        if user is None:
            r.set_cookie('user', get_random_string(length=32))
            return r
        else:
            a = Kufa.objects.filter(user=user, done=False).all()
            
            if(len(a)>0):
                return render(request, "cmd.html", {"cmd":getattr(a.first(), 'items')})#aaa 
            else:
                return r
    
    def post(self, request):

        lang=request.COOKIES.get('lang')
        if lang is None or lang=='ar': 
            ar= True
        else:
            ar= False

        user=request.COOKIES.get('user')

        if user is None:
            return HttpResponse(":( <a href="/"><---</a>")
        else:
            a = Kufa.objects.filter(user=user, done=False).all()
            if(len(a)>0):
                return render(request, "cmd.html", {"cmd":getattr(a.first(), 'items'),"lang":ar})

            print(request.POST['name'])
            nc = Kufa(name=request.POST['name'], phone=request.POST['phone'],\
                 adress= request.POST['adress'], items=request.POST['items'], user=user)
            nc.save()
            
            return render(request, "cmd.html", {"cmd":getattr(nc, 'items'),"lang":ar})

class Plus(View):
    def get(self, request):
        lang=request.COOKIES.get('lang')
        if lang is None or lang=='ar': 
            ar= True
        else:
            ar= False
        r = render(request, "rules.html", {'lang':ar} )
        if (ar):
            r.set_cookie('lang', 'ar')
        
        return r

class Delete(View):
    def get(self, request):
        user=request.COOKIES.get('user')
        if user is not None:
            Kufa.objects.filter(user=user, done=False).all().delete()
        return redirect('/')

def getLang(request):
    
    lang=request.COOKIES.get('lang')
    if lang is None or lang=='ar': 
        r = redirect('/')
        r.set_cookie('lang', 'fr')
    else:
        r = redirect('/')
        r.set_cookie('lang', 'ar')
    return r


# Configure stuff users later.
class Login(View):
    def get(self, request):
        pass

class Stuff(View):
    def get(self, request):
        pass
