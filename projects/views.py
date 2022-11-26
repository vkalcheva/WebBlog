from django.shortcuts import render, redirect

from projects.forms import ProjectForm
from projects.models import Project


def projects(request):
    projects = Project.objects.all()
    context = {
        'projects': projects
    }
    return render(request, "projects/projects.html", context)


def project(request, pk):
    project_obj = Project.objects.get(id=pk)
    tags = project_obj.tags.all()
    context = {
        'project': project_obj,
        'tags': tags
    }
    return render(request, "projects/single_project.html", context)


def create_project(request):
    form = ProjectForm()

    if request.method == 'POST':
        form =ProjectForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('projects')

    context = {
        'form': form
    }
    return render(request, "projects/project_form.html", context)
