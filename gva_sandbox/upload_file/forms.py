from django.forms import ModelForm
from upload_file.models import File

class FileForm(ModelForm):
    class Meta:
        model = File
        fields = ['name','file']