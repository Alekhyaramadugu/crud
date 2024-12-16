from django.shortcuts import render
from app.models import student
# Create your views here.
def index(request):
    data=student.objects.all()
    context={"data":data}
    return render(request,"index.html",context)
def insertdata(request):
    if request.method=="POST":
        name=request.POST.get('name')
        email=request.POST.get('email')
        age=request.POST.get('age')
        gender=request.POST.get('gender')
        query=student(name=name,email=email,age=age,gender=gender)
        query.save()
    return render(request,"index.html")
def updateData(request,id):
    x=student.objects.get(id=id)
    context={"x":x}

    if request.method=="POST":
        name=request.POST.get('name')
        email=request.POST.get('email') 
        age=request.POST.get('gender')  
        edit=student.object.get(id=id)
        edit.name=name
        edit.email=email
        edit.gender=gender
        edit.age=age
        query=student(name=name,email=email,age=age,gender=gender)
        query.save()     
        return redirect("/")
    return render(request,"edit.html",context)
def deleteData(request,id):
    x=student.objects.get(id=id)
    x.delete()
    return redirect("/")
    
    