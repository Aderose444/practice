from django.shortcuts import render

# Create your views here.
def team(request):
    return render(request,'team.html')

def member(request):
    return render(request,'member.html')