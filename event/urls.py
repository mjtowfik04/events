from django.urls import path
from event.views import home,event_form,dashboard,update_event,delete

urlpatterns = [
    path('home/',home,name='home'),
    path('from/',event_form ,name="event_form"),
    path('dashboard/',dashboard,name='dashboard'),
    path('update-event/<int:id>/',update_event, name='update-event'),
    path('delete-event/<int:id>/',delete,name='delete-event')
    
    
]



