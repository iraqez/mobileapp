from django.db import models
from phonenumber_field.modelfields import PhoneNumberField
from userinfo.models import UserNumber, OrgInfo


class TaxMob(models.Model):
    name = models.CharField(max_length=128, unique=True, blank=True, verbose_name= 'Назва тарифу')
    # OpMob = models.ForeignKey(OpMob, on_delete=models.PROTECT, default=None)
    OP = (
        (None, "Виберіть оператора зв'язку"),
        ('ks', 'Київстар'),
        ('vf', 'Водафон'),
        ('lf', 'Life:)'),
        ('it', 'Інтертелеком'),
    )
    opname = models.CharField(max_length=2, choices=OP, default=None, verbose_name='Мобільний оператор')
    MbInTax = models.IntegerField(default=0, verbose_name='К-кість Mb в тарифі')
    MbOffTax = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='Вартість Mb поза тарифом')
    MinInTax = models.IntegerField(default=0, verbose_name='Кількість хв. в мережі в тарифі')
    MinOffTax = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='Вартість хв. в мережі поза дарифом')
    MinInTaxOther = models.IntegerField(default=0, verbose_name='Кількість хв. на інші мережі в тарифі')
    MinOffTaxOther = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='Вартість хв. на інші мережі'
                                                                                       ' поза дарифом')
    SmsOnTax = models.IntegerField(default=0, verbose_name='Кількість СМС в тарифі')
    SmsOffTax = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='Вартість СМС поза тарифом')
    MmsOnTax = models.IntegerField(default=0, verbose_name='Кількість MМС в тарифі')
    MmsOffTax = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='Вартість MМС поза тарифом')
    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "тарифний план"
        verbose_name_plural = "тарифні плани"


class NumMob(models.Model):
    phone = PhoneNumberField(blank=True, help_text='Введіть номер телефону', verbose_name='Номер', unique=True)
    TaxMob = models.ForeignKey(TaxMob, on_delete=models.PROTECT, default='+380991111111', verbose_name='Тариф')

    def __str__(self):
        phone = str(self.phone)
        return phone

    class Meta:
        verbose_name = "мобільний номер"
        verbose_name_plural = "мобільні номери"


class OsRah(models.Model):
    numRah = models.CharField(max_length=6, verbose_name="Особовий рахунок")
    OrgInfo = models.ForeignKey(OrgInfo, on_delete=models.PROTECT, verbose_name='Організація')

    def __str__(self):
        return self.numRah

    class Meta:
        verbose_name = "особовий рахунок"
        verbose_name_plural = "особові рахунки"
