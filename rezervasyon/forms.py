from django import forms
from .models import Reservation
from django.core.validators import EmailValidator
from django.core.exceptions import ValidationError
from django.core.validators import validate_email
from datetime import datetime

class ReservationForm(forms.ModelForm):

    class Meta:
        model = Reservation
        fields = ["username","lastname","email","reserved_start_date","reserved_start_time","reserved_end_time", "status","status3"]



    def clean(self):
        username = self.cleaned_data.get("username")
        status = self.cleaned_data.get("status")
        status3 = self.cleaned_data.get("status3")
        lastname = self.cleaned_data.get("lastname")
        email = self.cleaned_data.get("email")
        reserved_start_date = self.cleaned_data.get("reserved_start_date")
        reserved_start_date = self.cleaned_data.get("reserved_start_date")
        reserved_start_time = self.cleaned_data.get("reserved_start_time")
        reserved_end_time = self.cleaned_data.get("reserved_end_time")

        if not username:
            raise forms.ValidationError("Adınızı Giriniz")
        if not lastname:
            raise forms.ValidationError("Soyadınızı Giriniz")
        if not email:
            raise forms.ValidationError("Email Adresini Giriniz")
        if not reserved_start_time:
            raise forms.ValidationError("Başlangıç Saatinizi Giriniz")
        if not reserved_end_time:
            raise forms.ValidationError("Son Saatinizi Giriniz")
        if email:
            validator = EmailValidator("^[a-zA-Z0-9.!#$%&'*+/=?^_`{|}~-]+@[a-zA-Z0-9](?:[a-zA-Z0-9-]{0,61}[a-zA-Z0-9])?(?:\.[a-zA-Z0-9](?:[a-zA-Z0-9-]{0,61}[a-zA-Z0-9])?)*$")
            validator(email)

        if reserved_start_time:
            tarih_queryset = Reservation.objects.all()
            tarih_queryset2 = str(tarih_queryset)

            queryset = Reservation.objects.values("reserved_start_time")
            queryset2 = str(queryset)

            bitis_queryset = Reservation.objects.values("reserved_end_time")
            bitis_queryset2 = str(bitis_queryset)

            durum_queryset = Reservation.objects.values("status")
            durum_queryset2 = str(durum_queryset)

            # baslangıç zamanı
            sayi = 50
            sayi2 = 95
            sayi3 = 95

            text = ""
            for i in range(49, len(queryset2)):

                if i <= sayi:
                    text += queryset2[i]
                    if i == sayi:
                        text += " "
                        if ',' in text:
                            text = text.replace(',', '0')
                            sayi = sayi - 1
                            sayi3 = sayi3 - 1
                            sayi2 = sayi2 - 1
                            if "00" in text:
                                text = text.replace('00', '00 ')
                            if "10" in text:
                                text = text.replace('10', '01 ')
                            if "20" in text:
                                text = text.replace('20', '02 ')
                            if "30" in text:
                                text = text.replace('30', '03 ')
                            if "40" in text:
                                text = text.replace('40', '04 ')
                            if "50" in text:
                                text = text.replace('50', '05 ')
                            if "60" in text:
                                text = text.replace('60', '06 ')
                            if "70" in text:
                                text = text.replace('70', '07 ')
                            if "80" in text:
                                text = text.replace('80', '08 ')
                            if "90" in text:
                                text = text.replace('90', '09 ')

                        sayi3 += 47

                elif i > sayi and i <= sayi2:
                    if i == sayi2:
                        sayi += 47
                        sayi2 = sayi3
                    continue
            for k in range(0, len(text)):
                if " " in text:
                    text = text.replace(' ', '')

            dizi = []
            text2 = ""
            onemli_zaman = 1
            for j in range(0, len(text)):
                if j <= onemli_zaman:
                    text2 += text[j]
                if j == onemli_zaman:
                    text2 += ":00:00"
                    dizi.append(text2)
                    text2 = ""
                    onemli_zaman += 2




            baslangic_zamani = str(reserved_start_time)


 #başlangıç tarihi
            sayi4 = 34
            sayi5 = 51
            sayi6 = 51

            text3 = ""
            for i in range(25, len(tarih_queryset2)):

                if i <= sayi4:
                    text3 += tarih_queryset2[i]
                    if i == sayi4:
                        sayi6 += 27
                elif i > sayi4 and i <= sayi5:
                    if i == sayi5:
                        sayi4 += 27
                        sayi5 = sayi6
                    continue


            dizi2 = []
            text4 = ""
            onemli_zaman2 = 9
            for j in range(0, len(text3)):
                if j <= onemli_zaman2:
                    text4 += text3[j]
                if j == onemli_zaman2:
                    dizi2.append(text4)
                    text4 = ""
                    onemli_zaman2 += 10

            baslangic_tarihi = str(reserved_start_date)


# bitiş zamanı

            sayi7 = 48
            sayi8 = 91
            sayi9 = 91

            text5 = ""
            for i in range(47, len(bitis_queryset2)):

                if i <= sayi7:
                    text5 += bitis_queryset2[i]
                    if i == sayi7:
                        text5 += " "
                        if ',' in text5:
                            text5 = text5.replace(',', '0')
                            sayi7 = sayi7 - 1
                            sayi8 = sayi8 - 1
                            sayi9 = sayi9 - 1
                            if "00" in text5:
                                text5 = text5.replace('00', '00 ')
                            if "10" in text5:
                                text5 = text5.replace('10', '01 ')
                            if "20" in text5:
                                text5 = text5.replace('20', '02 ')
                            if "30" in text5:
                                text5 = text5.replace('30', '03 ')
                            if "40" in text5:
                                text5 = text5.replace('40', '04 ')
                            if "50" in text5:
                                text5 = text5.replace('50', '05 ')
                            if "60" in text5:
                                text5 = text5.replace('60', '06 ')
                            if "70" in text5:
                                text5 = text5.replace('70', '07 ')
                            if "80" in text5:
                                text5 = text5.replace('80', '08 ')
                            if "90" in text5:
                                text5 = text5.replace('90', '09 ')

                        sayi9 += 45
                elif i > sayi7 and i <= sayi8:
                    if i == sayi8:
                        sayi7 += 45
                        sayi8 = sayi9
                    continue

            for k in range(0, len(text5)):
                if " " in text5:
                    text5 = text5.replace(' ', '')

            dizi3 = []
            text6 = ""
            onemli_zaman3 = 1
            for j in range(0, len(text5)):
                if j <= onemli_zaman3:
                    text6 += text5[j]
                if j == onemli_zaman3:
                    text6 += ":00:00"
                    dizi3.append(text6)
                    text6 = ""
                    onemli_zaman3 += 2


            bitis_zamanı = str(reserved_end_time)

            sayi10 = 22
            sayi11 = 36
            sayi12 = 36
            text7 = ""
            for i in range(22, len(durum_queryset2)):
                if i <= sayi10:
                    text7 += durum_queryset2[i]
                    if i == sayi10:
                        sayi12 += 15


                elif i > sayi10 and i <= sayi11:
                    if i == sayi11:
                        sayi10 += 15
                        sayi11 = sayi12

                continue

            dizi4 = []
            text8 = ""
            onemli_zaman4 = 0
            for m in range(0, len(text7)):
                if m <= onemli_zaman4:
                    text8 += text7[m]
                if m == onemli_zaman4:
                    dizi4.append(text8)
                    text8 = ""
                    onemli_zaman4 += 1

            durum = str(status)

            for k in range(0, len(dizi)):
                if dizi4[k] == durum and durum == '0':
                    if baslangic_zamani == dizi[k] and dizi2[k] == baslangic_tarihi:
                        raise forms.ValidationError("Başka bir zaman giriniz")
                    elif baslangic_zamani > dizi[k] and dizi3[k] > baslangic_zamani and dizi2[k] == baslangic_tarihi:
                        raise forms.ValidationError("Başka bir zaman giriniz")
                    elif dizi2[k] == baslangic_tarihi and bitis_zamanı > dizi[k] and bitis_zamanı < dizi3[k]:
                        raise forms.ValidationError("Başka bir zaman giriniz")
                    elif dizi2[k] == baslangic_tarihi and bitis_zamanı > dizi3[k] and baslangic_zamani < dizi[k]:
                        raise forms.ValidationError("Başka bir zaman giriniz")

                elif dizi4[k] == durum and durum == '1':
                    if baslangic_zamani == dizi[k] and dizi2[k] == baslangic_tarihi:
                        raise forms.ValidationError("Başka bir zaman giriniz")
                    elif baslangic_zamani > dizi[k] and dizi3[k] > baslangic_zamani and dizi2[k] == baslangic_tarihi:
                        raise forms.ValidationError("Başka bir zaman giriniz")
                    elif dizi2[k] == baslangic_tarihi and bitis_zamanı > dizi[k] and bitis_zamanı < dizi3[k]:
                        raise forms.ValidationError("Başka bir zaman giriniz")
                    elif dizi2[k] == baslangic_tarihi and bitis_zamanı > dizi3[k] and baslangic_zamani < dizi[k]:
                        raise forms.ValidationError("Başka bir zaman giriniz")

                elif dizi4[k] == durum and durum == '2':
                    if baslangic_zamani == dizi[k] and dizi2[k] == baslangic_tarihi:
                        raise forms.ValidationError("Başka bir zaman giriniz")
                    elif baslangic_zamani > dizi[k] and dizi3[k] > baslangic_zamani and dizi2[k] == baslangic_tarihi:
                        raise forms.ValidationError("Başka bir zaman giriniz")
                    elif dizi2[k] == baslangic_tarihi and bitis_zamanı > dizi[k] and bitis_zamanı < dizi3[k]:
                        raise forms.ValidationError("Başka bir zaman giriniz")
                    elif dizi2[k] == baslangic_tarihi and bitis_zamanı > dizi3[k] and baslangic_zamani < dizi[k]:
                        raise forms.ValidationError("Başka bir zaman giriniz")

            if baslangic_zamani > bitis_zamanı:
                raise forms.ValidationError("Bitiş zamanı başlangıç zamanından büyük olamaz")
            #if queryset.reserved_start_time == reserved_start_time:
            #    raise forms.ValidationError("yanlış")

        values = {
            "username": username,
            "lastname": lastname,
            "email": email,
            "reserved_start_date": reserved_start_date,
            "reserved_start_time": reserved_start_time,
            "reserved_end_time": reserved_end_time,
            "status" : status,
            "status3" : status3,
        }

        return values



