from .task import Task


class Section:
    def __init__(self, name: str):
        self.name = name
        self.tasks = []

    def add_task(self, new_task: Task):
        if new_task.name in list(map(lambda a: a.name, self.tasks)):
            return f"Task is already in the section {self.name}"
        self.tasks.append(new_task)
        return f"Task {new_task.details()} is added to the section"

    def complete_task(self, task_name: str):
        tasks = [task.name for task in self.tasks]
        if task_name not in tasks:
            return f"Could not find task with name {task_name}"
        task = self.tasks[tasks.index(task_name)]
        task.completed = True
        return f"Completed task {task_name}"

    def clean_section(self):
        old_len = len(self.tasks)
        self.tasks = [task for task in self.tasks if not task.completed]
        removed_tasks = old_len - len(self.tasks)
        return f"Cleared {removed_tasks} tasks."

    def view_section(self):
        section_info = [f"Section {self.name}:"]
        tasks_info = [
            task.details() for task in self.tasks
        ]

        return '\n'.join(section_info+tasks_info) + '\n'
