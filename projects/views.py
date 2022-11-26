from django.shortcuts import render


def projects(requests):
    return render(requests, "projects/projects.html")
