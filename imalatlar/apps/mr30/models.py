from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models
from django.urls import reverse

from ...common.models import WorkOrderAbstractModel

# WING_DATA = ((3, 3), (4, 4),)
MR30_TYPE_DATA = (
    ('uk_otomatik', 'OTOMATİK 3 KANATLI'),
    ('dk_otomatik', 'OTOMATİK 4 KANATLI'),
    ('uk_manuel', 'MANUEL 3 KANATLI'),
    ('dk_manuel', 'MANUEL 4 KANATLI'),
)

# Burdaki isimlendirmeler js tarafında da aynı şekilde olmalıdır!
# Herhanbi bi değişiklikte dikkatli olunmalı

OPTIONS_LIST = (
    ('HMI El Terminali', 'HMI El Terminali'),
    ('Acil Stop', 'Acil Stop'),
    ('Kart Okuyucu', 'Kart Okuyucu'),
    ('Batarya', 'Batarya'),
)
RADAR_ACTIVATION_LIST = (
    ('Mikrodalga Radar', 'Mikrodalga Radar'),
    ('CombineRadar Safety - Activation', 'CombineRadar Safety - Activation'),
    ('Yaklaşım Sensoru', 'Yaklaşım Sensoru'),
)

GLASS_TYPES = (
    ('4+4 Bombeli Seffaf Lamine', '4+4 Bombeli Seffaf Lamine'),
    ('5+5 Bombeli Seffaf Lamine', '5+5 Bombeli Seffaf Lamine'),
    ('6+6 Bombeli Seffaf Lamine', '6+6 Bombeli Seffaf Lamine'),
    ('4+4 Bombeli Opak Lamine', '4+4 Bombeli Opak Lamine'),
    ('5+5 Bombeli Opak Lamine', '5+5 Bombeli Opak Lamine'),
    ('6+6 Bombeli Opak Lamine', '6+6 Bombeli Opak Lamine'),
)

GLASS_TYPES_STANDART = (
    ('4+4 Seffaf Lamine', '4+4 Seffaf Lamine'),
    ('5+5 Seffaf Lamine', '5+5 Seffaf Lamine'),
    ('6+6 Seffaf Lamine', '6+6 Seffaf Lamine'),
    ('4+4 Opak Lamine', '4+4 Opak Lamine'),
    ('5+5 Opak Lamine', '5+5 Opak Lamine'),
    ('6+6 Opak Lamine', '6+6 Opak Lamine'),
    ('8 mm Temperli', '8 mm Temperli'),
    ('10 mm Temperli', '10 mm Temperli'),
    ('12 mm Temperli', '12 mm Temperli'),
)
COLOR = (
    ('Ral Boya', 'Ral Boya'),
    ('Mat Eloksal', 'Mat Eloksal'),
    ('Renkli Mat Eloksal', 'Renkli Mat Eloksal'),
    ('304 Kalite Mat Paslanmaz', '304 Kalite Mat Paslanmaz'),
    ('304 Kalite Ayna Paslanmaz', '304 Kalite Ayna Paslanmaz'),
    ('304 Kalite Satine Paslanmaz', '304 Kalite Satine Paslanmaz'),
    ('316 Kalite Mat Paslanmaz', '316 Kalite Mat Paslanmaz'),
    ('316 Kalite Ayna Paslanmaz', '316 Kalite Ayna Paslanmaz'),
    ('316 Kalite Satine Paslanmaz', '316 Kalite Satine Paslanmaz'),
)


class MR30(WorkOrderAbstractModel):
    mr30_type = models.CharField(default='OTOMATİK', max_length=30, choices=MR30_TYPE_DATA,
                                 verbose_name='MR30 Kapı Türü')
    dia = models.IntegerField(default=1600, validators=[MinValueValidator(1600), MaxValueValidator(4000)],
                              verbose_name='Çap')
    trans_height = models.IntegerField(default=1900, validators=[MinValueValidator(1900), MaxValueValidator(4000)],
                                       verbose_name='Geçiş Yüksekliği')
    canopy = models.IntegerField(default=100, validators=[MinValueValidator(100), MaxValueValidator(1500)],
                                 verbose_name='Kanopi')
    # wing_data = models.IntegerField(default=3, choices=WING_DATA, verbose_name='Kanat Sayısı')
    fixed_glass = models.CharField(max_length=100, verbose_name='Sabit Cam', choices=GLASS_TYPES,
                                   default='4bombeliseffaflamine')
    moving_glass = models.CharField(max_length=100, verbose_name='Hareketli Cam', choices=GLASS_TYPES_STANDART,
                                    default='8mmtemperli')
    broken_wing = models.BooleanField(default=False, verbose_name='Kırılan Kanat')
    ground_circle = models.BooleanField(default=False, verbose_name='Yer Çemberi')
    night_sensor = models.BooleanField(default=False, verbose_name='Gece Kalkanı')
    heel_sensor = models.BooleanField(default=False, verbose_name='Dikey Kanat pnomatigi')
    cati_izolasyonu = models.BooleanField(default=False, verbose_name='Cati Izolasyonu')
    hava_perdesi = models.BooleanField(default=False, verbose_name='Hava Perdesi')
    otomasyon_secimi = models.BooleanField(default=False, verbose_name='Otomasyon Secimi')
    spain_key = models.BooleanField(default=False, verbose_name='İspanyolet Kilit')
    stain_arm = models.BooleanField(default=False, verbose_name='Paslanmaz Kol')
    button_pole = models.BooleanField(default=False, verbose_name='Buton Direği')
    # opsiyonlar ve radar aktivasyonları aralarında boş bırakılarak "*_LIST" içerisindeki ilk verilerden olusturulmalı
    # ornek: "acil_stop batarya"
    options = models.CharField('Opsiyonlar', blank=True, null=True, max_length=250, choices=OPTIONS_LIST,
                               default='HMI El Terminali')
    radar_activations = models.CharField('RADAR ve AKTIVASYON SECENEKLERI', blank=True, null=True, max_length=250,
                                         choices=RADAR_ACTIVATION_LIST, default='CombineRadar Safety - Activation')
    colors = models.CharField('Renk', max_length=27, choices=COLOR)

    class Meta:
        db_table = 'MR30'
        verbose_name = 'MR30 Doner Kapilar'
        verbose_name_plural = 'MR30s'

    def __str__(self):
        return f'{self.crm} - {self.company_name} - {self.mr30_type}'
        # crm no ve firma isimleri database ve admin panelinde gozukur.

    def get_absolute_url(self):
        return reverse('mr30:detail', kwargs={'id': self.id})
        # nesnelerimizin adreslemesini yapariz.

    @property  # metodlara alanlara bir ozellikmis gibi erismeyi saglar, fonksiyonu parametre haline getirir.
    def get_display_options(self):
        if self.options:
            return [self.OPTIONS_LIST.get(option) for option in self.options.split(' ')]
        return None

    @property
    def get_display_radar_activations(self):
        if self.radar_activations:
            return [self.RADAR_ACTIVATION_LIST.get(radar) for radar in self.radar_activations.split(' ')]
        return None

    def door(self):
        return self.door_type.split('_')[-1]

    def wing(self):
        for i in self.MR30_TYPE_DATA:
            return i if i == self.mr30_type else ''

    def get_wing_count(self):
        """
        Sabit kanat sayısını hesaplama
        """
        if 'uk' in self.door_type:
            return 3
        elif 'dk' in self.door_type:
            return 4
        else:
            return 0

    def get_wings_info(self):
        """
        Kanat sayılarını alma
        """
        return self.get_wing_count()
