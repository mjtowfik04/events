from django import forms
from .models import Event, Participant, Category

class StyledFormMixin:

    default_classes = "border-2 border-gray-300 w-full rounded-lg shadow-sm p-2 focus:outline-none focus:border-rose-500 focus:ring-rose-500"

    def apply_styled_widgets(self):
        for field_name, field in self.fields.items():
            widget = field.widget
            widget.attrs.setdefault('class', self.default_classes)
            widget.attrs.setdefault('placeholder', f"Enter {field.label.lower()}")

            if isinstance(widget, forms.Textarea):
                widget.attrs['class'] += " resize-none"
                widget.attrs['rows'] = 5
            elif isinstance(widget, forms.Select):
                widget.attrs['class'] += " bg-white"
            elif isinstance(widget, forms.DateInput):
                widget.attrs.update({'class': self.default_classes, 'type': 'date'})
            elif isinstance(widget, forms.TimeInput):
                widget.attrs.update({'class': self.default_classes, 'type': 'time'})
            elif isinstance(widget, forms.CheckboxSelectMultiple):
                widget.attrs['class'] = "space-y-2"

class CategoryForm(StyledFormMixin, forms.ModelForm):
    class Meta:
        model = Category
        fields = []

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.apply_styled_widgets()

class ParticipantForm(StyledFormMixin, forms.ModelForm):
    class Meta:
        model = Participant
        fields = ['name', 'email', 'events']
        widgets = {
            'events': forms.CheckboxSelectMultiple()
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.apply_styled_widgets()


class EventForm(StyledFormMixin, forms.ModelForm):
    class Meta:
        model = Event
        fields = [ 'description', 'date', 'time', 'location', 'category']
        widgets = {
            'date': forms.DateInput(attrs={'type': 'date'}),
            'time': forms.TimeInput(attrs={'type': 'time'}),
            'category': forms.Select()
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.apply_styled_widgets()

