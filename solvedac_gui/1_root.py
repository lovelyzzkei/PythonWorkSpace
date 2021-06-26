import re
import os
import sys
import time
from urllib.request import urlretrieve
import requests
from PyQt5 import QtCore
from PyQt5.QtWidgets import *
from PyQt5.QtGui import QFont, QPixmap

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
import chromedriver_autoinstaller
import pyperclip
import time
import subprocess


class SolvedAc(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowFlag(QtCore.Qt.FramelessWindowHint)
        self.initUI()

    # solved.ac 로그인
    def login(self):
        # 디버거 크롬 -> 자동화된 소프트웨어로 제어되는 것이 아님을 알려주기 위한 코드
        try:
            subprocess.Popen(r'C:\Program Files\Google\Chrome\Application\chrome.exe --remote-debugging-port=9222 --user-data-dir="C:\chrometemp1"')  # 디버거 크롬 구동
        except:
            subprocess.Popen(r'C:\Program Files (x86)\Google\Chrome\Application\chrome.exe --remote-debugging-port=9222 --user-data-dir="C:\chrometemp1"')  # 디버거 크롬 구동
        option = Options()
        # option.add_argument(f'user-agent={userAgent}')
        option.add_experimental_option("debuggerAddress", "127.0.0.1:9222")

        # selenium 구동을 위한 chromedriver 설치 여부 확인. 없으면 설치
        chrome_ver = chromedriver_autoinstaller.get_chrome_version().split('.')[0]
        try:
            driver = webdriver.Chrome(f'./{chrome_ver}/chromedriver.exe', options=option)
        except:
            chromedriver_autoinstaller.install('./')
            driver = webdriver.Chrome(f'./{chrome_ver}/chromedriver.exe', options=option)
        driver.implicitly_wait(1)
        # 쿠키를 한번 생성해주는 것이 필요할 듯
        # driver.get("https://naver.com")

        # solved.ac와 연결되어 있는 로그인 사이트로 연결
        driver.get("https://www.acmicpc.net/login?next=%2Fsso%3Fsso%3Dbm9uY2U9ZWYwZTY0MTE4MWFlMDBlYTI5YzI5YmIzMjljNjExMDA%253D%26sig%3Ddf153da15f308ab03e3c71828da71b75e05537040fc62d6e7aafedfacf548435%26redirect%3Dhttps%253A%252F%252Fsolved.ac%252Fapi%252Fv3%252Fauth%252Fsso%253Fprev%253D%25252F")
        uid = "march381@naver.com"
        upw = 'conanthekiller13'

        tag_id = driver.find_element_by_name("login_user_id")
        tag_pw = driver.find_element_by_name("login_password")

        pyperclip.copy(uid)
        tag_id.send_keys(Keys.CONTROL, 'v')
        time.sleep(0.1)

        pyperclip.copy(upw)
        tag_pw.send_keys(Keys.CONTROL, 'v')
        time.sleep(0.1)

        driver.find_element_by_id("submit_button").click()
        driver.find_element_by_xpath('//*[@id="login_form"]/div[4]/div[2]/a').click()        
        
        # 사용자의 아이디가 email일 경우 / 그렇지 않을 경우 구분
        p = re.compile('^[a-zA-Z0-9+-_.]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$')
        if p.match(uid):
            p = re.compile('^[a-zA-Z0-9]+')
            uid = p.match(uid).group()

        driver.get(f"https://solved.ac/{uid}")
        return driver

    def get_profile_img(self, driver):
        img_url = driver.find_element_by_xpath('//*[@id="__next"]/div[3]/div[1]/div/div/div[1]/img[1]').get_attribute('src')
        urlretrieve(img_url, 'profile_img.jpg')

    def initUI(self):
        # GUI 폰트 설정
        # 프로그램 종료 버튼
        btn_exit = QPushButton('종료', self)
        btn_exit.setFont(QFont('카페24 써라운드', 12))
        btn_exit.move(540, 350)
        def exit_program():
            time.sleep(0.2)
            sys.exit()
        btn_exit.clicked.connect(exit_program)

        # solved.ac 홈페이지 접속
        driver = self.login()
        self.get_profile_img(driver)


        # 프로필 사진 불러오기
        profile_img = QLabel(self)
        profile_img.move(10, 10)

        pixmap = QPixmap('profile_img.jpg')
        profile_img.setPixmap(pixmap)


        self.setGeometry(1280, 0, 640, 400)
        self.show()



if __name__ == "__main__":
    # QApplication: 위젯을 채워넣는 공간. GUI 프로그램의 기본이 되는 클래스
    app = QApplication(sys.argv)

    w = SolvedAc()
    sys.exit(app.exec_())