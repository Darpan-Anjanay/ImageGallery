from django.urls import path
from .views import Home,ImageView,AlbumView,AddAlbum,Upload,ImgDel,Trash,TrashImageView,TrashDel,BulkAction,Login,Logout,ProfileUpdate,Register
urlpatterns = [
    path('Login/',Login,name='Login'),
    path('',Home,name='Home'),
    path('ImageView/',ImageView,name='ImageView'),
    path('AlbumView/',AlbumView,name='AlbumView'),
    path('AddAlbum/',AddAlbum,name='AddAlbum'),
    path('Upload/',Upload,name='Upload'),
    path('ImgDel/',ImgDel,name='ImgDel'),
    path('Trash/',Trash,name='Trash'),
    path('TrashImageView/',TrashImageView,name='TrashImageView'),
    path('TrashDel/',TrashDel,name='TrashDel'),
    path('BulkAction/',BulkAction,name='BulkAction'),
    path('Logout/',Logout,name='Logout'),
    path('ProfileUpdate/',ProfileUpdate,name='ProfileUpdate'),
    path('Register/',Register,name='Register'),



]
