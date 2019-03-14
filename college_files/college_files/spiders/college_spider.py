import scrapy
import os
import cgi
import tkinter.messagebox as tm
from scrapy.shell import inspect_response
from . import mesAndPaths as mp
# inspect_response(response, self) >>>> For debbuging.
import re


class CollegeSpider(scrapy.Spider):
    name = 'college_spider'
    
    def parse(self, response):
        return scrapy.FormRequest.from_response(
                response,
                formdata={'username': self.user_id, 'password': self.password_u},

                callback=self.after_login
        )


    def after_login(self, response):
        #inspect_response(response, self)
        if not mp.CHECK_IF_LOGIN_STR in response.url:
            tm.showwarning("Error",mp.INVALID_USERNAME_PASS_MESS)
            raise SystemExit
        else:
            user_name = response.xpath(mp.USER_NAME_PATH).extract()
            myFilesDir = "{0} - COURSES".format(user_name).encode('utf8')
            cursos_first = response.css(mp.COURSE_CONTAINER_PATH)
            myFilesDirUser = os.path.join(os.path.expanduser("~"), myFilesDir.decode('utf8'))
            if not os.path.exists(myFilesDirUser):
                os.makedirs(myFilesDirUser)
            for my_course in cursos_first.css('a'):
            # inspect_response(response, self)
                if mp.BLANK_SPACE_ON_HTML not in my_course.css(mp.A_ATTR_HTML).extract_first():
                    my_course_dir = os.path.join(myFilesDirUser, my_course.css(mp.A_ATTR_HTML).extract_first())
                    print(my_course_dir)
                    if not os.path.exists(my_course_dir):
                        os.makedirs(my_course_dir)
                    yield response.follow(my_course.css(mp.HREF_ATTR_HTML).extract_first(), callback=self.parse_files, meta={'file_dir':my_course_dir})
        


    def parse_files(self, response):
        topics = response.css(mp.CS_PATH_HTML_TOPICS)
        sections = topics.css(mp.CS_PATH_HTML_SECTION)
        folder_name = response.meta['file_dir']
        for link_s in sections.css(mp.HREF_ATTR_HTML).extract():
            if re.match(mp.REG_EXP_TAKE_ONLY_IDNUMBER, link_s):
                file_lname = os.path.join(folder_name, sections.css('span::text').extract_first())
                yield response.follow(link_s, callback=self.download_link, meta={'file_com_name':folder_name})

#2
    def download_link(self, response):
        check_cont_file = response.headers.getlist('Content-Type')
        check_cont_file3 = response.headers.getlist('Content-Disposition')
        check_cont_file2 = check_cont_file[0].decode("utf-8")
        check_cont_file4 = check_cont_file3[0].decode("utf-8")
        value, params = cgi.parse_header(check_cont_file4)
        folder_name2 = response.meta['file_com_name']
        file_name_saved3 = os.path.join(folder_name2, params.get('filename'))
        print(file_name_saved3)
        if not mp.A_REAL_FILE in check_cont_file2:
            print("NOT A FILE{0}".format(check_cont_file2)) #Debugging
            print(check_cont_file2)
        else:
            with open(file_name_saved3, 'wb') as out_file:
                out_file.write(response.body)
            print("Item: {0} was saved".format(file_name_saved3))#Debugging


