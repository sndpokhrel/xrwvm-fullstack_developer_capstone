from django.urls import path
from django.conf.urls.static import static
from django.conf import settings
from . import views
from django.contrib.auth import views as auth_views

app_name = 'djangoapp'

urlpatterns = [
    # path for registration

    # path for login
    path(route='login', view=views.login_user, name='login'),

    # path for logout
    path(route='logout', view=auth_views.LogoutView.as_view(next_page='/'), name='logout'),


    # path for dealer reviews view

    # path for add a review view

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
