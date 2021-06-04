# By Samora Machel
__version__ = 0.1
__status__ = "Prototype"
__date__ = "27-01-2020"
__maintainer__ = "samoraok@gmail.com"


from tkinter import *
from tkinter import scrolledtext as Scrolltxt
from tkinter import filedialog
import os
from tkinter import messagebox as message
from tkinter import ttk
from tkinter import font as ft 
import keyword
import re
import time


# Creates an object for the python Notebook 
class PythonPad:
    
    # Initialize the creation of a simple window
    def __init__(self):
        self.root = Tk()
        self.line_numberBar = Text(self.root, bg='antique white', width=5, relief='flat', state='disabled')
        self.textspace = Text(self.root, undo=True)

        global _font
        global _font_color
        global _font_size
        global _text_background
        global _lineBar_background
        global _lineBar_text_background
        global _keyword_color

        _font = StringVar()
        _font.set("Latin Modern Mono")

        _font_color = StringVar()
        _font_color.set("black")

        _font_size = IntVar()
        _font_size.set(12)

        _text_background = StringVar()
        _text_background.set('white')

        _lineBar_background = StringVar()
        _lineBar_background.set('antique white')

        _lineBar_text_background = StringVar()
        _lineBar_text_background.set('black')

        _keyword_color = StringVar()
        _keyword_color.set('teal')


    # Create a main window with a default title and size
    def Main_Window(self):
        self.root.title("PythonPad")
        self.root.geometry("600x600")
    
    # Add the Menu bar with various submenus
    def Menubar(self):
        self.menubar = Menu(self.root)
        self.filemenu = Menu(self.menubar, tearoff=0)
        self.viewmenu = Menu(self.menubar, tearoff=0)
        self.editmenu = Menu(self.menubar, tearoff=0)
        self.aboutmenu = Menu(self.menubar, tearoff=0)
        self.formatmenu = Menu(self.menubar, tearoff=0)
        

        

        # Adding commands in the File Menu 
        self.filemenu.add_command(label="New", accelerator="Ctrl+N", underline=0, compound=LEFT, command=self.new_file)
        self.filemenu.add_command(label="Open", accelerator="Ctrl+O", underline=0, compound=LEFT, command=self.open_command)
        self.filemenu.add_separator()
        self.filemenu.add_command(label="Save", accelerator="Ctrl+S", underline=0, compound=LEFT, command=self.save_command)
        self.filemenu.add_command(label="Save As", accelerator="Ctrl+Shift+S", compound=LEFT, command=self.save_as)
        self.filemenu.add_separator()
        self.filemenu.add_command(label="Close File", command=self.close_file)
        self.filemenu.add_command(label="Exit", accelerator="Alt+F4", compound=LEFT, command=self.exit_command)

        # Adding commands to the View menu
        self.line_info = IntVar()
        self.line_info.set(0)

        self.Highlight = IntVar()
        self.Highlight.set(0)

        self.viewmenu.add_checkbutton(label="Show Info at the bottom", onvalue=1, offvalue=0, variable=self.line_info)
        self.viewmenu.add_checkbutton(label="Highlight Current Line", onvalue=1, offvalue=0, variable=self.Highlight)

        # Adding commands for the Edit Menu
        self.editmenu.add_command(label="Copy", accelerator="Ctrl+C", compound=LEFT, underline=0, command=self.copy_command)
        self.editmenu.add_command(label="Paste", accelerator="Ctrl+V", compound=LEFT, command=self.paste_command)
        self.editmenu.add_command(label="Cut", accelerator="Ctrl+X", compound=LEFT, command=self.cut_command)
        self.editmenu.add_separator()
        self.editmenu.add_command(label="Undo", accelerator="Ctrl+Z", compound=LEFT, command=self.undo_command)
        self.editmenu.add_command(label="Redo", accelerator="Ctrl+Shift+Z", compound=LEFT, command=self.redo_command)
        self.editmenu.add_separator()
        self.editmenu.add_command(label="Find", accelerator="Ctrl+F", compound=LEFT, underline=0, command=self.find_command)
        self.editmenu.add_separator()
        self.editmenu.add_command(label="Select All", accelerator="Ctrl+A", compound=LEFT, underline=8, command=self.select_all_command)
        self.editmenu.add_command(label="Delete All", compound=LEFT, command=self.delete_all_command)

        # Adding commands for the About Menu
        self.aboutmenu.add_command(label="Author", command=self.Author_message)
        self.aboutmenu.add_command(label="Help", command=self.Help_message)

        
        # Section for adding commands for formatting fonts
        self.formatmenu.add_command(label='Font', command=self.format_font)
        self.formatmenu.add_command(label="Themeing", command=self.theme_formatting)



        # making all the menus' defined above to appear in the python Notepad
        self.menubar.add_cascade(label="File", menu=self.filemenu)
        self.menubar.add_cascade(label="Edit", menu=self.editmenu)
        self.menubar.add_cascade(label='Format', menu=self.formatmenu)
        self.menubar.add_cascade(label="View", menu=self.viewmenu)
        self.menubar.add_cascade(label="About", menu=self.aboutmenu)


        # Configuring the root window to recognize the menubar as the menu
        self.root.config(menu=self.menubar)
    
    # Function for formatting fonts 
    def format_font(self):
            _font_window = Toplevel()
            _font_window.transient()
            _font_window.resizable(False, False)
            _font_window.title("Font Formatting")
            Label(_font_window, text="Select Font : " ).grid(row=0, column=0, sticky='w')
            ttk.Combobox(_font_window, textvariable=_font, justify=CENTER, value=ft.families(), state='read only').grid(row=0, column=1, padx=2, sticky='e'+'w', pady=2)
            Label(_font_window, text="Change Color : ").grid(row=1, column=0, sticky='w', pady=2)
            color_list = ['Red', 'Green', 'Black', 'Violet', 'Teal', 'Crimson', 'Gray', 'Brown']
            ttk.Combobox(_font_window, textvariable=_font_color, value=color_list, justify=CENTER).grid(row=1, column=1, padx=2, pady=2, sticky='w'+'e') 
            Label(_font_window, text='Font Size : ').grid(row=2, column=0, sticky='w', pady=2)
            ttk.Spinbox(_font_window, from_=0, to=40, increment=2, textvariable=_font_size, justify=RIGHT, command=self.self_updates).grid(row=2, column=1, sticky='w'+'e', padx=2, pady=2)
    

    # Function for selecting themes 
    def theme_formatting(self):

        color_list = ['Red', 'Green', 'Black', 'Violet', 'Teal', 'Crimson', 'Gray', 'Brown']

        

        def configured_themes():
                _theme_window = Toplevel()
                _theme_window.transient()
                _theme_window.resizable(False, False)
                _theme_window.title('Configured themes')
                Label(_theme_window, text='Select Theme : ').grid(row=0, column=1, sticky='w', pady=2, columnspan=2)
                ttk.Combobox(_theme_window,  justify=RIGHT ).grid(row=1, column=2 , pady=2, columnspan=2) 

        _font_window = Toplevel()
        _font_window.transient()
        _font_window.resizable(False, False)
        _font_window.title("Theme Formatting")
        
        Label(_font_window, text="Background Color : " ).grid(row=0, column=0, sticky='w')
        ttk.Combobox(_font_window, textvariable=_text_background, justify=CENTER, value=color_list, state='read only').grid(row=0, column=1, padx=2, sticky='e'+'w', pady=2)

        Label(_font_window, text="Change Font Color : ").grid(row=1, column=0, sticky='w', pady=2)
        ttk.Combobox(_font_window, textvariable=_font_color, value=color_list, justify=CENTER).grid(row=1, column=1, padx=2, pady=2, sticky='w'+'e')
        
        Label(_font_window, text="Key Word Color : ").grid(row=3, column=0, sticky='w', pady=2)
        ttk.Combobox(_font_window, textvariable=_keyword_color, value=color_list, justify=CENTER).grid(row=3, column=1, padx=2, pady=2, sticky='w'+'e') 
        
        Label(_font_window, text='Side Bar Color : ').grid(row=4, column=0, sticky='w', pady=2)
        ttk.Combobox(_font_window, textvariable=_lineBar_background, value=color_list, justify=CENTER).grid(row=4, column=1, padx=2, pady=2, sticky='w'+'e')
        
        Label(_font_window, text='Side Bar FontColor : ').grid(row=5, column=0, sticky='w', pady=2)
        ttk.Combobox(_font_window, textvariable=_lineBar_text_background, value=color_list, justify=CENTER).grid(row=5, column=1, padx=2, pady=2, sticky='w'+'e')
        
        Button(_font_window, text="Preview  theme", command=self.self_updates).grid(row=6 , column=1, pady=3)
        Button(_font_window, text="Select a theme",  command=configured_themes).grid(row=7 , column=1, pady=3)
            





    # Function for updating the line_numberBar after each update on the textspace 
    def self_updates(self, Event=None):
        self.line_numberBar.config(state='normal')
        endline, endcolumn = self.textspace.index('end').split('.')
        text_= '\n'.join(map(str, range(1, int(endline))))

        # Works only if your using a Label widget but not in a text widget
        # self.line_numberBar.config(text=text_, anchor='nw')


        self.line_numberBar.delete('1.0', END)
        self.line_numberBar.insert(index=str(endline)+'.1', chars=text_)
        self.line_numberBar.config(state='disabled')

        self.textspace.config(bg=_text_background.get(), font=(_font.get(), _font_size.get()), fg=_font_color.get())
        self.line_numberBar.config(bg=_lineBar_background.get(), font=(_font.get(), _font_size.get()), fg=_lineBar_text_background.get())


        self.KeyWords_Highlight()
    
    
    def KeyWords_Highlight(self, Event=None):
        KeyWords = keyword.kwlist
        def search_keywords(needle, cssnstv, textPad):
            if needle:
                pos = '1.0'
                while True:
                    pos = textPad.search(needle, pos, nocase=cssnstv, stopindex=END)
                    if not pos :
                        break
                    lastpos = '%s+%dc' % (pos, len(needle))
                    self.textspace.tag_add('match', pos, lastpos)
                    pos = lastpos

                textPad.tag_config('match', foreground=_keyword_color.get())


        for i in KeyWords:
            search_keywords(i, 1, self.textspace)



    # Creating Bindings to various commands
    def command_bindings(self):
        self.root.bind('<Any-KeyPress>', self.self_updates)
        self.root.bind('<FocusIn>', self.self_updates)

        

    
    # Creating the text area with a scrollbar at the left and at the bottom
    def TextArea(self):
        
        self.line_numberBar.pack(side=LEFT, fill=Y)

        self.textspace.insert(1.0, "Project By Samora Machel \033")
        self.textspace.pack(fill=BOTH, expand=1)

        self.scroll = Scrollbar(self.textspace, bg='white')
        self.textspace.configure(yscrollcommand=self.scroll.set)
        self.line_numberBar.configure(yscrollcommand=self.scroll.set)
        self.scroll.config(command=self.textspace.yview)
        self.scroll.pack(side=RIGHT, fill=Y)


        # self.line_scroll = Scrollbar(self.line_numberBar)
        # self.line_numberBar.configure(yscrollcommand=self.line_scroll.set)
        # self.line_scroll.config(command=self.line_numberBar.yview)
        # self.scroll.pack(side=RIGHT, fill=Y)


        # self.Hrz_scroll = Scrollbar(self.textspace, orient=HORIZONTAL)
        # self.textspace.configure(xscrollcommand=self.Hrz_scroll.set)
        # self.Hrz_scroll.config(command=self.textspace.xview)
        # self.Hrz_scroll.pack(side=BOTTOM, fill=X)  
    def scrolling(self):
        
        self.line_numberBar.yview()
        
    
    # Section for creating commands that will be used in the menu bar
    def copy_command(self, Event=None):
        self.textspace.event_generate("<<Copy>>")
        self.self_updates()
    def paste_command(self, Event=None):
        self.textspace.event_generate("<<Paste>>")
        self.self_updates()
    def cut_command(self, Event=None):
        self.textspace.event_generate("<<Cut>>")
        self.self_updates()
    def find_command(self, Event=None):
        window = Toplevel()
        window.transient(self.root)
        window.title("Find")
        window.resizable(False, False)
        find_label = Label(window, text="Search").grid(column=0, row=0, sticky='e')
        searchVar = StringVar()
        find_entry = Entry(window, width=25, textvariable=searchVar)
        find_entry.grid(column=1, row=0, sticky='we', pady=2, padx=2)
        find_entry.focus_set()
        caseVar = IntVar()
        Checkbutton(window, text='Ignore Case', variable=caseVar).grid(row=1,column=1, sticky='e', padx=2, pady=2)
        Button(window,text="Find", underline=0, command=lambda: self.search_for(searchVar.get(), caseVar.get(), self.textspace, window, find_entry) ).grid(column=2, row=0, padx=2, pady=2, sticky='e'+'w')
    def undo_command(self, Event=None):
        self.textspace.edit_undo()
    def redo_command(self, Event=None):
        self.textspace.edit_redo()

    # Function used to parse the textspace area looking for the specific item searched for 
    def search_for(self, needle, cssnstv, textPad, window, e):
        # textPad.tag_remove('match', '1.0', END)
        count = 0
        if needle:
            pos = '1.0'
            while True:
                pos = textPad.search(needle, pos, nocase=cssnstv, stopindex=END, exact=1)
                if not pos :
                    break
                lastpos = '%s+%dc' % (pos, len(needle))
                self.textspace.tag_add('match', pos, lastpos)
                count += 1
                pos = lastpos

            if textPad == None or e == None or window == None:
                textPad.tag_config('match', foreground='teal')
            else:
                textPad.tag_config('match',background='yellow', foreground='red')
                e.focus_set()
                window.title("%d matches found" % count)
    # function for removing the textArea
    def close_file(self):

        self.textspace.forget()
        self.root.title("PythonPad")
        


    # Function for creating a new instance of the text are
    def new_file(self, Event=None):
        self.textspace.pack(fill=BOTH, expand=1)
        self.textspace.delete('1.0', END)
        self.root.title('Untitled.txt - PythonPad')
        

        self.self_updates()
    
    def open_command(self, Event=None):
        self.file_name = filedialog.askopenfilename(title='Open File - PythonPad' ,defaultextension='*.py', filetypes=[("Text Documents", '*.txt'), ('C//C++ Files',('*.c', '*.h', '*.cpp')), ('Python Files', '*.py')])
        if self.file_name == "":
            self.file_name = None
        else:
            self.root.title(os.path.basename(self.file_name) + ' - PythonPad')
            self.textspace.delete('1.0', END)
            _file = open(self.file_name, 'r')
            self.textspace.insert('1.0', _file.read())
            _file.close()
        self.textspace.pack(fill=BOTH, expand=1)
    
    def save_command(self, Event=None):
        try:
            _file = open(self.file_name, 'w')
            writting = self.textspace.get('1.0', END)
            _file.write(writting)
            _file.close()
        except:
            self.save_as()
    def save_as(self, Event=None):
        try:
            # First get the filename and the specific location to store the file to
            _filename = filedialog.asksaveasfilename(confirmoverwrite=True ,title="Save As - PythonPad",initialfile="Untitled.py", defaultextension='.py', filetypes=[("All Files", '*.*'), ("Text Files", '*.txt'), ("Python Files", '*.py'), ('C//C++ Files', ('*.c', '*.h', '*.cpp'))])
            _OpenFile= open(_filename, 'w')
            textWritting = self.textspace.get('1.0', END)
            _OpenFile.write(textWritting)
            _OpenFile.close()
            self.root.title(os.path.basename(_filename)+" - PythonPad")
        except:
            pass

    def exit_command(self, Event=None):
            ans = message.askyesno("Quit", "Do you really want to quit ? ")
            if ans == 1:
                self.root.destroy()
            else:
                pass
    
    def select_all_command(self, Event=None):
        self.textspace.tag_add("sel", 1.0, END)
    
    def delete_all_command(self, Event=None):
        self.textspace.delete('0.0', END)


    # This is a function used to bring a pop up message about the creator of this Project 
    def Author_message(self):
        message.showinfo('Creator', "This is a project creation by Samora Machel")

    def Help_message(self):
        message.showinfo("Help","This in a coding pad created specifically for Python\nbut support other programming languages such as C/C++")

    

    





if __name__ == '__main__':

    # This is a function for bringing the popup loading message before the pythonPad loads
    def pythonpad_popup(destroy=None):
        popup = Tk()
        # popup.geometry('500x500')
        popup.overrideredirect(1)


        popup.resizable(False, False)
        popup.title("PythonPad")
        
        popup_frame = Frame(popup, bg='teal').grid(row=0, column=0)
        Label(popup_frame,text="\033PythonPad\033", font=('Rock it',20, 'bold'), justify=CENTER, fg='Teal').grid(row=1, column=0, pady=1, columnspan=5)
        Label(popup_frame, text="\nMake your wildest dreams come True", font=('4990810', 14,), justify=CENTER, fg='gray').grid(row=3, column=2, columnspan=3, pady=2)
        Label(popup_frame, text="By: Samora Machel", font=('Quicksand Medium', 10,), justify=CENTER, fg='gray').grid(row=11, column=4, columnspan=2, pady=2)

        
        progress_bar = ttk.Progressbar(popup_frame, orient='horizontal', length=286, mode="determinate")
        progress_bar.grid(column=0, row=10, columnspan=5)
        def run_progressbar():                 # Creates a function to start the running of the progressbar and stop after its done
            progress_bar['maximum'] = 100
            for i in range(101):
                time.sleep(0.035)
                progress_bar['value'] = i       # increment progress bar
                progress_bar.update()           # have to call update in a loop 
            progress_bar['value'] = 0
            popup.destroy() 
        run_progressbar()
        popup.mainloop()
        

    pythonpad_popup()       # Brings in the popup-load message before PythonPad is ran
    Notebook = PythonPad()
    Notebook.Main_Window()
    Notebook.Menubar()
    Notebook.TextArea()
    Notebook.self_updates()
    Notebook.command_bindings()
    
    Notebook.KeyWords_Highlight()
    Notebook.root.mainloop()
