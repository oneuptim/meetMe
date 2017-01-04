from django.conf.urls import url, include
from django.contrib import admin
from apps.meetmeApp.models import User as U
from dashing.utils import router

class UAdmin(admin.ModelAdmin):
  pass
admin.site.register(U, UAdmin)

  # class FruitAdmin(admin.ModelAdmin):
  #     pass
  # admin.site.register(Fruit, FruitAdmin)
  #
  # class DonutAdmin(admin.ModelAdmin):
  #     pass
  # admin.site.register(Donut, DonutAdmin)
  #
# class GroupAdmin(admin.ModelAdmin):
#   pass
# admin.site.register(Group, GroupAdmin)

urlpatterns = [
    url(r'^admin/',admin.site.urls),
    url(r'^', include('apps.meetmeApp.urls')),
    url(r'^admin/dashboard/', include(router.urls)),
]
    
