from django.shortcuts import render


def contactPage(request):
    return render(request, 'blogapp/contactPage.html', {'title': 'Contact'})
