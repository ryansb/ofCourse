'''
Calendar management for ofCourse
Authors: Matt Soucy <msoucy@csh.rit.edu>
'''

from __future__ import print_function
from itertools import groupby
from operator import itemgetter
import re

from icalendar import Calendar, Event, vText

def load_calendar(fn):
    with open(fn) as infile:
        return Calendar.from_ical(infile.read())

def calendar_events(cal):
    return filter(lambda ev: type(ev) == Event, cal.subcomponents)

def sorted_events(cal):
    return sorted(calendar_events(cal), key=lambda ev: ev.decoded('dtstart'))

def normalize_categories(ev):
    ' Return an array of categories, all the time '
    if isinstance(ev['categories'], vText):
        return [str(ev['categories']).lower()]
    else:
        return [str(cat).lower() for cat in ev['categories']]

def calendar_weeks(cal):
    def week_num(ev):
        ' Simplest way without lots of string (un-)formatting '
        return ev.decoded('dtstart').isocalendar()[1]
    return [list(wk[1]) for wk in groupby(sorted_events(cal), week_num)]

assignment_re = re.compile(r"^(ASSIGNED|DUE): (.*)\w*(?:<(.*)>)")
def assignment_data(desc):
    ret = []
    for line in desc.split("\n"):
        evdata = assignment_re.match(line)
        if evdata:
            ret.append(evdata.groups(''))
    return ret

def items_assigned(items):
    return [it for it in items if it[0] == 'ASSIGNED']

def items_due(items):
    return [it for it in items if it[0] == 'DUE']
