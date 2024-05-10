from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path('menus/', views.get_menus, name='menus'),
    path('menus/<int:day>', views.get_menus_by_day, name='menu_by_day'),
    
    # path('new_menu/', views.post_menu, name='add_menu'),
    path('new_menu/', views.PostMenuAPIView.as_view(), name='add_menu'),

    path('ress/', views.get_ress, name='ress'),
    path('employees/', views.get_employees, name='employees'),

    # path('login/', views.login_user, name='login_employee'),
    path('login/', views.UserLoginAPIView.as_view(), name='login'),
]
