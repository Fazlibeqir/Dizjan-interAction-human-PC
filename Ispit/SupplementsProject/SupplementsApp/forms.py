from django import forms
from .models import Supplements


class SupplementForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(SupplementForm, self).__init__(*args, **kwargs)
        for field in self.visible_fields():
            field.field.widget.attrs['class'] = 'form-control'

    class Meta:
        model = Supplements
        fields = '__all__'
