from django.contrib import admin
from .models import Profile,Album,Image
from django.utils.html import format_html

class ProfileAdmin(admin.ModelAdmin):
    list_display = ['ProfileImgTag','User']
    def ProfileImgTag(self,obj):
        if obj.ProfileImgName:
            return format_html(f'<img src={obj.ProfileImgName.url} style="max-height: 100px; max-width: 100px;">')
        else:
            return 'Not Present'
admin.site.register(Profile,ProfileAdmin)


class AlbumAdmin(admin.ModelAdmin):
    list_display = ['User','AlbumName']

admin.site.register(Album,AlbumAdmin)


class ImageAdmin(admin.ModelAdmin):
    list_display = [
    'User','ImgTag','Album','Created_at','Modified_at','SoftDelete','Trash']
    list_editable = ['SoftDelete','Trash']
    list_filter =['SoftDelete','Trash','Album']
    def ImgTag(self,obj):
        if obj.Image:
            return format_html(f'<img src={obj.Image.url} style="max-height: 100px; max-width: 100px;">')
        else:
            return 'Not Present'
admin.site.register(Image,ImageAdmin)
