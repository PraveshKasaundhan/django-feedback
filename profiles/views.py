from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.views.generic import View
from django.views.generic.edit import CreateView
from django.views.generic import ListView

# from .forms import ProfileForm
from .models import UserProfile

# Create your views here.

# def creator(request):
#     return render(request,"profiles/creator.html")

# def store_file(imgfile):
#     with open("temp/img.png",'wb+') as dest:
#         for chunk in imgfile.chunks():
#             dest.write(chunk)

# class CreatorView(View):
#     def get(self,request):
#         form=ProfileForm()
#         return render(request,"profiles/creator.html",{"form":form})

#     def post(self,request):
#         form=ProfileForm(request.POST,request.FILES)
#         if form.is_valid():
#             profile=UserProfile(image=request.FILES['image'])
#             profile.save()
#             # print(profile.image)
#             # store_file(imgobj)
#             return HttpResponseRedirect("/pro")
        
#         return render(request,"profiles/creator.html",{"form":form})
    
class CreatorView(CreateView): #Dont need form with this
    template_name="profiles/creator.html"
    model=UserProfile
    success_url="/pro"
    fields="__all__"


class UserProfileView(ListView):
    template_name="profiles/userprofiles.html"
    model = UserProfile
    context_object_name = "profiles"



def thankyou(request):
    return render(request,"profiles/thankyou.html")
	
