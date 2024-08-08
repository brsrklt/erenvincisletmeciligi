from django.contrib import admin

from blog.models import Blog, Category, Makinelerimiz, Hakkimizda, İletisim

from django.utils.safestring import mark_safe # mark safe admin panel özelleştirmede kullanılır
# Register your models here.

class MakinelerimizAdmin(admin.ModelAdmin):
    list_display = ("title","slug")    
    search_fields = ("title",)
    readonly_fields = ("slug",)

admin.site.register(Makinelerimiz, MakinelerimizAdmin)


class HakkimizdaAdmin(admin.ModelAdmin):
    list_display = ("title",)  



class IletisimAdmin(admin.ModelAdmin):
    list_display = ("Ad_1","tel_1","Ad_2","tel_2",) 
    list_display_links = ("Ad_1","tel_1","Ad_2","tel_2",)    



admin.site.register(İletisim, IletisimAdmin)



class BlogAdmin(admin.ModelAdmin):
    list_display = ("title","is_active","slug","selected_categories")
    list_editable = ("is_active",)
    search_fields = ("title","description")
    readonly_fields = ("slug",)
    list_filter = ("is_active","categories",)

    def selected_categories(self,obj):
        html ="<ul>"
        for category in obj.categories.all():
            html+= "<li>" + category.name + "</li>"
        html+= "</ul>"
        return mark_safe(html)

admin.site.register(Blog, BlogAdmin)



class CategoryAdmin(admin.ModelAdmin):
    list_display = ("name","slug")    
    search_fields = ("name",)
    readonly_fields = ("slug",)

admin.site.register(Category, CategoryAdmin)
