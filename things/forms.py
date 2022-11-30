"""Forms of the project."""
from .models import Thing
from django.forms import ModelForm, Textarea,NumberInput
# Create your forms here.
class ThingForm(ModelForm) :
    class Meta:
        model = Thing
        fields = ['name', 'description','quantity']
        widgets = {
            'description' : Textarea(attrs={'cols': 80, 'rows': 20}),
            'quantity' : NumberInput(attrs= { 'required': True, 'type': 'number',})
        }

