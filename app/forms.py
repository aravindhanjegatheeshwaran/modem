from django import forms
from .models import Csv,User


def validate_file_extension(value):
        if not value.name.endswith('.csv'):
            raise forms.ValidationError("Only CSV file is accepted")
class CsvForm(forms.ModelForm):
    name = forms.CharField(label='Name', max_length=100)
    file_csv=forms.FileField(label='UploadFile',validators=[validate_file_extension])
    class Meta:
        model = Csv
        fields=['name','file_csv']
