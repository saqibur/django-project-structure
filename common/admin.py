from django.contrib import admin

class AuditAdmin(admin.ModelAdmin):
    """
    Base admin class to automatically set created_by and updated_by fields
    for models inheriting from BaseModel. Inherit this for all admin models
    using audit fields.
    """
    def save_model(self, request, obj, form, change):
        if not obj.pk and not obj.created_by:
            obj.created_by = request.user
        obj.updated_by = request.user
        super().save_model(request, obj, form, change) 