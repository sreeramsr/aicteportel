from django.db import models

from django.contrib.auth.models import User
# Create your models here.
class InstituteApplication(models.Model):
    institute_name = models.CharField(max_length=255)
    application_id = models.CharField(max_length=100)
    contact_details = models.TextField()
    faculty_details = models.TextField()
    programme_course = models.TextField()
    infrastructure_library = models.TextField()
    ter_charges = models.DecimalField(max_digits=10, decimal_places=2)
    payment_status = models.BooleanField(default=False)

    def __str__(self):
        return self.institute_name
class DocumentUpload(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='document_uploads')
    building_plan_approval = models.FileField(upload_to='documents/building_plan_approval/', null=True, blank=True)
    occupancy_certificate = models.FileField(upload_to='documents/occupancy_certificate/', null=True, blank=True)
    title_document = models.FileField(upload_to='documents/title_document/', null=True, blank=True)
    lease_deed = models.FileField(upload_to='documents/lease_deed/', null=True, blank=True)
    fire_safety_certificate = models.FileField(upload_to='documents/fire_safety_certificate/', null=True, blank=True)
    land_use_certificate = models.FileField(upload_to='documents/land_use_certificate/', null=True, blank=True)
    floor_plan = models.FileField(upload_to='documents/floor_plan/', null=True, blank=True)
    proof_of_working_capital = models.FileField(upload_to='documents/proof_of_working_capital/', null=True, blank=True)
    audited_statement = models.FileField(upload_to='documents/audited_statement/', null=True, blank=True)
    minority_status_certificate = models.FileField(upload_to='documents/minority_status_certificate/', null=True, blank=True)
    detailed_project_report = models.FileField(upload_to='documents/detailed_project_report/', null=True, blank=True)
    undertaking_form = models.FileField(upload_to='documents/undertaking_form/', null=True, blank=True)

    def __str__(self):
        return f"Documents uploaded by {self.user.username} ({self.pk})"

class Institution(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    # Basic Details
    current_application_number = models.IntegerField()
    academic_year = models.CharField(max_length=100)
    application_opened_date = models.DateField()

    # Contact Person/Registrar Details
    title = models.CharField(max_length=10)
    first_name = models.CharField(max_length=100)
    middle_name = models.CharField(max_length=100, blank=True, null=True)
    last_name = models.CharField(max_length=100)
    address = models.TextField()
    designation = models.CharField(max_length=100)
    state = models.CharField(max_length=100)
    town_city_village = models.CharField(max_length=100)
    postalcode = models.CharField(max_length=10)
    stdcode = models.CharField(max_length=10)
    landline_number = models.BigIntegerField()

    # Questionnaire Details
    apply_new_odl = models.CharField(max_length=3, choices=[('yes', 'Yes'), ('no', 'No')])
    parent_application_id = models.CharField(max_length=100, blank=True, null=True)
    existing_running_institute = models.CharField(max_length=3, choices=[('yes', 'Yes'), ('no', 'No')])

    # Infrastructure and Library Count
    land_details = models.IntegerField()
    building_details = models.TextField()

    # Calculation of TER Charges
    total_ter_charges = models.CharField(max_length=100)
    total_amount_paid = models.CharField(max_length=100)
    late_fee = models.CharField(max_length=100)
    balance_amount_to_be_paid = models.CharField(max_length=100)