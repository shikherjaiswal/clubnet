"""
This module registers URL patterns for the 'api' app.
"""

from django.conf.urls import url, include
from rest_framework.urlpatterns import format_suffix_patterns
from rest_framework.routers import DefaultRouter

from . import views

# Create a router and register the Viewsets with it.
router = DefaultRouter()
router.register(r'users', views.UserViewSet)
router.register(r'clubs', views.ClubViewSet)
router.register(r'clubroles', views.ClubRoleViewSet)
router.register(r'clubmembers', views.ClubMembershipViewSet)
router.register(r'channels', views.ChannelViewSet)
router.register(r'posts', views.PostViewSet)
router.register(r'conversations', views.ConversationViewSet)
router.register(r'projects', views.ProjectViewSet)
router.register(r'feedbacks', views.FeedbackViewSet)

urlpatterns = [
    url(r'^feedbackreplies/$', views.FeedbackReplyCreate.as_view()),
    url(r'^feedbackreplies/(?P<pk>[0-9]+)/$',
        views.FeedbackReplyDetail.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)

urlpatterns += [
    url(r'^', include(router.urls)),
    url(r'^api-auth/', include('rest_framework.urls',
                               namespace='rest_framework')),
]
