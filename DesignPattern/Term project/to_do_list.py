from tkinter import *
from tkinter import ttk
from tkcalendar import Calendar
from tkinter import messagebox
from tkinter.ttk import Combobox
from collections import defaultdict

from PIL import ImageTk
from PIL import Image
import os

import datetime
from abc import ABC, abstractmethod


class App(Tk):
    def __init__(self):
        super().__init__()
        self.title("나의 일상을 담아보세요")
        self.geometry("1000x400+100+100")
        self.resizable(0, 0)
        self._font = (None, 13)
        self._bg = "#ffffff"
        self._green = "#349E71"
        self._green2 = "#CDEFE0"
        style = ttk.Style()
        # 스타일 설정
        style.theme_use("clam")
        style.map("TCombobox", fieldbackground=[("readonly", "#ffffff")])
        style.map("TCombobox", selectbackground=[("readonly", "#ffffff")])
        style.map("TCombobox", selectforeground=[("readonly", "#000000")])
        style.map("TCombobox", background=[("readonly", "#ffffff")])
        style.configure("TNotebook", background=self._green)
        style.configure("TNotebook.Tab", font=(None, 10))
        style.map("TNotebook.Tab", background=[("selected", "#FEDF51")])

        ico_path = os.path.join(os.getcwd(), r"/Users/leewonseok/Desktop/coding/python_study/DesignPattern/Term project/img/icon.ico")  
        self.iconbitmap(ico_path)
        self._frame = None

        self.config(bg="#ffffff")
        Label(self, bg=self._bg, height=4).pack(fill="x")  # 상단 여백을 위해 추가
        # 로고 설정
        image = Image.open(r"/Users/leewonseok/Desktop/coding/python_study/DesignPattern/Term project/img/logo.jpg")
        photo_logo = ImageTk.PhotoImage(image)

        label_logo = Label(self, image=photo_logo, bg=self._bg)
        label_logo.image = photo_logo
        label_logo.pack()
        # 시작 버튼
        image = Image.open(r"/Users/leewonseok/Desktop/coding/python_study/DesignPattern/Term project/img/button-start.png")
        photo_button = ImageTk.PhotoImage(image)
        # self.cw = CalendarWindow()
        button = Button(
            self,
            image=photo_button,
            relief="flat",
            bg=self._bg,
            command=self.open_calendar_window
            # command=lambda: master.refresh_frame(cw),
        )
        button.image = photo_button
        button.pack(ipadx=3, ipady=2)

    def open_calendar_window(self):
        cw = CalendarWindow()  # CalendarWindow 인스턴스 생성
        cw.run()

class CalendarWindow:
    def __init__(self):
        self.root = Toplevel() 
        self.root.title("Calendar and ToDo")
        self.root.geometry("1000x400+100+100")

        self.cal = Calendar(self.root, selectmode="day")
        self.cal.pack(fill="both", expand=True)

        self.tasks = {}  # 날짜별 일정을 저장하는 딕셔너리
        self.todo_window = ToDoWindow(self.root, self.tasks, self.cal)

        self.diary_dict = defaultdict(Diary)  # 날짜별 일기를 저장하는 딕셔너리

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
            if selected_date in self.diary_dict:
                diary = self.diary_dict[selected_date]
                self.show_diary(diary)
            else:
                add_window = AddDiaryWindow(self, selected_date)
        if add_window:
            add_window.open()
    
    def save_diary(self, diary):
        date = diary.date
        self.diary_dict[date]= diary

    # 일기가 저장되어 있는 날짜를 다시 클릭했을 때 저장된 일기를 보여주는 함수
    def show_diary(self, diary):
        self.view_window = Toplevel()
        self.view_window.title("View Diary")
        self.view_window.geometry("300x500+1100+100")
        self.date_label = Label(self.view_window, text="Date:")
        self.date_label.pack()
        self.date_text = Label(self.view_window, text=diary.date)
        self.date_text.pack()
        self.title_label = Label(self.view_window, text="Title:")
        self.title_label.pack()
        self.title_text = Label(self.view_window, text=diary.title)
        self.title_text.pack()
        self.content_label = Label(self.view_window, text="Content:")
        self.content_label.pack()
        self.content_text = Text(self.view_window, height=10, width=40)
        self.content_text.insert("1.0", diary.content)
        self.content_text.configure(state="disabled")
        self.content_text.pack()
        self.additional_info_label = Label(self.view_window, text="Additional Info:")
        self.additional_info_label.pack()

        if isinstance(diary, WorkOutDiary):
            self.additional_info_text = Label(self.view_window, text=f"Body Part: {diary.body_part}, Time: {diary.time}")
        elif isinstance(diary, BookDiary):
            self.additional_info_text = Label(
                self.view_window,
                text=f"Book Title: {diary.book_title}, Author: {diary.author}, Start Page: {diary.start_page}, End Page: {diary.end_page}",
            )
        else:
            self.additional_info_text = Label(self.view_window, text="No additional info")
        self.additional_info_text.pack()
        self.edit_button = Button(self.view_window, text="Edit", command=lambda: self.edit_diary(diary))
        self.edit_button.pack()

        self.close_button = Button(self.view_window, text="Close", command=self.close_view_window)
        self.close_button.pack()

    # 일기를 편집하는 함수
    def edit_diary(self, diary):
        self.edit_window = Toplevel()
        self.edit_window.title("Edit Diary")
        self.edit_window.geometry("300x500+1100+100")

        self.title_label = Label(self.edit_window, text="Title:")
        self.title_label.pack()

        self.title_entry = Entry(self.edit_window)
        self.title_entry.insert(0, diary.title)
        self.title_entry.pack()

        self.content_label = Label(self.edit_window, text="Content:")
        self.content_label.pack()

        self.content_text = Text(self.edit_window, height=10, width=40)
        self.content_text.insert("1.0", diary.content)
        self.content_text.pack()

        if isinstance(diary, WorkOutDiary):
            self.body_part_label = Label(self.edit_window, text="Body Part:")
            self.body_part_label.pack()

            self.body_part_entry = Entry(self.edit_window)
            self.body_part_entry.insert(0, diary.body_part)
            self.body_part_entry.pack()

            self.time_label = Label(self.edit_window, text="Time:")
            self.time_label.pack()

            self.time_entry = Entry(self.edit_window)
            self.time_entry.insert(0, diary.time)
            self.time_entry.pack()

        elif isinstance(diary, BookDiary):
            self.book_title_label = Label(self.edit_window, text="Book Title:")
            self.book_title_label.pack()

            self.book_title_entry = Entry(self.edit_window)
            self.book_title_entry.insert(0, diary.book_title)
            self.book_title_entry.pack()

            self.author_label = Label(self.edit_window, text="Author:")
            self.author_label.pack()

            self.author_entry = Entry(self.edit_window)
            self.author_entry.insert(0, diary.author)
            self.author_entry.pack()

            self.start_page_label = Label(self.edit_window, text="Start Page:")
            self.start_page_label.pack()

            self.start_page_entry = Entry(self.edit_window)
            self.start_page_entry.insert(0, diary.start_page)
            self.start_page_entry.pack()

            self.end_page_label = Label(self.edit_window, text="End Page:")
            self.end_page_label.pack()

            self.end_page_entry = Entry(self.edit_window)
            self.end_page_entry.insert(0, diary.end_page)
            self.end_page_entry.pack()

        self.save_button = Button(self.edit_window, text="Save", command=lambda: self.save_edited_diary(diary))
        self.save_button.pack()

        self.close_button = Button(self.edit_window, text="Close", command=self.close_edit_window)
        self.close_button.pack()

    # 편집한 일기를 저장하는 함수
    def save_edited_diary(self, diary):
        # diary.date = self.date_entry.get()
        diary.title = self.title_entry.get()
        diary.content = self.content_text.get("1.0", "end")

        if isinstance(diary, WorkOutDiary):
            diary.body_part = self.body_part_entry.get()
            diary.time = self.time_entry.get()

        elif isinstance(diary, BookDiary):
            diary.book_title = self.book_title_entry.get()
            diary.author = self.author_entry.get()
            diary.start_page = self.start_page_entry.get()
            diary.end_page = self.end_page_entry.get()
            
        self.save_diary(diary)
        self.edit_window.destroy()
        self.show_diary(diary)
    
    def close_edit_window(self):
        self.edit_window.destroy()

    def close_view_window(self):
        self.view_window.destroy()

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
                date_parts = date.split("/")  # "/"를 기준으로 문자열을 분할하여 리스트로 반환
                month = int(date_parts[0])  # 월 값 추출
                day = int(date_parts[1])  # 일 값 추출
                year = int(date_parts[2])  # 연도 값 추출
                self.task_listbox.insert(END, f"Date: {year}년 {month}월 {day}일")
                for task in self.tasks[date]:
                    self.task_listbox.insert(END, f"- {task}")
                self.task_listbox.insert(END, "")  # 줄 간격을 위한 빈 줄 추가
        else:
            self.task_listbox.insert(END, "아직 등록된 일이 없습니다. 하루를 계획해 보세요.")
    
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
        date_parts = selected_date.split("/")  # "/"를 기준으로 문자열을 분할하여 리스트로 반환
        month = int(date_parts[0])  # 월 값 추출
        day = int(date_parts[1])  # 일 값 추출
        year = int(date_parts[2])  # 연도 값 추출
        self.date_text.config(text=f"Selected Date: {year}년 {month}월 {day}일")

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

        self.close_button = Button(self.add_task_window, text="Close", command=self.close_window)
        self.close_button.pack()
    
    def close_window(self):
        self.add_task_window.destroy()

    def open(self):
        self.create_command_objects()
        self.create_buttons()
        self.add_task_window.mainloop()


# Concrete strategy2
class AddDiaryWindow(IStrategy):
    def __init__(self, calendar_window, selected_date):
        self.diary_window = Tk()
        self.diary_window.title("Add Diary")
        self.diary_window.geometry("300x500+1100+100")

        self.calendar_window = calendar_window
        self.selected_date = selected_date

        self.date_label = Label(self.diary_window, text="Date:")
        self.date_label.pack()

        self.date_text = Label(self.diary_window, text="")
        self.date_text.pack()

        self.diary_type_label = Label(self.diary_window, text="Diary Type:")
        self.diary_type_label.pack()

        self.diary_type_combobox = Combobox(self.diary_window, values=["General Diary", "Workout Diary", "Book Diary"])
        self.diary_type_combobox.pack()

        self.title_label = Label(self.diary_window, text="제목:")
        self.title_label.pack()

        self.title_entry = Entry(self.diary_window)
        self.title_entry.pack()

        self.content_label = Label(self.diary_window, text="내용:")
        self.content_label.pack()

        self.content_entry = Text(self.diary_window, width = 25, height=5, relief="solid") 
        self.content_entry.pack()

        self.save_button = Button(self.diary_window, text="Save", command=self.save_diary)

        self.diary_type_combobox.bind("<<ComboboxSelected>>", self.handle_diary_type_selection)

        # Workout Diary에 필요한 추가 입력 필드
        self.sport_kind_label = Label(self.diary_window, text="운동 종류:")
        self.sport_kind_entry = Entry(self.diary_window)
        self.body_part_label = Label(self.diary_window, text="운동 부위:")
        self.body_part_entry = Entry(self.diary_window)
        self.time_label = Label(self.diary_window, text="시간:")
        self.time_entry = Entry(self.diary_window)
        self.sport_content_label = Label(self.diary_window, text="운동 내용:")
        self.sport_content_entry = Text(self.diary_window, width = 25, height=5, relief="solid") 
        

        # Book Diary에 필요한 추가 입력 필드
        self.book_title_label = Label(self.diary_window, text="책 제목:")
        self.book_title_entry = Entry(self.diary_window)
        self.author_label = Label(self.diary_window, text="작가:")
        self.author_entry = Entry(self.diary_window)
        self.start_page_label = Label(self.diary_window, text="시작 페이지:")
        self.start_page_entry = Entry(self.diary_window)
        self.end_page_label = Label(self.diary_window, text="마지막 페이지:")
        self.end_page_entry = Entry(self.diary_window)
        self.book_content_label = Label(self.diary_window, text="독후감:")
        self.book_content_entry = Text(self.diary_window, width = 25, height=5, relief="solid") 

        self.close_button = Button(self.diary_window, text="Close", command=self.close_window)
        self.close_button.pack(side="bottom")
        self.save_button.pack(side="bottom")


    def handle_diary_type_selection(self, event):
        selected_type = self.diary_type_combobox.get()
        if selected_type == "Workout Diary":
            # Workout Diary 선택 시 추가 입력 필드 표시
            self.sport_kind_label.pack()
            self.sport_kind_entry.pack()
            self.body_part_label.pack()
            self.body_part_entry.pack()
            self.time_label.pack()
            self.time_entry.pack()
            self.sport_content_label.pack()
            self.sport_content_entry.pack()
            # 일상 일기 콘텐츠 숨기기
            self.title_label.pack_forget()
            self.title_entry.pack_forget()
            self.content_label.pack_forget()
            self.content_entry.pack_forget()

            # 독서 일기 콘텐츠 숨기기
            self.book_title_label.pack_forget()
            self.book_title_entry.pack_forget()
            self.author_label.pack_forget()
            self.author_entry.pack_forget()
            self.start_page_label.pack_forget()
            self.start_page_entry.pack_forget()
            self.end_page_label.pack_forget()
            self.end_page_entry.pack_forget()
            self.book_content_label.pack_forget()
            self.book_content_entry.pack_forget()

        elif selected_type == "Book Diary":
            # 일상 일기 콘텐츠 숨기기
            self.title_label.pack_forget()
            self.title_entry.pack_forget()
            self.content_label.pack_forget()
            self.content_entry.pack_forget()
            # 운동 일기 콘텐츠 숨기기
            self.body_part_label.pack_forget()
            self.body_part_entry.pack_forget()
            self.time_label.pack_forget()
            self.time_entry.pack_forget()
            self.sport_kind_label.pack_forget()
            self.sport_kind_entry.pack_forget()
            self.sport_content_label.pack_forget()
            self.sport_content_entry.pack_forget()
            

            # Book Diary 선택 시 추가 입력 필드 표시
            self.book_title_label.pack()
            self.book_title_entry.pack()
            self.author_label.pack()
            self.author_entry.pack()
            self.start_page_label.pack()
            self.start_page_entry.pack()
            self.end_page_label.pack()
            self.end_page_entry.pack()
            self.book_content_label.pack()
            self.book_content_entry.pack()
            self.body_part_label.pack_forget()
            self.body_part_entry.pack_forget()
            self.time_label.pack_forget()
            self.time_entry.pack_forget()
        else:
            self.title_label.pack()
            self.title_entry.pack()
            self.content_label.pack()
            self.content_entry.pack()
            # 다른 Diary 선택 시 추가 입력 필드 숨김
            self.body_part_label.pack_forget()
            self.body_part_entry.pack_forget()
            self.time_label.pack_forget()
            self.time_entry.pack_forget()
            self.sport_kind_label.pack_forget()
            self.sport_kind_entry.pack_forget()
            self.sport_content_label.pack_forget()
            self.book_title_label.pack_forget()
            self.book_title_entry.pack_forget()
            self.author_label.pack_forget()
            self.author_entry.pack_forget()
            self.start_page_label.pack_forget()
            self.start_page_entry.pack_forget()
            self.end_page_label.pack_forget()
            self.end_page_entry.pack_forget()
            self.book_content_label.pack_forget()
            self.book_content_entry.pack_forget()
    
        self.update_date()

    # 일기를 보여주는 함수
    def show_diary(self, diary):
        self.diary_window.withdraw()  # 일기 추가 창 숨기기
        self.view_window = Toplevel(self.diary_window)
        self.view_window.title("View Diary")
        self.view_window.geometry("300x500+1100+100")

        self.date_label = Label(self.view_window, text="Date:")
        self.date_label.pack()

        date_parts = diary.date.split("/")  # "/"를 기준으로 문자열을 분할하여 리스트로 반환
        month = int(date_parts[0])  # 월 값 추출
        day = int(date_parts[1])  # 일 값 추출
        year = int(date_parts[2])  # 연도 값 추출

        self.date_text = Label(self.view_window, text=f"{year}년 {month}월 {day}일")

        self.date_text.pack()

        if isinstance(diary, WorkOutDiary):
            self.additional_info_text = Label(self.view_window, text=f"운동 종류: {diary.sport_kind}\n Body Part: {diary.body_part}\n Time: {diary.time}\n 운동 내용: {diary.sport_content}")
            self.title_label.pack_forget()
            self.content_label.pack_forget()
        elif isinstance(diary, BookDiary):
            self.additional_info_text = Label(
                self.view_window,
                text=f"책 제목: {diary.book_title}\n 작가: {diary.author}\n 시작 페이지: {diary.start_page}\n 마지막 페이지: {diary.end_page}\n 독후감: {diary.book_content}",
            )
        else:
            self.title_label = Label(self.view_window, text="제목:")
            self.title_label.pack()

            self.title_text = Label(self.view_window, text=diary.title)
            self.title_text.pack()

            self.content_label = Label(self.view_window, text="내용:")
            self.content_label.pack()
            self.content_text = Text(self.view_window, height=10, width=40)
            self.content_text.insert("1.0", diary.content)
            self.content_text.configure(state="disabled")
            self.content_text.pack()

            self.additional_info_text = Label(self.view_window, text="No additional info")

        self.additional_info_text.pack()

        self.edit_button = Button(self.view_window, text="Edit", command=lambda: self.edit_diary(diary))
        self.edit_button.pack()

        self.close_button = Button(self.view_window, text="Close", command=self.close_view_window)
        self.close_button.pack()

    # 일기를 편집하는 함수
    def edit_diary(self, diary):
        self.diary_window.withdraw()  # 일기 추가 창 숨기기
        self.edit_window = Toplevel(self.diary_window)
        self.edit_window.title("Edit Diary")
        self.edit_window.geometry("300x500+1100+100")

        self.title_label = Label(self.edit_window, text="Title:")
        self.title_label.pack()

        if isinstance(diary, WorkOutDiary):

            self.sport_kind_label = Label(self.edit_window, text="운동 종류:")
            self.sport_kind_label.pack()

            self.sport_kind_entry = Entry(self.edit_window)
            self.sport_kind_entry.insert(0, diary.sport_kind)
            self.sport_kind_entry.pack()

            self.body_part_label = Label(self.edit_window, text="운동 부위:")
            self.body_part_label.pack()

            self.body_part_entry = Entry(self.edit_window)
            self.body_part_entry.insert(0, diary.body_part)
            self.body_part_entry.pack()

            self.time_label = Label(self.edit_window, text="시간:")
            self.time_label.pack()

            self.time_entry = Entry(self.edit_window)
            self.time_entry.insert(0, diary.time)
            self.time_entry.pack()

            self.sport_content_label = Label(self.edit_window, text="운동 내용:")
            self.sport_content_label.pack()
            self.sport_content_entry = Text(self.edit_window, width = 25, height=5, relief="solid") 
            self.sport_content_entry.insert("1.0", diary.sport_content)
            self.sport_content_entry.pack()
            

        elif isinstance(diary, BookDiary):
            self.book_title_label = Label(self.edit_window, text="책 제목:")
            self.book_title_label.pack()

            self.book_title_entry = Entry(self.edit_window)
            self.book_title_entry.insert(0, diary.book_title)
            self.book_title_entry.pack()

            self.author_label = Label(self.edit_window, text="작가:")
            self.author_label.pack()

            self.author_entry = Entry(self.edit_window)
            self.author_entry.insert(0, diary.author)
            self.author_entry.pack()

            self.start_page_label = Label(self.edit_window, text="시작 페이지:")
            self.start_page_label.pack()

            self.start_page_entry = Entry(self.edit_window)
            self.start_page_entry.insert(0, diary.start_page)
            self.start_page_entry.pack()

            self.end_page_label = Label(self.edit_window, text="마지막 페이지:")
            self.end_page_label.pack()

            self.end_page_entry = Entry(self.edit_window)
            self.end_page_entry.insert(0, diary.end_page)
            self.end_page_entry.pack()

            self.book_content_label = Label(self.edit_window, text="독후감:")
            self.book_content_label.pack()

            self.book_content_entry = Text(self.edit_window, width = 25, height=5, relief="solid") 
            self.book_content_entry.insert("1.0", diary.book_content)
            self.book_content_entry.pack()
        
        else:
            self.title_entry = Entry(self.edit_window)
            self.title_entry.insert(0, diary.title)
            self.title_entry.pack()

            self.content_label = Label(self.edit_window, text="Content:")
            self.content_label.pack()

            self.content_text = Text(self.edit_window, height=10, width=40)
            self.content_text.insert("1.0", diary.content)
            self.content_text.pack()

        self.save_button = Button(self.edit_window, text="Save", command=lambda: self.save_edited_diary(diary))
        self.save_button.pack()

        self.close_button = Button(self.edit_window, text="Close", command=self.close_edit_window)
        self.close_button.pack()

    # 초기 작성한 일기를 저장하는 함수
    def save_diary(self):
        diary_type = self.diary_type_combobox.get()
        title = self.title_entry.get().strip()
        content = self.content_entry.get("1.0", "end-1c").strip()

        if diary_type == "General Diary":
            # General Diary 작성 코드
            if title and content:
                diary_builder = DiaryBuilder().set_date(self.selected_date).set_title(title).set_content(content)
                diary = diary_builder.build()
                self.calendar_window.save_diary(diary)  # 일기 저장
                self.show_diary(diary)
        elif diary_type == "Workout Diary":
            # Workout Diary 작성 코드
            sport_kind = self.sport_kind_entry.get().strip()
            body_part = self.body_part_entry.get().strip()
            time = self.time_entry.get().strip()
            sport_content = self.sport_content_entry.get("1.0", "end-1c").strip()
            if body_part and time and sport_kind and sport_content:
                diary_builder = WorkOutDiaryBuilder().set_date(self.selected_date)
                diary_builder.set_sport_kind(sport_kind).set_body_part(body_part).set_time(time).set_sport_content(sport_content)
                diary = diary_builder.build()
                self.calendar_window.save_diary(diary)  # 일기 저장
                self.show_diary(diary)
            else:
                messagebox.showwarning("Incomplete Information", "Please enter all fields.")
        elif diary_type == "Book Diary":
            # Book Diary 작성 코드
            book_title = self.book_title_entry.get().strip()
            author = self.author_entry.get().strip()
            start_page = self.start_page_entry.get().strip()
            end_page = self.end_page_entry.get().strip()
            book_content = self.book_content_entry.get("1.0", "end-1c").strip()

            if book_title and author and start_page and end_page and book_content:
                diary_builder = (
                    BookBuilder()
                    .set_date(self.selected_date)
                    .set_title(title)
                    .set_content(content)
                    .set_book_title(book_title)
                    .set_author(author)
                    .set_start_page(start_page)
                    .set_end_page(end_page)
                    .set_book_content(book_content)
                )
                diary = diary_builder.build()
                self.calendar_window.save_diary(diary)  # 일기 저장
                self.show_diary(diary)
            else:
                messagebox.showwarning("Incomplete Information", "Please fill in all fields for Book Diary.")
        else:
            messagebox.showwarning("Incomplete Information", "Please select a diary type.")

    # 편집한 일기를 저장하는 함수
    def save_edited_diary(self, diary):
        # diary.date = self.date_entry.get()

        if isinstance(diary, WorkOutDiary):
            diary.sport_kind = self.sport_kind_entry.get()
            diary.body_part = self.body_part_entry.get()
            diary.time = self.time_entry.get()
            diary.sport_content = self.sport_content_entry.get("1.0", "end")

        elif isinstance(diary, BookDiary):
            diary.book_title = self.book_title_entry.get()
            diary.author = self.author_entry.get()
            diary.start_page = self.start_page_entry.get()
            diary.end_page = self.end_page_entry.get()
            diary.book_content = self.book_content_entry.get("1.0", "end")

        else:
            diary.title = self.title_entry.get()
            diary.content = self.content_text.get("1.0", "end")
            
        self.show_diary(diary)
        self.edit_window.destroy()
        # self.view_diary()

    def close_window(self):
        self.diary_window.destroy()

    def close_edit_window(self):
        self.edit_window.destroy()

    def close_view_window(self):
        self.view_window.destroy()

    def update_date(self):
        selected_date = self.calendar_window.cal.get_date()
        date_parts = selected_date.split("/")  # "/"를 기준으로 문자열을 분할하여 리스트로 반환
        month = int(date_parts[0])  # 월 값 추출
        day = int(date_parts[1])  # 일 값 추출
        year = int(date_parts[2])  # 연도 값 추출
        self.date_text.config(text=f"Selected Date: {year}년 {month}월 {day}일")

    def open(self):
        self.diary_window.mainloop()
        
class Diary:
    def __init__(self, date, title, content):
        self.date = date
        self.title = title
        self.content = content

    def set_title(self, title):
        self.title = title

    def set_content(self, content):
        self.content = content

    def get_additional_info(self):
        return ""

class WorkOutDiary(Diary):
    def __init__(self, date, title, content):
        super().__init__(date, title, content)
        self.sport_kind = ""
        self.sport_content = ""
        self.body_part = ""
        self.time = 0
    
class BookDiary(Diary):
    def __init__(self, date, title, content):
        super().__init__(date, title, content)
        self.book_title = ""
        self.author = ""
        self.start_page = 0
        self.end_page = 0
        self.book_content = ""
    
class DiaryBuilder:
    def __init__(self):
        self.date = None
        self.title = None
        self.content = None

    def set_date(self, date):
        self.date = date
        return self

    def set_title(self, title):
        self.title = title
        return self

    def set_content(self, content):
        self.content = content
        return self

    def build(self):
        return Diary(self.date, self.title, self.content)

class WorkOutDiaryBuilder(DiaryBuilder):
    def __init__(self):
        super().__init__()
        self.sport_kind = ""
        self.body_part = "" # 운동 부위
        self.time = 0 # 운동 시간
        self.sport_content = ""
    
    def set_sport_kind(self, sport_kind):
        self.sport_kind = sport_kind
        return self

    def set_body_part(self, body_part):
        self.body_part = body_part
        return self

    def set_time(self, time):
        self.time = time
        return self
    
    def set_sport_content(self, sport_content):
        self.sport_content = sport_content
        return self

    def build(self):
        diary = WorkOutDiary(self.date, self.title, self.content)
        diary.sport_kind = self.sport_kind
        diary.body_part = self.body_part
        diary.time = self.time
        diary.sport_content = self.sport_content
        return diary

class BookBuilder(DiaryBuilder):
    def __init__(self):
        super().__init__()
        self.book_title = ""
        self.author = ""
        self.start_page = 0
        self.end_page = 0
        self.book_content = ""

    def set_book_title(self, book_title):
        self.book_title = book_title
        return self

    def set_author(self, author):
        self.author = author
        return self

    def set_start_page(self, start_page):
        self.start_page = start_page
        return self

    def set_end_page(self, end_page):
        self.end_page = end_page
        return self
    
    def set_book_content(self, book_content):
        self.book_content = book_content
        return self

    def build(self):
        diary = BookDiary(self.date, self.title, self.content)
        diary.book_title = self.book_title
        diary.author = self.author
        diary.start_page = self.start_page
        diary.end_page = self.end_page
        diary.book_content = self.book_content
        return diary


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
    app = App()
    app.mainloop()