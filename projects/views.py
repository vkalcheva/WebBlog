from django.shortcuts import render

from projects.forms import ProjectForm
from projects.models import Project


def projects(requests):
    projects = Project.objects.all()
    context = {
        'projects': projects
    }
    return render(requests, "projects/projects.html", context)


def project(requests, pk):
    project_obj = Project.objects.get(id=pk)
    context = {
        'project': project
    }
    return render(requests, "projects/single_project.html", context)


def create_project(requests):
    form = ProjectForm()
    context = {
        'form': form
    }
    return render(requests, "projects/project_form.html", context)
