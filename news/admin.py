from django.contrib import admin
from .models.customer import Customer
from .models.aduestiment import Aduestiment
from .models.new import News
from .models.photo import Photo
from .models.category import Category

from embed_video.admin import AdminVideoMixin
from .models.video import Item

# Register your models here.
admin.site.register(Customer)
admin.site.register(Aduestiment)
admin.site.register(News)
admin.site.register(Photo)
class MyModelAdmin(AdminVideoMixin, admin.ModelAdmin):
    pass

admin.site.register(Item, MyModelAdmin)
admin.site.register(Category)