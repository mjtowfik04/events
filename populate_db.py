import os
import django
from faker import Faker
import random
from event.models import Category, Event, Participant

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'event_management.settings')
django.setup()

def populate_db():
    fake = Faker()

    categories = [Category.objects.create(name=fake.word().capitalize()) for _ in range(5)]
    print(f"Created {len(categories)} categories.")

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

    participants = []
    for _ in range(20):
        while True:
            email = fake.email()
            if not Participant.objects.filter(email=email).exists():  
                break

        participant = Participant.objects.create(
            name=fake.name(),
            email=email,
        )
        participants.append(participant)

    print(f"Created {len(participants)} participants.")

    for event in events:
        assigned_participants = random.sample(participants, random.randint(1, 5))
        event.participants.add(*assigned_participants)  

    print("Assigned participants to events.")
    print("Database populated successfully!")

if __name__ == "__main__":
    populate_db()
