from django.shortcuts import render, redirect  
from django.http import HttpResponse
from .forms import *
from .models import *  

# Create your views here.  
def home(request):  
    if request.method == "POST":  
        form = StudentForm(request.POST)
        print(dict(form.errors))
        if form.is_valid():  
            try:  
                form.save()  
                return HttpResponse("<h3>Application successfully submitted!</h3><br><center><a href='' class='btn btn-primary'>Apply to Work Study Programme</a></center>")
            except Exception as e:  
                print(e)
    else:  
        form = StudentForm()  
    return render(request,'home.html',{'form':form})  
def show(request):  
    students = Student.objects.all()  
    return render(request,"show.html",{'students':students})  
def edit(request, id):  
    student = Student.objects.get(id=id)  
    if request.method == "POST":  
        form = RecommendationForm(request.POST)
        print(dict(form.errors))
        if form.is_valid():  
            try:  
                form.save() 
                return HttpResponse("<h3>Application successfully submitted!</h3><br><center><a href='/show' class='btn btn-primary'>Update another Work Study Profile</a></center>")
            except:  
                pass  
    else:  
        form = RecommendationForm()   
    return render(request,'edit.html', {'student':student, 'form': form })  
def update(request, id):  
    student = Student.objects.get(id=id)  
    recommendation=None
    try:
        recommendation = student.recommendation
    except:
        pass
    form2 = RecommendationForm(request.POST, instance=recommendation)
    
    if request.method == 'POST':
        form = StudentForm(request.POST, instance = student) 
        form2 = RecommendationForm(request.POST, instance=recommendation)
        if form.is_valid() and form2.is_valid():  
            recommendation_data = form.save(commit=False)
            recommendation_data.student = student
            recommendation_data.save()  

            form.save()
            return redirect("/show")  
    return render(request, 'edit.html', {'student': student}) 
def destroy(request, id):  
    student = Student.objects.get(id=id)  
    student.delete()  
    return redirect("/show")  
def trys(request):
    return render(request,"department.html") 