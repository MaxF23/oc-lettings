from django.contrib import admin
from django.urls import path

from .views import index
import lettings.views
import profiles.views


def trigger_error(request):
    return 1 / 0


urlpatterns = [
    path('', index, name='index'),
    path('lettings/', lettings.views.index, name='lettings_index'),
    path('lettings/<int:letting_id>/', lettings.views.letting, name='letting'),
    path('profiles/', profiles.views.index, name='profiles_index'),
    path('profiles/<str:username>/', profiles.views.profile, name='profile'),
    path('admin/', admin.site.urls),
    path('sentry-debug/', trigger_error)
]
