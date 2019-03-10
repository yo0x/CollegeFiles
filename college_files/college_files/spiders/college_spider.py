import scrapy
import os
import cgi
import tkinter.messagebox as tm
from scrapy.shell import inspect_response
# this can check the response of the pider at any time with: inspect_response(response, self)
import re


class CollegeSpider(scrapy.Spider):

    name = 'college_spider'
    urlToCrawl = ''
    start_urls = ['https://moodle.kinneret.ac.il']
    #start_urls = [urlToCrawl]



    def parse(self, response):

        return scrapy.FormRequest.from_response(
                response,
                formdata={'username': self.user_id, 'password': self.password_u},

                callback=self.after_login

        )


    def after_login(self, response):
        #inspect_response(response, self)
        if not '/my' in response.url:
            tm.showwarning("Error","Invalid username or password. Try again.")
        else:
            
            user_name = response.xpath('//div/header/div/div/h1/text()').extract()
            myFilesDir = "הקורסים של:  {0}".format(user_name).encode('utf8')
            cursos_first = response.css('div.well')
            myFilesDirUser = os.path.join(os.path.expanduser("~"), myFilesDir.decode('utf8'))
            if not os.path.exists(myFilesDirUser):
                os.makedirs(myFilesDirUser)
            print("Hello MR.ROBOT {0}".format(user_name))

            for my_course in cursos_first.css('a'):
            # inspect_response(response, self)
                if "\n" not in my_course.css('a::text').extract_first():
                    my_course_dir = os.path.join(myFilesDirUser, my_course.css('a::text').extract_first())
                    print(my_course_dir)
                    if not os.path.exists(my_course_dir):
                        os.makedirs(my_course_dir)
                    yield response.follow(my_course.css('a::attr(href)').extract_first(), callback=self.parse_files, meta={'file_dir':my_course_dir})
                    print("DID NOT YIELD")
        


    def parse_files(self, response):
        topics = response.css('ul.topics')
        sections = topics.css('li.section')
        folder_name = response.meta['file_dir']

        for link_s in sections.css('a::attr(href)').extract():
            print(">>>>>>>>>>>>>>>>>>>>>>>>FOROPEN>>>>>>>>>>>>>>>>>>>>>>>>>")
            if re.match('https:\/\/moodle\.kinneret\.ac\.il\/mod\/resource\/view\.php\?id\=.*', link_s):
                file_lname = os.path.join(folder_name, sections.css('span::text').extract_first())
                yield response.follow(link_s, callback=self.download_link, meta={'file_com_name':folder_name})
            print("<<<<<<<<<<<<<<<<<<<<<<<<<FOR CLOSED<<<<<<<<<<<<<<<<<<<<<<<<")

#2
    def download_link(self, response):
        print("ANTES DEL IF:>>>")
        check_cont_file = response.headers.getlist('Content-Type')
        check_cont_file3 = response.headers.getlist('Content-Disposition')
        check_cont_file2 = check_cont_file[0].decode("utf-8")
        check_cont_file4 = check_cont_file3[0].decode("utf-8")
        value, params = cgi.parse_header(check_cont_file4)
        folder_name2 = response.meta['file_com_name']
        file_name_saved3 = os.path.join(folder_name2, params.get('filename'))
        print(file_name_saved3)
        if not "application" in check_cont_file2:
            print("NOT A FILE{0}".format(check_cont_file2))
            print(check_cont_file2)
        else:
            with open(file_name_saved3, 'wb') as out_file:
                out_file.write(response.body)
            print("Item: {0} was saved".format(file_name_saved3))


#1
    """
    
#response.xpath('//div/header/div/div/h1/text()').extract() name_student
#-----------------------------------------------------Cursos
#fase1 = response.css('div.well')      >>>>>>>>>Cursos
#fase1.css('a::text').extract()     >>>>>> nombres de cursos.
#fase1.css('a::attr(href)').extract() >>> links cursos
#-----------------------------------------------------Cursos
#topics = response.css('ul.topics')
#sections = topics.css('li.section')
#sections.css('a::text').extract_first() nombres topics
#sections.css('span::text').extract() >> nombres archivos curso
#sections.css('a::attr(href)').extract() >> link to files course



"""

