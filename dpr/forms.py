from django import forms
from .models import cabletray

class CableTrayForm(forms.ModelForm):
    class Meta:
        model = cabletray
        fields = '__all__'
        widgets = {
            'unit': forms.Select(attrs={'id': 'id_unit'}),
            'id': forms.TextInput(attrs={'id': 'id_id'}),
            'tag': forms.TextInput(attrs={'id': 'id_tag'}),
            'type': forms.Select(attrs={'id': 'id_type'}),
            'size': forms.Select(attrs={'id': 'id_size'}),
            'from_col': forms.TextInput(attrs={'id': 'id_from_col'}),
            'to_col': forms.TextInput(attrs={'id': 'id_to_col'}),
            'from_ele': forms.TextInput(attrs={'id': 'id_from_ele'}),
            'to_ele': forms.TextInput(attrs={'id': 'id_to_ele'}),
            'length_completed': forms.NumberInput(attrs={'id': 'id_length_completed'}),
            'area': forms.TextInput(attrs={'id': 'id_area'}),
            'tray_size_code': forms.TextInput(attrs={'id': 'id_tray_size_code'}),
            'ISMC_100': forms.NumberInput(attrs={'id': 'id_ISMC_100'}),
            'ISA_50': forms.NumberInput(attrs={'id': 'id_ISA_50'}),
            'ISA_40': forms.NumberInput(attrs={'id': 'id_ISA_40'}),
        }
