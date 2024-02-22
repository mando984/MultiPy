
import tkinter as tk
from tkinter import ttk
from ttkbootstrap import*

from data.table import read_rang_list

class MainPage(tk.Frame):
    def __init__(self, next_page_callback):
        super().__init__()

        self.next_page_callback= next_page_callback

        # displays application name on header
        self.header_label = ttk.Label(self, text="MultiPy", font=("Helvetica", 30), foreground="#CA9A07")
        self.header_label.pack(pady=20)

       
        self.list_name = ttk.Label(self, text="RangList", font=("Helvetica", 18), foreground="#CA9A07")
        self.list_name.pack(pady=10)

        #print table
        self.tree = ttk.Treeview(self)

        self.tree["columns"] = ("#", "Name", "Score", "Time")
        self.tree.column("#", width=100, minwidth=50, stretch=tk.NO)
        self.tree.column("Name", width=150, minwidth=50, stretch=tk.NO)
        self.tree.column("Score", width=150, minwidth=50, stretch=tk.NO)
        self.tree.column("Time", width=150, minwidth=50, stretch=tk.NO)

        self.tree.heading("#", text="Place", anchor=tk.W)
        self.tree.heading("Name", text="Name", anchor=tk.W)
        self.tree.heading("Score", text="Score", anchor=tk.W)
        self.tree.heading("Time", text="Time", anchor=tk.W)

        # Postavi podatke u Treeview
        self.refresh_table()  # ažuriranje tabele

        # Set the start_button to move to secund_page
        self.start_button = ttk.Button(self, text=" Start new game! ",style= "outline", command=self.next_page_callback)
        self.start_button.pack(pady=30)

        self.quit_button = ttk.Button(self, text="Quit game",  width=20, style= "outline", command=self.quit)
        self.quit_button.pack(pady=10)

        #  every show frame1 call on_show mhetod 
        self.bind("<Visibility>", lambda event: self.on_show(event, self)) 

    def on_show(self, event, widget):
        widget.refresh_table()  # update table 
       # widget.update_idletasks()    
 

       # ažuriranje tabele
    def refresh_table(self):
        self.tree.delete(*self.tree.get_children())  # clear table
        #self.tree.update_idletasks()
        players = read_rang_list() 
        for i, player in enumerate(players, start=1):
            self.tree.insert("", "end", values=(i, player["Name"], player["Score"], player["Time"]))    
        self.tree.pack(pady=10)    


    def start_application(self):
        self.mainloop()    


def main():
    next_page_callback = ''
    apps = MainPage(next_page_callback)
    apps.start_application()


if __name__ == "__main__":
    main()