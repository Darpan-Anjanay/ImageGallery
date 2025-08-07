from django.urls import path
from .views import Home,ImageView,AlbumView,AddAlbum,Upload,ImgDel,Trash,TrashImageView,TrashDel,BulkAction,Login,Logout,ProfileUpdate,Register,DeleteAlbum
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('',Home,name='Home'),


    path('Login/',Login,name='Login'),
    path('Register/',Register,name='Register'),
    path('Logout/',Logout,name='Logout'),
    path('ProfileUpdate/',ProfileUpdate,name='ProfileUpdate'),
    
    path('Upload/',Upload,name='Upload'),
    
    path('ImageView/',ImageView,name='ImageView'),
    path('ImgDel/',ImgDel,name='ImgDel'),
    
    path('AddAlbum/',AddAlbum,name='AddAlbum'),
    path('AlbumView/',AlbumView,name='AlbumView'),
    path('DeleteAlbum/',DeleteAlbum,name='DeleteAlbum'),

    
    path('Trash/',Trash,name='Trash'),
    path('TrashImageView/',TrashImageView,name='TrashImageView'),
    path('TrashDel/',TrashDel,name='TrashDel'),
    
    path('BulkAction/',BulkAction,name='BulkAction'),

     # Password 
    path('password_reset/', auth_views.PasswordResetView.as_view(
        template_name='Password/password_reset_form.html'
    ), name='password_reset'),

    path('password_reset/done/', auth_views.PasswordResetDoneView.as_view(
        template_name='Password/password_reset_done.html'
    ), name='password_reset_done'),

    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(
        template_name='Password/password_reset_confirm.html'
    ), name='password_reset_confirm'),

    path('reset/done/', auth_views.PasswordResetCompleteView.as_view(
        template_name='Password/password_reset_complete.html'
    ), name='password_reset_complete'),

    path('password_change/', auth_views.PasswordChangeView.as_view(
        template_name='Password/password_change_form.html'
    ), name='password_change'),

    path('password_change/done/', auth_views.PasswordChangeDoneView.as_view(
        template_name='Password/password_change_done.html'
    ), name='password_change_done'),



]
