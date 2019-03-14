
'''
This _Messages and Paths__ file contains the Needed parameters for the Script to work.
Please feel free to make Changes here depending on your MOODLE version.
I might add automation to this file in the future.

Yo0x.


Observations to the MOODLE VERSION: 3.17
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
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
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
'''
# #################### - Please change this paramaters according to your Moodle version ###########################
#The URL of your Moodle Site.
#url_moodle_to_crawl = ''
#The Message you want tell the user.
INVALID_USERNAME_PASS_MESS = "Invalid username or password. Try again."
#Condition to Know if the user has logged in successfully.
CHECK_IF_LOGIN_STR = '/my'
#STR with the information about the user's full name:
USER_NAME_PATH = '//div/header/div/div/h1/text()'
#CSS selector, that points to the Courses.
COURSE_CONTAINER_PATH = 'div.well'
#Str to avoid wrong file downlading.
BLANK_SPACE_ON_HTML = "\n"
#CSS selector that brings the <text/ field from the <DIV> Container.
A_ATTR_HTML = 'a::text'
#CSS selector that brings the <href/ attribute from the <DIV> Container.
HREF_ATTR_HTML = 'a::attr(href)'
#CSS selector that holds the TOPICS
CS_PATH_HTML_TOPICS = 'ul.topics'
#CSS selector that holds the SECTIONS
CS_PATH_HTML_SECTION = 'li.section'
#Regular expression that makes sure that the URL passed to the download_link method is a file.
REG_EXP_TAKE_ONLY_IDNUMBER = 'https:\/\/moodle\.kinneret\.ac\.il\/mod\/resource\/view\.php\?id\=.*'
#STR makes sure is a file and not a link.
A_REAL_FILE = "application"

#GUI Messages
WATNING_MSG = "CollegeFiles was written by Yo0x. It is free software, and can be used, modified and distributed under the terms of the ​Do W.T.F.P License. http://www.wtfpl.net"
FILES_DOWNLOADED_MSG = "Your files have been downloaded to the home folder!"
WINDOWS_TITILE = "<<< Moodle Downloader V1.0 By-Yo0x>>>"
EMPTY_FIELDS_MSG = "username and password cannot be empty."
CUSTUM_URL_EMPTY_MSG = "Error. \n Custom url cannot be empty"