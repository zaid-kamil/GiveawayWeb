from django import forms

from comments.models import Comment


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ["content", "gid", 'user', ]
        widgets = {
            "content": forms.Textarea(attrs={'class': 'mdl-textfield__input','placeholder':'Add a new comment'}),
            "gid": forms.HiddenInput(),
            "user": forms.HiddenInput()
        }
