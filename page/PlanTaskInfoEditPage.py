import ast
import uuid
from typing import Union

import streamlit as st

from listener.PlanTaskInfoEditListener import PlanTaskInfoEditListener
from page.BasePage import BasePage
from page.component.Calendar import Calendar
from system.task.Task import create_task, BaseTask, TriggerTask, TemporalTask, PeriodicTask, create_empty_task, \
    transform_task

from datetime import datetime


def update_task_type(task, new_task_type):
    if task.task_type != new_task_type:
        return transform_task(task, new_task_type)
    return task


class PlanTaskInfoEditPage(BasePage):
    listener: PlanTaskInfoEditListener

    def __init__(self):
        super().__init__(PlanTaskInfoEditListener())

        self.new_task = create_empty_task()
        self.calendar = None

    def main(self):
        plan = self.get_parameters()[0]
        task = self.get_parameters()[1]

        self.new_task.task_id = task.task_id
        self.new_task.plan_id = task.plan_id

        task: Union[BaseTask, TriggerTask, TemporalTask, PeriodicTask]

        st.title("Task")

        st.subheader("Task Type")
        task_type_options = ("trigger", "temporal", "periodic")
        new_task_type = st.selectbox(options=task_type_options, index=task_type_options.index(task.task_type),
                                     key=f"{task.task_id}_task_type",
                                     label="task_type", label_visibility="collapsed")

        st.subheader("Name")
        self.new_task.name = st.text_input(value=f"{task.name}", key=f"{task.task_id}_name",
                                           label="name", label_visibility="collapsed")

        st.subheader("Description")
        self.new_task.description = st.text_area(value=f"{task.description}", key=f"{task.task_id}_description",
                                                 height=10, label="description", label_visibility="collapsed")

        if new_task_type == "trigger":
            self.new_task = update_task_type(self.new_task, new_task_type)

            st.subheader("Trigger Time")
            if hasattr(task, "trigger_time"):
                datetime_trigger_time = datetime.strptime(task.trigger_time, '%Y-%m-%d %H:%M:%S')

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

            self.new_task.trigger_time = (
                datetime.combine(new_datetime_trigger_time_date, new_datetime_trigger_time_time)
                .strftime('%Y-%m-%d %H:%M:%S'))

        elif new_task_type == "temporal":
            self.new_task = update_task_type(self.new_task, new_task_type)

            if hasattr(task, "start_time") and hasattr(task, "end_time"):
                datetime_start_time = datetime.strptime(task.start_time, '%Y-%m-%d %H:%M:%S')
                datetime_end_time = datetime.strptime(task.end_time, '%Y-%m-%d %H:%M:%S')

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
                                                             key=f"{task.task_id}_temporal_start_time_date")
            with start_time_time_column:
                new_datetime_start_time_time = st.time_input(label="Time", value=datetime_start_time_time, step=1800,
                                                             key=f"{task.task_id}_temporal_start_time_time")

            st.subheader("End Time")
            end_time_date_column, end_time_time_column = st.columns(2)
            with end_time_date_column:
                new_datetime_end_time_date = st.date_input(label="Date", value=datetime_end_time_date,
                                                           key=f"{task.task_id}_temporal_end_time_date")
            with end_time_time_column:
                new_datetime_end_time_time = st.time_input(label="Time", value=datetime_end_time_time, step=1800,
                                                           key=f"{task.task_id}_temporal_end_time_time")

            self.new_task.start_time = (datetime.combine(new_datetime_start_time_date, new_datetime_start_time_time)
                                        .strftime('%Y-%m-%d %H:%M:%S'))
            self.new_task.end_time = (datetime.combine(new_datetime_end_time_date, new_datetime_end_time_time)
                                      .strftime('%Y-%m-%d %H:%M:%S'))

        elif new_task_type == "periodic":
            self.new_task = update_task_type(self.new_task, new_task_type)

            if hasattr(task, "start_time") and hasattr(task, "end_time"):
                datetime_start_time = datetime.strptime(task.start_time, '%Y-%m-%d %H:%M:%S')
                datetime_end_time = datetime.strptime(task.end_time, '%Y-%m-%d %H:%M:%S')

                datetime_start_time_date = datetime_start_time.date()
                datetime_end_time_date = datetime_end_time.date()
            else:
                datetime_start_time_date = "today"
                datetime_end_time_date = "today"

            if hasattr(task, "time_list"):
                init_events = task.time_list
            else:
                init_events = ""

            st.subheader("Start Time")
            new_datetime_start_time_date = st.date_input(label="Date", value=datetime_start_time_date,
                                                         key=f"{task.task_id}_periodic_start_time_date",
                                                         label_visibility="collapsed")

            st.subheader("End Time")
            new_datetime_end_time_date = st.date_input(label="Date", value=datetime_end_time_date,
                                                       key=f"{task.task_id}_periodic_end_time_date",
                                                       label_visibility="collapsed")

            self.new_task.start_time = new_datetime_start_time_date.strftime('%Y-%m-%d %H:%M:%S')
            self.new_task.end_time = new_datetime_end_time_date.strftime('%Y-%m-%d %H:%M:%S')

            st.subheader("Time List")
            if init_events == "":
                init_events = "[]"
            init_events = ast.literal_eval(init_events)

            self.calendar = Calendar(task.task_id, init_events)

            if st.button("add event"):
                event = {
                    "event_id": f"{str(uuid.uuid4())}",
                    "title": "test_event",
                    "start": "2024-09-01T15:00:00+09:00",
                    "end": "2024-09-01T16:30:00+09:00"
                }
                self.calendar.add_event(event)

            self.calendar.render()
            self.new_task.time_list = str(self.calendar.get_events())

    def side(self):
        st.title("Selection")

        if st.button("Save", use_container_width=True):
            plan = self.get_parameters()[0]
            task = self.get_parameters()[1]
            self.listener.change_task_info(self.new_task)
            task = self.listener.get_task(task.task_id)
            self.calendar.update()
            self.listener.switch_page("PlanTaskInfoPage", plan, task)

        if st.button("Cancel", use_container_width=True):
            plan = self.get_parameters()[0]
            task = self.get_parameters()[1]
            self.listener.switch_page("PlanTaskInfoPage", plan, task)

        st.divider()

        if st.button("Remove", use_container_width=True):
            plan = self.get_parameters()[0]
            task = self.get_parameters()[1]
            self.listener.remove_task(task.task_id)
            self.listener.switch_page("PlanSchedulePage", plan)
