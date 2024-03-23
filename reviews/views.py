from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.views import View
from django.views.generic.base import TemplateView
from django.views.generic import ListView, DetailView
from django.views.generic.edit import FormView, CreateView

from .forms import ReviewForm
from .models import Review
# Create your views here.

# def review(request):
#     if request.method == 'POST':
#         enteredname= request.POST['user_name']
#         print(enteredname)
#         if enteredname=="":
#             return render(request,"reviews/review.html",{"has_error":True})
#         # return render(request, "reviews/thankyou.html")
#         return HttpResponseRedirect("/thankyou")
#     return render(request,"reviews/review.html",{"has_error":False})

# def review(request):
#     if request.method =="POST":
#         # exist_object=Review.objects.get(id='some_value') #fetch the required object
#         # form=ReviewForm(request.POST , instance=exist_object) #when we wish to update the object entry
#         form=ReviewForm(request.POST)
#         if form.is_valid():
#             # print(form.cleaned_data)
#             # review=Review(user_name=form.cleaned_data["user_name"],review_text=form.cleaned_data["review_text"],rating=form.cleaned_data["rating"])
#             # review.save()
#             form.save()   #via ModelForms, Upper Instantiation is not required here.
#             return HttpResponseRedirect("/thankyou")
#     else:
#         form=ReviewForm
#     return render(request,"reviews/review.html",{"form":form})


# class ReviewView(View):
#     def get(self,request):
#         form=ReviewForm()
#         return render(request,"reviews/review.html",{'form':form})
#     def post(self,request):
#         form=ReviewForm(request.POST)
#         if form.is_valid():
#             form.save()
#             return HttpResponseRedirect("/thankyou")
#         return render(request,"reviews/review.html",{'form':form})

# class ReviewView(FormView):
#     form_class = ReviewForm
#     template_name = "reviews/review.html"
#     success_url = "/thankyou"

#     def form_valid(self,form):
#         form.save()
#         return super().form_valid(form)


class ReviewView(CreateView):
    model = Review
    form_class = ReviewForm
    template_name = "reviews/review.html"
    success_url = "/rev/thankyou"

# def thankyou(request):
#     return render(request, "reviews/thankyou.html")
    
# class ThankyouView(View):
#     def get(self,request):
#         return render(request,"reviews/thankyou.html")
    
class ThankyouView(TemplateView):
    template_name = "reviews/thankyou.html"

    def get_context_data(self,**kwargs):
        context=super().get_context_data(**kwargs)
        context['message']="ByeByeNow!"
        return context

# class ReviewslistView(TemplateView):
#     template_name = "reviews/reviewslist.html"

#     def get_context_data(self,**kwargs):
#         context = super().get_context_data(**kwargs)
#         context['reviews']= Review.objects.all()
#         return context
    
class ReviewslistView(ListView):
    template_name = "reviews/reviewslist.html"
    model = Review
    context_object_name = "reviews"     # default is object_list
    
    def get_queryset(self):
        base_query=super().get_queryset()
        new_data=base_query.filter(rating__gt=1)
        return new_data

# class SinglereviewView(TemplateView):
#     template_name = "reviews/singlereview.html"

#     def get_context_data(self,**kwargs):
#         review_id = kwargs['id']
#         context = super().get_context_data(**kwargs)
#         review_detail = Review.objects.get(id=review_id)
#         context['detail'] = review_detail
#         return context
    
# class SinglereviewView(DetailView):
#     template_name = "reviews/singlereview.html"
#     model = Review
#     # objects or review(model name in all small)
#     # By default either of above variable is passed to the template for the rendering
    
class SinglereviewView(DetailView):
    template_name="reviews/singlereview.html"
    model= Review
    def get_context_data(self,**kwargs):
        context=super().get_context_data(**kwargs)
        request=self.request
        loaded_obj=self.object
        ldd_rev_id=loaded_obj.id
        fav_id=request.session.get("fav_rev_id")
        context["is_fav"]= ldd_rev_id == fav_id
        return context


class AddFavoriteView(View):
    def post(self,request):
        rev_id=request.POST["rev_id"]
        request.session["fav_rev_id"]=int(rev_id)    # Cannot store obj coz its not serializable hence storing primitive rev_id
        return HttpResponseRedirect("/rev/reviews/"+rev_id)