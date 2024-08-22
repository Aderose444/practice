from django.shortcuts import render
def home(request):
    context = {
        'first name' : 'Adebusola'
    }
    return render(request, 'member.html', context) 