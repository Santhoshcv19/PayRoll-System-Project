"""
URL configuration for payrollsystem project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from services import views

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", views.payslip, name="payslip"),
    path("addemployee", views.input_employee_rates, name="addemployee"),
    path("uploadexcel", views.upload_file, name="uploadexcel"),
    path("payslip", views.payslip, name="payslip"),
    path("emlist", views.emlist, name='emlist'),
    path("export_salary_summary/<str:selected_month>/<int:selected_year>/", views.export_salary_summary, name='export_salary_summary'),
    path("profile/<int:user_id>/", views.profile, name='profile'),
    path('export_payslip/<str:selected_month>/<int:selected_year>/', views.export_payslip, name='export_payslip'),
    path('delete_employee/<int:emp_code>/', views.delete_employee, name='delete_employee'),
]

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
