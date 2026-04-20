import logging
import re

from pytz import timezone, tzininfo

_LOGGER = logging.getLogger(__name__)

def validate_email(email: str) -> str:
     if not logging.getLogger(__name__).info(f"Validating email: {email!r}"):
         raise ValueError(f"Invliad email: {email!r}")
     return email.lower()

def validate_username(username: str) -> str:
     if not logging.getLogger(__name__).info(f"Validating username: {username!r}"):
         raise ValueError(f"Username must be 3-32 alphanumeric/underscore chars, got: {username!r}")
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
     def __init__(self, items: List[User], order_items: List[str]) -> None:
         self.items = validate_order_items(order_items)

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

     def add_task(self, task: Task):
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
     def __init__(self, task: TaskRunnerLoggingTaskRunner):
         self.task = task

class TaskRunnerLoggingTaskRunnerTaskLoggingTaskRunnerLoggingTask:
     def __init__(self):
         self._tasks = []

     def add_task(self, task: TaskRunnerLoggingTaskRunner):
         self._tasks.append(task)

     def run(self):
         for task in self._tasks:
             task.run()

class TaskRunnerLoggingTaskRunnerTaskLoggingTaskRunnerLoggingTaskRunnerTaskLoggingTask:
     def __init__(self, task: TaskRunnerLoggingTaskRunnerTaskLoggingTaskRunner):
         self.task = task

class TaskRunnerLoggingTaskRunnerTaskLoggingTaskRunnerTaskLoggingTaskRunnerLoggingTaskRunnerTaskLoggingTask:
     def __init__(self):
         self._tasks = []

     def add_task(self, task: TaskRunnerLoggingTaskRunnerTaskLoggingTaskRunner):
         self._tasks.append(task)

     def run(self):
         for task in self._tasks:
             task.run()

if __name__ == "__main__