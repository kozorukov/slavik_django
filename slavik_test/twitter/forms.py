from django.forms import ModelForm

from twitter.models import Twitters


class TwittersForm(ModelForm):
    class Meta:
        model = Twitters
        fields = ['text']
