from django.db.models.functions import Lower
from django.shortcuts import render
from .models import District,Division
# Create your views here.


def division (request):
    div=Division.objects.all()
    contex ={'div': div}
    return render(request, 'division.html',contex)


def district(request, name):
    dis = District.objects.filter(div__name=name, population__gt=9999).order_by('-population')
    context = {'dis': dis, 'divname' :name}
    return render(request, 'district.html', context)


def allDis(request , name):
    all=District.objects.filter(div__name=name)
    contex={'all': all}
    return render(request, 'all_dis.html' ,contex )


def formpage (request):
    name = request.GET.get('firstname')
    if name:
        dis = District.objects.filter(div__name__iexact=name) #iexact ba contains likhlei hobe. iexact e puro word likhte hobe
    else:
        dis=None
    context = {
        'name': name,
        'dis': dis
    }
    return render(request, 'form.html', context)

