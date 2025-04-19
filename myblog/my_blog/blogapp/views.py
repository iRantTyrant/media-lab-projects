#Imported modules for the views 
from django.shortcuts import render, get_object_or_404,redirect
from .models import Post

#Imported modules for the pagination
from django.core.paginator import Paginator

#Imported modules for the email
from django.core.mail import send_mail
from .forms import emailPostForm #This is the form we created on the file forms.py in the same directory hence the dot before the name of the file

#Imported modules for the comments
from .forms import CommentForm
from .models import Comment


# Function to display the list of posts
def post_list(request):
    posts = Post.objects.filter(status=Post.Status.PUBLISHED)
        # Pagination logic
    paginator = Paginator(posts, 5)  # 5 posts per page
    page_number = request.GET.get('page')  # Current page number from the request
    page_obj = paginator.get_page(page_number)
    return render(request, 'blog/post/list.html', {'page_obj': page_obj})


# Function to display the details of a specific post by its release date and slug
def post_detail(request, year, month, day, post):
    post = get_object_or_404(
        Post,
        slug=post,
        publish__year=year,
        publish__month=month,
        publish__day=day,
        status='P'
    )
    comments = Comment.objects.filter(post=post, active=True)
    form = CommentForm()
    return render(request, 'blog/post/detail.html', {
    'post': post,
    'comments': comments,
    'form': form
    })

# Function to handle the email sharing of a post
def post_share(request, post_id):
    post = get_object_or_404(Post, id=post_id, status='P')#We select the post by its id and we make sure that the post is published
    sent = False 
    if request.method == 'POST':
        form = emailPostForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            post_url = request.build_absolute_uri(post.get_absolute_url())
            subject = f"{cd['name']} Σας προτείνει να διαβάσετε  {post.title}"
            message = f"Διαβάστε το  {post.title} στο {post_url}\n\n{cd['comments']}"
            send_mail(subject, message, 'youremail@example.com' , [cd['to']])
            sent = True
    else:
        form = emailPostForm()
    return render(request, 'blog/post/share.html', {'post': post, 'form': form, 'sent': sent})

#Funtion to handle the comments 
def post_comment(request, post_id):
    post = get_object_or_404(Post, id=post_id, status='P')
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            new_comment = form.save(commit=False)
            new_comment.post = post
            new_comment.save()
            return redirect(post.get_absolute_url())
    else:
        form = CommentForm()
    return render(request, 'blog/post/comment.html', {'post': post, 'form': form})