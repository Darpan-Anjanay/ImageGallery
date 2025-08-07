import json
from django.shortcuts import render,redirect,HttpResponse
from .models import Album,Profile,Image
from django.contrib.auth.models import User
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404
from django.contrib.auth import login,logout,authenticate
from django.contrib import messages

# Login
def Login(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username,password=password)
        if user is not None:
            login(request,user)
            return redirect('Home')
        else:
            messages.warning(request,'Invalid credentials')
            return redirect('Login')
    return render(request,'image/Login.html')

# Regsiter
def Register(request):
    if request.method == "POST":
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        confirmpassword = request.POST.get('confirmpassword')
        
        if password != confirmpassword:
            messages.error(request, "Passwords do not match.")
            return render(request, 'image/Register.html')

        if User.objects.filter(username=username).exists():
            messages.error(request, "User already exists.")
            return render(request, 'image/Register.html')

        user = User.objects.create_user(username=username, password=password,email=email)
        user.save()
        
        login(request, user)
        
        return redirect('ProfileUpdate')
    
    return render(request, 'image/Register.html')  


 # Logout
@login_required(login_url='Login')
def Logout(request):
    logout(request)
    return redirect('Login')


# Profile Update
@login_required(login_url='Login')
def ProfileUpdate(request):
    user = request.user
    Profileobj = Profile.objects.filter(User=user).first()
    if request.method == "POST":
        ProfileImg = request.FILES.get('Image')
        if Profileobj is not None:
            Profileobj.ProfileImgName = ProfileImg
            Profileobj.save()
        else:
            Profileobj = Profile.objects.create(User=user,ProfileImgName=ProfileImg)
        return redirect('Home')
    context = {'Profileobj':Profileobj}
    return render(request,'image/Profile.html',context)


# Home
@login_required(login_url='Login')
def Home(request):
    user = request.user

    Albums = Album.objects.filter(User=user)
    Images = Image.objects.filter(SoftDelete=False,Trash=False,User=user)
    
    context = {'user':user,'Albums':Albums,'Images':Images}
    return render(request,'image/Home.html',context)


# Image  View
@login_required(login_url='Login')
def ImageView(request):
    user = request.user
   
    aid = request.GET.get('aid')
    image_id_str = request.GET.get('i')

    if aid is not None:
        images = Image.objects.filter(SoftDelete=False, Trash=False, User=user, Album_id=aid).order_by('id')
    else:
        images = Image.objects.filter(SoftDelete=False, Trash=False, User=user).order_by('id')

    image_list = list(images.values_list('id', flat=True))

    current_image = None
    previous_image = None
    next_image = None

    try:
        if image_id_str:
            image_id = int(image_id_str)
            current_image = images.get(id=image_id)
            try:
                current_index = image_list.index(image_id)
                if current_index > 0:
                    previous_image = Image.objects.get(id=image_list[current_index - 1])
                if current_index < len(image_list) - 1:
                    next_image = Image.objects.get(id=image_list[current_index + 1])
            except ValueError:
                if image_list:
                    current_image = images.first()
                    if len(image_list) > 1:
                        next_image = Image.objects.get(id=image_list[1])
        else:
            if images.exists():
                current_image = images.first()
                if len(image_list) > 1:
                    next_image = Image.objects.get(id=image_list[1])

    except Image.DoesNotExist:
        pass

    context = {
        'user': user,
     
        'current_image': current_image,
        'previous_image': previous_image,
        'next_image': next_image,
        'aid': aid
    }
    return render(request, 'image/ImageView.html', context)




# Album View
@login_required(login_url='Login')
def AlbumView(request):
    user = request.user
  
    
    aid  = request.GET.get('aid')
    album = Album.objects.filter(User=user,id=aid).first()
    Albums = Album.objects.filter(User=user).exclude(id=aid)
    
    Images = Image.objects.filter(SoftDelete=False,Trash=False,User=user,Album=album)

    context = {'user':user,'album':album,'Images':Images,'Albums':Albums,'aid':aid}
    return render(request,'image/AlbumView.html',context)

# Add Album
@login_required(login_url='Login')
def AddAlbum(request):
    user = request.user
   
    if request.method == "POST":
        AlbumName = request.POST['AlbumName']
       
        newAlbum = Album.objects.create(User=user,AlbumName = AlbumName)
        return redirect('Home')

    context = {'user':user}
    return render(request,'image/AddAlbum.html',context)



# Delete Album
@login_required(login_url='Login')
def DeleteAlbum(request):
    user = request.user
    id  = request.GET.get('id')
    album = Album.objects.filter(User=user,id=id)
    if album.exists():
        album.first().delete()
        return redirect('Home')




# Upload
@login_required(login_url='Login')
def Upload(request):
    user = request.user
   
    Albums = Album.objects.filter(User=user)
    aid  = request.GET.get('aid')

    if request.method == "POST":
        Album_id = request.POST.get('Album_id') or aid
        Imagefile = request.FILES.get('Image')

        newimage = Image.objects.create(User=user,Album_id=Album_id,Image=Imagefile)
        if aid is not None:
           return redirect(reverse('AlbumView') + f'?aid={aid}')
        else:
            return redirect('Home')

    context = {'user':user,'Albums':Albums,'aid':int(aid) if aid  is not None else None}    
    return render(request,'image/Upload.html',context)

# Image Delete 
@login_required(login_url='Login')
def ImgDel(request):
    Imid =  request.GET.get('Imid')
    aid =  request.GET.get('aid')

    if Imid is not None:
        img = Image.objects.filter(SoftDelete=False,Trash=False,id=Imid).first()
        img.Trash = True
        img.save()
        if aid is not None:
           return redirect(reverse('ImageView') + f'?aid={aid}')
        else:
            return redirect('ImageView')

# Bulk Action
@login_required(login_url='Login')
def BulkAction(request):
         
    if request.method == "POST":
        Imgidlist_json = request.POST.get('Imgidlist', '[]')
        Action = request.POST.get('Action')
        Page = request.POST.get('Page')
        aid = request.POST.get('aid')
  
        
        try:
            Imgidlist = json.loads(Imgidlist_json)
        except json.JSONDecodeError:
            Imgidlist = []
        if Imgidlist: 
            if Action == 'Trash':
                for id in Imgidlist:
                    try:
                        img = Image.objects.get(id=int(id)) 
                        img.Trash = True
                        img.save()
                    except Image.DoesNotExist:
                        print(f"Image with id {id} does not exist.")
                    except Exception as e:
                        print(f"Error processing image ID {id}: {e}")
            if Action == 'Restore':
                for id in Imgidlist:
                    try:
                        img = Image.objects.get(id=int(id)) 
                        img.Trash = False
                        img.save()
                    except Image.DoesNotExist:
                        print(f"Image with id {id} does not exist.")
                    except Exception as e:
                        print(f"Error processing image ID {id}: {e}")

            if Action == 'Delete':
                for id in Imgidlist:
                    try:
                        img = Image.objects.get(id=int(id)) 
                        img.SoftDelete = True
                        img.save()
                    except Image.DoesNotExist:
                        print(f"Image with id {id} does not exist.")
                    except Exception as e:
                        print(f"Error processing image ID {id}: {e}")
            
            if  Action.startswith('M'):
                AlbumID = Action.split('-')[1]
                Albumboj =  Album.objects.filter(id=AlbumID).first()
                for Imid in Imgidlist:
                    imgobj = Image.objects.filter(SoftDelete=False,Trash=False,id=Imid).first()
                    imgobj.Album = Albumboj
                    imgobj.save()

        if aid is not None:
            return redirect(reverse(Page)+f'?aid={aid}')
        else:
            return redirect(Page)



# Trash
@login_required(login_url='Login')
def Trash(request):
    user = request.user
   
    Images = Image.objects.filter(SoftDelete=False,Trash=True,User=user)
    context = {'user':user,'Images':Images}
    return render(request,'image/Trash.html',context)


# Trash Image 
@login_required(login_url='Login')
def TrashImageView(request):
    user = request.user
   
    Images = Image.objects.filter(SoftDelete=False,Trash=True,User=user)
    image_id_str = request.GET.get('i')
    
    image_list = list(Images.values_list('id', flat=True))

    current_image = None
    previous_image = None
    next_image = None

    try:
        if image_id_str:
            image_id = int(image_id_str)
            current_image = Images.get(id=image_id)
            try:
                current_index = image_list.index(image_id)
                if current_index > 0:
                    previous_image = Image.objects.get(id=image_list[current_index-1])
                if current_index < len(image_list)-1:
                    next_image = Image.objects.get(id=image_list[current_index+1])
                    
            except ValueError:
                 if image_list:
                    current_image = Images.first()
                    if len(image_list) > 1:
                        next_image = Image.objects.get(id=image_list[1])
        else:
            if Images.exists():
                current_image = Images.first()
                if len(image_list) > 1:
                    next_image = Image.objects.get(id=image_list[1])
    except Image.DoesNotExist:
        pass
    
    context = {
        'user': user,
   
        'current_image': current_image,
        'previous_image': previous_image,
        'next_image': next_image,
    
    }
    return render(request,'image/TrashImageView.html',context)

# Trash Delete
@login_required(login_url='Login')
def TrashDel(request):
    Imid =  request.GET.get('Imid')
    aid =  request.GET.get('aid')

    if Imid is not None:
        img = Image.objects.filter(SoftDelete=False,Trash=True,id=Imid).first()
        img.SoftDelete = True
        img.save()
        return redirect('TrashImageView')






 