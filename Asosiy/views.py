from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from .models import *


def maqola(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            Maqola.objects.create(muallif = request.user,
                sarlavha = request.POST['sarlavha'],
                sana = request.POST['sana'],
                mavzu = request.POST['mavzu'],
                matn = request.POST['matn'],
                muallif1 = Muallif.objects.get(id=request.POST.get('m_ism'))
                )
            return redirect('/maqola/')
        content = {
            "maqola": Maqola.objects.filter(muallif1 = Muallif.objects.get(user = request.user)),
            'muallif': Muallif.objects.all()
        }
        return render(request, 'muallif.html', content)
    return redirect('/')


def home(request):
    if request.method == 'POST':
        user = authenticate(
            username = request.POST['login'],
            password = request.POST['parol'],
        )
        if user is None:
            return redirect('/')
        login(request, user)
        return redirect('/muallif/')
    return render(request, 'index.html')

def logout1(request):
    logout(request)
    return redirect('/')


def login_qoshish(request):
    if request.method == 'POST' and request.POST.get('parol1') == request.POST.get('parol2'):
        User.objects.create_user(
            username = request.POST.get('login'),
            password = request.POST.get('parol1')
        )
        return redirect('/')
    return render(request, 'register.html')


# Create your views here.
