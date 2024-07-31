from django.urls import path
from health import views
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from health.views import *
from django.urls import path, register_converter
# from .api import router
from .apirep import routerep
from .converters import FloatConverter
# Register the custom converter
register_converter(FloatConverter, 'float')

urlpatterns = [
    # path('api/sensoviz/', include(router.urls)),
    path('api/v1/', include(routerep.urls)),
    path('admin/', admin.site.urls),
    path('', views.Home, name="home"),
    path('patient_home', views.User_Home, name="patient_home"),
    path('doctor_home', views.Doctor_Home, name="doctor_home"),
    path('admin_home', views.Admin_Home, name="admin_home"),
    path('about', views.About, name="about"),
    path('contact', views.Contact, name="contact"),
    path('gallery', views.Gallery, name="gallery"),
    path('login', views.Login_User, name="login"),
    path('login_admin', views.Login_admin, name="login_admin"),
    path('signup', views.Signup_User, name="signup"),
    path('logout', views.Logout, name="logout"),
    path('change_password', views.Change_Password, name="change_password"),
    path('add_fetaldetail', views.add_fetaldetail, name="add_fetaldetail"),
    path('view_search_pat', views.view_search_pat, name="view_search_pat"),
    path('view_doctor', views.View_Doctor, name="view_doctor"),
    path('add_doctor', views.add_doctor, name="add_doctor"),
    path('change_doctor/<int:pid>/', views.add_doctor, name="change_doctor"),
    path('view_patient', views.View_Patient, name="view_patient"),
    path('view_feedback', views.View_Feedback, name="view_feedback"),
    path('edit_profile', views.Edit_My_deatail, name="edit_profile"),
    path('profile_doctor', views.View_My_Detail, name="profile_doctor"),
    path('sent_feedback', views.sent_feedback, name="sent_feedback"),
    path('delete_searched/<int:pid>', views.delete_searched, name="delete_searched"),
    path('delete_doctor<int:pid>', views.delete_doctor, name="delete_doctor"),
    path('assign_status<int:pid>', views.assign_status, name="assign_status"),
    path('delete_patient<int:pid>', views.delete_patient, name="delete_patient"),
    path('delete_feedback<int:pid>', views.delete_feedback, name="delete_feedback"),
    path('predict_disease/<str:pred>/<float:accuracy>/', views.predict_disease, name='predict_disease'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
