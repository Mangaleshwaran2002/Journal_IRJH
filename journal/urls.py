from django.urls import path
from .views import homepage,editorialpage,policypage,issuespage,authorInfopage,manuscript_page,Publication_Policy,Plagiarism_Policy,Peer_Review_Policy,Open_Access_Policy,indexing,Multiple_Publications,Correction_and_Retraction,Cope_Guidelines,Guidelines_for_Editors,Guidelines_for_Reviewers,Privacy_Statement,ContactPage,issuespage2
urlpatterns = [
    path('', homepage,name='homescreen'),
    path('editorialpage/', editorialpage,name='editorialpage'),
    path('issuespage/', issuespage,name='issuespage'),
    path('issuespage/<int:id>', issuespage,name='issuespage'),
    path('issuespage2/', issuespage2,name='issuespage2'),
    path('authorInfopage/', authorInfopage,name='authorInfopage'),
    path('ContactPage/', ContactPage,name='ContactPage'),
    path('manuscript_page/', manuscript_page,name='manuscript_page'),
    # policies
    path('policypage/', policypage,name='policypage'),
    path('Publication_Policy/', Publication_Policy,name='Publication_Policy'),
    path('Plagiarism_Policy/', Plagiarism_Policy,name='Plagiarism_Policy'),
    path('Peer_Review_Policy/', Peer_Review_Policy,name='Peer_Review_Policy'),
    path('Open_Access_Policy/', Open_Access_Policy,name='Open_Access_Policy'),
    path('indexing/', indexing,name='indexing'),
    path('Multiple_Publications/', Multiple_Publications,name='Multiple_Publications'),
    path('Correction_and_Retraction/', Correction_and_Retraction,name='Correction_and_Retraction'),
    path('COPE_Guidelines/', Cope_Guidelines,name='COPE_Guidelines'),
    path('Guidelines_for_Editors/', Guidelines_for_Editors,name='Guidelines_for_Editors'),
    path('Guidelines_for_Reviewers/', Guidelines_for_Reviewers,name='Guidelines_for_Reviewers'),
    path('Privacy_Statement/', Privacy_Statement,name='Privacy_Statement'),
]