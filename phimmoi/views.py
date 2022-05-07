from django.shortcuts import render
from django.views import View
from django.http import HttpResponse
from django.contrib.auth import authenticate
from django.contrib.auth.models import User
from .models import Movie, Viewer, episode

class indexclass(View):
    def get(self, request):
        m = Movie.objects.all().order_by('-id')[:5]
        a = Movie.objects.filter(type="Anime").order_by('-id')[:5]
        h = Movie.objects.filter(type="Horror").order_by('-id')[:5]
        context = {"m": m, "a": a, "h": h}
        return render(request, "homepage.html", context)


class userclass(View):
    def get(self, request):
        m = Movie.objects.all().order_by('-id')[:5]
        a = Movie.objects.filter(type="Anime").order_by('-id')[:5]
        h = Movie.objects.filter(type="Horror").order_by('-id')[:5]
        context = {"m": m, "a": a, "h": h}
        return render(request, "user.html", context)


class loginclass(View):
    def get(self, request):
        return render(request, "login.html")

    def post(self, request):
        username = request.POST.get("username")
        password = request.POST.get("password")
        my_user = authenticate(username=username, password=password)
        if my_user is None:
            return HttpResponse("ko co user nao nhu the")
        else:
            m = Movie.objects.all().order_by('-id')[:5]
            a = Movie.objects.filter(type="Anime").order_by('-id')[:5]
            h = Movie.objects.filter(type="Horror").order_by('-id')[:5]
            context = {"m": m, "a": a, "h": h}
            return render(request, "user.html", context)



class signupclass(View):
    def get(self, request):
        return render(request, "dang-ky.html")

    def post(self, request):
        username = request.POST.get("username")
        password = request.POST.get("password")
        repassword = request.POST.get("repassword")
        email = request.POST.get("email")
        fullname = request.POST.get("fullname")
        birthday = request.POST.get("birthday")
        sex = request.POST.get("sex")
        new_user = Viewer(username=username, password=password, repassword=repassword, email=email, fullname=fullname,
                        birthday=birthday, sex=sex)
        account = User.objects.create_user(username, email, password)
        if password != repassword:
            return HttpResponse("có mỗi cái password mà nhập lại cũng ko đúng")
        else:
            new_user.save()
            account.save()

            return render(request, "dang-ky.html")



class theloaiclass(View):
    def get(self, request):
        a = Movie.objects.filter(type="Anime").order_by('-id')
        context = {"a": a}
        return render(request, "theo-the-loai.html", context)


class usertheloaiclass(View):
    def get(self, request):
        a = Movie.objects.filter(type="Anime").order_by('-id')
        context = {"a": a}
        return render(request, "user-theo-the-loai.html", context)


class watchclass(View):
    def get(self, request, movie_id):
        e = episode.objects.all()
        m = Movie.objects.get(pk=movie_id)
        context = {"m": m, "e": e}
        return render(request, "watch.html", context)