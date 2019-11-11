"""Posts views"""
from django.shortcuts import render
from django.contrib.auth.decorators import login_required

from datetime import datetime

posts = [
    {
        'title': 'Xiaomi Redmi Note 9',
        'user': {
            'name': 'Gonzalo',
            'picture': 'https://img.icons8.com/plasticine/2x/user.png'
        },
        'timestamp': datetime.now().strftime('%b %dth, %Y - %H:%M hrs '),
        'photo': 'https://www.notebookcheck.net/fileadmin/Notebooks/News/_nc3/mi_9_se_gizmo.jpg'
    },
    {
        'title': 'Iphone X',
        'user': {
            'name': 'Gonzalo',
            'picture': 'https://img.icons8.com/plasticine/2x/user.png'
        },
        'timestamp': datetime.now().strftime('%b %dth, %Y - %H:%M hrs '),
        'photo': 'https://static.toiimg.com/photo/61654288.cms'
    },
    {
        'title': 'Macbook Pro',
        'user': {
            'name': 'Gonzalo',
            'picture': 'https://img.icons8.com/plasticine/2x/user.png'
        },
        'timestamp': datetime.now().strftime('%b %dth, %Y - %H:%M hrs '),
        'photo': 'https://cdn.pocket-lint.com/r/s/970x/assets/images/149132-laptops-review-macbook-pro-13-inch-2019-review-business-as-usual-image1-mjmo9napgu.jpg'
    }
]


@login_required
def list_posts(request):
    """list existing posts."""
    return render(request, 'posts/feed.html', {'posts': posts})
