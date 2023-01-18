from django.db import models
from django.conf import settings
from django.contrib.auth.models import User
from django.utils import timezone
from django.contrib.contenttypes.models import ContentType
from django.contrib.contenttypes.fields import GenericForeignKey
from django.utils.translation import ugettext_lazy as _
import uuid
from django import forms
from multiselectfield import MultiSelectField
import sqlite3

con = sqlite3.connect(r"D:\CyberwiseMacBook\Eski masaüstü\en son masaustu\rezervasyon_sistemi\ESXi.db")
cursor = con.cursor()
def read_value():
    cursor.execute("Select * from ESXi")
    liste = cursor.fetchall()
    return liste


esxi_array = read_value()
con.close()

# Create your models here.
class Reservation(models.Model):
    STATUS3 = ()
    for i in esxi_array:
        if i[2] == 1:
            STATUS3 += (
                (i[1], (i[0])),
            )

    Power_System = 0
    Water_System = 1
    Blade = 2
    DENIED = 3
    BORROWED = 4
    RETURNED = 5
    STATUS = (
        (Power_System, _("Power System")),
        (Water_System, _("Water System")),

    )

    STATUS2 = (
        (0, _("Evet")),
        (1, _("Hayır")),
    )
    user = models.ForeignKey("auth.User", on_delete=models.CASCADE)
    username = models.CharField(max_length=20, blank=True, verbose_name="Adınız")
    lastname = models.CharField(max_length=20, blank=True, verbose_name="Soyadınız")
    email = models.EmailField(max_length=50, blank=True, verbose_name="E-mail Adresiniz")
    reserved_start_date = models.DateField(default=timezone.now,verbose_name="Tarih")
    reserved_start_time = models.TimeField(blank=True, null=True, verbose_name="Başlangıç Zamanı")
    reserved_end_time = models.TimeField(blank=True, null=True, verbose_name="Bitiş Zamanı")
    status = models.SmallIntegerField(choices=STATUS, default=Power_System, verbose_name="Seçenekler")
    status2 = models.SmallIntegerField(choices=STATUS2, default=1, verbose_name="Kontrol Paneli")
    status3 = MultiSelectField(choices=STATUS3, verbose_name="ESXi", null=True)
    updated_datetime = models.DateTimeField(auto_now=True)

    def __str__(self):
        return str(self.reserved_start_date)
