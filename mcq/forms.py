from django import forms  
from django.forms import ModelForm 
from .models import AllQuestions, CustomUser, Result
from django.contrib.auth.forms import UserCreationForm



class AllQuestionsForm(ModelForm):
    class Meta:
        model = AllQuestions
        fields = ['question', 'option_a', 'option_b', 'option_c', 'option_d', 
                  'answer', 'subject']


        labels = {
           'question': '',
           'option_a': '',
           'option_b': '',
           'option_c': '',
           'option_d': '', 
           'answer': '',
           'subject': '',
        }
    
        widgets = {
           'question': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Question', 
                     'style': 'font-family: Courier New; height: 52px; font-size: 110%'}),
           'option_a': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Option-a', 
                     'style': 'font-family: Courier New; font-size: 110%'}),
           'option_b': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Option-b', 
                     'style': 'font-family: Courier New; font-size: 110%'}),
           'option_c': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Option-c', 
                     'style': 'font-family: Courier New; font-size: 110%'}),
           'option_d': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Option-d', 
                     'style': 'font-family: Courier New; font-size: 110%'}),
           'answer': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Correct Answer', 
                     'style': 'font-family: Courier New; font-size: 110%'}),
           'subject': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Subject', 
                     'style': 'font-family: Courier New; font-size: 110%'}),
        }
    


class CustomUserCreationForm(UserCreationForm):
   password1 = forms.CharField(max_length = 16, widget = forms.PasswordInput(attrs = {'class': 'form-control', 'placeholder': 'Password'}))
   password2 = forms.CharField(max_length = 16, widget = forms.PasswordInput(attrs = {'class': 'form-control', 'placeholder': 'Confirm Password'}))
   class Meta:
      model = CustomUser
      fields = ['username', 'first_name', 'last_name','picture', 'phone', 'gender',
                'address', 'country', 'password1', 'password2', 'user_type']
      
      widgets = {
         'user_type': forms.RadioSelect(attrs = {
            
         }),
         'username': forms.TextInput(attrs = {
            'class': 'form-control',
            'placeholder': 'Username',
         }), 
         'first_name': forms.TextInput(attrs = {
            'class': 'form-control',
            'placeholder': 'First Name'
         }), 
         'last_name': forms.TextInput(attrs = {
            'class': 'form-control',
            'placeholder': 'Last Name'
         }),
         'picture': forms.FileInput(attrs = {
            'class': 'form-control',
         }),
         'phone': forms.TextInput(attrs = {
            'class': 'form-control',
            'placeholder': 'Phone Number'
         }),
         'gender': forms.TextInput(attrs = {
            'class': 'form-control',
            'placeholder': 'Gender'
         }),
         'address': forms.TextInput(attrs = {
            'class': 'form-control',
            'placeholder': 'Address'
         }),
         'country': forms.TextInput(attrs = {
            'class': 'form-control',
            'placeholder': 'Country'
         }),
      }
      
class UpdateCustomUserCreationForm(UserCreationForm):
   password1 = forms.CharField(max_length = 16, widget = forms.PasswordInput(attrs = {'class': 'form-control', 'placeholder': 'Password'}))
   password2 = forms.CharField(max_length = 16, widget = forms.PasswordInput(attrs = {'class': 'form-control', 'placeholder': 'Confirm Password'}))
   class Meta:
      model = CustomUser
      fields = ['first_name', 'last_name','picture', 'phone', 'gender',
                'address', 'country', 'password1', 'password2']
      
      widgets = {
         'first_name': forms.TextInput(attrs = {
            'class': 'form-control',
            'placeholder': 'First Name'
         }), 
         'last_name': forms.TextInput(attrs = {
            'class': 'form-control',
            'placeholder': 'Last Name'
         }),
         'picture': forms.FileInput(attrs = {
            'class': 'form-control',
         }),
         'phone': forms.TextInput(attrs = {
            'class': 'form-control',
            'placeholder': 'Phone Number'
         }),
         'gender': forms.TextInput(attrs = {
            'class': 'form-control',
            'placeholder': 'Gender'
         }),
         'address': forms.TextInput(attrs = {
            'class': 'form-control',
            'placeholder': 'Address'
         }),
         'country': forms.TextInput(attrs = {
            'class': 'form-control',
            'placeholder': 'Country'
         }),
         
      }
      
      
      
class loginForm(forms.ModelForm):
   class Meta:
      model = CustomUser
      fields = ['username', 'password']
      
      widgets = {
         'username': forms.TextInput(attrs = {
            'class': 'form-control', 
            'placeholder': 'Username',
         }),
         'password': forms.PasswordInput(attrs = {
            'class': 'form-control',
            'placeholder': 'Password'
         })
      }