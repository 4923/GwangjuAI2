import pandas as pd
import csv

# 결제 일자 관련
import time
import datetime as dt

# 보안코드 생성
import string
import random

# 캡쳐
import pyautogui 

# 이미지 첨부해서 이메일 보내기
import smtplib
import os
from email.mime.base import MIMEBase
from email import encoders

class Commerce6_product :

  def __init__(self, ACCOUNT_INFO) :
    self.id = ACCOUNT_INFO['id'].to_list()[0]
    self.pw = ACCOUNT_INFO['pw'].to_list()[0]
    self.nickname = ACCOUNT_INFO['nickname'].to_list()[0]
    self.location = ACCOUNT_INFO['location'].to_list()[0]
    with open("C:/Users/wjsdn/Desktop/woong/my_cart.csv", "r+") as file:
      file.truncate(0)

  # 보안코드 출력 함수
  def secure():
    code =  string.ascii_letters  # 영어 소문자부터 대문자까지 생성(abc ... XYZ) string.ascii_lowercase, string.ascii_uppercase

    while True:
      secure_code= ''
      for i in range(6):
        secure_code+= random.choice(code)
      print( " ----------" )
      print("ㅣ "+'\033[33m' + secure_code + '\033[0m' + " ㅣ")
      print( " ----------" )
      secure_code_check = input("안전결제를 위해 위에 보이는 문자를 그대로 입력해 주세요. : ")
      if secure_code ==secure_code_check :
        print("인증이 완료되었습니다.")
        break
      else:
        print("틀렸습니다.\n")
        continue 

    return True

  # 이메일 보내기
  def send_mail(name, email) : 

    s = smtplib.SMTP('smtp.gmail.com', 587)
    s.starttls()

    s.login(email, 'rtersvtvnhshrmyg')

    msg = MIMEBase('multipart', 'mixed') #객체 생성 / maintype(내용 포맷)과 subtype(내용 형식)

    # MIME은 메시지 말고 다른 이진 파일들을 보내려면 인코딩 하여 텍스트로 바꾸어 전달하고 다시 이진 파일로 디코딩
    path = 'C:/Users/wjsdn/Desktop/woong/reciept.png' #보낼 이미지의 경로
    part = MIMEBase("application", "octet-stream")
    part.set_payload(open(path, 'rb').read())  # 'rb' : byte 타입으로 변환
    encoders.encode_base64(part)
    part.add_header('Content-Disposition', 'attachment; filename="%s"'% os.path.basename(path))

    msg.attach(part)

    msg['Subject'] = '{}님 파이썬에서 결제하신 영수증입니다.'.format(name)

    s.sendmail(email, email, msg.as_string()) # 보내는 이메일 / 받는 이메일
    s.quit()

  # 상품 정보 보기
  def product_infomation_resule(self) :

    global product_df
    global login_df
    global choice_product_booknumber

    login_df = pd.read_csv("C:/Users/wjsdn/Desktop/woong/Commerce6_login.csv", encoding = 'euc-kr')
    product_df = pd.read_csv("C:/Users/wjsdn/Desktop/woong/bestsellers with categories.csv")
    
    while True :
      product_df = pd.read_csv("C:/Users/wjsdn/Desktop/woong/bestsellers with categories.csv")
      product_choice_options = int(input("평점높은순(1) / 리뷰많은순(2) / 낮은가격순(3) / 높은가격순(4) / 최신출시순(5) / 장르별(6) / 장바구니 확인(7): "))
      
      if product_choice_options == 1 :
        product_df = product_df.sort_values(by=['User Rating'], axis=0, ascending=False)
      elif product_choice_options == 2 :
        product_df = product_df.sort_values(by=['Reviews'], axis=0, ascending=False)
      elif product_choice_options == 3 :
        product_df = product_df.sort_values(by=['Price'], axis=0, ascending=True)
      elif product_choice_options == 4 :
        product_df = product_df.sort_values(by=['Price'], axis=0, ascending=False)
      elif product_choice_options == 5 :
        product_df = product_df.sort_values(by=['Year'], axis=0, ascending=False)
      elif product_choice_options ==6:
        select_Genre=int(input("장르를 선택하세요(Fiction(1) /Non Fiction(2)) : "))
        # Fiction
        if select_Genre== 1 :
          product_df= product_df[(product_df['Genre']=='Fiction')]
          print("\n장르(Fiction)순으로 정렬되었습니다.")
          select_rating=input("평점높은순(1) / 리뷰많은순(2) / 낮은가격순(3) / 높은가격순(4) / 최신출시순(5) : ")
          if select_rating=="1":
            product_df=product_df.sort_values(by=['User Rating'], axis=0, ascending=False)
          elif select_rating=="2":
            product_df=product_df.sort_values(by=['Reviews'], axis=0, ascending=False)
          elif select_rating=="3":
            product_df=product_df.sort_values(by=['Price'], axis=0, ascending=True)   
          elif select_rating=="4":
            product_df = product_df.sort_values(by=['Price'], axis=0, ascending=False)
          elif select_rating=="5":
            product_df = product_df.sort_values(by=['Year'], axis=0, ascending=False)
        # Non_fiction
        elif select_Genre == 2 :          
          product_df= product_df[(product_df['Genre']=='Non Fiction')]
          print("\n장르(Non Fiction)순으로 정렬되었습니다.")
          select_rating=input("평점높은순(1) / 리뷰많은순(2) / 낮은가격순(3) / 높은가격순(4) / 최신출시순(5) : ")
          if select_rating=="1":
            product_df=product_df.sort_values(by=['User Rating'], axis=0, ascending=False)
          elif select_rating=="2":
            product_df=product_df.sort_values(by=['Reviews'], axis=0, ascending=False)
          elif select_rating=="3":
            product_df=product_df.sort_values(by=['Price'], axis=0, ascending=True)   
          elif select_rating=="4":
            product_df = product_df.sort_values(by=['Price'], axis=0, ascending=False)
          elif select_rating=="5":
            product_df = product_df.sort_values(by=['Year'], axis=0, ascending=False)
      elif product_choice_options == 7:
        Commerece6_purchase(self.id, self.pw).cart_look()
        break
      
      product_df = product_df.reset_index(drop=True) 

      for i in range( 5 ) :
        print( "-------------------------------" )
        print( "-{} 번째 서적번호------------------".format(i+1) )
        print( "-------------------------------" )
        for j in range( len(product_df.columns) ) :
          if j == 4 :
            print( "{} : {} 원".format(product_df.columns.to_list()[j], format(product_df.loc[i][j]*1000, ",") ) )
          else :
            print( "{} : {}".format(product_df.columns.to_list()[j], product_df.loc[i][j]) )
        print( "-------------------------------" )

      choice_product_booknumber = int(input("구매하실 서적 번호를 입력 : "))

      print( "{} 님, 구매 신청하신 서적은 {} 입니다.".format( login_df.loc[(login_df['id'] == self.id) & (login_df['pw'] == self.pw)]['nickname'].values[0], product_df.loc[choice_product_booknumber-1][0] ) )
      print( "가격은 {} 원입니다.".format( product_df.loc[choice_product_booknumber-1][4]*1000 ) )

      choice_product_bookorder = int(input("구매(1) / 비구매(2) / 장바구니에 담기(3) : "))
      break_number2 = 0

      if choice_product_bookorder == 1:
        data_list = (self.id, product_df.loc[choice_product_booknumber-1][0], (product_df.loc[choice_product_booknumber-1][4])*1000) #제목, 가격 data
        with open("C:/Users/wjsdn/Desktop/woong/my_cart.csv", "a") as file:
          writer = csv.writer(file)
          writer.writerow(data_list)
        Commerece6_purchase(self.id, self.pw).cart_look()
        break

      elif choice_product_bookorder == 2 :
        print("다른 서적을 확인 중")
        pass

      elif choice_product_bookorder == 3:
        data_list = (self.id, product_df.loc[choice_product_booknumber-1][0], (product_df.loc[choice_product_booknumber-1][4])*1000) #제목, 가격 data
        with open("C:/Users/wjsdn/Desktop/woong/my_cart.csv", "a", newline='') as file:
          writer = csv.writer(file)
          writer.writerow(data_list)
        print("{}님이 선택하신 책 {}({})가 장바구니에 담겼습니다.\n".format(self.id, product_df.loc[choice_product_booknumber-1][0], product_df.loc[choice_product_booknumber-1][1]))
      if break_number2 == 1 :
        break

    return 'product_choose_success'

  # 영수증 출력 함수
  def product_receipt(self):
    
    cartedit_df = pd.read_csv("C:/Users/wjsdn/Desktop/woong/my_cartedit.csv", header=None, names=['Title', 'Price'], usecols=[1,2])
    
    now = dt.datetime.now()
    
    receipt_string = input("영수증을 발급하시겠습니까? Y / N : ")
    if receipt_string == 'Y' :
      print("영수증을 발급 중입니다.")
      time.sleep(2)
      print("-------------------------------")
      print("영수증")
      print("주문 목록 : {} 등 {}개".format(cartedit_df['Title'][0],len(cartedit_df)))
      print("금액 : {}원".format(cartedit_df['Price'].sum()))
      print("상기 금액을 {}년 {}월 {}일 수령하고 위 금액의 수령을 증표로서 본 영수증을 발행합니다.".format(now.year, now.month, now.day))
      print("주소 : {}".format(login_df.loc[(login_df['id'] == self.id) & (login_df['pw'] == self.pw)]['location'].values[0]))
      print("닉네임 : {}".format(login_df.loc[(login_df['id'] == self.id) & (login_df['pw'] == self.pw)]['nickname'].values[0]))
      print("-------------------------------")
      time.sleep(0.1)
      pyautogui.screenshot('C:/Users/wjsdn/Desktop/woong/reciept.png', region=(115, 737, 1500, 200) )
      Commerce6_product.send_mail("전웅", "wjsdnd03@gmail.com")
    elif receipt_string == 'N' :
      pass

    request = input("배송 시 요청사항이 있으신가요? ")
    time.sleep(1)
    print("배송을 시작합니다.\n")
    print("-------------------------------")
    print("배송정보")
    print("{}님이 구매 신청하신 서적 {}등 {}개가 {}로 3일내로 도착 예정입니다.".format(login_df.loc[(login_df['id'] == self.id) & (login_df['pw'] == self.pw)]['nickname'].values[0],cartedit_df['Title'][0],len(cartedit_df),login_df.loc[(login_df['id'] == self.id) & (login_df['pw'] == self.pw)]['location'].values[0]))
    if request != None:
      print("요청사항 : {}".format(request))
    print("구매해 주셔서 감사합니다!")
    print("-------------------------------")
  
  # 장바구니 관련
class Commerece6_purchase() :
  def __init__(self, id, pw) :
    self.id = id
    self.pw = pw

  def cart_look(self):
    
    cart_df = pd.read_csv("C:/Users/wjsdn/Desktop/woong/my_cart.csv", header=None, names=['Title', 'Price'], usecols=[1,2])
    total_price = 0

    for i in range(len(cart_df)):
      total_price += cart_df['Price'][i]

    if cart_df.empty:
      print('현재 {}님의 장바구니가 비어있습니다.'.format(self.id))
      self.product_infomation_resule()
    else:
      print('----------{}님의 장바구니 입니다. 총 {}권--------------\n{}'.format(login_df.loc[(login_df['id'] == self.id) & (login_df['pw'] == self.pw)]['nickname'].values[0], len(cart_df), cart_df))
      print('')
      print('-----------------------------------------------------------')
      number = (int(input('전체 구입을 원하시면 1번, 부분 구입을 원하시면 2번을 눌러주세요: ')))
      print("구매 진행중입니다.")
      time.sleep(2)
      if number == 1:
        if Commerce6_product.secure() :
          print("결제처리 진행 중")
          time.sleep(3)
          self.all_purchase()
      elif number == 2:
        self.choice_purchase()    

  def all_purchase(self):

    cart_df = pd.read_csv("C:/Users/wjsdn/Desktop/woong/my_cart.csv", header=None, names=['Title', 'Price'], usecols=[1,2])

    total_price = 0

    with open('C:/Users/wjsdn/Desktop/woong/my_cart.csv', 'r') as inp, open('C:/Users/wjsdn/Desktop/woong/my_cartedit.csv', 'w', newline='') as out:  
      writer = csv.writer(out)
      
      for data in csv.reader(inp): 
        writer.writerow(data)

    for i in range(len(cart_df)):
      total_price += cart_df['Price'][i]
    print('{}님, 총 {}원이 구매가 완료되었습니다.'.format(login_df.loc[(login_df['id'] == self.id) & (login_df['pw'] == self.pw)]['nickname'].values[0], total_price))

  
  def choice_purchase(self):
    cart_df = pd.read_csv("C:/Users/wjsdn/Desktop/woong/my_cart.csv", header=None, names=['Title', 'Price'], usecols=[1,2])
    total_price = 0

    print("구매를 원하시는 책 번호를 입력해주세요.(형식 : 0 1 4 5)")
    choice_cart = [int(x) for x in input().split()]
    for i in range(len(choice_cart)):
        print(cart_df['Title'][choice_cart[i]])
        total_price += cart_df['Price'][choice_cart[i]]

    with open('C:/Users/wjsdn/Desktop/woong/my_cart.csv', 'r') as inp, open('C:/Users/wjsdn/Desktop/woong/my_cartedit.csv', 'w', newline='') as out:  
      writer = csv.writer(out)

      for data in csv.reader(inp): 
        for i in range(len(choice_cart)):
          if data[1] == cart_df['Title'][choice_cart[i]]:
           writer.writerow(data)

    if Commerce6_product.secure() :
      print("결제처리 진행 중")
      time.sleep(3)
      print('{}님, 선택하신 책의 총 {}원 구매가 완료되었습니다.'.format(login_df.loc[(login_df['id'] == self.id) & (login_df['pw'] == self.pw)]['nickname'].values[0], total_price))

