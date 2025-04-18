from django.shortcuts import render, get_object_or_404
from .models import Post
from django.core.paginator import Paginator

# Συνάρτηση για να εμφανίσεις τη λίστα των δημοσιευμένων posts
def post_list(request):
    posts = Post.objects.filter(status=Post.Status.PUBLISHED)
        # Pagination logic
    paginator = Paginator(posts, 5)  # Παράδειγμα: 5 posts ανά σελίδα
    page_number = request.GET.get('page')  # Αριθμός σελίδας από το query string
    page_obj = paginator.get_page(page_number)
    return render(request, 'blog/post/list.html', {'page_obj': page_obj})


# Συνάρτηση για να εμφανίσεις ένα συγκεκριμένο post με βάση το id
def post_detail(request, year, month, day, post):
    post = get_object_or_404(
        Post,
        slug=post,
        publish__year=year,
        publish__month=month,
        publish__day=day,
        status='P'
    )
    return render(request, 'blog/post/detail.html', {'post': post})
