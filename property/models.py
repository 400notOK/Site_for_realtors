from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from phonenumber_field.modelfields import PhoneNumberField


class Flat(models.Model):
    owners = models.ManyToManyField("Owner", blank=True, db_index=True, verbose_name="Владельцы")
    owner_depricated = models.CharField("ФИО владельца", max_length=200)
    created_at = models.DateTimeField("Когда создано объявление", default=timezone.now, db_index=True)

    new_building = models.NullBooleanField(db_index=True, verbose_name="Новое здание")
    
    description = models.TextField("Текст объявления", blank=True)
    price = models.IntegerField("Цена квартиры", db_index=True)

    town = models.CharField("Город, где находится квартира", max_length=50, db_index=True)
    town_district = models.CharField("Район города, где находится квартира", max_length=50, blank=True, help_text='Чертаново Южное')
    address = models.TextField("Адрес квартиры", help_text='ул. Подольских курсантов д.5 кв.4')
    floor = models.CharField("Этаж", max_length=3, help_text='Первый этаж, последний этаж, пятый этаж')

    rooms_number = models.IntegerField("Количество комнат в квартире", db_index=True)
    living_area = models.IntegerField("количество жилых кв.метров", null=True, blank=True, db_index=True)

    has_balcony = models.NullBooleanField("Наличие балкона", db_index=True)
    active = models.BooleanField("Активно-ли объявление", db_index=True)
    construction_year = models.IntegerField("Год постройки здания", null=True, blank=True, db_index=True)
    liked_by = models.ManyToManyField(
        User, related_name="liked_posts", verbose_name="Кто лайкнул", blank=True)

    def __str__(self):
        return f"{self.town}, {self.address} ({self.price}р.)"


class Owner(models.Model):
    name = models.CharField("ФИО владельца", max_length=200, db_index=True)
    phone_number = models.CharField("Номер владельца", max_length=20, db_index=True)
    pure_phone_number = PhoneNumberField(
        blank=True, region="RU", db_index=True, verbose_name="Нормализованный номер владельца")
    owners_flats = models.ManyToManyField(
        Flat, related_name="flat_owners", blank=True, verbose_name="Квартиры в собственности")


class Report(models.Model):
    report_owner = models.ForeignKey(
        User, on_delete=models.CASCADE, verbose_name="Кто жаловался", related_name='report_owners')
    report_flat = models.ForeignKey(
        Flat, on_delete=models.CASCADE, null=True, verbose_name="Квартира, на которую жаловались", related_name='report_flats')
    report_description = models.TextField(max_length=400, blank=True, verbose_name="Текст жалобы")
