from django.shortcuts import render



def HomePage(request):
    return render(request,"home.html")


def StudentReg(request):
    return render(request,"StudentReg.html")


def registration(request):
    r=request.POST["s1"]
    n = request.POST["s1"]
    fn = request.POST["s1"]
    c = request.POST["s1"]
    d = request.POST["s1"]
    e = request.POST["s1"]
    p = request.POST["s1"]

    return None