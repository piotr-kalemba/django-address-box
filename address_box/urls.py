
from django.urls import path
from . import views

urlpatterns = [
    path('new/', views.NewPerson.as_view(), name='add-person'),
    path('delete/<int:id>/', views.DelPerson.as_view(), name='delete-person'),
    path('show/<int:id>/', views.ShowPerson.as_view(), name='show-person'),
    path('', views.AllPerson.as_view(), name='show-all'),
    path('groups/', views.Groups.as_view(), name='groups'),
    path('group/<int:id>/', views.ShowGroup.as_view(), name='show-group'),
    path('del_group/<int:id>/', views.DelGroup.as_view(), name='del-group'),
    path('add_group/', views.AddGroup.as_view(), name='add-group'),
    path('del_from_group/<int:g_id>/<int:m_id>/', views.DelMemberFromGroup.as_view(), name='del-from-group'),
    path('add_email/<int:id>/', views.AddEmail.as_view(), name='add-email'),
    path('add_group_to_person/<int:id>/', views.AddGroupToPerson.as_view(), name='add-group-to-person'),
]
