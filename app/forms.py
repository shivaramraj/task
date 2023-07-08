from django import forms
from app.models import *

class UserForm(forms.ModelForm):
    class Meta():
        model=User
        fields=['username','password']
        widgets={'password':forms.PasswordInput()}

        help_texts={'username':' '}

        widgets={
            'TrainName':forms.TextInput(attrs={'class':'form-control'}),
            'TrainNo':forms.TextInput(attrs={'class':'form-control'}),
            'TrainImage':forms.FileInput(attrs={'class':'form-control'}),
            'No_of_Coaches':forms.NumberInput(attrs={'class':'form-control'}),
            'From_To':forms.TextInput(attrs={'class':'form-control'}),
        }

        
            

class TrainForm(forms.ModelForm):
    class Meta():
        model = Trains
        fields = '__all__'
    