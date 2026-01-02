"""
URL configuration for newborn project.

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
from django.urls import path, include

from myapp import views

urlpatterns = [
    path('',views.login),
    path('addashaworker',views.addashaworker),
    path('addpanchayath',views.addpanchayath),
    path('adminhome',views.adminhome),
    path('ashaworkermanagement',views.ashaworkermanagement),
    path('manageexpert',views.manageexpert),
    path('managepanchayath',views.managepanchayath),
    path('viewashaworker',views.viewashaworker),
    path('viewexpert',views.viewexpert),
    path('wardmanagement',views.wardmanagement),
    path('login_post',views.login_post),
    path('addwardmanagement',views.addwardmanagement),
    path('addpanchayath_post',views.addpanchayath_post),
    path('addashaworker_post',views.addashaworker_post),
    path('addward_post',views.addward_post),
    path('addexpert_post',views.addexpert_post),
    path('deletepanchayath/<id>',views.deletepanchayath),
    path('deleteexpert/<id>',views.deleteexpert),
    path('editpanchayth/<id>',views.editpanchayth),
    path('editpanchayathpost',views.editpanchayathpost),
    path('editward/<id>',views.editward),
    path('editwardpost',views.editwardpost),
    path('deleteward/<id>',views.deleteward),
    path('editexpert/<id>',views.editexpert),
    path('editexpertpost',views.editexpertpost),
    path('deleteashaworker/<id>',views.deleteashaworker),
    path('editashaworker/<id>',views.editashaworker),
    path('editashaworkpost',views.editashaworkpost),
    path('logout',views.logout),



    path('add_allocated_food',views.add_allocated_food),
    path('addchild', views.addchild),
    path('addvacc_details_of_child',views.addvacc_details_of_child),
    path('add_vacc_details',views.add_vacc_details),
    path('ashaworker_home',views.ashaworker_home),
    path('verify_mothers',views.verify_mothers),
    path('view_allocated_food/<id>',views.view_allocated_food),
    path('edit_food_allocation/<id>',views.edit_food_allocation),
    path('view_child/<id>',views.view_child),
    path('view_vacc_details',views.view_vacc_details),
    path('view_vacc_details_child/<id>',views.view_vacc_details_child),
    path('accept_mother/<id>',views.accept_mother),
    path('reject_mother/<id>',views.reject_mother),
    path('deleteechild/<id>',views.deleteechild),
    path('addchildpost',views.addchildpost),
    path('add_vacc_detail_post',views.add_vacc_detail_post),
    path('add_vacc_detail_child_post',views.add_vacc_detail_child_post),
    path('deletevacc_details_child/<id>',views.deletevacc_details_child),
    path('delete_vacc_details/<id>',views.delete_vacc_details),
    path('editvacc_detail_of_child/<id>',views.editvacc_detail_of_child),
    path('editvacc_detail_of_child_post',views.editvacc_detail_of_child_post),
    path('add_food',views.add_food),
    path('view_food',views.view_food),
    path('add_food_post',views.add_food_post),
    path('delete_foodallocation/<id>',views.delete_foodallocation),
    path('delete_food/<id>',views.delete_food),
    path('edit_food/<id>',views.edit_food),
    path('edit_food_post',views.edit_food_post),
    path('edit_vaccination/<id>',views.edit_vaccination),
    path('edit_vaccination_post',views.edit_vaccination_post),
    path('add_allocated_food_post',views.add_allocated_food_post),
    path('edit_food_allocation_post',views.edit_food_allocation_post),


    path('add_shedule',views.add_shedule),
    path('add_prescription_post',views.add_prescription_post),
    path('expert_home',views.expert_home),
    path('view_booking',views.view_booking),
    path('view_profile',views.view_profile),
    path('view_shedule',views.view_shedule),
    path('add_shedule_post',views.add_shedule_post),
    path('edit_shedule/<id>',views.edit_shedule),
    path('edit_shedule_post',views.edit_shedule_post),
    path('deletee_shedule/<id>',views.deletee_shedule),
    path('accept_shedule/<id>',views.accept_shedule),
    path('reject_shedule/<id>',views.reject_shedule),
    path('add_prescription/<id>',views.add_prescription),






    path('logincode',views.logincode),
    path('view_motherprofile',views.view_motherprofile),
    path('userreg',views.userreg),
    path('/view_expert',views.view_expert),
    path('/motherview_shedule',views.motherview_shedule),
    path('/booknow',views.booknow),
    path('/user_view_booking',views.user_view_booking),
    path('view_childd',views.view_childd),
    path('/add_baby',views.add_baby),
    path('view_feedingremainder',views.view_feedingremainder),
    path('/add_feedingremainder',views.add_feedingremainder),
    path('/chatbot_response',views.chatbot_response),
    path('user_view_prescription',views.user_view_prescription),
    path('user_view_vaccindetails',views.user_view_vaccindetails),
    path('user_view_ward', views.user_view_ward),

]


