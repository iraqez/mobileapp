from django.db import models
from mobinfo.models import NumMob, UserNumber, OsRah, TaxMob
from userinfo.models import UserInfo, OrgInfo
from phonenumber_field.modelfields import PhoneNumberField
from datetime import datetime


class CardNum(models.Model):
    pass


class ActivationsNum(models.Model):
    NumMob = PhoneNumberField(blank=True, help_text='Введіть номер телефону', verbose_name='Номер')
    OsRah = models.ForeignKey(OsRah, on_delete=models.PROTECT, verbose_name='Особовий рахунок')
    UserInfo = models.ForeignKey(UserInfo, on_delete=models.PROTECT, verbose_name='Абонент')
    TaxMob = models.ForeignKey(TaxMob, on_delete=models.PROTECT, verbose_name='Тариф')
    date = models.DateTimeField(default=datetime.now())

    def __str__(self):
        phone = str(self.NumMob)
        return phone

    class Meta:
        verbose_name = "активація номера"
        verbose_name_plural = "активація номерів"


class StopNum(models.Model):
    pass


class PausedNum(models.Model):
    pass


class ReplaceTax(models.Model):
    pass


class ReplaceOsRah(models.Model):
    pass


class ReplaceUserNum(models.Model):
    pass


class ReplaceOrgNum(models.Model):
    pass