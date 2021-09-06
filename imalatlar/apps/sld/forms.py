from bootstrap_datepicker_plus import DatePickerInput
from django import forms

from .models import SLD


class SLDForm(forms.ModelForm):
    class Meta:
        model = SLD
        fields = "__all__"



        # fields = [
        #     'crm', 'company_name', 'billing_address', 'delivery_address', 'delivery_date', 'delivery_type', 'has_chest',
        #     'glass', 'color', 'notes', 'drawing', 'control', 'manufacturing_chief', 'door_type', 'pass_width',
        #     'pass_height', 'pass_height', 'ustluk', 'total_width', 'total_height', 'mechanism_width',
        #     'opening_direction', 'options', 'radar_activations',
        # ]
        widgets = {
            # 'crm': forms.TextInput(attrs={'placeholder': 'crm no', 'class': 'form-control'}),
            # 'crm': forms.TextInput,
            # 'company_name': forms.TextInput(attrs={'placeholder': 'firma adi', 'class': 'form-control'}),
            # 'billing_address': forms.TextInput(attrs={'placeholder': 'fatura adresi', 'class': 'form-control'}),
            # 'delivery_address': forms.TextInput(attrs={'placeholder': 'sevk adresi', 'class': 'form-control'}),
            'delivery_date': DatePickerInput(format='%d/%m/%Y',
                                             attrs={'placeholder': 'teslim tarihi', 'class': 'form-control'}),
            # 'delivery_type': forms.Select(attrs={'placeholder': 'Teslim sekli', 'class': 'form-control'}),
            # 'glass': forms.Select(attrs={'placeholder': 'cam', 'class': 'form-control'}),
            #
            # 'notes': forms.CharField(required=False, widget=forms.Textarea(attrs={
            #     "cols": 50,
            #     "rows": 20,
            #     "label": 'firma bilgileri',
            #     'class': 'form-control',
            # })),
            # 'pass_width': forms.NumberInput(attrs={'placeholder': 'gecis genisligi', 'class': 'form-control'})
        }
