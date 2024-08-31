import json

import streamlit as st
from streamlit_calendar import calendar

calendar_options = {
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
if 'calendar_events' not in st.session_state:
    st.session_state.calendar_events = [
    ]

custom_css = """
"""

if st.button("add event"):
    st.session_state.calendar_events.append({
        "title": "test_event",
        "start": "2024-08-30T15:00:00+09:00",
        "end": "2024-08-30T16:30:00+09:00"
    })

if st.button("check events"):
    print(st.session_state.calendar_events)

query = calendar(events=st.session_state.calendar_events, options=calendar_options, custom_css=custom_css)


def update_event(changed_event):
    # 기존 이벤트 리스트에서 해당 이벤트를 찾아 업데이트
    for event in st.session_state.calendar_events:
        if (event["title"] == changed_event["oldEvent"]["title"] and
                event["start"] == changed_event["oldEvent"]["start"] and
                event["end"] == changed_event["oldEvent"]["end"]):
            print("yes")
            event["start"] = changed_event["event"]["start"]
            event["end"] = changed_event["event"]["end"]


print(query)

# JSON 형식의 콜백 데이터를 처리
if 'callback' in query:
    if query['callback'] == 'eventChange':
        update_event(query['eventChange'])

st.write(calendar)
