import os
import random
import shutil
import tempfile
from itertools import count
from random import randint
import requests
import undetected_chromedriver.v2 as uc
from time import sleep
from selenium import webdriver
import json
import string
from PyQt5.QtWidgets import *
from PyQt5.QtCore import QThread,pyqtSignal
from PyQt5 import uic






class UI(QMainWindow):
    def __init__(self):
        super(UI,self).__init__()
        uic.loadUi('Data/uiRobocat.ui',self)
        self.pushButton = self.findChild(QPushButton,'pushButton')
        self.pushButton.clicked.connect(self.start)
        self.spinBox = self.findChild(QSpinBox,'spinBox')
        self.spinBox_2 = self.findChild(QSpinBox,'spinBox_2')
        self.label_3 = self.findChild(QLabel,'label_3')
        self.label_4 = self.findChild(QLabel,'label_4')
        self.lineEdit = self.findChild(QLineEdit,'lineEdit')
        self.lineEdit_2 = self.findChild(QLineEdit,'lineEdit_2')
        self.loadApiSim()
        self.loadURL()
        self.show()
        self.callThread = StartThread()
    def showStatus(self,status):
        self.label_4.setText(status)
    def totalSuccess(self,sucess):
        self.label_3.setText(sucess)
    def loadApiSim(self):
        try:
            with open('Data/Reload/ApiSim.txt','r') as Api:self.lineEdit.setText(Api.read())
        except:pass
    def saveApiSim(self):
        try:
            with open('Data/Reload/ApiSim.txt', 'w') as Api:
                Api.write(self.lineEdit.text())
        except:pass
    def loadURL(self):
        try:
            with open('Data/Reload/URL.txt','r') as URL:self.lineEdit_2.setText(URL.read())
        except:pass
    def saveURL(self):
        try:
            with open('Data/Reload/URL.txt', 'w') as URL:
                URL.write(self.lineEdit_2.text())
        except:pass
    def start(self):
        self.saveApiSim()
        self.saveURL()
        self.callThread.spinBox = self.spinBox
        self.callThread.spinBox_2 = self.spinBox_2
        self.callThread.lineEdit = self.lineEdit
        self.callThread.lineEdit_2 = self.lineEdit_2
        self.callThread.start()
        self.callThread.lbstatus.connect(self.showStatus)
        self.callThread.totalSucessfull.connect(self.totalSuccess)

class StartThread(QThread):
    totalSucessfull = pyqtSignal(str)
    countTotal = count(0)
    lbstatus = pyqtSignal(str)
    def __init__(self):
        super(StartThread,self).__init__()
    def run(self):
        count = 0
        while count < self.spinBox_2.value():
            try:
                self.active()
                count += 1
                timesleep = random.randint(0,self.spinBox.value()*60)
                for i in range(timesleep,0,-1):
                    self.lbstatus.emit(f'Hệ Thống Sẽ Khởi Động Sau {i}s')
                    sleep(1)
            except:count += 1

    def getPhonenumber(self):
        # Get PhoneNumber
        dataPhoneNumber = requests.get(f'https://chothuesimcode.com/api?act=number&apik={self.lineEdit.text()}&appId=1249')
        jsonData = json.loads(dataPhoneNumber.text)
        phoneNumber = jsonData['Result']['Number']
        idNumber = jsonData['Result']['Id']
        return phoneNumber, idNumber

    def getCodeSMS(self,idNumber):
        count = 0
        while count <= 30:
            try:
                dataCodeSms = requests.get(f'https://chothuesimcode.com/api?act=code&apik={self.lineEdit.text()}&id={idNumber}')

                jsonData = json.loads(dataCodeSms.text)

                smsCode = jsonData['Result']['Code']
                return smsCode
                break
            except:
                sleep(5)
                count += 1

    def fullName(self):
        lastName = ['Nguyễn', 'Phạm', 'Trần', 'Lê', 'Hoàng', 'Phan', 'Vũ', 'Võ', 'Đặng', 'Bùi', 'Đỗ', 'Hồ', 'Ngô']
        midName = ['Hoài', 'Tú', 'Ngọc', 'Bảo', 'Nguyệt', 'Minh', 'Hương', 'Lan', 'Mai', 'Hạc', 'Nhật', 'Vân', 'Lam']
        firstName = ['An', 'Anh', 'Bích', 'Bình', 'Cát', 'Châu', 'Chi', 'Cúc', 'Dạ', 'Diệu', 'Du', 'Dung', 'Duyên',
                     'Đan', 'Đào', 'Giang', 'Hà', 'Hạ', 'Hằng']
        return f'{lastName[randint(0, len(lastName) - 1)]} {midName[randint(0, len(midName) - 1)]} {firstName[randint(0, len(firstName) - 1)]}'

    def createNameFriends(self):
        lastName = ['Nguyễn', 'Phạm', 'Trần', 'Lê', 'Hoàng', 'Phan', 'Vũ', 'Võ', 'Đặng', 'Bùi', 'Đỗ', 'Hồ', 'Ngô']
        firstName = ['An', 'Anh', 'Bích', 'Bình', 'Cát', 'Châu', 'Chi', 'Cúc', 'Dạ', 'Diệu', 'Du', 'Dung', 'Duyên',
                     'Đan',
                     'Đào', 'Giang', 'Hà', 'Hạ', 'Hằng']
        return f'{lastName[randint(0, len(lastName) - 1)]} {firstName[randint(0, len(firstName) - 1)]}'

    def createEmail(self):
        ascii = string.ascii_lowercase
        digits = string.digits
        theLastEmail = ['@gmail.com', '@yahoo.com.vn', '@outlook.com']

        email = random.choices(ascii, k=9)
        numbers = random.choices(digits, k=5)
        email = email + numbers
        email = ''.join(email) + theLastEmail[random.randint(0, len(theLastEmail) - 1)]
        return email

    def createCMT(self):
        firstNumber = ["001", "002", "004", "006", "010", "011", "012", "014", "015", "017", "019", "020", "022", "024",
                       "025", "026", "027",
                       "030", "031", "033", "034", "035", "036", "037", "038", "040", "042", "044", "045", "046", "048",
                       "049", "051", "052",
                       "054", "056", "058", "060", "062", "064", "066", "067", "068", "070", "072", "074", "075", "077",
                       "079", '080', '083']
        cmt = [firstNumber[random.randint(0, len(firstNumber) - 1)]]
        for i in range(0, 9):
            cmt.append(str(random.randint(0, 9)))
        numberCMT = ''.join(cmt)
        return numberCMT

    def createFBID(self):
        cmt = ['1000']
        for i in range(0, 11):
            cmt.append(str(random.randint(0, 9)))
        fbID = ''.join(cmt)
        return fbID

    def createBank(self):
        firstNumber = ['970436', '970418', '970406', '970426', '970422', '970423', '970432', '970431']
        return firstNumber[random.randint(0, len(firstNumber) - 1)] + str(random.randint(1000000, 9999999)) + str(
            random.randint(100000, 999999))

    def setBrowser(self):
        self.lbstatus.emit('Đang Khởi Tạo Hệ Thống')
        self.temp = os.path.normpath(tempfile.mkdtemp())
        opts = webdriver.ChromeOptions()
        args = ["hide_console", ]
        opts.add_argument("--window-size=920,880")
        opts.add_argument("--disable-popup-blocking")
        opts.add_argument("--incognito")
        opts.add_argument('--user-data-dir=' + self.temp)
        opts.add_argument("--use-fake-ui-for-media-stream")
        self.browser = uc.Chrome(options=opts)
        with self.browser:
            self.browser.get(self.lineEdit_2.text())
        self.lbstatus.emit('Khởi Tạo Thành Công')

    def active(self):
        try:
            self.lbstatus.emit('Đang Sử Lý Vui Lòng Đợi !')
            self.setBrowser()
            sleep(1)
            phoneNumber, idNumber = self.getPhonenumber()
            print(phoneNumber)
            self.browser.find_element_by_xpath('//*[@id="phone"]').send_keys(phoneNumber)
            sleep(1)
            # Submit Form

            self.browser.find_element_by_css_selector('.brand-submit-button.check-phone-btn.get-loan-button').click()
            sleep(1)


            self.browser.find_element_by_css_selector('.phone-check-btn.continue-btn').click()
            sleep(10)

            # Get Code SMS From PhoneNumber
            smsCode = self.getCodeSMS(idNumber)

            # Input Code SMS

            self.browser.find_element_by_xpath('//*[@id="sms_code"]').send_keys(smsCode)

            sleep(0.5)

            # Submit Form

            self.browser.find_element_by_id('btnDataRegister').click()

            sleep(2)


            fullName = self.fullName()

            self.browser.find_element_by_id('full_name').send_keys(fullName)
            sleep(0.5)

            # sendEmail

            email = self.createEmail()

            self.browser.find_element_by_id('email').send_keys(email)

            sleep(0.5)

            # Active CheckBox

            self.browser.find_element_by_id('agreementContentIndex').click()

            sleep(0.5)


            numberCMT = self.createCMT()
            self.browser.find_element_by_id('personnum').send_keys(numberCMT)

            sleep(1)
            dateCMT = f'{random.randint(0, 29)}{random.randint(0, 9)}{random.randint(2015, 2020)}'

            for item in list(dateCMT):
                self.browser.find_element_by_id('document_date').send_keys(item)
                sleep(0.1)
            # Noi Cap
            self.browser.find_element_by_xpath(f'//*[@id="document_location"]/option[{random.randint(2, 67)}]').click()

            sleep(2)


            # Ngay Sinh
            birthDay = f'{random.randint(0, 29)}{random.randint(0, 9)}{random.randint(1985, 2000)}'
            for item in list(birthDay):
                self.browser.find_element_by_id('birthday').send_keys(item)
                sleep(0.1)
            # Input Facebook ID

            fbID = self.createFBID()
            self.browser.find_element_by_id('facebook_id').send_keys(fbID)
            sleep(0.5)

            # Gioi Tinh

            check = random.randint(0, 1)
            if check == 0:
                self.browser.execute_script("""document.querySelector("#male").click();""")
            else:
                self.browser.execute_script("""document.querySelector("#female").click();""")
            sleep(1)

            #
            # Tinh Trang Hon Nhan

            self.browser.find_element_by_xpath('//*[@id="marital_status"]/option[2]').click()

            sleep(0.5)

            # Tinh Trang Con Cai

            self.browser.find_element_by_xpath('//*[@id="amount_children"]/option[2]').click()

            sleep(0.5)

            # Submit Form

            self.browser.find_element_by_id('btnDataRegister').click()

            sleep(4)

            # checkConfirm

            try:
                self.browser.find_element_by_id('full_name')
                sleep(0.5)
                self.browser.find_element_by_id('btnDataRegister').click()
                sleep(4)
            except:
                pass


            self.browser.find_element_by_xpath(f'//*[@id="address-municipality_id"]/option[{random.randint(2, 64)}]').click()
            sleep(3)


            self.browser.find_element_by_xpath(f'//*[@id="address-district_id"]/option[{random.randint(2, 6)}]').click()
            sleep(3)

            # Tower
            self.browser.find_element_by_xpath(f'//*[@id="address-ward_id"]/option[{random.randint(2, 6)}]').click()
            sleep(1.5)

            # Send PostCode

            self.browser.find_element_by_id('address-postcode').send_keys(random.randint(100000, 350000))
            sleep(1)

            # Get Info

            # Send Address

            self.browser.find_element_by_id('address-street').send_keys('Số 68')

            sleep(1)

            # Confirm Form
            self.browser.find_element_by_id('btnDataRegister').click()
            sleep(3)

            # Select Work
            self.browser.find_element_by_xpath('//*[@id="social_status_id"]/option[6]').click()
            sleep(1)

            # Send Name
            friendsName = self.createNameFriends()
            self.browser.find_element_by_id('relative_name').send_keys(friendsName)
            sleep(1)

            # Send PhoneNumber

            self.browser.find_element_by_id('relative_phone').send_keys(int(phoneNumber) + randint(10, 50))

            # Send Money

            self.browser.find_element_by_id('amount_monthly').send_keys('10000000')

            sleep(1)

            self.browser.find_element_by_xpath('//*[@id="btnDataRegister"]').click()

            sleep(5)

            # select Bank

            self.browser.find_element_by_xpath('//*[@id="payment_system_name_tmp"]/option[2]').click()

            sleep(1)
            numberBank = self.createBank()
            self.browser.find_element_by_id('BankCard-account_number').send_keys(numberBank)
            sleep(1)

            self.browser.find_element_by_xpath('//*[@id="addAccount"]/div[5]/button').click()

            sleep(5)

            # Click Start Take a Picture

            self.browser.find_element_by_xpath('/html/body/div[1]/div[3]/div/div/div[2]/div[3]/a').click()
            sleep(8)
            # take-snapshot
            # save-btn
            # btn-continue

            # Take A Picture
            self.browser.find_element_by_id('take-snapshot').click()
            sleep(3)
            self.browser.find_element_by_id('save-btn').click()
            sleep(3)
            self.browser.find_element_by_id('take-snapshot').click()
            sleep(3)
            self.browser.find_element_by_id('save-btn').click()
            sleep(5)
            self.browser.find_element_by_id('btn-continue').click()
            total = self.countdown()
            self.totalSucessfull.emit(f'Thành Công: {total + 1}')

            sleep(10)

            self.lbstatus.emit('Đang Dọn Dẹp Hệ Thống !')
            shutil.rmtree(r'{}'.format(self.temp))
            self.browser.close()
            self.browser.quit()
            sleep(3)
            self.lbstatus.emit('Hoàn Thành')
        except:
            self.lbstatus.emit('Đang Khởi Tạo Hệ Thống')
            shutil.rmtree(r'{}'.format(self.temp))
            self.browser.close()
            self.browser.quit()
            sleep(3)
            self.lbstatus.emit('Xảy Ra Lỗi ')
    def countdown(self):
        value = next(self.countTotal)
        return value
if __name__ == '__main__':
    import sys
    app = QApplication(sys.argv)
    UIWindow = UI()
    app.exec()

