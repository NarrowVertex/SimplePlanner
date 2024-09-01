import ast
import uuid

import streamlit as st

from listener.PlanTaskInfoEditListener import PlanTaskInfoEditListener
from page.BasePage import BasePage
from page.component.Calendar import Calendar
from system.task.Task import create_task

from datetime import datetime


class PlanTaskInfoEditPage(BasePage):
    listener: PlanTaskInfoEditListener

    def __init__(self):
        super().__init__(PlanTaskInfoEditListener())

        self.new_task_type = ""
        self.new_name = ""
        self.new_description = ""
        self.new_trigger_time = ""
        self.new_start_time = ""
        self.new_end_time = ""
        self.new_time_list = ""

    def main(self):
        plan = self.get_parameters()[0]
        task = self.get_parameters()[1]
        task_type = task[2]

        st.title("Task")

        st.subheader("Task Type")
        task_type_options = ("trigger", "temporal", "periodic")
        self.new_task_type = st.selectbox(options=task_type_options, index=task_type_options.index(task[2]), key=f"{task[0]}_task_type",
                                          label="task_type", label_visibility="collapsed")

        st.subheader("Name")
        self.new_name = st.text_input(value=f"{task[3]}", key=f"{task[0]}_name",
                                      label="name", label_visibility="collapsed")

        st.subheader("Description")
        self.new_description = st.text_area(value=f"{task[4]}", key=f"{task[0]}_description", height=10,
                                            label="description", label_visibility="collapsed")

        if self.new_task_type == "trigger":
            st.subheader("Trigger Time")
            if task[5] != "":
                datetime_trigger_time = datetime.strptime(task[5], '%Y-%m-%d %H:%M:%S')

                datetime_trigger_time_date = datetime_trigger_time.date()
                datetime_trigger_time_time = datetime_trigger_time.time()
            else:
                datetime_trigger_time_date = "today"
                datetime_trigger_time_time = "now"

            date_column, time_column = st.columns(2)
            with date_column:
                new_datetime_trigger_time_date = st.date_input("Date", datetime_trigger_time_date)
            with time_column:
                new_datetime_trigger_time_time = st.time_input("Time", datetime_trigger_time_time, step=1800)

            self.new_trigger_time = (datetime.combine(new_datetime_trigger_time_date, new_datetime_trigger_time_time)
                                     .strftime('%Y-%m-%d %H:%M:%S'))

        elif self.new_task_type == "temporal":
            if task[6] != "" or task[7] != "":
                datetime_start_time = datetime.strptime(task[6], '%Y-%m-%d %H:%M:%S')
                datetime_end_time = datetime.strptime(task[7], '%Y-%m-%d %H:%M:%S')

                datetime_start_time_date = datetime_start_time.date()
                datetime_start_time_time = datetime_start_time.time()

                datetime_end_time_date = datetime_end_time.date()
                datetime_end_time_time = datetime_end_time.time()
            else:
                datetime_start_time_date = "today"
                datetime_start_time_time = "now"

                datetime_end_time_date = "today"
                datetime_end_time_time = "now"

            st.subheader("Start Time")
            start_time_date_column, start_time_time_column = st.columns(2)
            with start_time_date_column:
                new_datetime_start_time_date = st.date_input(label="Date", value=datetime_start_time_date,
                                                             key=f"{task[0]}_temporal_start_time_date")
            with start_time_time_column:
                new_datetime_start_time_time = st.time_input(label="Time", value=datetime_start_time_time, step=1800,
                                                             key=f"{task[0]}_temporal_start_time_time")

            st.subheader("End Time")
            end_time_date_column, end_time_time_column = st.columns(2)
            with end_time_date_column:
                new_datetime_end_time_date = st.date_input(label="Date", value=datetime_end_time_date,
                                                       key=f"{task[0]}_temporal_end_time_date")
            with end_time_time_column:
                new_datetime_end_time_time = st.time_input(label="Time", value=datetime_end_time_time, step=1800,
                                                       key=f"{task[0]}_temporal_end_time_time")

            self.new_start_time = (datetime.combine(new_datetime_start_time_date, new_datetime_start_time_time)
                                   .strftime('%Y-%m-%d %H:%M:%S'))
            self.new_end_time = (datetime.combine(new_datetime_end_time_date, new_datetime_end_time_time)
                                 .strftime('%Y-%m-%d %H:%M:%S'))

        elif self.new_task_type == "periodic":
            if task[6] != "" or task[7] != "":
                datetime_start_time = datetime.strptime(task[6], '%Y-%m-%d %H:%M:%S')
                datetime_end_time = datetime.strptime(task[7], '%Y-%m-%d %H:%M:%S')

                datetime_start_time_date = datetime_start_time.date()
                datetime_end_time_date = datetime_end_time.date()
            else:
                datetime_start_time_date = "today"
                datetime_end_time_date = "today"

            st.subheader("Start Time")
            new_datetime_start_time_date = st.date_input(label="Date", value=datetime_start_time_date,
                                                         key=f"{task[0]}_periodic_start_time_date",
                                                         label_visibility="collapsed")

            st.subheader("End Time")
            new_datetime_end_time_date = st.date_input(label="Date", value=datetime_end_time_date,
                                                       key=f"{task[0]}_periodic_end_time_date",
                                                       label_visibility="collapsed")

            self.new_start_time = new_datetime_start_time_date.strftime('%Y-%m-%d %H:%M:%S')
            self.new_end_time = new_datetime_end_time_date.strftime('%Y-%m-%d %H:%M:%S')

            st.subheader("Time List")
            init_events = task[8]
            if init_events == "":
                init_events = "[]"
            init_events = ast.literal_eval(init_events)

            calendar = Calendar(task[0], init_events)

            if st.button("add event"):
                event = {
                    "event_id": f"{uuid.uuid4()}",
                    "title": "test_event",
                    "start": "2024-09-01T15:00:00+09:00",
                    "end": "2024-09-01T16:30:00+09:00"
                }
                calendar.add_event(event)

            calendar.render()
            self.new_time_list = str(calendar.get_events())

    def side(self):
        st.title("Selection")

        if st.button("Save", use_container_width=True):
            plan = self.get_parameters()[0]
            task = self.get_parameters()[1]
            new_task = create_task(task[0], task[1], self.new_task_type, self.new_name, self.new_description,
                                   self.new_trigger_time, self.new_start_time, self.new_end_time, self.new_time_list)
            self.listener.change_task_info(new_task)
            task = self.listener.get_task(task[0])
            self.listener.switch_page("PlanTaskInfoPage", plan, task)

        if st.button("Cancel", use_container_width=True):
            plan = self.get_parameters()[0]
            task = self.get_parameters()[1]
            self.listener.switch_page("PlanTaskInfoPage", plan, task)

        st.divider()

        if st.button("Remove", use_container_width=True):
            plan = self.get_parameters()[0]
            task = self.get_parameters()[1]
            self.listener.remove_task(task[0])
            self.listener.switch_page("PlanSchedulePage", plan)

