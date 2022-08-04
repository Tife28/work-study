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
    # if request.method == "POST":  
    #     print(dict(form.errors))
    #     form = RecommendationForm(request.POST)
    #     print(dict(form.errors))
    #     if form.is_valid():  
    #         try:  
    #             form.save() 
    #             return HttpResponse("<h3>Application successfully submitted!</h3><br><center><a href='/show' class='btn btn-primary'>Update another Work Study Profile</a></center>")
    #         except:  
    #             pass  
    # else:  
    #     form = RecommendationForm()   
    #     print(dict(form.errors))
    return render(request,'edit.html', {'student':student})#, 'form': form })  
def update(request, id):  
    student = Student.objects.get(id=id)  
    recommendation=None
    try:
        recommendation = student.recommendation
    except:
        pass
    form = StudentForm(instance=student)
    form2 = RecommendationForm(instance= recommendation)
    
    if request.method == 'POST':
        form = StudentForm(request.POST, instance = student) 
        form2 = RecommendationForm(request.POST, request.FILES, instance=recommendation)
        print(dict(form2.errors),dict(form.errors), request.POST, request.FILES)
        if form.is_valid() and form2.is_valid():  
            recommendation_data = form2.save(commit=False)
            recommendation_data.student = student
            recommendation_data.save()  

            form.save()
            return redirect("/show")  
    return render(request, 'edit.html', {'student': student, 'form': form2, 'studentform': form}) 
def destroy(request, id):  
    student = Student.objects.get(id=id)  
    student.delete()  
    return redirect("/show")  
def trys(request):
    return render(request,"department.html") 