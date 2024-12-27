#from django.shortcuts import render #1
#from django.http import HttpResponse
#from django.views import View #2
from django.views.generic import TemplateView

# Create your views here.
#def messageView(request): #1
#     return render(request,'home.html')

#class MessageView(View): #2
#     def get(self,requset):
#          return render(requset, 'home.html')

class MessageView(TemplateView):
     template_name = 'home.html'