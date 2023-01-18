from django.shortcuts import render,redirect
from .models import Reservation
from user.forms import LoginForm
from django.contrib.auth.models import User
from django.contrib.auth import login, authenticate, logout
from .forms import ReservationForm
# Create your views here.
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.core.exceptions import ValidationError
from django.core.mail import  send_mail
from django.conf import settings



@login_required(login_url="user:login")
def rezervasyon_islemleri(request):

    rezervasyon_list = Reservation.objects.all()
    rezervasyon_list2 = Reservation.objects.values("reserved_start_time")
    rezervasyon_list3 = Reservation.objects.values("reserved_end_time")
    rezervasyon_list4 = Reservation.objects.values("status")
    if request.method == 'POST':
        reserve_form = ReservationForm(request.POST)
        if reserve_form.is_valid():
            reserve = reserve_form.save(commit=False)
            reserve.user = request.user
            reserve.save()
            subject = "Yeni Kayıt"
            message = "Sevgili Prof. Dr İbrahim Özçelik, \n" \
                      "{} kullanıcısı kayıt olmuştur. Diğer işlemleri yapabilmek için onayınız beklenmektedir.\n" \
                      "İyi Günler, Teşekkürler".format(reserve.user)
            from_email = settings.EMAIL_HOST_USER
            to_list = [settings.EMAIL_HOST_USER]

            send_mail(subject,message,from_email,to_list,fail_silently = True)


            return redirect("rezervasyon_islemleri:rezervasyon islemleri")
            #reserve_form.save()
    else:
        reserve_form = ReservationForm()
    context = {
        'rezervasyon_list' : rezervasyon_list,
        'rezervasyon_list2': rezervasyon_list2,
        'rezervasyon_list3': rezervasyon_list3,
        'rezervasyon_list4': rezervasyon_list4,
        'reserve_form' : reserve_form
    }
      

    return render(request, 'rezervasyon.html', context)

def index(request):
    return render(request,'base.html')


