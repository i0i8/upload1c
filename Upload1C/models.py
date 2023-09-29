from django.db import models

# Create your models here.


class DateLink(models.Model):
    date = models.DateField(verbose_name='Дата заполнения')

    def __str__(self):
        return f'Дата отчета {self.date}'


class SmallOpt(models.Model):
    unitate = models.CharField(
        max_length=10, verbose_name='Еденица измерения', default='тн', null=True, blank=True)
    typeOil = models.CharField(
        max_length=25, verbose_name='Тип топлива')
    summMonth = models.FloatField(
        max_length=10, verbose_name='Показатели за месяц')
    summQuarter = models.FloatField(
        max_length=10, verbose_name='Сумма квартал')
    summYear = models.FloatField(
        max_length=10, verbose_name='Сумма за год')
    summFactMonth = models.FloatField(
        max_length=10, verbose_name='Показатели факт за месяц')
    summFactQuarter = models.FloatField(
        max_length=10, verbose_name='Сумма факт квартал')
    summFactYear = models.FloatField(
        max_length=10, verbose_name='Сумма факт за год')
    summFactBeforeMonth = models.FloatField(
        max_length=10, verbose_name='Показатели предыдущий месяц')
    date = models.DateField(verbose_name='Дата выгрузки')

    class Meta:
        verbose_name = 'Малый отп'
        verbose_name_plural = 'Малые опты'

    def __str__(self):
        return f'Дата выгрузки - {self.date}'


class RetailValue(models.Model):
    unitate = models.CharField(
        max_length=10, verbose_name='Еденица измерения', default='тн', null=True, blank=True)
    typeOil = models.CharField(
        max_length=25, verbose_name='Тип топлива')
    summMonth = models.FloatField(
        max_length=10, verbose_name='Показатели за месяц')
    summQuarter = models.FloatField(
        max_length=10, verbose_name='Сумма квартал')
    summYear = models.FloatField(
        max_length=10, verbose_name='Сумма за год')
    summFactMonth = models.FloatField(
        max_length=10, verbose_name='Показатели факт за месяц')
    summFactQuarter = models.FloatField(
        max_length=10, verbose_name='Сумма факт квартал')
    summFactYear = models.FloatField(
        max_length=10, verbose_name='Сумма факт за год')
    summFactBeforeMonth = models.FloatField(
        max_length=10, verbose_name='Показатели предыдущий месяц')
    date = models.DateField(verbose_name='Дата выгрузки')

    class Meta:
        verbose_name = 'Розница объем'
        verbose_name_plural = 'Розница объемы'

    def __str__(self):
        return f'Дата выгрузки - {self.date}'


class FuelBase(models.Model):
    storage = models.CharField(
        max_length=100, verbose_name='Склад', blank=True)
    fuel = models.CharField(max_length=20, verbose_name='Номенклатура')
    balance = models.FloatField(verbose_name='Остаток')
    owner = models.CharField(max_length=255, verbose_name='Владелец')
    date = models.DateField(verbose_name='Дата')

    class Meta:
        verbose_name = 'База'
        verbose_name_plural = 'Базы'

    def __str__(self):
        return f'Остаток на начала {self.date}, склад {self.storage} владелец {self.owner}'


class Mony(models.Model):
    unitate = models.CharField(max_length=10, verbose_name='Еденица измерения')
    summDay = models.FloatField(verbose_name='Сумма день')
    owner = models.CharField(max_length=150, verbose_name='Организация')
    typeSela = models.CharField(max_length=50, verbose_name='Вид продажи')
    summMonth = models.FloatField(verbose_name='Сумма месяц')
    summYear = models.FloatField(verbose_name='Сумма год')
    date = models.DateField(verbose_name='Дата')

    class Meta:
        verbose_name = 'Деньги'
        verbose_name_plural = 'Деньги'

    def __str__(self):
        return f'Дата выгрузки {self.date}'
