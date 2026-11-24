from django import forms
from django.utils import timezone

from .models import Bottle


class BottleForm(forms.ModelForm):
    class Meta:
        model = Bottle
        fields = ['text', 'open_at']
        widgets = {
            'text': forms.Textarea(attrs={'rows': 7, 'placeholder': "Kelajakdagi o'zingizga xat yozing..."}),
            'open_at': forms.DateInput(attrs={'type': 'date'}, format='%Y-%m-%d'),
        }

    def clean_open_at(self):
        d = self.cleaned_data['open_at']
        if d <= timezone.localdate():
            raise forms.ValidationError("Ochilish sanasi kelajakda bo'lishi kerak.")
        return d
