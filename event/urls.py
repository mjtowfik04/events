from django.urls import path
from event.views import event_form,organizer_dashboard,update_event,delete,home_dashboard
urlpatterns = [
    # path('home/',home,name='home'),
    path('from/',event_form ,name="event_form"),
    path('organizer-dashboard/',organizer_dashboard,name='organizer-dashboard'),
    path('update-event/<int:id>/',update_event, name='update-event'),
    path('delete-event/<int:id>/',delete,name='delete-event'),
    path('home-dashboard/',home_dashboard,name='home-dashboard')
    
    
]



