from django.shortcuts import render, get_object_or_404,redirect
from django.utils import timezone
from . models import BlogPost
from . forms import BlogPostForm
from django.contrib.auth.decorators import login_required
from django.contrib.admin.views.decorators import staff_member_required


def homepage(request):
    blog_list = BlogPost.objects.all()[:5]
    context = {'blog_list':blog_list,}
    return render(request,'blog/home.html',context)


def post_list_view(request):
    qs = BlogPost.objects.all().published()
    if request.user.is_authenticated:
        my_qs = BlogPost.objects.filter(user=request.user)
        qs = (qs | my_qs).distinct()

    # if request.user.is_authenticated:
    #     qs = BlogPost.objects.filter(user=request.user)
    # else:
    #     qs = BlogPost.objects.all().published()
    context = {'object_list': qs,}
    return render(request, 'blog/post_list.html', context)


@staff_member_required
def post_create_view(request):
    if request.method == 'POST':
        form = BlogPostForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.user = request.user
            post.save()
            # form = BlogPostForm()
            # title = form.cleaned_data['title']
            # slug = form.cleaned_data['slug']
            # content = form.cleaned_data['content']
            # BlogPost.objects.create(title=title,slug=slug,content=content)
            # BlogPost.objects.create(**form.cleaned_data)
            form = BlogPostForm()
            return redirect('homepage')
    else:
        form = BlogPostForm()
    context = {
        'form': form,
    }
    return render(request, 'blog/post_create.html', context)



def post_detail_view(request, post_slug):
    post = get_object_or_404(BlogPost, slug=post_slug)
    context = {'post': post}
    return render(request, 'blog/post_detail.html', context=context)


@staff_member_required
def post_update_view(request,post_slug):
    post = get_object_or_404(BlogPost, slug=post_slug)
    if request.method == 'POST':
        form = BlogPostForm(request.POST, request.FILES, instance=post)
        if form.is_valid():
            form.save()
            return redirect(f'homepage')
    else:
        form = BlogPostForm(instance=post)

    context = {
        'post': post,
        'form':form
    }
    return render(request, 'blog/post_update.html', context=context)


@staff_member_required
def post_delete_view(request,post_slug):
    post = get_object_or_404(BlogPost, slug=post_slug)
    slug = post.slug
    if request.method == 'POST':
        post.delete()
        return redirect(f'post-list')
    context = {'post': post}
    return render(request, 'blog/post_delete.html', context=context)



