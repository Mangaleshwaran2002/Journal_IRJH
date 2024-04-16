from django.shortcuts import render,HttpResponse,redirect
from django.contrib.auth.decorators import login_required
from app_auth.models import Role
from manuscript.models import Manuscript
# Create your views here.
@login_required
def editor_dashboard(request):
    if request.user.role == Role.EDITOR:
        manuscript=Manuscript.objects.filter(verified=False,under_review=True).all()
        return render(request,'editordashbord.html',context={
            "manuscript":manuscript
        })
    
    return HttpResponse("you are not a editor")


@login_required
def accept_manuscript(request,id):
    if request.user.role == Role.EDITOR:
        print("manuscript id:",id)
        manuscript=Manuscript.objects.filter(id=id).get()
        manuscript.verified=True
        manuscript.under_review=True
        manuscript.save()
        return redirect('editor_dashboard')
    
    return HttpResponse("you are not a editor")


@login_required
def reject_manuscript(request,id):
    if request.user.role == Role.EDITOR:
        print("manuscript id:",id)
        manuscript=Manuscript.objects.filter(id=id).get()
        manuscript.verified=False
        manuscript.under_review=False
        manuscript.save()
        return redirect('editor_dashboard')
    
    return HttpResponse("you are not a editor")