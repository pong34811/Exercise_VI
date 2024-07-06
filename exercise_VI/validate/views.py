from django.shortcuts import render
from django.contrib import messages
from validate.models import Animal_list

# Create your views here.

def Animepage (request):
    if request.method == 'POST':
        anime_order = request.POST['anime_order']
        anime_name_th = request.POST['anime_name_th']
        anime_name_en = request.POST['anime_name_en']
        anime_seasons = request.POST['anime_seasons']
        anime_channel = request.POST['anime_channel']
        print (anime_order,anime_name_th, anime_name_en, anime_seasons, anime_channel)    

        animal = Animal_list.objects.create(
            anime_order = anime_order,
            anime_name_th = anime_name_th,
            anime_name_en = anime_name_en,
            anime_seasons = anime_seasons,
            anime_channel = anime_channel,
           
           
        )
        animal.save()
        messages.success(request, "Successfully")
        return render(request, 'add.html')

    else:
        return render(request, 'add.html')
