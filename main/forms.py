from django import forms 
from django.forms import Form



class DateInput(forms.DateInput):
    input_type = "date"



# Gender choices defined outside the form class
GENDER_CHOICES = (
    ('Male', 'Male'),
    ('Female', 'Female')
)

class AddStudentForm(forms.Form):
    email = forms.EmailField(label="Email", max_length=50, widget=forms.EmailInput(attrs={"class":"form-control"}))
    password = forms.CharField(label="Password", max_length=50, widget=forms.PasswordInput(attrs={"class":"form-control"}))
    first_name = forms.CharField(label="First Name", max_length=50, widget=forms.TextInput(attrs={"class":"form-control"}))
    last_name = forms.CharField(label="Last Name", max_length=50, widget=forms.TextInput(attrs={"class":"form-control"}))
    username = forms.CharField(label="Username", max_length=50, widget=forms.TextInput(attrs={"class":"form-control"}))
    address = forms.CharField(label="Address", max_length=50, widget=forms.TextInput(attrs={"class":"form-control"}))

    gender_list = (
        ('Male','Male'),
        ('Female','Female')
    )

    def __init__(self, *args, **kwargs):
        super(AddStudentForm, self).__init__(*args, **kwargs)
        self.fields['course_id'] = forms.ChoiceField(
            label="Course", 
            widget=forms.Select(attrs={"class":"form-control"})
        )
        self.fields['gender'] = forms.ChoiceField(
            label="Gender", 
            choices=self.gender_list, 
            widget=forms.Select(attrs={"class":"form-control"})
        )
        self.fields['profile_pic'] = forms.FileField(
            label="Profile Pic", 
            required=False, 
            widget=forms.FileInput(attrs={"class":"form-control"})
        )



class EditStudentForm(forms.Form):
    email = forms.EmailField(label="Email", max_length=50, widget=forms.EmailInput(attrs={"class":"form-control"}))
    first_name = forms.CharField(label="First Name", max_length=50, widget=forms.TextInput(attrs={"class":"form-control"}))
    last_name = forms.CharField(label="Last Name", max_length=50, widget=forms.TextInput(attrs={"class":"form-control"}))
    username = forms.CharField(label="Username", max_length=50, widget=forms.TextInput(attrs={"class":"form-control"}))
    address = forms.CharField(label="Address", max_length=50, widget=forms.TextInput(attrs={"class":"form-control"}))

    #For Displaying Session Years


    
    gender_list = (
        ('Male','Male'),
        ('Female','Female')
    )
    
 
    gender = forms.ChoiceField(label="Gender", choices=gender_list, widget=forms.Select(attrs={"class":"form-control"}))
    profile_pic = forms.FileField(label="Profile Pic", required=False, widget=forms.FileInput(attrs={"class":"form-control"}))