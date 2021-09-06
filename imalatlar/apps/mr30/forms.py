from bootstrap_datepicker_plus import DatePickerInput
from django import forms

from .models import MR30


class MR30Form(forms.ModelForm):
    class Meta:
        model = MR30
        fields = "__all__"



        widgets = {
            'delivery_date': DatePickerInput(format='%d/%m/%Y',
                                             attrs={'placeholder': 'teslim tarihi', 'class': 'form-control'}),
        }


# fields = [
#             'company_name',
#             'crm',
#             'billing_adress', 'delivery_date',
#             'delivery_adress',
#             'delivery_type',
#             'created_time',
#             'has_chest', # sandikli mi
#             'glass', # GLASS_TYPES
#             'color', # COLORS
#             'notes',
#             'drawing',
#             'control',
#             'manufacturing_chief',

#             'mr30_type',
#             'dia',
#             'trans_height',
#             'canopy',
#             'wing_data', # WING_DATA
#             'fixed_glass', # GLASS_TYPES
#             'moving_glass', # GLASS_TYPES_STANDART

#             'broken_wing',
#             'ground_circle',
#             'night_sensor',
#             'heel_sensor',
#             'cati_izolasyonu',
#             'hava_perdesi',
#             'otomasyon_secimi',
#             'spain_key',
#             'stain_arm',
#             'button_pole',
#             'options', 'radar_activations', colors
#         ]
