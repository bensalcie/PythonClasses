from django import  forms

from application.models import  Student

class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = '__all__'

        widgets ={
            'name':forms.TextInput(attrs={'class':'form-control','placeholder':'Enter your name'}),
            'admNo': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter your Admission number'}),
            'age':forms.NumberInput(attrs={'class':'form-control','placeholder':'Enter your age'}),
            'gender':forms.TextInput(attrs={'class':'form-control','placeholder':'Enter your Gender'}),
            'course':forms.TextInput(attrs={'class':'form-control','placeholder':'Enter your Course'}),
            'image':forms.ClearableFileInput(attrs={'class':'form-control',
                                                    'accept':'image/*',
                                                    'title':'Upload Image here'})
        }
