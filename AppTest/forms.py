from django.forms import ModelForm
from .models import GameInfo
from django import forms


# 绑定GameInfo model
class GameInfoForm(ModelForm):
    class Meta:
        model = GameInfo
        fields = "__all__"


class AddForm(forms.Form):

    pass
