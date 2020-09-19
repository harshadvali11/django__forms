from django import forms

value=[['MALE','male'],('female','female')]

#(content to store in database,content to display in our front end)

class New_Form(forms.Form):
    name=forms.CharField(max_length=50,min_length=5,label='FIRST_NAME',label_suffix='AS',help_text='write only Characters')
    email=forms.EmailField()
    url=forms.URLField()
    number=forms.IntegerField()
    date=forms.DateField()
    datetime=forms.DateTimeField()
    time=forms.TimeField()
    password=forms.CharField(widget=forms.PasswordInput)
    address=forms.CharField(widget=forms.Textarea())
    gender=forms.ChoiceField(choices=value)