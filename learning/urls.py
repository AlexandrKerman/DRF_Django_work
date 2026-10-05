from django.urls import path, include
from rest_framework.routers import DefaultRouter

from learning.views import CourseViewSet, LessonList, LessonRetrieve, LessonCreate, LessonUpdate, LessonDestroy

router = DefaultRouter()
router.register(r'courses', CourseViewSet, basename='course')

urlpatterns = [
    path('', include(router.urls)),
    path('lessons/', LessonList.as_view(), name='lesson-list'),
    path('lessons/create/', LessonCreate.as_view(), name='lesson-create'),
    path('lessons/<int:pk>/', LessonRetrieve.as_view(), name='lesson-detail'),
    path('lessons/<int:pk>/update/', LessonUpdate.as_view(), name='lesson-update'),
    path('lessons/<int:pk>/delete/', LessonDestroy.as_view(), name='lesson-delete')
]

