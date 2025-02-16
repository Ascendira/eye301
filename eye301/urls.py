"""
URL configuration for eye301 project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
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
from eye301 import settings
from django.conf.urls.static import static
import patientInfo.views

app_name = 'patientInfo'

urlpatterns = [
    path("admin/", admin.site.urls),
    path('index/', patientInfo.views.index),
    path("basicInfo/add/<str:date>",patientInfo.views.BaseInfo.as_view()),
    path("basicInfo/get/<int:pageNum>/<int:pageSize>",patientInfo.views.BaseInfo.as_view()),
    path("patientInfo/post/<str:date>",patientInfo.views.PatientInfoView.as_view()),
    path("patientInfo/get/<int:pageNum>/<int:pageSize>",patientInfo.views.PatientInfos.as_view()),
    path("patientInfo/get/<str:patient_id>",patientInfo.views.PatientInfoView.as_view()),
    path("patientInfo/get/base/<str:patient_id>", patientInfo.views.PatientInfoView.as_view()),
    path("patientInfo/delete/<str:patient_id>", patientInfo.views.PatientInfoView.as_view()),
    path("otherInfo/img/post/<str:patient_id>/<str:img_type>", patientInfo.views.Image.as_view()),
    path("otherInfo/img/get/<str:patient_id>/", patientInfo.views.Image.as_view())
]

urlpatterns += static(settings.IMG_URL, document_root=settings.IMG_UPLOAD)
