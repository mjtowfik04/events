from django.urls import path
from event.views import event_form,organizer_dashboard,update_event,delete,dashboard

urlpatterns = [
    # path('home/',home,name='home'),
    path('from/',event_form ,name="event_form"),
    path('organizer-dashboard/',organizer_dashboard,name='organizer_dashboard'),
    path('update-event/<int:id>/',update_event, name='update-event'),
    path('delete-event/<int:id>/',delete,name='delete-event'),
    path('dashboard/',dashboard,name='dashboard')
    
    
]



