from django import forms
from courses.models import Course

# class CourseCreateForm(forms.Form):
#     title = forms.CharField(
#         label="Kurs Başlığı",
#         required=True,
#         error_messages={
#             "required": "Kurs başlığı alanı zorunludur."},
#         widget=forms.TextInput(attrs={"class":"form-control"}))
    
#     description = forms.CharField(widget=forms.Textarea(attrs={"class":"form-control"}))
#     imageUrl = forms.CharField(widget=forms.TextInput(attrs={"class":"form-control"}))
#     slug = forms.SlugField(widget=forms.TextInput(attrs={"class":"form-control"}))
    

class CourseCreateForm(forms.ModelForm):
    class Meta:
        model = Course
        # fields = '__all__'
        fields = ('title', 'description', 'imageUrl', 'slug')
        labels = {
            'title':'Kurs Başlığı',
            'description':'Açıklama',
        },
        widgets = {
            "title": forms.TextInput(attrs={"class":"form-control"}),
            "description": forms.Textarea(attrs={"class":"form-control"}),
            "imageUrl": forms.TextInput(attrs={"class":"form-control"}),
            "slug": forms.TextInput(attrs={"class":"form-control"}),
        }
        error_messages = {
            "title": {
                "required": "kurs başlığı alanı zorunludur.",
                "max_length": "maksimum 50 karakter girilebilir",
            },
            "description":{
                "required": "kurs açıklaması alanı zorunludur."
            }
        }
    

class CourseEditForm(forms.ModelForm):
    class Meta:
        model = Course
        # fields = '__all__'
        fields = ('title', 'description', 'imageUrl', 'slug', "categories","isActive")
        labels = {
            'title':'Kurs Başlığı',
            'description':'Açıklama',
        },
        widgets = {
            "title": forms.TextInput(attrs={"class":"form-control"}),
            "description": forms.Textarea(attrs={"class":"form-control"}),
            "imageUrl": forms.TextInput(attrs={"class":"form-control"}),
            "slug": forms.TextInput(attrs={"class":"form-control"}),
            "categories": forms.SelectMultiple(attrs={"class":"form-control"}),
            "isActive": forms.CheckboxInput()
        }
        error_messages = {
            "title": {
                "required": "kurs başlığı alanı zorunludur.",
                "max_length": "maksimum 50 karakter girilebilir",
            },
            "description":{
                "required": "kurs açıklaması alanı zorunludur."
            }
        }