from reg.models import Students
from django.forms import ModelForm

class Student_creation_form(ModelForm):
    class Meta:
        model = Students
        fields = '__all__'