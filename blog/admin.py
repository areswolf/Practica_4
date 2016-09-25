from django.contrib import admin
from django.utils.safestring import mark_safe

from blog.models import BlogPost, Category


class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'introduction', 'media_url', 'modified_at',)
    list_filter = ('blog_category', 'owner',)
    search_fields = ('title', 'blog_category',)
    readonly_fields = ('image_tag',)


    fieldsets = (
        ("Name and description", {
            'fields': ('title', 'introduction',),
            'classes': ('wide',)
        }),
        ('Author', {
            'fields': ('owner',),
            'classes': ('wide',)
        }),
        ('URL', {
            'fields': ('media_url', 'image_tag',),
            'classes': ('wide',)
        }),
        ('License and visibility', {
            'fields': ('status', 'visibility',),
            'classes': ('wide', 'collapse')
        })
    )

    def owner_name(self, blog_post):
        return "{0} {1}".format(blog_post.owner.first_name, blog_post.owner.last_name)

    owner_name.admin_order_field = 'owner'
    owner_name.short_description = 'Propietario'

    def image_tag(self, post):
        return mark_safe("<img src={0}>".format(post.media_url))

admin.site.register(BlogPost, PostAdmin)
admin.site.register(Category)









