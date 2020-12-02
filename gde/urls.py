from django.urls import path, include
from django.contrib.auth import views as auth_views
from . import views
from .views import *
from .decorators import allowed_users
from django.contrib.auth.decorators import login_required
#app_name = 'gde'

urlpatterns = [

	path('password_change/', auth_views.PasswordChangeView.as_view(), name= 'password_change'),
	path('password_change/done/', auth_views.PasswordChangeDoneView.as_view(), name= 'password_change_done'),
	path('password_reset/',auth_views.PasswordResetView.as_view(), name='password_reset'),
	path('password_reset/done/', auth_views.PasswordResetDoneView.as_view(), name='password_reset_done'),
	path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(), name='password_reset_confirm'),
	path('reset/done/', auth_views.PasswordResetCompleteView.as_view(), name='password_reset_complete'),

	path('videogames/', login_required(VideogameList_view.as_view()), name="videogames"),
	path('packages/', PackageList_view.as_view(), name="packages"),	
	path('dlcs/', DlcList_view.as_view(), name="dlcs"),

	path('videogames/<str:pk>/', VideogameDetail_view.as_view(), name="videogame_detail"),
	path('packages/<str:pk>/', PackageDetail_view.as_view(), name="package_detail"),
	path('dlcs/<str:pk>/', DlcDetail_view.as_view(), name="dlc_detail"),

	path('videogames/<str:pk>/delete/', VideogameDelete_view.as_view(), name="videogame_delete"),
	path('packages/<str:pk>/delete/', PackageDelete_view.as_view(), name="package_delete"),
	path('dlcs/<str:pk>/delete/', DlcDelete_view.as_view(), name="dlc_delete"),

	path('videogames/<str:pk>/update/', VideogameUpdate_view.as_view(), name="videogame_update"),
	path('packages/<str:pk>/update/', PackageUpdate_view.as_view(), name="package_update"),
	path('dlcs/<str:pk>/update/', DlcUpdate_view.as_view(), name="dlc_update"),

	path('videogame/new/', VideogameCreate_view.as_view(), name= "videogame_create"),
	path('package/new/', PackageCreate_view.as_view(), name= "package_create"),
	path('dlc/new/', DlcCreate_view.as_view(), name= "dlc_create"),

	path('',views.main_menu, name="main_menu"),
	path('store/', views.store, name='store'),
	path('store/videogame/', list_videogame , name= "list_videogame"),
	path('store/dlc/', list_dlc_dic , name= "list_dlc_dic"),
	path('store/package/', list_package , name= "list_package"),


	path('login/', auth_views.LoginView.as_view(), name='login'),
	path('logout/', auth_views.LogoutView.as_view(), name='logout'),

	path('', include('django.contrib.auth.urls')),
	
	path('register_store/', views.register_store, name= 'register_store'),
	path('register_dispatcher/', views.register_dispatcher, name='register2'),
	path('register_admin/', views.register_admin, name= 'register_admin'),
	
	path('edit_admin/', views.edit_admin, name= 'edit_admin'),	
	path('edit_store/', views.edit_store, name= 'edit_store'),
	path('edit_dispatcher/', views.edit_dispatcher, name= 'edit_store'),

	path('delivery/list_orders/', DeliveryList_view.as_view(), name= 'list_orders'),
	path('delivery/list_orders/<str:pk>/', DeliveryDetail_view.as_view(), name="detail_order"),
	path('delivery/list_orders/<str:pk>/confirm', DeliveryConfirm_view.as_view(), name="confirm_order"),
	]