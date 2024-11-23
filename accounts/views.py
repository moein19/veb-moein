from django.shortcuts import render,redirect
from django.contrib import messages,auth
from django.contrib.auth.models import  User
from bloggers.models import Blogger

def register(request):
    if request.method == 'POST':
        name = request.POST['name']
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        password2 = request.POST['password2']

        if password == password2:
            if User.objects.filter(username=username).exists():
                messages.error(request, 'این نام کاربری در دسترس نیست')
                return redirect('register')
            else:
                if User.objects.filter(email=email).exists():
                    messages.error(request, 'این ایمیل قبلا استفاده شده است')
                    return redirect('register')
                else:
                    user = User.objects.create_user(username = username, password=password, email = email , first_name = name)

                    blogger = Blogger.objects.create(user = user , name = name , email = email)

                    auth.login(request, user)
                    messages.success(request, 'ثبت نام با موفقیت انجام شد')

                    return redirect('index')

        else:
            messages.error(request, 'رمز عبور هاس وارد شده مطابق نیستند')
            return redirect('register')
    else:
        return render(request, 'accounts/register.html')

def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = auth.authenticate(username=username, password=password)

        if user is not None:
            auth.login(request,user)
            messages.success(request, 'شما با موفقیت وارد سایت شدید')
            return redirect('index')
            
        else:
            messages.error(request, 'لطفا دوباره امتحان کنید نام کاربری یا رمز عبور اشتباه وارد شده')
            return redirect('login')
    else:
        return render(request, 'accounts/login.html')


def logout(request):
    if request.method == 'POST':
        auth.logout(request)
        messages.success(request, 'شما با موفقیت از حساب کاربری خود خارج شدید')
        return redirect('index')

    else:
        return redirect('index')

