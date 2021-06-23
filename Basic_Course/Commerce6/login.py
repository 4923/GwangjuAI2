# modulel import
import pandas as pd 
import numpy as np
import string   # for create randomKey


global login_df
# [Issue] encoding: google drive의 csv 파일 그대로 받으면 어떤 encoding 방법으로도 제대로 된 한글이 출력되지 않아 google spread sheet에서 csv파일 추출 후 utf-8 변환
login_df = pd.read_csv("./login/Commerce6_login.csv", encoding="UTF-8")     

class Welcome():    # 시작 1회만 실행되는 class
    def __init__(self):
        if self.authority():     # 로그인 한 경우
            print(f"환영합니다 `nickname`님")     # nickname : 임시변수
        else: self.isCustomer()    # 로그인 하도록 유도

    # 회원여부 확인
    def isCustomer(self):
        cmd = int(input("OOO 쇼핑몰에 오신 것을 환영합니다.\n회원이면 1 비회원이면 2 를 입력하세요 : "))
        if cmd == 1: return True 
        elif cmd == 2: return False
        else: 
            "잘못된 입력입니다. 다시 입력하세요"
            return self.isCustomer()

    # 로그인 여부
    def authority(self, status = False):    # boolean
        # 로그인 상태이면 True 반환
        return status 
        # 비로그인 상태이면 로그인 하도록 유도
    
    # 다른 Class로 전달하기 위한 계정 정보
    def accountInfo(self, id):  # if = str
        info = login_df.loc[login_df['id'] == id]     # 열을 돌면서 True, False를 반환 (Name : id, dtype : bool)
        return info
