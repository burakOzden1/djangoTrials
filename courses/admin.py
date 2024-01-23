from django.contrib import admin
from .models import Course, Category

# Register your models here.

@admin.register(Course) # bu ifade asagidaki admin.site.register(Course, CourseAdmin) ifadesi tanimlamak anlamina gelir.
class CourseAdmin(admin.ModelAdmin):
    list_display = (
        "title", 
        "isActive",
        "slug",
    )

    list_display_links = (
        "title",
    )

    readonly_fields = (
        "slug",
    )

    list_filter = (
        "isActive",
    )

    list_editable = (
        "isActive",
    )

    search_fields = (
        "title",
        "description",
    )


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    pass





# admin.site.register(Course)
# admin.site.register(Category)
# Bu ifadeler yerine yukarida decorator kullandik.