from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth import login, authenticate 
from django.contrib.auth.decorators import login_required,permission_required 
from .forms import *
from django.http import HttpResponse
from .decorators import allowed_users
from .models import Videogame, Package, Dlc
from django.contrib.auth.models import Group
from django.contrib import messages
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from cart.cart import Cart
from order.models import Order
from django.core.mail import send_mail

from django.template.loader import render_to_string
from django.utils.html import strip_tags



@login_required
def store(request):
	return render(request,'main_menu/store.html')



class DlcList_view(ListView):
	model = Dlc
	template_name = "list_dlc.html"
	context_object_name = "DLC"



class DlcDetail_view(DetailView):
    model = Dlc
    template_name= "detail_dlc.html"
    context_object_name= "DLC"

class DlcDelete_view(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model= Dlc
    success_url= "/"
    template_name= "delete_dlc.html"
    context_object_name= "DLC"
    def test_func(self):
        objeto = self.get_object()
        if self.request.user == objeto.administrator:
            return True
        return False



class DlcCreate_view(LoginRequiredMixin, CreateView):
    model= Dlc
    template_name= "create_dlc.html"
    context_object_name= "DLC"
    fields= ["dlc_name", "unit_price", "administrator", "videogame", "Release_date", "photo"]
    def form_valid(self, form):
        form.instance.administrator = self.request.user
        return super().form_valid(form)


class DlcUpdate_view(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model= Dlc
    template_name= "create_dlc.html"
    context_object_name= "DLC"
    fields= ["dlc_name", "unit_price", "administrator", "videogame", "Release_date", "photo"]
    def form_valid(self, form):
        form.instance.administrator = self.request.user
        return super().form_valid(form)
    def test_func(self):
        objeto = self.get_object()
        if self.request.user == objeto.administrator:
            return True
        return False

class PackageList_view(ListView):
    model = Package
    template_name= "list_pck.html"
    context_object_name= "PCK"

class PackageDetail_view(DetailView):
    model = Package
    template_name= "detail_pck.html"
    context_object_name= "PCK"


class PackageDelete_view(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model= Package
    success_url= "/"
    template_name= "delete_pck.html"
    context_object_name= "PCK"
    def test_func(self):
        objeto = self.get_object()
        if self.request.user == objeto.administrator:
            return True
        return False

class PackageCreate_view(LoginRequiredMixin, CreateView):
    model= Package
    template_name= "create_pck.html"
    context_object_name= "PCK"
    fields= ["package_name", "unit_price", "administrator", "videogames", "photo"]
    def form_valid(self, form):
        form.instance.administrator = self.request.user
        return super().form_valid(form)

class PackageUpdate_view(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model= Package
    template_name= "create_pck.html"
    context_object_name= "PCK"
    fields= ["package_name", "unit_price", "administrator", "videogames", "photo"]
    def form_valid(self, form):
        form.instance.administrator = self.request.user
        return super().form_valid(form)
    def test_func(self):
        objeto = self.get_object()
        if self.request.user == objeto.administrator:
            return True
        return False

class VideogameList_view(ListView):
    model = Videogame
    template_name= "list_vg.html"
    context_object_name= "VG"

class VideogameDetail_view(DetailView):
    model = Videogame
    template_name= "detail_vg.html"
    context_object_name= "VG"

class VideogameCreate_view(LoginRequiredMixin, CreateView):
    model= Videogame
    template_name= "create_vg.html"
    context_object_name= "VG"
    fields= ["videogame_name", "rating", "release_date", "engine", "production_cost", "unit_price", "genre", "formats", "language", "platform", "photo"]
    def form_valid(self, form):
        form.instance.administrator = self.request.user
        return super().form_valid(form)

class VideogameDelete_view(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model= Videogame
    success_url= "/"
    template_name= "delete_vg.html"
    context_object_name= "VG"
    def test_func(self):
        objeto = self.get_object()
        if self.request.user == objeto.administrator:
            return True
        return False

class VideogameUpdate_view(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model= Videogame
    template_name= "create_vg.html"
    context_object_name= "VG"
    fields= ["videogame_name", "rating", "release_date", "engine", "production_cost", "unit_price", "genre", "formats", "language", "platform", "photo"]
    def form_valid(self, form):
        form.instance.administrator = self.request.user
        return super().form_valid(form)
    def test_func(self):
        objeto = self.get_object()
        if self.request.user == objeto.administrator:
            return True
        return False
    


class DeliveryList_view(UserPassesTestMixin, ListView):
    model= Order
    template_name= "list_od.html"
    context_object_name= "OD"
    def test_func(self):
        return self.request.user.groups.filter(name='Dispatcher').exists()


class DeliveryDetail_view(UserPassesTestMixin, DetailView):
    model= Order
    template_name= "detail_od.html"
    context_object_name= "OD"
    def test_func(self):
        return self.request.user.groups.filter(name='Dispatcher').exists()






class DeliveryConfirm_view(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model= Order
    success_url= "/delivery/list_orders/" 
    template_name= "confirm_od.html"
    context_object_name= "OD"
    def test_func(self):
        objeto = self.get_object()
        if self.request.user == objeto.dispatcher.user:
            return True
        return False





def main_menu(request):
	return render(request,'main_menu.html')
def register_store(request):
    if request.method== 'POST':
        user_form= UserRegistrationForm(data= request.POST)
        store_form= UserRegistrationFormStore(data= request.POST, files=request.FILES)
        if user_form.is_valid() and store_form.is_valid():
            user=user_form.save(commit= False)
            store=store_form.save(commit= False)
            store.user= user
            user.save()
            store_form.save(commit=True)
            username=user_form.cleaned_data.get('username')
            password=user_form.cleaned_data.get('password1')
            user=authenticate(username=username, password= password)
            group=Group.objects.get(name='Store')
            user.groups.add(group)
            login(request, user) 
            return render(request, 'register_done.html', {'user': user})
            
    else:
        user_form= UserRegistrationForm()
        store_form= UserRegistrationFormStore()
    return render(request, 'register_store.html', {'user_form': user_form, 'store_form': store_form})

@login_required
@allowed_users(allowed_roles= ['Admin'])
def register_dispatcher(request):
    if request.method== 'POST':
        user_form= UserRegistrationForm2(data= request.POST)
        dispatcher_form= UserRegistrationFormDispatcher(data= request.POST, files=request.FILES)
        if user_form.is_valid() and dispatcher_form.is_valid():
            user=user_form.save()
            dispatcher=dispatcher_form.save(commit= False)
            dispatcher.user= user
            dispatcher.save()
            username=user_form.cleaned_data.get('username')
            password=user_form.cleaned_data.get('password1')
            user=authenticate(username=username, password= password)
            group=Group.objects.get(name='Dispatcher')
            user.groups.add(group) 
            return render(request, 'register_done.html', {'user': user})
        
    else:
        user_form= UserRegistrationForm2()
        dispatcher_form= UserRegistrationFormDispatcher()
    return render(request, 'register2.html', {'user_form': user_form, 'dispatcher_form': dispatcher_form})

@login_required
@allowed_users(allowed_roles= ['Admin'])
def register_admin(request):
    if request.method== 'POST':
        user_form= UserRegistrationForm3(request.POST)
        if user_form.is_valid():
            user=user_form.save()
            username=user_form.cleaned_data.get('username')
            password=user_form.cleaned_data.get('password1')
            user=authenticate(username=username, password= password)
            group=Group.objects.get(name='Admin')
            user.groups.add(group)
            login(request, user) 
            return render(request, 'register_done.html', {'user': user})
        
    else:
        user_form= UserRegistrationForm3()
    return render(request, 'register3.html', {'user_form': user_form})

@login_required
@allowed_users(allowed_roles= ['Store'])
def edit_store(request):
    if request.method== 'POST':
        user_form= StoreEditForm(instance= request.user, data= request.POST)
        store_form=StoreEditForm2(instance= request.user.store, data= request.POST, files= request.FILES)
        if user_form.is_valid() and store_form.is_valid():
            user_form.save()
            store_form.save()
            messages.success(request, 'Profile updated successfully')
        else:
            messages.error(request, 'Error updating your profile')
    else:
        user_form= StoreEditForm(instance= request.user)
        store_form= StoreEditForm2(instance= request.user.store)
    return render(request, 'edit_store.html', {'user_form': user_form, 'store_form': store_form})

@login_required
@allowed_users(allowed_roles= ['Dispatcher'])
def edit_dispatcher(request):
    if request.method== 'POST':
        user_form= DispatcherEditForm(instance= request.user, data= request.POST)
        dispatcher_form=DispatcherEditForm2(instance= request.user.dispatcher, data= request.POST, files= request.FILES)
        if user_form.is_valid() and dispatcher_form.is_valid():
            user_form.save()
            dispatcher_form.save()
            messages.success(request, 'Profile updated successfully')
        else:
            messages.error(request, 'Error updating your profile')
    else:
        user_form= StoreEditForm(instance= request.user)
        dispatcher_form= DispatcherEditForm2(instance= request.user.dispatcher)
    return render(request, 'edit_dispatcher.html', {'user_form': user_form, 'dispatcher_form': dispatcher_form})

@login_required
@allowed_users(allowed_roles= ['Admin'])
def edit_admin(request):
    if request.method== 'POST':
        user_form= AdminEditForm(instance= request.user, data= request.POST)
        if user_form.is_valid():
            user_form.save()
            messages.success(request, 'Profile updated successfully')
        else:
            messages.error(request, 'Error updating your profile')
    else:
        user_form= AdminEditForm(instance= request.user)
    return render(request, 'edit_admin.html', {'user_form': user_form})

#@allowed_users(allowed_roles= ['Store'])
@login_required
def list_videogame(request):
	cart = Cart(request)
	videogames = Videogame.objects.all()
	return render(request, "list_videogame.html", {"videogames":videogames})

#@allowed_users(allowed_roles= ['Store'])
@login_required
def list_dlc_dic(request):
	cart = Cart(request)
	dlcs = Dlc.objects.all()
	return render(request, "list_dlc_dic.html", {"dlcs":dlcs})

#@allowed_users(allowed_roles= ['Store'])
@login_required
def list_package(request):
	cart = Cart(request)
	packages = Package.objects.all()
	return render(request, "list_package.html", {"packages":packages})





















