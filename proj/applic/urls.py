from django.urls import path
from . import views
from .views import institution_form_view
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('',views.home,name='home'),
    path('register/',views.register,name='register'),
    path('login/',views.login_page,name='login'),
    path('logout/',views.logout_page,name='logout'),
    path('dashboard/', views.institution_dashboard, name='institution_dashboard'),  # Dashboard URL
    path('upload/', views.upload_documents, name='upload_documents'),
    path('form/', institution_form_view, name='institution_form_view'),
    path('dashboardq/<int:pk>/', views.institution_detail, name='institution_detail'),  # Detail view URL
    path('dashboardfile/', views.dashboard, name='dashboardfile'),
    ]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)