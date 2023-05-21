from tkinter import *
from tkinter import ttk
from tkcalendar import Calendar
import datetime
from abc import ABC, abstractmethod

class CalendarWindow:
    def __init__(self):
        self.root = Tk()
        self.root.title("Calendar and ToDo")
        self.root.geometry("1000x400+100+100")

        self.cal = Calendar(self.root, selectmode="day")
        self.cal.pack(fill="both", expand=True)

        self.tasks = {}  # 날짜별 일정을 저장하는 딕셔너리
        self.todo_window = ToDoWindow(self.root, self.tasks, self.cal)

        self.selection_var = StringVar()  # 작업 유형 선택을 위한 변수
        self.selection_var.set("Task")  # 기본값은 "Task"로 설정

        self.task_radio = Radiobutton(self.root, text="Task", variable=self.selection_var, value="Task")
        self.task_radio.pack(anchor="w")

        self.diary_radio = Radiobutton(self.root, text="Diary", variable=self.selection_var, value="Diary")
        self.diary_radio.pack(anchor="w")

        self.cal.bind("<<CalendarSelected>>", self.show_add_window)
    
    def update_task_listbox(self):
        self.todo_window.update_tasks()

    def show_add_window(self, event):
        selected_date = self.cal.get_date()
        add_window = None
        if self.selection_var.get() == "Task":
            add_window = AddTaskWindow(selected_date, self.tasks, self, self.todo_window)
        elif self.selection_var.get() == "Diary":
            add_window = AddDairyWindow(self)
        if add_window:
            add_window.open()

    def run(self):
        self.root.mainloop()


class ToDoWindow(Frame):
    def __init__(self, parent, tasks, calendar):
        super().__init__(parent)
        self.tasks = tasks

        self.task_label = Label(self, text="Task:")
        self.task_label.pack()

        self.task_listbox = Listbox(self)
        self.task_listbox.pack(fill=BOTH, expand=True)

        self.update_tasks()

        self.pack(fill=BOTH, expand=True)

    def update_tasks(self):
        self.task_listbox.delete(0, END)  # 기존 목록 삭제

        if self.tasks:
            # 빠른 날짜대로 정렬해서 보여주기
            sorted_dates = sorted(self.tasks.keys(), key=lambda date: datetime.datetime.strptime(date, "%m/%d/%y"))
            for date in sorted_dates:
                self.task_listbox.insert(END, f"Date: {date}")
                for task in self.tasks[date]:
                    self.task_listbox.insert(END, f"- {task}")
                self.task_listbox.insert(END, "")  # 줄 간격을 위한 빈 줄 추가
        else:
            self.task_listbox.insert(END, "No tasks")
    
# 전력패턴 인터페이스
class IStrategy(ABC):
    @abstractmethod
    def open(self):
        pass

# Concrete strategy1
class AddTaskWindow(IStrategy):
    def __init__(self, selected_date, tasks, calendar_window, todo_window):
        self.add_task_window = Tk()
        self.add_task_window.title("Add Task")
        self.add_task_window.geometry("300x400+1100+100")

        self.selected_date = selected_date
        self.tasks = tasks
        self.calendar_window = calendar_window
        self.todo_window = todo_window

        self.date_label = Label(self.add_task_window, text="Date:")
        self.date_label.pack()

        self.date_text = Label(self.add_task_window, text="")
        self.date_text.pack()

        self.task_label = Label(self.add_task_window, text="Task:")
        self.task_label.pack()

        self.task_entry = Entry(self.add_task_window)
        self.task_entry.pack()

        self.task_listbox = Listbox(self.add_task_window)
        self.task_listbox.pack()

        self.task_listbox.bind("<<ListboxSelect>>", self.enable_buttons)  # Listbox 선택 이벤트에 바인딩

        self.update_date()
        self.update_task_listbox()

    def update_date(self):
        selected_date = self.calendar_window.cal.get_date()
        self.date_text.config(text=f"Selected Date: {selected_date}")

    def enable_buttons(self, event):
        selected_index = self.task_listbox.curselection()
        if selected_index:
            self.delete_button.config(state=NORMAL)
            self.complete_button.config(state=NORMAL)
        else:
            self.delete_button.config(state=DISABLED)
            self.complete_button.config(state=DISABLED)

    def update_task_listbox(self):
        self.task_listbox.delete(0, END)
        selected_date = self.calendar_window.cal.get_date()
        if selected_date in self.calendar_window.tasks:
            tasks = self.calendar_window.tasks[selected_date]
            for task in tasks:
                self.task_listbox.insert(END, task)

    def create_command_objects(self):
        self.add_task_command = AddTaskCommand(self.task_listbox, self.task_entry, self.calendar_window, self.todo_window)
        self.delete_task_command = DeleteTaskCommand(self.task_listbox, self.calendar_window, self.todo_window)
        self.complete_task_command = CompleteTaskCommand(self.task_listbox, self.calendar_window, self.todo_window)

    def create_buttons(self):
        self.add_button = Button(self.add_task_window, text="Add Task", command=self.add_task_command.execute)
        self.add_button.pack()

        self.delete_button = Button(self.add_task_window, text="Delete Task", command=self.delete_task_command.execute)
        self.delete_button.pack()

        self.complete_button = Button(self.add_task_window, text="Complete Task", command=self.complete_task_command.execute)
        self.complete_button.pack()

    def open(self):
        self.create_command_objects()
        self.create_buttons()
        self.add_task_window.mainloop()


# Concrete strategy1
class AddDairyWindow(IStrategy):
    def __init__(self, calendar_window):
        self.dairy_window = Tk()
        self.dairy_window.title("Add Diary")
        self.dairy_window.geometry("300x400+1100+100")

        self.calendar_window = calendar_window

        self.date_label = Label(self.dairy_window, text="Date:")
        self.date_label.pack()

        self.date_text = Label(self.dairy_window, text="")
        self.date_text.pack()

        self.dairy_label = Label(self.dairy_window, text="Diary:")
        self.dairy_label.pack()

        self.dairy_entry = Entry(self.dairy_window)
        self.dairy_entry.pack()

        self.save_button = Button(self.dairy_window, text="Save", command=self.save_diary)
        self.save_button.pack()

        self.update_date()

    def update_date(self):
        selected_date = self.calendar_window.cal.get_date()
        self.date_text.config(text=f"Selected Date: {selected_date}")

    def save_diary(self):
        diary = self.dairy_entry.get().strip()
        if diary:
            selected_date = self.calendar_window.cal.get_date()
            # Diary 저장 또는 업데이트하는 로직 추가
            # 예: self.calendar_window.diaries[selected_date] = diary
            self.dairy_window.destroy()

    def open(self):
        self.dairy_window.mainloop()
        

class Command(ABC):
    @abstractmethod
    def execute(self):
        pass

    def update_task_listbox(self):
        self.task_listbox.delete(0, END)
        selected_date = self.calendar_window.cal.get_date()
        if selected_date in self.calendar_window.tasks:
            tasks = self.calendar_window.tasks[selected_date]
            for task in tasks:
                self.task_listbox.insert(END, task)

# 할 일 추가
class AddTaskCommand(Command):
    def __init__(self, task_listbox, task_entry, calendar_window, todo_window):
        self.task_listbox = task_listbox
        self.task_entry = task_entry
        self.calendar_window = calendar_window
        self.todo_window = todo_window

    def execute(self):
        task = self.task_entry.get().strip()
        if task:
            selected_date = self.calendar_window.cal.get_date()
            if selected_date not in self.calendar_window.tasks:
                self.calendar_window.tasks[selected_date] = []
            self.calendar_window.tasks[selected_date].append(task)
            self.calendar_window.update_task_listbox()
            self.todo_window.update_tasks()
            self.update_task_listbox()
            self.task_entry.delete(0, END)

# 할 일 삭제
class DeleteTaskCommand(Command):
    def __init__(self, task_listbox, calendar_window, todo_window):
        self.task_listbox = task_listbox
        self.calendar_window = calendar_window
        self.todo_window = todo_window

    def execute(self):
        selected_index = self.task_listbox.curselection()
        if selected_index:
            selected_task = self.task_listbox.get(selected_index)
            selected_date = self.calendar_window.cal.get_date()
            if selected_date in self.calendar_window.tasks and selected_task in self.calendar_window.tasks[selected_date]:
                self.calendar_window.tasks[selected_date].remove(selected_task)
                self.calendar_window.update_task_listbox()
                self.update_task_listbox()
                self.todo_window.update_tasks()

# 할 일 완료 표시
class CompleteTaskCommand(Command):
    def __init__(self, task_listbox, calendar_window, todo_window):
        self.task_listbox = task_listbox
        self.calendar_window = calendar_window
        self.todo_window = todo_window

    def execute(self):
        selected_index = self.task_listbox.curselection()
        if selected_index:
            selected_task = self.task_listbox.get(selected_index)
            selected_date = self.calendar_window.cal.get_date()
            if selected_date in self.calendar_window.tasks and selected_task in self.calendar_window.tasks[selected_date]:
                self.calendar_window.tasks[selected_date].remove(selected_task)
                completed_task = f"{selected_task} ✔"
                self.calendar_window.tasks[selected_date].append(completed_task)
                self.calendar_window.update_task_listbox()
                self.update_task_listbox()
                self.todo_window.update_tasks()


if __name__ == "__main__":
    calendar_window = CalendarWindow()
    calendar_window.run()