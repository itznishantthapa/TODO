from django.shortcuts import render,redirect
from .models import Note

# Create your views here.
def todo_list(request):
    note=Note.objects.all()
    return render(request, 'todo_list.html',{'note':note})

def add_note(request):
    if request.method == 'POST':
        heading=request.POST['heading']
        description=request.POST['description']
        # note=Note(heading=heading,description=description)
        Note.objects.create(heading=heading,description=description)
        print("Added Successfully")
        return redirect('todo_list')
    return render(request,'todo_add.html')

def delete(request,pk):
    note=Note.objects.get(id=pk)
    note.delete()
    return redirect('todo_list')


def edit(request,pk):
    note=Note.objects.get(id=pk)
    if request.method=='POST':
        note.heading=request.POST['heading']
        note.description=request.POST['description']
        note.save()
        return redirect('todo_list')
    return render(request,'edit.html',{'note':note})
