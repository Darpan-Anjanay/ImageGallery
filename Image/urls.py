from django.urls import path
from .views import Home,ImageView,AlbumView,AddAlbum,Upload,ImgDel,Trash,TrashImageView,TrashDel,BulkAction,Login,Logout,ProfileUpdate,Register,DeleteAlbum
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



]
