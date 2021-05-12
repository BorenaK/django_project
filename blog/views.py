from django.shortcuts import render
from django.http import HttpResponse

# function that handles traffic from the homepage to the blog
# takes in request argument
posts = [
	{
		'author': 'Jane Smith',
		'title': 'Blog Post 1',
		'content': 'First post content',
		'date_posted': '11th May 2021',
	},
	{
		'author': 'Orecchio Tappato',
		'title': 'Blog Post 2',
		'content': 'Second post content',
		'date_posted': '12th May 2021',
	}
]

def home(request):
	context = {
		'posts': posts
	}
	return render(request, 'blog/home.html', context)
	
def about(request):
	return render(request, 'blog/about.html', {'title': 'About'})

