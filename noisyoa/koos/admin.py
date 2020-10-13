from django.contrib import admin
from koos.models import Koos, Koos_ps


# Register your models here.
@admin.register(Koos)
class KoosAdmin(admin.ModelAdmin):
    list_display = [field.name for field in Koos._meta.get_fields()]


@admin.register(Koos_ps)
class Koos_psAdmin(admin.ModelAdmin):
    list_display = (
        "a3_function",
        "a5_function",
        "a9_function",
        "a10_function",
        "sp1_exercise",
        "sp4_exercise",
        "sp5_exercise",
        # "total_score",
        "user",
    )

    def save_model(self, request, instance, form, change):
        user = request.user
        instance = form.save(commit=False)
        if not change or not instance.user:
            instance.user = user
        instance.modified_by = user
        instance.save()
        form.save_m2m()
        return instance
