from django.urls import path
from . import views

urlpatterns = [
    # Employee URLs
    path('', views.EmployeeListView.as_view(), name='employee-list'),
    path('employee/<int:pk>/', views.EmployeeDetailView.as_view(), name='employee-detail'),
    path('employee/new/', views.EmployeeCreateView.as_view(), name='employee-create'),
    path('employee/<int:pk>/update/', views.EmployeeUpdateView.as_view(), name='employee-update'),
    path('employee/<int:pk>/delete/', views.EmployeeDeleteView.as_view(), name='employee-delete'),
    
    # Department URLs
    path('departments/', views.DepartmentListView.as_view(), name='department-list'),
    path('department/new/', views.DepartmentCreateView.as_view(), name='department-create'),
    path('department/<int:pk>/update/', views.DepartmentUpdateView.as_view(), name='department-update'),
    path('department/<int:pk>/delete/', views.DepartmentDeleteView.as_view(), name='department-delete'),
]