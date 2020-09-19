from django.shortcuts import render

# Create your views here.
from app.forms import *

def new_Form(request):
    form=New_Form()          #it is empty html input element class 

    if request.method=='POST':
        form_data=New_Form(request.POST) # it is form which has the submitted data
        if form_data.is_valid():
            #print(form_data.cleaned_data)# this displays all the data
            #print(form_data.cleaned_data['name'])# this displays the paricular data
            name=form_data.cleaned_data['name']
            email=form_data.cleaned_data['email']
            url=form_data.cleaned_data['url']
            number=form_data.cleaned_data['number']
            date=form_data.cleaned_data['date']
            datetime=form_data.cleaned_data['datetime']
            time=form_data.cleaned_data['time']
            password=form_data.cleaned_data['password']
            
            address=form_data.cleaned_data['address']
            
            gender=form_data.cleaned_data['gender']
            d={'name':name,'email':email,'url':url,'number':number}
            return render(request,'form_data.html',context=d)
    return render(request,'New_Form.html',context={'form':form})


