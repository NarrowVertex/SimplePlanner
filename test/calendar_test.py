import json
from copy import deepcopy

import streamlit as st
from streamlit_calendar import calendar


def update_event(changed_event):
    # 기존 이벤트 리스트에서 해당 이벤트를 찾아 업데이트
    for event in st.session_state.latest_calendar_events:
        if (event["title"] == changed_event["oldEvent"]["title"] and
                event["start"] == changed_event["oldEvent"]["start"] and
                event["end"] == changed_event["oldEvent"]["end"]):
            event["start"] = changed_event["event"]["start"]
            event["end"] = changed_event["event"]["end"]


def set_events(events):
    st.session_state.latest_calendar_events.clear()
    for event in events:
        st.session_state.latest_calendar_events.append({
            "title": event["title"],
            "start": event["start"],
            "end": event["end"]
        })


def add_event(event):
    st.session_state.old_calendar_events = deepcopy(st.session_state.latest_calendar_events)
    st.session_state.old_calendar_events.append(event)


class Calendar:
    def __init__(self):
        if 'old_calendar_events' not in st.session_state:
            st.session_state.old_calendar_events = [
            ]
            st.session_state.latest_calendar_events = [
            ]

        self.calendar_options = {
            "initialView": "timeGridWeek",
            "headerToolbar": {
                "left": "",
                "center": "",
                "right": "",
            },
            "allDaySlot": False,
            "dayHeaderFormat": {
                "weekday": 'short'
            },
            "editable": "true",
            "selectable": "true",
            "height": 1254
        }

    def render(self):
        callback = calendar(events=st.session_state.old_calendar_events, options=self.calendar_options)

        if 'callback' in callback:
            if callback['callback'] == 'eventChange':
                update_event(callback['eventChange'])
            elif callback['callback'] == 'eventsSet':
                set_events(callback['eventsSet']['events'])


if "calendar" not in st.session_state:
    st.session_state.calendar = Calendar()

if st.button("add event"):
    event = {
        "title": "test_event",
        "start": "2024-09-01T15:00:00+09:00",
        "end": "2024-09-01T16:30:00+09:00"
    }
    add_event(event)

if st.button("check events"):
    print(st.session_state.latest_calendar_events)

st.session_state.calendar.render()
