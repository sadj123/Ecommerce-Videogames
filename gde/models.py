from django.db import models

from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse
# Create your models here.
class PackagesManager(models.Manager):
	def get_queryset(self):
		return super(PackagesManager, self).get_queryset()
class RandomManager(models.Manager): 
    def get_query_set(self): 
     return super(RandomManager, self).get_queryset()


class GamesManager(models.Manager):
	def get_queryset(self):
		return super(GamesManager,self).get_queryset()
class DlcManager(models.Manager):
	def get_queryset(self):
		return super(DlcManager,self).get_queryset()
class Category(models.Model):
	category_name= models.CharField(max_length= 20, blank= False, unique= True)
	def __str__(self):
	    return self.category_name

class Language(models.Model):
    language= models.CharField(max_length= 50, unique= True)
    def __str__(self):
        return self.language

class Genre(models.Model):
    genre=models.CharField(max_length= 50, unique= True)
    def __str__(self):
        return self.genre


class Format(models.Model):
    formats= models.CharField(max_length= 50, unique= True)
    def __str__(self):
        return self.formats

class Platform(models.Model):
	platform= models.CharField(max_length= 50, unique= True)
	
	def __str__(self):
		return self.platform


class Videogame(models.Model):
	videogame_name= models.CharField(primary_key= True, max_length= 50)
	RATING_CHOICES=(
	('Early childhood', 'EC'), 
	('Every one','E'), ('Every one 10+', 'E10+'), ('Teen', 'T'), 
	('Mature', 'M'), ('Rating Pending', 'RP'), ('Adults', 'A')
	)
	ENGINE_CHOICES=(('Unity', 'Unity'),('Unreal', 'Unreal'), ('GameMaker', 'GameMaker'),
		('Godot', 'Godot'), ('AppGameKit', 'AppGameKit'), ('CryEngine', 'CryEngine'), 
		('Amazon lumberyard','Amazon lumberyard'), ('RPG Maker', 'RPG Maker'), 
		('Lib GDX', 'Lib GDX')
	)
	rating= models.CharField(max_length=20, choices= RATING_CHOICES, default= 'Rating Pending')
	release_date= models.DateField(blank= False)
	engine= models.CharField(max_length=50, choices= ENGINE_CHOICES, blank= False)
	production_cost= models.DecimalField(decimal_places= 2, max_digits= 18, blank= False)
	unit_price= models.DecimalField(decimal_places= 2, max_digits= 18, blank= False)
	administrator= models.ForeignKey(User, on_delete= models.PROTECT)
	category= models.ForeignKey(Category, on_delete= models.PROTECT, default= 2, editable= False)
	genre= models.ManyToManyField(Genre)
	formats= models.ManyToManyField(Format)
	platform= models.ManyToManyField(Platform)
	language= models.ManyToManyField(Language)
	photo= models.ImageField(upload_to='videogame/%Y/%m/%d/', blank= True)
	def get_absolute_url(self):
		return reverse('videogame_detail', kwargs={'pk':self.videogame_name})
	def __str__(self):
		return self.videogame_name
	objects = models.Manager()
	show = GamesManager()
	

class Dlc(models.Model):
	dlc_name= models.CharField(primary_key= True, max_length= 50)
	videogame=  models.ForeignKey(Videogame, on_delete= models.CASCADE)
	Release_date= models.DateField()
	unit_price = models.DecimalField(decimal_places=2, max_digits=18, blank= False)
	administrator = models.ForeignKey(User, on_delete=models.PROTECT)
	category = models.ForeignKey(Category, on_delete=models.PROTECT, default= 3, editable= False)
	photo= models.ImageField(upload_to='dlc/%Y/%m/%d/', blank= True)
	def get_absolute_url(self):
		return reverse('dlc_detail', kwargs={'pk':self.dlc_name})
	def __str__(self):
		return self.dlc_name
	objects = models.Manager()
	show = DlcManager()
class Package(models.Model):
	package_name= models.CharField(primary_key= True, max_length= 50)
	unit_price= models.DecimalField(decimal_places= 2, max_digits= 18, blank= False)
	administrator= models.ForeignKey(User, on_delete= models.PROTECT)
	category= models.ForeignKey(Category, on_delete= models.PROTECT, default= 1, editable= False)
	videogames= models.ManyToManyField(Videogame)
	photo= models.ImageField(upload_to='package/%Y/%m/%d/', blank= True)
	objects = models.Manager()
	show = PackagesManager()
	
	def __str__(self):
		return self.package_name
	def get_absolute_url(self):
		return reverse('package_detail', kwargs={'pk':self.package_name})
class Shopping_cart(models.Model):
    expiration_date= models.DateField()
    total= models.FloatField()
    def __str__(self):
        return 'El carro expira: {0}'.format(self.expiration_date)
class Shopping_cart_packages(models.Model):
	class Meta:
		unique_together = (('cart', 'package'),)
	cart= models.ForeignKey(Shopping_cart, on_delete= models.CASCADE)
	package=models.ForeignKey(Package, on_delete= models.PROTECT)
	units= models.IntegerField(blank= False)
	def __str__(self):
		return self.package
class Shopping_cart_videogames(models.Model):
	class Meta:
		unique_together = (('cart', 'videogame'),)
	cart= models.ForeignKey(Shopping_cart, on_delete= models.CASCADE)
	videogame=models.ForeignKey(Videogame, on_delete= models.PROTECT)
	units= models.IntegerField(blank= False)
	def __str__(self):
		return self.videogame
class Shopping_cart_dlc(models.Model):
	class Meta:
		unique_together = (('cart', 'dlc'),)
	cart= models.ForeignKey(Shopping_cart, on_delete= models.CASCADE)
	dlc=models.ForeignKey(Dlc, on_delete= models.PROTECT)
	units= models.IntegerField(blank= False)
	def __str__(self):
		return self.dlc

class Dispatcher(models.Model):
	BLOOD_CHOICES=(
		('A', 'A'), ('B', 'B'),('AB', 'AB'),('O', 'O')
	)
	RH_CHOICES=(
		('+', '+'), ('-', '-')
		)
	user= models.OneToOneField(User, primary_key= True, on_delete= models.CASCADE)
	telephone= models.CharField(blank= False, unique= True, max_length= 20)
	plate= models.CharField(blank=False, unique=True, max_length= 10)
	weight= models.DecimalField(decimal_places=2, max_digits=10, blank= False)
	height= models.DecimalField(decimal_places=2, max_digits=10, blank= False)
	blood_type= models.CharField(max_length= 20, blank= False, choices= BLOOD_CHOICES)
	rh_type= models.CharField(max_length= 20, blank= False, choices= RH_CHOICES)
	photo= models.ImageField(upload_to='users/%Y/%m/%d/', blank= True)
	def __str__(self):
		return str(self.user)
	objects = models.Manager()  
	randoms = RandomManager() 
		
class Store_location(models.Model):
	city= models.CharField(max_length= 50)
	country= models.CharField(blank= False, max_length= 50)
	state= models.CharField(max_length=20, blank= False)
	class Meta:
		unique_together = (('city', 'country'),)
	def __str__(self):
		return "{0} ({1})".format(self.city, self.country)
class Store(models.Model):
    
	user= models.OneToOneField(User, primary_key= True, on_delete= models.CASCADE)
	street_number= models.CharField(max_length= 50, blank= False)
	street_name= models.CharField(blank= False, max_length= 50)
	city= models.ForeignKey(Store_location, on_delete= models.PROTECT)
	phone = models.CharField(max_length= 20, blank= False)
	photo= models.ImageField(upload_to='users/%Y/%m/%d/', blank= True)
	def __str__(self):
		return str(self.user)
class Checkout(models.Model):
	dispatcher= models.ForeignKey(Dispatcher, on_delete= models.PROTECT)
	Delivery_date= models.DateField()
	store=models.ForeignKey(Store, on_delete= models.PROTECT)
	cart= models.OneToOneField(Shopping_cart, on_delete= models.CASCADE)
	def __str__(self):
		return "Su domiciliario es {0}".format(self.dispatcher)	

