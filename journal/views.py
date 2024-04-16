from django.shortcuts import render
from manuscript.models import Manuscript,Volume
from editor.models import Editors
# Create your views here.
def homepage(request):
    return render(request,'homepage.html')

def policypage(request):
    return render(request,'policypage.html')

def editorialpage(request):
    editors=Editors.objects.all()
    return render(request,'editorial_board_page.html',context={
            "editors":editors
        })


def issuespage(request):
    manuscript=Manuscript.objects.filter(verified=True,under_review=True).all()
    return render(request,'Issues.html',context={
            "manuscript":manuscript
        })

def issuespage(request,id):
    manuscript=Manuscript.objects.filter(verified=True,under_review=True,volume=id).all()
    return render(request,'Issues.html',context={
            "manuscript":manuscript
        })

def issuespage2(request):
    volume=Volume.objects.all()
    return render(request,'Issues2.html',context={
            "volumes":volume,
        })

def authorInfopage(request):
    return render(request,'Info_Author_page.html')

def ContactPage(request):
    return render(request,'contactpage.html')

def manuscript_page(request):
    return render(request,'manuscript_page.html')


def Publication_Policy(request):
    return render(request,'Publication_Policy.html')

def Plagiarism_Policy(request):
    return render(request,'Plagiarism_Policy.html')

def Peer_Review_Policy(request):
    return render(request,'Peer_Review_Policy.html')

def Open_Access_Policy(request):
    return render(request,'Open_Access_Policy.html')

def indexing(request):
    return render(request,'indexing.html')

def Multiple_Publications(request):
    return render(request,'Multiple_Publications.html')

def Correction_and_Retraction(request):
    return render(request,'Correction_and_Retraction.html')

def Cope_Guidelines(request):
    return render(request,'COPE_Guidelines.html')

def Guidelines_for_Editors(request):
    return render(request,'Guidelines_for_Editors.html')

def Guidelines_for_Reviewers(request):
    return render(request,'Guidelines_for_Reviewers.html')

def Privacy_Statement(request):
    return render(request,'Privacy_Statement.html')

