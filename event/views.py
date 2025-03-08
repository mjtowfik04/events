from django.shortcuts import render,redirect,get_object_or_404
from django.http import HttpResponse
from event.forms import CategoryForm, EventForm, ParticipantForm  
from django.shortcuts import render
from .models import Event,Category,Participant
from django.utils.timezone import now
from django.contrib import messages
from django.shortcuts import get_object_or_404




def event_form(request):
    if request.method == "POST":
        event_form = EventForm(request.POST)
        participant_form = ParticipantForm(request.POST)

        if event_form.is_valid() and participant_form.is_valid():
            event = event_form.save()
            participant = participant_form.save(commit=False)
            participant.save()  
            participant.events.add(event)  
            messages.success(request, "Event added successfully!")
        else:
            messages.error(request, "Please fix the errors below.")
    else:
        event_form = EventForm()
        participant_form = ParticipantForm()

    context = {
        "event_form": event_form,
        "participant_form": participant_form,
    }
    return render(request, "test.html", context)


def update_event(request, id):
    participant = Participant.objects.get(id=id)

    if participant.events.exists():
        event = participant.events.first() 
    else:
        event = None 

    if request.method == "POST":
        event_form = EventForm(request.POST, instance=event)
        participant_form = ParticipantForm(request.POST, instance=participant)

        if event_form.is_valid() and participant_form.is_valid():
            updated_event = event_form.save()

            participant_form.save()
            participant.events.set([updated_event])  

            messages.success(request, "Event updated successfully!")
            return redirect("home-dashboard")  
        else:
            messages.error(request, "Please fix the errors below.")
    else:
        event_form = EventForm(instance=event)
        participant_form = ParticipantForm(instance=participant)

    context = {
        "event_form": event_form,
        "participant_form": participant_form,
    }
    return render(request, "test.html", context)



def delete(request, id):
    if request.method =='POST':
        event = get_object_or_404(Event, id=id)
        event.delete()
        messages.success(request, 'Task Deleted Successfully')
        return redirect('organizer-dashboard')  
    else:
            messages.error(request, 'Something went wrong')

    return (request,redirect('organizer-dashboard'))

 
    
def organizer_dashboard(request):
    type = request.GET.get('type', 'all')
    participants_all = Participant.objects.all()
    total_participant = participants_all.count()
    total_event = Event.objects.count()
    today = now().date()
    upcoming_events = Event.objects.filter(date__gte=today).order_by("date")
    past_events = Event.objects.filter(date__lt=today).order_by("-date")
    categories = Category.objects.all() 
    events = Event.objects.select_related('category').prefetch_related('participants').all()
    category_filter = request.GET.get("category", None)
    events = Event.objects.select_related("category").all()
    if category_filter:
        events = events.filter(category__name=category_filter)


    participants = None
    events = None  

    if type == 'totalparticipants':  
        participants = participants_all 
    elif type == 'total_events':
        events = Event.objects.all() 
    elif type == 'upcoming_events':
        events = upcoming_events 
    elif type == 'past_events':
        events = past_events  

    context = {
        "categories":categories,
        "events":events,
        "total_Participant": total_participant,
        "total_event": total_event,
        "upcoming_events": upcoming_events.count(),
        "past_events": past_events.count(),
        "participants": participants,  
        "events": events, 
    }


    return render(request, "dashboard/organizer_dashboard.html", context)


def home_dashboard(request):
    events = Event.objects.all()
    categorys = Event.objects.select_related('category').all()
    # status_choices = Category.STATUS_CHOICES 

    context = {
        "events": events,
        # "categorys": categorys,
        # "status_choices":status_choices,
    }
    return render(request, "dashboard/mana.html", context)