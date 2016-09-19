from django.contrib import admin
from blog.models import BlogPost, Category


class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'introduction', 'created_at', 'blog_category', 'post_likes', )
    list_filter = ('blog_category', 'owner',)
    search_fields = ('title', 'blog_category',)

    fieldsets = (
        ("Name and description", {
            'fields': ('title', 'introduction',),
            'classes': ('wide',)
        }),
        ('Author', {
            'fields': ('owner',),
            'classes': ('wide',)
        })
    )

    def owner_name(self, blog_post):
        return "{0} {1}".format(blog_post.owner.first_name, blog_post.owner.last_name)

    owner_name.admin_order_field = 'owner'
    owner_name.short_description = 'Propietario'


admin.site.register(BlogPost)
admin.site.register(Category)