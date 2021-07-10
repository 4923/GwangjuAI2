# import module
import pandas as pd
import numpy as np
import string  # for create randomKey

# import customed modules
# import login_df
import Welcome

# 계정 확인 : 로그인
# 로그인 실패시 : 비밀번호 찾기, 회원가입, 보안문자 출력
class AccountCheck:
    def __init__(self):
        # login_df = login_df
        self.welcome = Welcome()
        pass

    def signin(self):
        login_df = pd.read_csv("../../login/Commerce6_login.csv", encoding="UTF-8")
        print(login_df, type(login_df))
        print("ID와 비밀번호를 입력하세요.")
        id = input("ID : ")
        pw = input("PW : ")

        # 정상 로그인
        if login_df.loc[login_df["id"] == self.id]["pw"].values[0] == self.pw:
            # self.welcome.authority(True)    # 이후에도 login 여부 확인하기 위해 변경
            print(f"환영합니다. {self.welcome.accountInfo(id)['nickname']}님")
        else:
            # 재로그인
            for remainCount in range(3, 0, -1):
                print(f"잘못된 정보입니다. (남은 로그인 가능 횟수 : {remainCount}회)")
                self.signin()
            # 로그인 시도 횟수 초과
            print(
                """로그인 시도 횟수를 초과했습니다.
            비밀번호를 찾으려면 password, 회원가입을 하려면 signup, 다시 로그인을 시도하려면 try를 입력하세요."""
            )
            cmd = input(": ").strip()
            while True:
                if cmd == "password":  # password : 비밀번호 찾기
                    self.findPW(id, pw)
                    break
                elif cmd == "signup":  # signup : 회원가입
                    self.signup()
                    break
                elif cmd == "try":  # try : 보안문자 입력
                    if self.security():
                        print("올바른 입력입니다. 다시 로그인하세요.")
                        self.signin()  # 처음부터 다시 로그인
                else:
                    print("잘못된 입력입니다. 올바른 명령어를 입력해주세요")

    def findID(self):
        login_df = pd.read_csv("../../login/Commerce6_login.csv", encoding="UTF-8")
        print("닉네임과 주소를 입력하세요.")
        # 입력
        while True:
            nickname = input("닉네임 : ")
            if not login_df.loc[login_df["nickname"] == nickname]:
                print("잘못된 닉네임입니다. 다시 입력하세요.")
                print("과정을 중단하려면 0을 입력하세요")
            elif nickname == "0":
                return self.welcome
            else:
                break
        while True:
            location = input("주소 : ")
            if not login_df.loc[
                login_df["nickname"] == nickname and login_df["location"] == location
            ]:
                print("잘못된 주소입니다. 다시 입력하세요.")
                print("과정을 중단하려면 0을 입력하세요")
            elif nickname == "0":
                return self.welcome
            else:
                break
        # 찾기
        your_ID = login_df.loc[login_df["nickname"] == nickname]
        print(your_ID)

    def findPW(self, id):
        login_df = pd.read_csv("../../login/Commerce6_login.csv", encoding="UTF-8")
        pass

    def signup(self):
        login_df = pd.read_csv("../../login/Commerce6_login.csv", encoding="UTF-8")
        pass

    def security(self, length):  # type(length) : int
        # randomPool ref : https://bskyvision.com/1020
        # [Issue] to aviod 'ValueError: a must be 1-dimensional or an integer' -> transform randomPool LIST
        randomPool = list(
            string.ascii_letters + string.digits + string.punctuation
        )  # 영어 대소문자, 숫자, 특수문자
        randomKey = "".join(
            np.random.choice(randomPool, length)
        )  # to compare with answer -> transform randomKey STR
        # Check
        print(f"보안을 위해 다음 단어를 정확히 입력해주세요.\n{randomKey}")  # guide message
        answer = input(": ").strip()
        print(randomKey, answer)
        if answer == randomKey:
            return True
        else:
            return False


A = AccountCheck()
A.signin()
