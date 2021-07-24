from django import forms
from .models import Post,Comment,Reply




class CommentForm(forms.ModelForm):
    class Meta:
        model=Comment
        fields=('username','comment','audio')
        widgets={
            'username':forms.TextInput(attrs={'placeholder':'enter ur name'}),
            'comment':forms.Textarea(attrs={'placeholder':'write your comments'}),
            }


class ReplyForm(forms.ModelForm):
    class Meta:
        model=Reply
        fields=('name_of_user','reply')