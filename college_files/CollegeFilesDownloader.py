'''
This file, contains a simple GUI for the Spyder.



'''

from tkinter import *
import tkinter.messagebox as tm
from scrapy.crawler import CrawlerProcess
from college_files.spiders.college_spider import CollegeSpider
from college_files.spiders import mesAndPaths as mp
from tkinter.ttk import Progressbar
import time
import threading


class LoginFrame(Frame):
    
    def __init__(self, master):
        super().__init__(master)
        self.var = IntVar()
        self.img = PhotoImage(file="logo.gif")
        self.df_url = StringVar(self, value='<Custom MOODLE URL>')
        self.passed_moodle_url = ""
        tm.showwarning("Disclaimer", mp.WATNING_MSG)
        self.label_username = Label(self, text="Username (ID NUMBER): ")
        self.label_password = Label(self, text="Password: ")
        self.label_msg = Label(self,image=self.img)
        self.label_msg.grid(row=0,column=0, sticky=W)
        self.entry_username = Entry(self)
        self.entry_password = Entry(self, show="*")
        # on change dropdown value
        self.label_username.grid(row=1, sticky=E)
        self.label_password.grid(row=3, sticky=E)
        self.entry_username.grid(row=1, column=1)
        self.entry_password.grid(row=3, column=1)
        #self.checkbox = Checkbutton(self, text="Keep me logged in")
        #self.checkbox.grid(columnspan=3)
        self.btnDownload = Button(self, text="<<Download my files>>", command=self._login_btn_clicked)
        self.btnDownload.grid(row=6, column=0, sticky=S)
        self.brnClose = Button(self, text="Close", command=root.destroy)
        self.brnClose.grid(row=6, column=1, sticky=W)
        self.btnBoxKinneret = Radiobutton(self, text="Kinneret College", variable=self.var, value=0, command=self._radio_Button_Option)
        self.btnBoxKinneret.grid(row=4, column=1,sticky=W)
        self.btnBoxOther = Radiobutton(self, text="Other", variable=self.var, value=1, command=self._radio_Button_Option)
        self.btnBoxOther.grid(row=4, column=0,sticky=E)
        self.label_custom_url = Label(self, text="Custom MOODLE url: ")
        self.label_custom_url.grid(row=5, column=0,sticky=E)
        self.entry_custom_url = Entry(self, textvariable=self.df_url)
        self.entry_custom_url.grid(row=5, column=1,sticky=S)
        self.entry_custom_url['state'] = 'disable'

        self.pack()
        #staus bar
        self.progress = Progressbar(self, orient=HORIZONTAL,length=300,  mode='indeterminate')
        #status bar end

    def _radio_Button_Option(self):
        if self.var.get()==0:
            self.entry_custom_url['state'] = 'disable'
        elif self.var.get()==1:
              self.entry_custom_url['state'] = 'normal'
              



    def my_spider(self):
        self.progress.grid(row=1,column=0,sticky=W)
        self.progress.start()
        self.process = CrawlerProcess({'USER_AGENT': 'Mozilla/5.0 (X11; Linux x86_64; rv:61.0) Gecko/20100101 Firefox/61.0', 'Accept-Language': 'he,en-US;q=0.7,en;q=0.3'})
        #process.crawl(CollegeSpider, urlToCrawl=self.myUrlChoise, user_id=self.entry_username.get(), password_u=self.entry_password.get())
        self.process.crawl(CollegeSpider,start_urls=[self.passed_moodle_url], user_id=self.entry_username.get(), password_u=self.entry_password.get())
        self.process.start()
        self.progress.stop()
        self.progress.grid_forget()
        self.btnDownload['state']='normal'
        tm.showinfo(title="GREAT!", message=mp.FILES_DOWNLOADED_MSG)
        #self.btnDownload['state']='disabled'
    
    def _login_btn_clicked(self):
        #def real_traitement():
        self.CREDS_EMPTY = (self.entry_password.get()=="" or self.entry_username.get()=="")
        self.URL_KIN_CHOUSEN = (self.var.get()==0)
        self.URL_OTHER_CHOUSEN = (self.var.get()==1)
        self.CUSTOM_URL_ENTRY_EMPTY = (self.entry_custom_url.get()=="")
        if self.CREDS_EMPTY and self.URL_KIN_CHOUSEN:
            tm.showinfo(title="Invalid Input", message=mp.EMPTY_FIELDS_MSG)
        elif self.CREDS_EMPTY and self.CUSTOM_URL_ENTRY_EMPTY:
            tm.showinfo(title="Invalid Input", message=mp.EMPTY_FIELDS_MSG+" "+mp.CUSTUM_URL_EMPTY_MSG)
        elif(not self.CREDS_EMPTY and self.URL_KIN_CHOUSEN):
            self.passed_moodle_url = 'https://moodle.kinneret.ac.il'
            self.my_spider()
        elif(not self.CREDS_EMPTY and self.URL_OTHER_CHOUSEN):
            self.passed_moodle_url = self.entry_custom_url.get()
            self.my_spider()





root = Tk()
root.geometry("500x190")
root.title(mp.WINDOWS_TITILE)
lf = LoginFrame(root)
root.mainloop()
