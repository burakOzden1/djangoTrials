from django import forms

class CourseCreateForm(forms.Form):
    title = forms.CharField(
        label="Kurs Başlığı",
        required=True,
        error_messages={
            "required": "Kurs başlığı alanı zorunludur.",
        }
    )
    description = forms.CharField(widget=forms.Textarea)
    imageUrl = forms.CharField()
    slug = forms.SlugField()
    