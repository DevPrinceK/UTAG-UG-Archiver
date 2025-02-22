from django.urls import path
from . import views
app_name = 'website'
urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('about/', views.AboutView.as_view(), name='about_us'),
    path('contact/', views.ContactView.as_view(), name='contact_us'),
    path('events/', views.EventsView.as_view(), name='events'),
    path('events/<str:slug>/UG-UTAG', views.EventsDetailView.as_view(), name='events_detail'),
    path('news/', views.NewsView.as_view(), name='news'),
    path('news/<str:slug>/UG-UTAG', views.NewsDetailView.as_view(), name='news_detail'),
    path('executive_officers/', views.ExecutiveOfficersView.as_view(), name='executive_officers'),
    path('executive_committee_members/', views.ExecutiveCommitteeMembersView.as_view(), name='executive_committee_members'),
    path('gallery/', views.GalleryView.as_view(), name='gallery'),
    path('add_click/<int:pk>/', views.AddClick.as_view(), name='add_click'),
]