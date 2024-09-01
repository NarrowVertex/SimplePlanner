import streamlit as st
from streamlit_calendar import calendar

from copy import deepcopy


# 유저 수마다, 혹은 스케쥴마다 캘린더가 생성되고 session_state에 남게 되는 것이므로 이 메모리 관리를 해줄 가비지컬랙터가 따로 필요하거나
# 자체적으로 해결할 수단을 마련할 필요가 있음
class Calendar:
    def __init__(self, key, init_events):
        self.key_old_calendar_events = f'{key}_old_calendar_events'
        self.key_latest_calendar_events = f'{key}_latest_calendar_events'

        if f'{key}_old_calendar_events' not in st.session_state:
            st.session_state[self.key_old_calendar_events] = deepcopy(init_events)
            st.session_state[self.key_latest_calendar_events] = []

        """
        if f'{key}_calendar' not in st.session_state:
            st.session_state[f'{key}_calendar'] = self
        """

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
            "selectable": "true"
        }

    def render(self):
        callback = calendar(events=self.old_calendar_events, options=self.calendar_options)
        print("callback: \n", callback)

        if 'callback' in callback:
            if callback['callback'] == 'eventChange':
                self.update_event(callback['eventChange'])
            elif callback['callback'] == 'eventsSet':
                self.set_events(callback['eventsSet']['events'])

    def update_event(self, changed_event):
        # 기존 이벤트 리스트에서 해당 이벤트를 찾아 업데이트
        for event in self.latest_calendar_events:
            if event["event_id"] == changed_event["oldEvent"]["extendedProps"]["event_id"]:
                event["start"] = changed_event["event"]["start"]
                event["end"] = changed_event["event"]["end"]

    def set_events(self, events):
        self.latest_calendar_events.clear()
        for event in events:
            self.latest_calendar_events.append({
                "event_id": event["extendedProps"]["event_id"],
                "title": event["title"],
                "start": event["start"],
                "end": event["end"]
            })

    def add_event(self, event):
        self.update()
        self.old_calendar_events.append(event)

    def update(self):
        self.old_calendar_events = deepcopy(self.latest_calendar_events)

    def get_events(self):
        return self.latest_calendar_events

    @property
    def old_calendar_events(self):
        return st.session_state[self.key_old_calendar_events]

    @old_calendar_events.setter
    def old_calendar_events(self, new_value):
        st.session_state[self.key_old_calendar_events] = new_value

    @property
    def latest_calendar_events(self):
        return st.session_state[self.key_latest_calendar_events]
