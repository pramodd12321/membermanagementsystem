from django.contrib import admin

# Register your models here.
from . models import *

admin.site.register(Member)
admin.site.register(Designation)
admin.site.register(Organization)
admin.site.register(FiscalYearRecord)
admin.site.register(MembershipFee)
admin.site.register(LogRecord)
