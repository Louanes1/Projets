from django import forms
from .models import Company, Note


class CompanyForm(forms.ModelForm):
    note = forms.CharField(max_length=500, required=False, label='Ajouter une note')

    class Meta:
        model = Company
        fields = (
            'name', 'website', 'email_address', 'physical_address', 'contact_name', 'job_listing_site',
        )
        widgets = {
            'notes': forms.CheckboxSelectMultiple(attrs={'class': 'form-check-input'}),
        }

class NoteForm(forms.ModelForm):
    class Meta:
        model = Note
        fields = ('text',)
