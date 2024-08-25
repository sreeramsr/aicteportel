from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import Institution

admin.site.register(Institution)
from .models import DocumentUpload

@admin.register(DocumentUpload)
class DocumentUploadAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'building_plan_approval', 'occupancy_certificate', 'title_document', 'lease_deed', 'fire_safety_certificate', 'land_use_certificate', 'floor_plan', 'proof_of_working_capital', 'audited_statement', 'minority_status_certificate', 'detailed_project_report', 'undertaking_form')
    search_fields = ('user__username', 'id')
    list_filter = ('user',)