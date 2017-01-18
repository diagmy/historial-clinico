from django.contrib.auth import (
        authenticate,
        get_user_model,
        login,
        logout,)
from django.shortcuts import render, redirect, get_object_or_404
from .forms import UserLoginForm, UserRegisterForm, PerfilForm
from django.contrib.auth.decorators import login_required
from .models import *

def login_view(request):
       print(request.user.is_authenticated())
       next = request.GET.get('next')
       title = "Ingresar al Sistema"
       title_1 = "Entrar"
       form = UserLoginForm(request.POST or None)

       if form.is_valid():
           username = form.cleaned_data.get("username")
           password = form.cleaned_data.get('password')
           user = authenticate(username=username, password=password)
           login(request, user)

           if next:
              return redirect(next)
           return redirect("/")

       return render(request, "form.html", {"form":form, "title": title, "title_1": title_1})


def register_view(request):
    print(request.user.is_authenticated())
    next = request.GET.get('next')
    title = "Registro"
    title_1 = "Registrar"
    form = UserRegisterForm(request.POST or None)
    if form.is_valid():
        user = form.save(commit=False)
        password = form.cleaned_data.get('password')
        user.set_password(password)
        user.save()
        new_user = authenticate(username=user.username, password=password)
        login(request, new_user)
        if next:
            return redirect(next)
        return redirect("/")

    context = {
        "form": form,
        "title": title,
        "title_1": title_1
    }
    return render(request, "form.html", context)


def logout_view(request):
    logout(request)
    return redirect("/")

def perfil_view(request):
    print(request.user.is_authenticated())
    next = request.GET.get('next')
    title = "Perfil"
    title_1 = "Guardar"
    perfil = get_object_or_404(Perfil, pk="1")
    form = PerfilForm(request.POST or None)
    if form.is_valid():
        perfil = form.save(commit=False)

        perfil.save()


    return render(request, "perfil.html", {"perfil": perfil,"form":form, "title": title, "title_1": title_1})















    
# @login_required
# def editar_usuario(request):
#     if request.method == 'POST':
#         user_form = UserEditForm(instance=request.user,data=request.POST)
#         perfil_form = PerfilForm(instance=request.user.perfil,
#                        data=request.POST,
#         )
#         if user_form.is_valid() and profile_form.is_valid():
#             user_form.save()
#             profile_form.save()
#             messages.success(request, 'Profile updated successfully')
#     else:
#         messages.success(request, 'Error updating your profile')
#         user_form = UserEditForm(instance=request.user)
#         perfil_form = PerfilForm(
#         instance=request.user.profile)
#     return render(request,
#                   'editar_perfil.html',
#                   {'user_form': user_form,
# 'perfil_form': perfil_form})

# @login_required(login_url='/login/')
# def perfil(request):
#   return render(request, "perfil.html", {"perfil": perfil}) 