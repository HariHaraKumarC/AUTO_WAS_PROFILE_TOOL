# Author: HARIHARAKUMAR CHANDRABOSE

import tkinter as tk
from tkinter import ttk
import subprocess;


class AutoProfilerApp(tk.Tk):
    def __init__(self,*args,**kwargs):
        tk.Tk.__init__(self,*args,**kwargs)
        self.title("AUTO WAS PROFILE CREATION TOOL")
        self.geometry("800x700")
        self.resizable(width=tk.FALSE,height=tk.FALSE)
        self.menu_initialisation()
        container = tk.Frame(self, bg="white")
        container.pack(side="top",fill="both",expand="True")
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)
        self.frames = {}
        for F in (HomePage, CreateProfilePage, CreateProfileProgressPage, DeleteProfileInputPage, DeleteProfileProgressPage):
            frame=F(container,self)
            self.frames[F] = frame
            frame.grid(row=0,column=0,sticky="nsew")
        self.show_frame(HomePage)
        self.application_name=""
        self.profile_name=""

    def show_frame(self,name):
        frame = self.frames[name]
        frame.tkraise()

    def set_profile_details_and_switch_frame(self,application_name,profile_name,frame_name):
        print("test usha")
        self.application_name=application_name
        self.profile_name=profile_name
        print(self.application_name)
        print(self.profile_name)
        self.show_frame(frame_name)

    def menu_initialisation(self):
        menu_bar = tk.Menu(self)
        # File Menu
        file_menu = tk.Menu (menu_bar,tearoff=0)
        file_menu.add_command(label="New Profile", command=lambda: self.show_frame(CreateProfilePage))
        file_menu.add_separator()
        file_menu.add_command(label="Exit",command=self.app_exit)
        # Profile Menu
        profile_menu = tk.Menu(menu_bar,tearoff=0)
        profile_menu.add_command(label="Delete",command=lambda: self.show_frame(DeleteProfileInputPage))
        # Help Menu
        help_menu = tk.Menu(menu_bar,tearoff=0)
        help_menu.add_command(label="Help Links")
        help_menu.add_separator()
        help_menu.add_command(label="About")
        menu_bar.add_cascade(label="File",menu=file_menu)
        menu_bar.add_cascade(label="Profiles",menu=profile_menu)
        menu_bar.add_cascade(label="Help",menu=help_menu)
        self.config(menu = menu_bar)

    def app_exit(self):
        exit()


class HomePage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self,parent)
        # Setting frame background
        self.configure(background='white')
        # Spacer
        spacer_label = tk.Label(self)
        spacer_label.pack()
        # Logo
        logo = tk.PhotoImage(file="C:\Data\Hari\Git\Local_Repository\AUTO_WAS_PROFILE_TOOL\images\homeLogo1.gif")
        logo_label = tk.Label(self, image=logo, borderwidth=0)
        logo_label.image = logo
        logo_label.pack()
        # create new profile link
        new_profile_label_name = tk.StringVar()
        new_profile_label_name.set("Create New Profile:")
        new_profile_label_button = tk.Button(self, textvariable=new_profile_label_name, borderwidth=0, background="white", cursor="hand2", font='Helvetica 10 bold', fg="blue", command=lambda: controller.show_frame(CreateProfilePage))
        new_profile_label_button.pack()


class CreateProfilePage(tk.Frame):
    def __init__(self,parent,controller):
        tk.Frame.__init__(self,parent)
        self.columnconfigure(0,weight=1)
        self.columnconfigure(1,weight=20)
        self.columnconfigure(2,weight=1)
        # Spacer
        spacer_label = tk.Label(self)
        spacer_label.grid(row=0)
        # Header
        header_label = tk.Label(self, text="Create New Profile  >", borderwidth=0, font='Helvetica 11 bold', fg="blue")
        header_label.grid(row=1,padx=5)
        # Spacer
        spacer_label = tk.Label(self)
        spacer_label.grid(row=2)
        # Application Entry
        application_name_label=tk.Label(self, text="Application:", borderwidth=0, font='Helvetica 10 bold', fg="black")
        application_name_label.grid(row=3,sticky='w',padx=10,pady=10)
        application_values = ('Default','MAPC', 'MAPS')
        application_name_entry=ttk.Combobox(self,values=application_values,width=100)
        application_name_entry.bind("<<ComboboxSelected>>")
        application_name_entry.grid(row=3,column=1,columnspan=2,sticky='w')
        # Profile Name
        profile_name_label=tk.Label(self, text="Profile Prefix:", borderwidth=0, font='Helvetica 10 bold', fg="black")
        profile_name_label.grid(row=4,sticky='w',padx=10,pady=10)
        profile_name_entry = tk.Entry(self,width=103)
        profile_name_entry.grid(row=4,column=1,columnspan=2,sticky='w')
        # Cancel & Create Button
        cancel_button=tk.Button(self,text="Cancel",font='Helvetica 9 bold', fg="red",command=lambda: controller.show_frame(HomePage))
        cancel_button.grid(row=5,column=1,sticky='e',padx=10,pady=10)
        create_button=tk.Button(self, text="Create Profile", font='Helvetica 9 bold', fg="green", command=lambda: controller.set_profile_details_and_switch_frame(application_name_entry.get(),profile_name_entry.get(),CreateProfileProgressPage))
        create_button.grid(row=5,column=2,sticky='w')


class CreateProfileProgressPage(tk.Frame):
    def __init__(self,parent,controller):
        tk.Frame.__init__(self,parent)
        self.columnconfigure(0,weight=1)
        self.columnconfigure(1,weight=20)
        # Spacer
        spacer_label = tk.Label(self)
        spacer_label.grid(row=0)
        # Header
        header_label = tk.Label(self, text="Create New Profile  >", borderwidth=0, font='Helvetica 11 bold', fg="blue")
        header_label.grid(row=1,padx=5)
        # Spacer
        spacer_label = tk.Label(self)
        spacer_label.grid(row=2)
        # Progress Bar
        create_profile_progress_bar=ttk.Progressbar(self, mode="indeterminate", name="create_profile_progress_bar",length=750)
        create_profile_progress_bar.grid(row=3,columnspan=2)
        # Finish Button
        finish_button=tk.Button(self,text="Finish",font='Helvetica 9 bold', fg="red",command=lambda: controller.show_frame(HomePage))
        finish_button.grid(row=4,column=1,sticky='e',padx=30,pady=10)


class DeleteProfileInputPage(tk.Frame):
    def __init__(self,parent,controller):
        tk.Frame.__init__(self,parent)
        self.columnconfigure(0,weight=1)
        self.columnconfigure(1,weight=20)
        self.columnconfigure(2,weight=1)
        # Spacer
        spacer_label = tk.Label(self)
        spacer_label.grid(row=0)
        # Header
        header_label = tk.Label(self, text="Delete WAS Profile  >", borderwidth=0, font='Helvetica 11 bold', fg="blue")
        header_label.grid(row=1,padx=5)
        # Spacer
        spacer_label = tk.Label(self)
        spacer_label.grid(row=2)
        # WAS Profiles
        profile_path_label=tk.Label(self, text="WAS Profiles:", borderwidth=0, font='Helvetica 10 bold', fg="black")
        profile_path_label.grid(row=3,sticky='w',padx=10,pady=10)
        # Calling listAllProfiles.bat for getting the list of WAS profiles
        list_all_profiles_batch_output = subprocess.Popen("listAllProfiles.bat",stdout=subprocess.PIPE).stdout
        for line in list_all_profiles_batch_output:
            if line[:1] == b'[':
                temp_string = line[1:-3]
                profiles = temp_string.decode().split(',')
                profiles = self.trim_list(profiles)
                print(profiles)
        list_all_profiles_batch_output.close()
        profiles_entry=ttk.Combobox(self,values=profiles,width=100,state='readonly')
        profiles_entry.grid(row=3,column=1,columnspan=2,sticky='w')
        print(profiles_entry.current())
        # Cancel & Delete Profile Button
        cancel_button=tk.Button(self,text="Cancel",font='Helvetica 9 bold', fg="red",command=lambda: controller.show_frame(HomePage))
        cancel_button.grid(row=4,column=1,sticky='e',padx=10,pady=10)
        delete_profile_button=tk.Button(self, text="Delete Profile", font='Helvetica 9 bold', fg="green", command=lambda: controller.show_frame(DeleteProfileProgressPage))
        delete_profile_button.grid(row=4,column=2,sticky='w')

    def trim_list(self,input_list):
        return [x.strip() for x in input_list]


class DeleteProfileProgressPage(tk.Frame):
    def __init__(self,parent,controller):
        tk.Frame.__init__(self,parent)
        self.columnconfigure(0,weight=1)
        self.columnconfigure(1,weight=20)
        self.columnconfigure(2,weight=1)
        # Spacer
        spacer_label = tk.Label(self)
        spacer_label.grid(row=0)
        # Header
        header_label = tk.Label(self, text="Delete WAS Profile  >", borderwidth=0, font='Helvetica 11 bold', fg="blue")
        header_label.grid(row=1,padx=5)
        # Spacer
        spacer_label = tk.Label(self)
        spacer_label.grid(row=2)
        # Progress Bar
        delete_profile_progress_bar=ttk.Progressbar(self, mode="indeterminate", name="delete_profile_progress_bar", length=750)
        delete_profile_progress_bar.grid(row=3,columnspan=2)
        delete_profile_progress_bar.start()
        # Calling deleteProfiles.bat for deleting the selected WAS profile
        return_code=9999
        delete_profile_progress_bar.stop()
        self.display_delete_profile_result(return_code,controller)

    def display_delete_profile_result(self,return_code,controller):
        if return_code == 0000:
            message = "Success:Profile deleted Successfully."
            message_label = tk.Message(self, text=message, borderwidth=0, font='Helvetica 9 bold', fg="green", width=500)
        else:
            message = "Error: Profile deletion operation was unsuccessful."
            message_label = tk.Message(self, text=message, borderwidth=0, font='Helvetica 9 bold', fg="red", width=500)
        message_label.grid(row=4, columnspan=2,sticky='w',padx=25,pady=10)
        # Finish Button
        finish_button=tk.Button(self,text="Finish",font='Helvetica 9 bold', fg="blue",command=lambda: controller.show_frame(HomePage))
        finish_button.grid(row=5, column=1,sticky='e',padx=30,pady=10)

app=AutoProfilerApp()
app.mainloop()