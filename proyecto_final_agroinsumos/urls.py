from django.contrib import admin
from django.urls import path, include

from django.conf.urls.static import static

from proyecto_final_agroinsumos.settings import MEDIA_ROOT, MEDIA_URL
from proyecto_final_agroinsumos.views import index

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index, name = 'index'),

    path('products/', include ('products.urls')),
    path('orders/', include ('orders.urls')),
    path('providers/', include ('providers.urls')),
    path('users/', include ('users.urls')),
    
] + static(MEDIA_URL, document_root = MEDIA_ROOT)
