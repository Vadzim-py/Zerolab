from django.contrib import admin
from django.contrib.auth import views as auth_views
from django.urls import path, include
from core.views import index
from django.conf.urls.static import static
from django.conf import settings

admin.site.site_header = 'Zerolab_1'
admin.site.site_title = 'Zerolab_1'
admin.site.index_title = 'Administration'

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index, name='index'),
    path('users/', include('users.urls', namespace='users')),
    path('products/', include('products.urls', namespace='products')),
    path('crud/', include('crud.urls', namespace='crud')),
    path('password-reset/', auth_views.PasswordResetView.as_view(
        template_name='pass_reset_via_email/password_reset.html'),
        name='password_reset'),
    path('password-reset/done/', auth_views.PasswordResetDoneView.as_view(
        template_name='pass_reset_via_email/password_reset_sent.html'),
        name='password_reset_done'),
    path('password-reset-confirm/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(
        template_name='pass_reset_via_email/password_reset_fill.html'),
        name='password_reset_confirm'),
    path('reset/done/', auth_views.PasswordResetCompleteView.as_view(
        template_name='pass_reset_via_email/password_reset_complete.html'),
        name='password_reset_complete'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
