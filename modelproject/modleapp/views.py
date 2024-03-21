from django.shortcuts import render
from .forms import StudentForm
# Create your views here.
def home(request):
    if request.method=='GET':
        student=StudentForm()
        return render(request,'index.html',{'student':student})
    else:
        student=StudentForm(request.POST)
        if student.is_valid():
            student.save()
            return render(request,'index.html',{'student':student})    