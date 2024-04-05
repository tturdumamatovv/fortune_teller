from django.urls import path
from . import views

urlpatterns = [
    path('services/', views.ServiceListAPIView.as_view(), name='service-list'),
    path('services/<int:pk>/', views.ServiceDetailAPIView.as_view(), name='service-detail'),
    path('comments/', views.CommentListAPIView.as_view(), name='comment-list'),
    path('certificates/', views.CertificateListAPIView.as_view(), name='certificate-list'),
]
