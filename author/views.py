from django.shortcuts import render,redirect,HttpResponse
from django.contrib.auth.decorators import login_required
from app_auth.models import Role
from manuscript.models import Manuscript
# Create your views here.

def index(request):
    return redirect('Manuscript_status')



@login_required
def Manuscript_submit(request):
    if request.user.role == Role.AUTHOR:
        if request.method == 'POST':
            # print(request.FILES['file_field'])
            title=request.POST.get('Manuscript_Title')
            articletype=request.POST.get('articletype')
            Abstract=request.POST.get('Abstract')
            co_authors=request.POST.get('Manuscript_co_authors')
            manuscript=Manuscript.objects.create(Title=title,Type=articletype,abstract=Abstract,pdf_file=request.FILES["file_field"],author=request.user,co_authors=co_authors)
            manuscript.save()
            return redirect('Manuscript_status')
        else:
            return render(request,'manuscriptsubmit_page.html')
    else:
        return HttpResponse('author only upload manuscript')

@login_required
def Manuscript_status(request):
    if request.user.role == Role.AUTHOR:
        manuscript=Manuscript.objects.filter(author=request.user).all()
        return render(request,'statuspage.html',context={
            "manuscript":manuscript
        })
    
    return HttpResponse("you are not a author")