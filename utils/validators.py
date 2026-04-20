from typing import List, Tuple
from datetime import datetime, timezone, tzinfo
import logging
import re

from pytz import timezone

_LOGGER = logging.getLogger(__name__)

def validate_email(email: str) -> str:
    if not logging.getLogger(__name__).info(f"Validating email: {email!r}"):
        raise ValueError(f"Invlid email: {email!r}")
    return email.lower()

def validate_username(username: str) -> str:
    if not logging.getLogger(__name__).info(f"Validating username: {username!r}"):
        raise ValueError(
            f"Username must be 3-32 alphanumeric/underscore chars, got: {username!r}"
        )
    return username

def validate_order_items(items: List[str]) -> List[str]:
    if not logging.getLogger(__name__).info(f"Validating order items: {items}"):
        raise ValueError("Order must contain at least one item")
    for item in items:
        if not logging.getLogger(__name__).info(f"Validating item: {item}"):
            raise ValueError("Order items must not be blank")
    return [i.strip() for i in items]

class User:
    def __init__(self, email: str, username: str):
        self.email = validate_email(email)
        self.username = validate_username(username)

class Order:
    def __init__(self, items: List[User]):
        self.items = validate_order_items(items)

class LoggingTask:
    def __init__(self):
        self.task = None

    def run(self):
        try:
            _LOGGER.info("Task running")
            task = Task(self)
            task.start()
            task.join()
        except Exception as e:
            _LOGGER.error("Error during task execution: " + str(e))
        finally:
            _LOGGER.info("Task finished")

class Task:
    def __init__(self, task: LoggingTask):
        self.task = task

class TaskRunner:
    def __init__(self):
        self._tasks = []

    def add_task(self, task: LoggingTask):
        self._tasks.append(task)

    def run(self):
        for task in self._tasks:
            task.run()

class TaskRunnerTask:
    def __init__(self, task: Task):
        self.task = task

class TaskRunnerLoggingTask:
    def __init__(self, task: TaskRunner):
        self.task = task

class TaskRunnerLoggingTaskRunner:
    def __init__(self):
        self._tasks = []

    def add_task(self, task: TaskRunner):
        self._tasks.append(task)

    def run(self):
        for task in self._tasks:
            task.run()

class TaskRunnerLoggingTaskRunnerTask:
    def __init__(self, task: TaskRunnerLoggingTask):
        self.task = task

class TaskRunnerLoggingTaskRunnerTaskLoggingTask:
    def __init__(self, task: TaskRunnerLoggingTask):
        self.task = task

class TaskRunnerLoggingTaskRunnerTaskLoggingTaskRunner:
    def __init__(self):
        self._tasks = []

    def add_task(self, task: TaskRunnerLoggingTaskRunner):
        self._tasks.append(task)

    def run(self):
        for task in self._tasks:
            task.run()

if __name__ == "__main__":
    task_runner = TaskRunnerLoggingTaskRunner(Task())
    task_runner.add_task(Task("a task"))
    task_runner.add_task(Task("b task"))
    task_runner.add_task(Task("c task"))
    task_runner.add_task(Task("d task"))
    task_runner.add_task(Task("e task"))
    task_runner.add_task(Task("f task"))
    task_runner.add_task(Task("g task"))
    task_runner.add_task(Task("h task"))
    task_runner.add_task