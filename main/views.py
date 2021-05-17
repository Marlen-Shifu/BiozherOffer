from django.shortcuts import render

from django.views.generic import ListView, DetailView, TemplateView

from .models import *


class HomePageView(TemplateView):
	template_name = 'index.html'


class AboutPageView(TemplateView):
	template_name = 'about.html'


class PostListView(ListView):
	model = Post
	template_name = "blog.html"


class PostDetailView(DetailView):
	model = Post
	template_name = "blog_info.html"


class ProductListView(ListView):
	model = Product
	template_name = 'catalog.html'


class DocumentationBlockListView(ListView):
	model = DocumentationBlock
	template_name = 'documentation.html'


class TrialsPhotoListView(ListView):
	model = TrialsPhoto
	template_name = 'gallery.html'


class ContactPageView(TemplateView):
	template_name = 'contacts.html'