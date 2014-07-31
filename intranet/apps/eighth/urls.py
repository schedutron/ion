from django.conf.urls import include, url
from .views import routers, student_signup, teacher_attendance
from .views.admin.general import (
    eighth_admin_index_view, EighthAdminExampleWizard)


urlpatterns = [
    url(r"^$", routers.eighth_redirect_view, name="eighth_redirect"),

    # Students
    url(r"^signup(?:/(?P<block_id>\d+))?$", student_signup.eighth_signup_view, name="eighth_signup"),

    # Teachers
    url(r"^attendance$", teacher_attendance.eighth_teacher_attendance_view, name="eighth_teacher_attendance"),

    # Admin
    url(r"^admin$", eighth_admin_index_view, name="eighth_admin_index"),
]


eighth_admin_patterns = [
    url(r"^example$", EighthAdminExampleWizard.as_view(EighthAdminExampleWizard.FORMS), name="eighth_admin_form_example"),
]

urlpatterns += [
    url(r"^admin/", include(eighth_admin_patterns)),
]
