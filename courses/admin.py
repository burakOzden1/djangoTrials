from django.contrib import admin
from .models import Course, Category

# Register your models here.

@admin.register(Course) # bu ifade asagidaki admin.site.register(Course, CourseAdmin) ifadesi tanimlamak anlamina gelir.
class CourseAdmin(admin.ModelAdmin):
    list_display = (
        "title", 
        "isActive",
        "slug",
        # "category", # many to many iliskisi kurdugumuz icin bu satiri sildik.
        "category_list", # model icerisinde yok ama bu class icerisinde olusturduk.
    )

    list_display_links = (
        "title",
    )

    # readonly_fields = (
    #     "slug",
    # )

    prepopulated_fields = {"slug": ("title",),}
    # slug bilgisini title bilgisine gore otomatik olustur.

    list_filter = (
        "isActive",
        # "category", # many to many iliskisi kurdugumuz icin bu satiri sildik.
    )

    list_editable = (
        "isActive",
    )

    search_fields = (
        "title",
        "description",
    )

    def category_list(self, obj):
        html = ""
        for category in obj.categories.all():
            html += category.name + ", "
        return html
    # kurs kategorilerinin admin paneldeki liste uzerinde gorunmesi icin boyle bir fonk yazdik.


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = (
        "name", 
        "slug", 
        "course_count",
    )

    prepopulated_fields = {"slug": ("name",),}

    def course_count(self, obj):
        return obj.course_set.count()
    # kategori kurslarinin admin paneldeki liste uzerinde gorunmesi icin boyle bir fonk yazdik.





# admin.site.register(Course)
# admin.site.register(Category)
# Bu ifadeler yerine yukarida decorator kullandik.