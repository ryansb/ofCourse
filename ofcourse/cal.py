'''
Calendar management for ofCourse
Authors: Matt Soucy <msoucy@csh.rit.edu>
'''

from __future__ import print_function
from itertools import groupby
import re

from icalendar import Calendar, Event, vText


def load_calendar(fn):
    ' Load a calendar file and parse it into a Calendar structure '
    with open(fn) as infile:
        return Calendar.from_ical(infile.read())


def event_start_time(ev):
    '''
    Get the start time of an event
    Handle "all-day" events
    '''
    from datetime import datetime
    return datetime.fromordinal(ev.decoded('dtstart').toordinal())


def sorted_events(cal):
    ' Organize the relevant events from the calendar '
    return sorted([ev for ev in cal.subcomponents if type(ev) == Event],
                  key=event_start_time)


def normalize_categories(ev):
    ' Always return an array of categories '
    if isinstance(ev['categories'], vText):
        return [str(ev['categories']).lower()]
    else:
        return [str(cat).lower() for cat in ev['categories']]


def calendar_weeks(cal):
    ' Organize calendar event by week '
    def week_num(ev):
        ' Simplest way without lots of string (un-)formatting '
        return ev.decoded('dtstart').isocalendar()[1]
    return [list(wk[1]) for wk in groupby(sorted_events(cal), week_num)]


assignment_re = re.compile(r"^(ASSIGNED|DUE): (.*)\w*(?:<(.*)>)")


def assignment_data(desc):
    ' Parse the description for assignments '
    ret = []
    for line in desc.split("\n"):
        evdata = assignment_re.match(line)
        if evdata:
            ret.append(evdata.groups(''))
    return ret


def items_assigned(items):
    ' Only return assignments that are newly assigned '
    return [it for it in items if it[0] == 'ASSIGNED']


def items_due(items):
    ' Only return assignments that are due '
    return [it for it in items if it[0] == 'DUE']
