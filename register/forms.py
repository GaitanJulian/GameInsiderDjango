from django import forms
from Author.models import Author

class UpdateForm(forms.ModelForm):

    class Meta:
        model = Author
        fields = ("fullname", "bio", "profile_pic")
