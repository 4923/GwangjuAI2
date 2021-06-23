# import module
import pandas as pd 
import numpy as np
import string   # for create randomKey

# import customed modules
import Welcome, login_df 

# 계정 확인 : 로그인
# 로그인 실패시 : 비밀번호 찾기, 회원가입, 보안문자 출력
class AccountCheck(Welcome):
    def signin(self):
        print("ID와 비밀번호를 입력하세요.")
        id = input("ID : ")
        pw = input("PW : ")
        
        # 정상 로그인
        if login_df.loc[login_df['id'] == id and login_df['pw'] == pw]: 
            Welcome.authority(True)
            print(f"환영합니다. {Welcome.accountInfo(id).loc['nickname']}님")
        else:
            # 재로그인
            for remainCount in range(3, 0, -1):
                print(f"잘못된 정보입니다. (남은 로그인 가능 횟수 : {remainCount}회)")
                self.signin()
            # 로그인 시도 횟수 초과
            print("""로그인 시도 횟수를 초과했습니다.
            비밀번호를 찾으려면 password, 회원가입을 하려면 signup, 다시 로그인을 시도하려면 try를 입력하세요.""")
            cmd = input(": ").strip()
            while True: 
                if cmd == "password":                   # password : 비밀번호 찾기
                    self.findPW(id, pw)
                    break 
                elif cmd == "signup":                   # signup : 회원가입
                    self.signup()
                    break 
                elif cmd == "try":                      # try : 보안문자 입력
                    if self.security():
                        print("올바른 입력입니다. 다시 로그인하세요.")
                        self.signin()                   # 처음부터 다시 로그인
                else: print("잘못된 입력입니다. 올바른 명령어를 입력해주세요")
    def findID(self):
        pass 
    
    def findPW(self, id):
        pass

    def signup(self):
        pass 

    def security(self, length):   # type(length) : int
        # randomPool ref : https://bskyvision.com/1020
        # [Issue] to aviod 'ValueError: a must be 1-dimensional or an integer' -> transform randomPool LIST
        randomPool = list(string.ascii_letters + string.digits + string.punctuation)    # 영어 대소문자, 숫자, 특수문자
        randomKey = ''.join(np.random.choice(randomPool, length))   # to compare with answer -> transform randomKey STR
        # Check
        print(f"보안을 위해 다음 단어를 정확히 입력해주세요.\n{randomKey}") # guide message
        answer = input(': ').strip()
        print(randomKey, answer)
        if answer == randomKey: return True 
        else: return False

