from django import forms

from web.models import ContactUs


class AddContactUs(forms.ModelForm):
    class Meta:
        model = ContactUs
        fields = ["name", "email", "location", "msg"]

        widgets = {

            "name": forms.TextInput(attrs={'class': 'mdl-textfield__input'}),
            "email": forms.EmailInput(attrs={'class': 'mdl-textfield__input'}),
            "location": forms.TextInput(attrs={'class': 'mdl-textfield__input'}),
            "msg": forms.TextInput(attrs={'class': 'mdl-textfield__input'}),

        }
        labels = {
            "Name": "Enter your Name",
            "Email": "Enter your Email",
            "Location": "Enter your Location or Address",
            "msg": "Enter your message",
        }
