from django import forms
from Author.models import Author

class UpdateForm(forms.ModelForm):

    class Meta:
        model = Author
        fields = ("fullname", "bio", "profile_pic")

    def __init__(self, *args, **kwargs):
        super(UpdateForm, self).__init__(*args, **kwargs)
        self.fields['profile_pic'].required = False
