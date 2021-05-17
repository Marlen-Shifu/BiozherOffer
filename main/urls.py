from django.urls import path, include

from django.conf import settings
from django.conf.urls.static import static

from .views import *

urlpatterns = [
	path('', HomePageView.as_view(), name = 'home'),
	path('about/', AboutPageView.as_view(), name = 'about'),
	path('documentation/', DocumentationBlockListView.as_view(), name = 'documentation'),
	path('gallery/', TrialsPhotoListView.as_view(), name = 'gallery'),
	path('products/', ProductListView.as_view(), name = 'products'),
	path('blog/', PostListView.as_view(), name = 'blog'),
	path('blog/<int:pk>/', PostDetailView.as_view(), name = 'blog_detail'),
	path('contacts/', ContactPageView.as_view(), name = 'contacts'),
]


if settings.DEBUG:
	urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
