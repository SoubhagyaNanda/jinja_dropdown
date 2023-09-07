from django.shortcuts import render
from app.models import *
from django.http import *
# Create your views here.


def insert_webpage(request):
    LTO = Topic.objects.all()
    d= {'LTO':LTO}

    if request.method=='POST':
        tn= request.POST['tn']
        na= request.POST['nm']
        ur= request.POST['ur']
        
        TO= Topic.objects.get(topic_name=tn)
        WO = Webpage.objects.get_or_create(topic_name=TO,name=na,url=ur)[0]
        WO.save()

        QSWO= Webpage.objects.all()
        d1= {'QSWO':QSWO}
        return render(request,'display_webpage.html',context= d1)
    return render(request,'insert_web.html',context= d)

def insert_access(request):
    LWO= Webpage.objects.all()
    d={'LWO':LWO}

    if request.method=='POST':
        nme= request.POST['nm']
        at = request.POST['aut']
        dte= request.POST['dt']

        WO= Webpage.objects.get(name=nme)
        ace= AccessRecord.objects.get_or_create(name=WO, author= at, date= dte)[0]
        ace.save()

        QSAR= AccessRecord.objects.all()
        d1 = {'QSAR':QSAR}
        return render(request,'display_acce.html',context=d1)
    return render(request,'insert_acce.html',context=d)


def select_tag(request):
    LTO= Topic.objects.all()
    d={'LTO':LTO}
    if request.method=='POST':

        tolist= request.POST.getlist('tn')
        print(tolist)

        QSWO = Webpage.objects.none()

        for tn in tolist:
            QSWO= QSWO|Webpage.objects.filter(topic_name='tn')
        
        d1 = {'QSWO':QSWO}
        return render(request,'display_webpage.html',d1)        
    return render(request,'select.html',d)

def checkbox_c(request):
    LTO=Topic.objects.all()
    d={'LTO':LTO}
    
    return render(request,'checkbox.html',d)