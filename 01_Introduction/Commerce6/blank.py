# 로그인 / 회원 DB 처리  #홍예은 #최인남 
# 상품보기 / 상품결제   #전선유 #김세연 #전웅

import pandas as pd
import time
import string
import random
import datetime as dt
import csv

# 캡쳐
import pyautogui 

# 이미지 첨부해서 이메일 보내기
import smtplib
import os
from email.mime.base import MIMEBase
from email import encoders

# User information

class Commerece6_purchase :
    def __init__(self, ACCOUNT_INFO) :
        self.id = ACCOUNT_INFO['id'].to_list()[0]
        self.pw = ACCOUNT_INFO['pw'].to_list()[0]
    def cart_look(self):
        
        # pd.set_option('display.max.colwidth', 30 )  # 터미널 다음줄로 넘어가면 넓이 줄이기
        cart_df = pd.read_csv("./my_cart.csv", header=None, names=['Title', 'Price'], usecols=[1,2])
        total_price = 0
        for i in range(len(cart_df)):
            total_price += cart_df['Price'][i]
        if cart_df.empty:
            print('현재 {}님의 장바구니가 비어있습니다.'.format(self.id))
        else:
            print('----------{}님의 장바구니 입니다. 총 {}권--------------\n{}'.format(self.id, len(cart_df), cart_df))
            print('')
            print('-----------------------------------------------------------')
            number = (int(input('전체 구입을 원하시면 1번, 부분 구입을 원하시면 2번을 눌러주세요: ')))
            if number == 1:
              if Commerce6_product.secure() :
                self.all_purchase()
            elif number == 2:
                self.choice_purchase()    
    def all_purchase(self):
        product_df = pd.read_csv("./product/bestsellers with categories.csv")
        cart_df = pd.read_csv("./my_cart.csv", header=None, names=['Title', 'Price'], usecols=[1,2])
        total_price = 0
        for i in range(len(cart_df)):
            total_price += cart_df['Price'][i]
        print('{}님, 총 {}원이 구매가 완료되었습니다.'.format(self.id, total_price))
    def choice_purchase(self):
        cart_df = pd.read_csv("./my_cart.csv", header=None, names=['Title', 'Price'], usecols=[1,2])
        total_price = 0
        #cart_choice = [int(x) for x in input().split()] #사용자 선택 번호 list화
        print("구매를 원하시는 책 번호를 입력해주세요.(형식 : 0 1 4 5)")
        choice_cart = [int(x) for x in input().split()]
        for i in range(len(choice_cart)):
            print(cart_df['Title'][choice_cart[i]])
            total_price += cart_df['Price'][choice_cart[i]]
        print('{}님, 선택하신 책의 총 {}원 구매가 완료되었습니다.'.format(self.id, total_price))


class Commerce6_product :
  def __init__(self, ACCOUNT_INFO) :
      self.id = ACCOUNT_INFO['id'].to_list()[0]
      self.pw = ACCOUNT_INFO['pw'].to_list()[0]
  with open("./my_cart.csv", "r+") as file:
    file.truncate(0)

  def secure():
    code =  string.ascii_letters  # string.ascii_lowercase, string.ascii_uppercase

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

  def send_mail(name, email) : 

    s = smtplib.SMTP('smtp.gmail.com', 587)
    s.starttls()

    s.login(email, 'rtersvtvnhshrmyg')

    msg = MIMEBase('multipart', 'mixed') #객체 생성 / maintype(내용 포맷)과 subtype(내용 형식)

    # MIME은 메시지 말고 다른 이진 파일들을 보내려면 인코딩 하여 텍스트로 바꾸어 전달하고 다시 이진 파일로 디코딩
    path = './reciept.png' #보낼 이미지의 경로
    part = MIMEBase("application", "octet-stream")
    part.set_payload(open(path, 'rb').read())  # 'rb' : byte 타입으로 변환
    encoders.encode_base64(part)
    part.add_header('Content-Disposition', 'attachment; filename="%s"'% os.path.basename(path))

    msg.attach(part)

    msg['Subject'] = '{}님 파이썬에서 결제하신 영수증입니다.'.format(name)

    s.sendmail(email, email, msg.as_string()) # 보내는 이메일 / 받는 이메일
    s.quit()

  def product_infomation_resule(self) :

    global product_df
    global login_df
    global choice_product_booknumber

    login_df = pd.read_csv("./login/Commerce6_login.csv")
    product_df = pd.read_csv("./product/bestsellers with categories.csv")
    
    while True :
      product_df = pd.read_csv("./product/bestsellers with categories.csv")
      product_choice_options = int(input("평점높은순(1) / 리뷰많은순(2) / 낮은가격순(3) / 높은가격순(4) / 최신출시순(5) / 장르별(6) / 장바구니 확인(7): "))
      s = Commerece6_purchase # modified

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
        s.cart_look()
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
        if Commerce6_product.secure() :
          choice_list = pd.Series([login_df.loc[(login_df['id'] == self.id) & (login_df['pw'] == self.pw)]['nickname'].values[0], product_df.loc[choice_product_booknumber-1][0],int(product_df.loc[choice_product_booknumber-1][4]*1000)], index = ['nickname','choice_book','price'])
          # cart_df = cart_df.append(choice_list, ignore_index = True)
          print("결제처리 진행 중")
          break

      elif choice_product_bookorder == 2 :
        print("다른 서적을 확인 중")
        pass

      elif choice_product_bookorder == 3:
        data_list = (self.id, product_df.loc[choice_product_booknumber-1][0], (product_df.loc[choice_product_booknumber-1][4])*1000) #제목, 가격 data
        with open("./my_cart.csv", "a") as file:
          writer = csv.writer(file)
          writer.writerow(data_list)
        print("{}님이 선택하신 책 {}({})가 장바구니에 담겼습니다.\n".format(self.id, product_df.loc[choice_product_booknumber-1][0], product_df.loc[choice_product_booknumber-1][1]))
      if break_number2 == 1 :
        break

    return 'product_choose_success'

  def product_receipt(self):

    cart_df = pd.read_csv("./my_cart.csv", header=None, names=['Title', 'Price'], usecols=[1,2])
    now = dt.datetime.now()
    
    if input("영수증을 발급하시겠습니다? Y / N : ") == 'Y' :
      print("-------------------------------")
      print("영수증")
      print("주문 목록 : {} 등 {}개".format(cart_df['Title'][0],len(cart_df)))
      # if cart_df['Price'].sum() <= 100000 :
      #   print("금액 : {}원".format(cart_df['Price'].sum()+3000))
      # else:
      print("금액 : {}원".format(cart_df['Price'].sum()))
      print("상기 금액을 {}년 {}월 {}일 수령하고 위 금액의 수령을 증표로서 본 영수증을 발행합니다.".format(now.year, now.month, now.day))
      print("주소 : {}".format(login_df.loc[(login_df['id'] == self.id) & (login_df['pw'] == self.pw)]['location'].values[0]))
      print("성명 : {}".format(login_df.loc[(login_df['id'] == self.id) & (login_df['pw'] == self.pw)]['id'].values[0]))
      print("-------------------------------")
      time.sleep(0.1)
      pyautogui.screenshot('./reciept.png', region=(83, 833, 780, 135) )
      # Commerce6_product.send_mail("전웅", "wjsdnd03@gmail.com")
    else:
      pass
    
    cart_df = pd.read_csv("./my_cart.csv", header=None, names=['Title', 'Price'], usecols=[1,2])

    request = input("배송 시 요청사항이 있으신가요? ")
    print("배송을 시작합니다. \n\n 배송정보\n")
    print("{}님이 구매 신청하신 서적 {}이 {}로 3일내로 도착 예정입니다.".format(login_df.loc[(login_df['id'] == self.id) & (login_df['pw'] == self.pw)]['nickname'].values[0],cart_df['Title'][0],login_df.loc[(login_df['id'] == self.id) & (login_df['pw'] == self.pw)]['location'].values[0]))
    if request != None:
      print("요청사항 : {}".format(request))
    print("구매해 주셔서 감사합니다!")
    print("-------------------------------")
  
        
# from purchase import Commerce6_purchase
# a = Commerce6_product("나호용", 3456)
# s = Commerece6_purchase("나호용", 3456)
# a.product_infomation_resule()

# a.product_receipt()

# # def product_basket(product):

