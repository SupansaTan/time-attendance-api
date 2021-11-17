from django.contrib import admin
from app.models import PlanShift, Employee, TimeRecord, ShiftCode, Department

# Register your models here.
admin.site.register(PlanShift)
admin.site.register(Employee)
admin.site.register(TimeRecord)
admin.site.register(ShiftCode)
admin.site.register(Department)