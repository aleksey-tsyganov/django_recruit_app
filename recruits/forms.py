from django import forms
from .models import Recruit, Answer, Planet


class RecruitForm(forms.ModelForm):
    city = forms.ModelChoiceField(queryset=Planet.objects.all())

    class Meta:
        model = Recruit
        fields = "__all__"


class AnswerForm(forms.ModelForm):
    answer = forms.CheckboxInput()

    class Meta:
        model = Answer
        fields = ('question', 'answer')

