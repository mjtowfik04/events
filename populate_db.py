import os
import django
from faker import Faker
import random
from event.models import Category, Event, Participant
from django.contrib.auth.models import User

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'event_management.settings')
django.setup()

def create_unique_category(fake):
    name = fake.word().capitalize()
    while Category.objects.filter(name=name).exists():
        name = fake.word().capitalize()
    return Category.objects.create(name=name)

def populate_db():
    fake = Faker()

    # Create unique categories
    categories = [create_unique_category(fake) for _ in range(5)]
    print(f"Created {len(categories)} categories.")

    # Create events
    events = []
    for _ in range(10):
        event = Event.objects.create(
            name=fake.sentence(nb_words=4),
            description=fake.paragraph(),
            date=fake.date_this_year(),
            time=fake.time_object(),
            location=fake.city(),
            category=random.choice(categories)
        )
        events.append(event)
    print(f"Created {len(events)} events.")

    # Create participants and assign them random events
    participants = []
    for _ in range(20):
        email = fake.unique.email()
        participant = Participant.objects.create(
            name=fake.name(),
            email=email
        )
        assigned_events = random.sample(events, random.randint(1, 3))
        participant.events.add(*assigned_events)
        participants.append(participant)
    print(f"Created {len(participants)} participants.")

if __name__ == "__main__":
    populate_db()
