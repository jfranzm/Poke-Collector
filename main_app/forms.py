from django.forms import ModelForm
from .models import Stats

class StatForm(ModelForm):
    class Meta:
        model = Stats
        fields = ['Stat', 'Stat_Value', 'EVs']