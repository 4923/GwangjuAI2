# import module
import pandas as pd 
import numpy as np

# import customed modules
import Welcome, AccountCheck

def main():
    print("--------------------------------------")
    print("\tModule Check\t")
    print("--------------------------------------")

    # Welcome
    C = Welcome()   # Welcome.isCustomer : 회원여부 확인
    C.suthority(status = True)      # 로그인여부 확인
    C.accountInfo(id)       # id에 해당하는 열을 반환

    # AccountCheck
    A = AccountCheck()  # init : X
    A.signin()      # 로그인 (정상로그인, 재로그인, 로그인시도 횟수)
    A.findID()      # ID 찾기
    A.findPW()      # PW 찾기
    A.signup()      # 회원가입
    print("보안문자 확인 : return boolean")
    print(A.security())    # 유사 reCaptcha -> 재로그인