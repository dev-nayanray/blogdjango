from django.shortcuts import render, get_object_or_404, redirect
from django.core.paginator import Paginator
from .models import Post
from .forms import NewsletterSubscriptionForm
from django.contrib import messages
from django.core.mail import send_mail
from django.conf import settings
from django.http import JsonResponse
from .models import TeamMember

# Home view with pagination
def home(request):
    posts_list = Post.objects.all().order_by('-created_at')  # Get posts ordered by creation date
    paginator = Paginator(posts_list, 6)  # Show 6 posts per page
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, 'blog/index.html', {'page_obj': page_obj})

# Blog home view (without pagination)
def blog_home(request):
    posts = Post.objects.all()  # Get all posts (without pagination)
    return render(request, 'blog/blog_home.html', {'posts': posts})

# Post detail view
def post_detail(request, id):
    post = get_object_or_404(Post, id=id)  # Get a specific post by ID
    return render(request, 'blog/post_detail.html', {'post': post})

# Newsletter subscription view
def subscribe(request):
    if request.method == 'POST':
        form = NewsletterSubscriptionForm(request.POST)
        if form.is_valid():
            # Save the email to the database
            subscription = form.save()

            # Optionally, send a confirmation email
            send_mail(
                'Thank you for subscribing!',
                'You have successfully subscribed to our newsletter.',
                settings.DEFAULT_FROM_EMAIL,
                [subscription.email],
                fail_silently=False,
            )

            # Success message
            messages.success(request, 'Thank you for subscribing!')
            return redirect('blog:index')  # Adjust to the correct redirect URL
        else:
            messages.error(request, 'There was an issue with your submission. Please try again.')
    else:
        form = NewsletterSubscriptionForm()

    return render(request, 'subscribe.html', {'form': form})

# Search view with JSON response for autocomplete or search results
def search(request):
    query = request.GET.get('q')  # Get the search query from the request
    if query:
        posts = Post.objects.filter(title__icontains=query)  # Search for posts with a title containing the query (case-insensitive)
    else:
        posts = Post.objects.all()  # If no query, return all posts

    # Prepare a list of post titles and URLs to send as JSON
    results = [{'title': post.title, 'url': post.get_absolute_url()} for post in posts]

    return JsonResponse({'results': results})

# About page view with dynamic content
def about(request):
    context = {
        'title': 'About Us',
        'team_members': [
            {'name': 'John Doe', 'role': 'CEO', 'bio': 'Lorem ipsum dolor sit amet, consectetur adipiscing elit.'},
            {'name': 'Jane Smith', 'role': 'CTO', 'bio': 'Lorem ipsum dolor sit amet, consectetur adipiscing elit.'},
            {'name': 'Emily Johnson', 'role': 'Marketing', 'bio': 'Lorem ipsum dolor sit amet, consectetur adipiscing elit.'}
        ]
    }
    return render(request, 'about.html', context)
# views.py
from django.shortcuts import render
from .models import ContactInfo

def contact(request):
    contact_info = ContactInfo.objects.first()  # Assuming there is only one record for contact info
    context = {
        'title': 'Contact Us',
        'address': contact_info.address,
        'phone': contact_info.phone,
        'email': contact_info.email
    }
    return render(request, 'contact.html', context)


# blog/views.py
 


def about(request):
    team_members = TeamMember.objects.all()  # Fetch all team members from the database
    context = {
        'title': 'About Us',
        'team_members': team_members,
    }
    return render(request, 'about.html', context)
