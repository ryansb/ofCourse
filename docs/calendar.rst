.. Calendar documentation

Adding events to the calendar
=============================

This tutorial will help you prepare a course outline for ofCourse.

About ofCourse scheduling
-------------------------

ofCourse schedules are in the `iCalendar format <https://en.wikipedia.org/wiki/ICalendar>`__.
The files, `course.ics`, can be edited in any calendar editor, including:

- Google Calendar
- Apple Calendar
- Lightning (for Mozilla Thunderbird and Seamonkey)

Events in ofCourse
------------------

Classes
+++++++

A class session is an event, optionally tagged with the "Class" category.

The event title will show up as the class topic.

The description gets parsed for lines that are formatted like so::

    ASSIGNED: First Flight Assignment <http://assignment/link>
    ASSIGNED: Bug Report (no link)
    DUE: Midterm Project Outline </hw/midterm>

These lines will appear in the "Assigned" and "Due" columns of the syllabus.

Hackathons
++++++++++

A hackathon is also an event, with the mandatory "Hackathon" tag.

The event location and URL (as a URL attachment) will be displayed.

Special Events
++++++++++++++

Special events (IRC meetings, field trips) are all ordinary calendar events, though with appropriate categories.

The default special categories are:

- `Special`
- `Cancelled`
- `Guest` - for guest lectures
- `Hackathon`
- `Vaycay` for vacations
