from django.shortcuts import render , get_list_or_404
from django.core.paginator import Paginator

from .models import Comments


def comments(request):
    comments_list = Comments.objects.order_by('-comment_date')

    paginator = Paginator(comments_list , 6)
    page = request.GET.get('page')
    paged_posts_list = paginator.get_page(page)

    context = {
        'comments': paged_posts_list
    }

    return render(request, 'comments/comments.html', context)

