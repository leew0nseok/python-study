# Using Selenium
import selenium
import time
from selenium import webdriver


options = webdriver.ChromeOptions()
# 창 숨기는 옵션 추가
options.add_argument("headless")
options.add_argument('disable-gpu')  # GPU 사용 안함
options.add_argument('lang=ko_KR')
driver = webdriver.Chrome(options=options)

# url = 'http://e-book.hufs.ac.kr/20220214_freshman_h2/'  # 신입생 수강편람 홈페이지
url = 'https://www.hufs.ac.kr/'  # 신입생 수강편람 홈페이지
driver.get(url)
driver.implicitly_wait(3)


# Calendar_img = driver.find_element_by_id('EBook1L')  # 학사일정표
Calendar_img = driver.find_element_by_css_selector(
    '#hd_quick > div.quick_menuR > ul:nth-child(1) > li:nth-child(4) > a')  # 학사일정표
# Calendar_img.screenshot(f'imgfolder/AcademicCalendar.png')

print(Calendar_img.text)
