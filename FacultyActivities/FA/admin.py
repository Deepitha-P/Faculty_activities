from django.contrib import admin
from .models import AdminLogin,FacultyLogin,SDP_attended,Talks_invited,SDP_organised
# Register your models here.
admin.site.register(AdminLogin)
admin.site.register(FacultyLogin)
admin.site.register(SDP_attended)
admin.site.register(SDP_organised)
admin.site.register(Talks_invited)



