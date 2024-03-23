from django import forms
from .models import Review

# class ReviewForm(forms.Form):
#     user_name=forms.CharField(label="Your Name", max_length=50,error_messages=
#                              {"required":"Name field cannot be empty",
#                               "max_length":"Please enter shorter name"})
#     review_text=forms.CharField(widget=forms.Textarea,label="Your Feedback",max_length=100,error_messages=
#                                 {"max_length":"Please enter shorter details"})
#     rating=forms.IntegerField(label="Your Rating",min_value=1,max_value=5)

class ReviewForm(forms.ModelForm):
    class Meta:
        model=Review
        fields = "__all__"
        # fields = ['user_name','review_text','rating']
        # exclude = ['owner_comment']
        error_messages = {
            'user_name':{'required':'This is required field','max_length':'Max length is fixed'},
            'review_text':{'required':'This is required field'},
            'rating':{'required':'This is required field'}
        }
        labels = {
            'user_name':'Your Name',
            'review_text':'Your Feedback',
            'rating':'Your Rating'
        }
	
