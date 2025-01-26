from django import template
from datetime import datetime
import pytz

register = template.Library()

@register.filter
def timesince_hours(value):
    now = datetime.now(pytz.utc)  # Ensure 'now' is timezone-aware
    if value.tzinfo is None:
        value = value.replace(tzinfo=pytz.utc)  # Make 'value' timezone-aware if it is naive
    diff = now - value
    hours = diff.total_seconds() // 3600
    return f"{int(hours)} hours ago"