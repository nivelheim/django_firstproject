from django import forms

class ContactForm(forms.Form):
    contact_email = forms.EmailField(required=True, max_length=30, label='Email Address')
    contact_title = forms.CharField(required=True, max_length=50, label='Title')
    contact_content = forms.CharField(required=True, widget=forms.Textarea, label='Content')
        