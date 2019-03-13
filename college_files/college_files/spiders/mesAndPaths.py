

URL_MOODLE_TO_CRAWL = 'https://moodle.kinneret.ac.il'
INVALID_USERNAME_PASS_MESS = "Invalid username or password. Try again."
CHECK_IF_LOGIN_STR = '/my'
#STR with the information about the user:
USER_NAME_PATH = '//div/header/div/div/h1/text()'
COURSE_CONTAINER_PATH = 'div.well'
BLANK_SPACE_ON_HTML = "\n"
A_ATTR_HTML = 'a::text'
HREF_ATTR_HTML = 'a::attr(href)'
CS_PATH_HTML_TOPICS = 'ul.topics'
CS_PATH_HTML_SECTION = 'li.section'
REG_EXP_TAKE_ONLY_IDNUMBER = 'https:\/\/moodle\.kinneret\.ac\.il\/mod\/resource\/view\.php\?id\=.*'
A_REAL_FILE = "application"





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

