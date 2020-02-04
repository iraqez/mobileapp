from django.db import models


class OrgInfo(models.Model):
    name = models.CharField(max_length=128)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "організація"
        verbose_name_plural = "організації"


class UserInfo(models.Model):
    inn = models.CharField(max_length=10, unique=True, verbose_name='ІПН')
    name = models.CharField(max_length=30, verbose_name="Ім'я")
    patronymic = models.CharField(max_length=40, verbose_name='По батькові')
    surname = models.CharField(max_length=40, verbose_name='Прізвище')
    company = models.ForeignKey(OrgInfo, on_delete=models.PROTECT, verbose_name='Організація')

    def __str__(self):
        return '%s %s' % (self.name, self.surname)

    class Meta:
        verbose_name = "абонент"
        verbose_name_plural = "абоненти"


class UserNumber(models.Model):
    pass
