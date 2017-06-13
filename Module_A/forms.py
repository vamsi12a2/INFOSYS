from models import User
from django import forms

class User_Form(forms.ModelForm):
    class Meta:
        model= User
        fields=[
            "user_id",
            "name",
            "email",
            "city",
        ]