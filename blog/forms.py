from django import forms
from . models import BlogPost


# class BlogPostForm(forms.Form):
#     title = forms.CharField()
#     slug =  forms.SlugField()
#     content = forms.CharField(widget=forms.Textarea)



class BlogPostForm(forms.ModelForm):
    class Meta:
        model = BlogPost
        fields = ['title', 'content','publish_date','image']

    # self means actual form
    def clean_title(self, *args, **kwargs):
        print(self.instance)
        instance = self.instance
        title = self.cleaned_data['title']
        qs = BlogPost.objects.filter(title__iexact=title)
        print(qs)
        if instance is not None:
                qs = qs.exclude(pk=instance.pk)
        if qs.exists():
            raise forms.ValidationError('The post with that title already exists')
        return title















