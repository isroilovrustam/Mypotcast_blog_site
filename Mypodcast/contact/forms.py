from django import forms
from .models import Contact, Subscribe


class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super(ContactForm, self).__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'
            field.widget.attrs['placeholder'] = field_name


class SubscribeForm(forms.ModelForm):
    class Meta:
        model = Subscribe
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super(SubscribeForm, self).__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'
            # field.widget.attrs['placeholder'] = field_name
