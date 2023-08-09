from todo_list import forms
from todo_list import models
from .models import List


class ListForm(forms.Modelform):
    class Meta:
        model = List
        fields = ["item", "completed"]
