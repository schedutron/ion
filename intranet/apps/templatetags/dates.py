# -*- coding: utf-8 -*-

import logging
from datetime import date as datetime_date
from datetime import datetime

from django import template

register = template.Library()
logger = logging.getLogger(__name__)


@register.filter(expects_localtime=True)
def fuzzy_time(time):
    """Formats a `datetime.time` object relative to the current time."""
    dt = time_to_date(time)
    return fuzzy_date(dt)


@register.filter(expects_localtime=True)
def time_to_date(time):
    """Returns a `datetime.datetime` object from a `datetime.time` object using the current date."""
    d = datetime_date.today()
    return datetime.combine(d, time)


@register.filter(expects_localtime=True)
def fuzzy_date(date):
    """Formats a `datetime.datetime` object relative to the current time."""

    date = date.replace(tzinfo=None)

    if date <= datetime.now():
        diff = datetime.now() - date

        seconds = diff.total_seconds()
        minutes = seconds // 60
        hours = minutes // 60

        if minutes <= 1:
            return "moments ago"
        elif minutes < 60:
            return "{} minutes ago".format(int(seconds // 60))
        elif hours < 24:
            hrs = int(diff.seconds // (60 * 60))
            return "{} hour{} ago".format(hrs, "s" if hrs != 1 else "")
        elif diff.days == 1:
            return "yesterday"
        elif diff.days < 7:
            return "{} days ago".format(int(seconds // (60 * 60 * 24)))
        elif diff.days < 14:
            return date.strftime("last %A")
        else:
            return date.strftime("%A, %B %d, %Y")
    else:
        diff = date - datetime.now()

        seconds = diff.total_seconds()
        minutes = seconds // 60
        hours = minutes // 60

        if minutes <= 1:
            return "moments ago"
        elif minutes < 60:
            return "in {} minutes".format(int(seconds // 60))
        elif hours < 24:
            hrs = int(diff.seconds // (60 * 60))
            return "in {} hour{}".format(hrs, "s" if hrs != 1 else "")
        elif diff.days == 1:
            return "tomorrow"
        elif diff.days < 7:
            return "in {} days".format(int(seconds // (60 * 60 * 24)))
        elif diff.days < 14:
            return date.strftime("next %A")
        else:
            return date.strftime("%A, %B %d, %Y")
