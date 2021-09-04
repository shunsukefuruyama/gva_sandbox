from django.shortcuts import render, redirect
from upload_file.forms import FileForm
from upload_file.models import File

def index(request):

    if request.method == "POST":

        print(request.POST)
        print(request.FILES)

        file_form = FileForm(request.POST, request.FILES)

        if file_form.is_valid():
            file_form.save()
            
            return redirect('/upload_file/')

    file_form = FileForm()

    return render(request, 'upload_file/index.html', {
        'file_form': file_form,
    })