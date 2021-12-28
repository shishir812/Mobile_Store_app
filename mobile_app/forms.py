from django import forms
from .models import Mobile

class MobileForm(forms.ModelForm):
    class Meta:
        model = Mobile
        fields = "__all__"
        #fields = ('brand_name', 'model', 'color', 'jan_code', 'image', 'cou')



    def clean_brand_name(self):
        brand_name = self.cleaned_data.get('brand_name')
        if (brand_name == ""):
            raise forms.ValidationError('This field can not be left blank')
        return brand_name


    def clean_model(self):
        model = self.cleaned_data.get('model')
        if(model==""):
            raise forms.ValidationError('This field can not be left blank')

        for instance in Mobile.objects.all():
            if instance.model == model:
                raise forms.ValidationError('There is already a model named ' + model)

        return model

    def clean_color(self):
        color = self.cleaned_data.get('color')
        if (color == ""):
            raise forms.ValidationError('This field can not be left blank')
        return color



