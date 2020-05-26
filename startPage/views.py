from django.shortcuts import render


def startPage(request):
    return render(request, 'blogapp/startPage.html', {'title': 'Start Page'})
