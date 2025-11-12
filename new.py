# enhanced todo list 
import json
import os
import threading
import tkinter as tk
from tkinter import filedialog, simpledialog, messagebox

import customtkinter as ctk

#images/videos
try:
    from PIL import Image, ImageTk
    PIL_AVAILABLE = True
except Exception:
    PIL_AVAILABLE = False

try:
    import cv2
    CV2_AVAILABLE = True
except Exception:
    CV2_AVAILABLE = False

ctk.set_appearance_mode("System")
ctk.set_default_color_theme("blue")


class TodoApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Modern To-Do List (Enhanced)")
        self.root.geometry("640x420")
        self.tasks = []  
        self.video_capture = None
        self.video_running = False
        self.video_frame_image = None
        self.follow_cursor = tk.BooleanVar(value=False)
        self.bg_label = None
        self.bg_img = None

        
        self.header = ctk.CTkFrame(self.root, height=48)
        self.header.pack(fill="x", side="top")
        self.header.pack_propagate(False)

        # Header draggable area + controls 
        header_inner = ctk.CTkFrame(self.header, corner_radius=0)
        header_inner.pack(fill="both", padx=8, pady=6)

        title = ctk.CTkLabel(header_inner, text="🗒️ Modern To-Do", anchor="w", font=ctk.CTkFont(size=14, weight="bold"))
        title.pack(side="left", padx=(4, 8))

        follow_chk = ctk.CTkCheckBox(header_inner, text="Follow cursor", variable=self.follow_cursor, command=self._on_follow_toggle)
        follow_chk.pack(side="right", padx=6)

        import_btn = ctk.CTkButton(header_inner, text="Import Background", width=160, command=self.import_background)
        import_btn.pack(side="right", padx=6)

        self.main_frame = ctk.CTkFrame(self.root)
        self.main_frame.place(relx=0.5, rely=0.5, anchor="center")  #size manually

        # Entry and add/edit buttons
        top_row = ctk.CTkFrame(self.main_frame)
        top_row.pack(padx=12, pady=(12, 6), fill="x")

        self.entry = ctk.CTkEntry(top_row, placeholder_text="Enter a task...", width=320)
        self.entry.pack(side="left", padx=(0, 8), expand=True, fill="x")

        add_btn = ctk.CTkButton(top_row, text="Add", command=self.add_task)
        add_btn.pack(side="left", padx=6)
        edit_btn = ctk.CTkButton(top_row, text="Edit", command=self.edit_task)
        edit_btn.pack(side="left", padx=6)

        # Listbox + scrollbar
        lb_frame = ctk.CTkFrame(self.main_frame)
        lb_frame.pack(padx=12, pady=6, fill="both", expand=True)

        self.listbox = tk.Listbox(lb_frame, width=50, height=12, bd=0, highlightthickness=0, activestyle="none")
        self.listbox.pack(side="left", fill="both", expand=True)
        sb = ctk.CTkScrollbar(lb_frame, command=self._on_scroll)
        sb.pack(side="right", fill="y")
        self.listbox.config(yscrollcommand=sb.set)

        # Buttons row
        btn_row = ctk.CTkFrame(self.main_frame)
        btn_row.pack(padx=12, pady=(6, 12), fill="x")

        remove_btn = ctk.CTkButton(btn_row, text="Remove", command=self.remove_task)
        remove_btn.pack(side="left", padx=6)
        toggle_btn = ctk.CTkButton(btn_row, text="Toggle Done", command=self.toggle_done)
        toggle_btn.pack(side="left", padx=6)
        clear_done_btn = ctk.CTkButton(btn_row, text="Clear Done", command=self.clear_done)
        clear_done_btn.pack(side="left", padx=6)

        save_btn = ctk.CTkButton(btn_row, text="Save", command=self.save_tasks)
        save_btn.pack(side="right", padx=6)
        load_btn = ctk.CTkButton(btn_row, text="Load", command=self.load_tasks)
        load_btn.pack(side="right", padx=6)

        # Bindings for dragging and edit with double click
        self.header.bind("<ButtonPress-1>", self.start_move)
        self.header.bind("<B1-Motion>", self.do_move)
        self.listbox.bind("<Double-Button-1>", lambda e: self.edit_task())
        self.root.bind("<Escape>", lambda e: self.root.quit())

        # position for the main frame
        self.main_frame.configure(width=580, height=340)
        # set geometry update when window draws
        self.root.after(50, self._center_main_frame)

    # UI help
    def _on_scroll(self, *args):
        self.listbox.yview(*args)

    def _center_main_frame(self):
        # center main frame in the root window
        w = self.root.winfo_width()
        h = self.root.winfo_height()
        self.main_frame.place_configure(relx=0.5, rely=0.5, anchor="center")
    
    def _on_follow_toggle(self):
    #follow cursor toggle

        if self.follow_cursor.get():
            print("Follow cursor: ON")
        else:
            print("Follow cursor: OFF")

    def import_background(self):
        from tkinter import filedialog
        file_path = filedialog.askopenfilename(
            title ="Select Background Image/Video",
            filetypes=[("Image and Video Files", "*.png *.jpg *.jpeg *.bmp *.gif *.mp4)]")]
        )
        if not file_path:
            return #canceled
        
        try:
            from PIL import Image, ImageTk
            img = Image.open(file_path)
            img = img.resize((self.root.winfo_width(), self.root.winfo_height()))
            self.bg_img = ImageTk.PhotoImage(img)
            if self.bg_label is None:
                self.bg_label = tk.Label(self.root, image=self.bg_img)
                self.bg_label.place(relx=0.5, rely=0.5, anchor ="center")
                self.bg.label.lower() #send to back
            else:
                self.bg_label.config(image=self.bg_img)
        except Exception as e:
            messagebox.showerror("Error", f"Failed to load background: {e}")
