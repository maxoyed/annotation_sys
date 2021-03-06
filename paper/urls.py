from django.urls import path,include

from . import views
from rest_framework import routers

router = routers.DefaultRouter()
router.register('subject', views.SubjectViewSet)
router.register('domain', views.DomainViewSet)
router.register('paper', views.PaperViewSet)
router.register('paperundispatched', views.PaperundispatchedViewSet)#PaperundispatchedViewSet
router.register('content', views.Paper_contentsViewSet)
router.register('paragraph', views.ParagraphViewSet)

#app_name = 'paper'
urlpatterns = [
    path('', include(router.urls)),
    path('reg_paper',views.reg_paper)
]