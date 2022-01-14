from django.shortcuts import render
from django .views import View

# Create your views here.
class index(View):
    def get(self,request):
        return render(request,'web/index-2.html')

# Create your views here.
class home(View):
    def get(self,request):
        return render(request,'web/index.html')

class about(View):
    def get(self,request):
        return render(request,'web/about.html')

class contact(View):
    def get(self,request):
        return render(request,'web/contact.html')

class services(View):
    def get(self,request):
        return render(request,'web/services.html')

class team(View):
    def get(self,request):
        return render(request,'web/team.html')

class portfolio(View):
    def get(self,request):
        return render(request,'web/portfolio.html')
