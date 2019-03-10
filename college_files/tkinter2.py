from tkinter import *
import tkinter.messagebox as tm
from scrapy.crawler import CrawlerProcess
from college_files.spiders.college_spider import CollegeSpider
from tkinter.ttk import Progressbar
import time
import threading
class LoginFrame(Frame):
    def __init__(self, master):
        super().__init__(master)
        tm.showwarning("Disclaimer", "CollegeFiles was written by Yo0x. It is free software, and can be used, modified and distributed under the terms of the ​Do W.T.F.P License. http://www.wtfpl.net  ")
        self.label_username = Label(self, text="Username (ID NUMBER)")
        self.label_password = Label(self, text="Password")
        self.entry_username = Entry(self)
        self.entry_password = Entry(self, show="*")
        # on change dropdown value
        self.label_username.grid(row=0, sticky=E)
        self.label_password.grid(row=2, sticky=E)
        self.entry_username.grid(row=0, column=1)
        self.entry_password.grid(row=2, column=1)
        #self.checkbox = Checkbutton(self, text="Keep me logged in")
        #self.checkbox.grid(columnspan=3)
        self.logbtn = Button(self, text="<<Download my files>>", command=self._login_btn_clicked)
        self.logbtn.grid(columnspan=2)
        self.logbtn2 = Button(self, text="Close", command=root.destroy)
        self.logbtn2.grid(row=4, column=2)

        self.pack()
        #staus bar
       
        self.progress = Progressbar(self, orient=HORIZONTAL,length=300,  mode='indeterminate')
        self.myUrlChoise = 'https://moodle.kinneret.ac.il'


        #status bar end

    def my_spider(self):
        self.process = CrawlerProcess({'USER_AGENT': 'Mozilla/5.0 (X11; Linux x86_64; rv:61.0) Gecko/20100101 Firefox/61.0', 'Accept-Language': 'he,en-US;q=0.7,en;q=0.3'})
        #process.crawl(CollegeSpider, urlToCrawl=self.myUrlChoise, user_id=self.entry_username.get(), password_u=self.entry_password.get())
        self.process.crawl(CollegeSpider, user_id=self.entry_username.get(), password_u=self.entry_password.get())
        self.process.start()
    
    def _login_btn_clicked(self):
        #def real_traitement():

        self.progress.grid(columnspan=2)
        self.progress.start()
        self.my_spider()
        self.progress.stop()
        self.progress.grid_forget()
        self.logbtn['state']='normal'
        tm.showinfo(title="GREAT!", message="Your files have been downloaded to the home folder!")

        self.logbtn['state']='disabled'
        #threading.Thread(target=real_traitement).start()

'''
            process = CrawlerProcess({'USER_AGENT': 'Mozilla/5.0 (X11; Linux x86_64; rv:61.0) Gecko/20100101 Firefox/61.0', 'Accept-Language': 'he,en-US;q=0.7,en;q=0.3'})
            process.crawl(CollegeSpider, urlToCrawl=self.myUrlChoise, user_id=self.entry_username.get(), password_u=self.entry_password.get())
            process.start()
'''            

            
        
        
root = Tk()
root.geometry("400x100")
root.title("<<< Moodle Downloader V1.0 By-Yo0x>>>")
lf = LoginFrame(root)
root.mainloop()
