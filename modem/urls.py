"""modem URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.conf import settings
from django.conf.urls import url
from django.conf.urls.static import static
from django.views.generic import TemplateView
from app import views


urlpatterns = [
    url('admin/', admin.site.urls),
    url(r'^$',views.index,name='index'),
    url('manage/',views.manage,name='manage'),
    url('csvfile/',views.csvfile,name='csvfile'),
    url('compose/',views.compose,name='compose'),
    url('device/',views.device,name='device'),
    url('inbox/',views.inbox,name='inbox'),
    url('user/',views.user,name='user'),
    url('outbox/',views.outbox,name='outbox'),
    url('test/',views.test,name='test'),
    url('report/',views.report,name='report'),  
    url('item/',views.item,name='item'),
    url('model/',views.model,name='model')
]


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
