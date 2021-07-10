# import customed modules
# import login_df
import AccountCheck
import pandas as pd


class Welcome:  # 시작 1회만 실행되는 class
    def __init__(self):
        # self.login_df = login_df
        self.account = AccountCheck
        pass

    # 로그인 여부
    def authority(self, status=False):  # boolean
        return status
        # 비로그인 상태이면 로그인 하도록 유도

    # 회원여부 확인
    def isCustomer(self):
        login_df = pd.read_csv("../../login/Commerce6_login.csv", encoding="UTF-8")

        cmd = int(input("OOO 쇼핑몰에 오신 것을 환영합니다.\n회원이면 1 비회원이면 2 를 입력하세요 : "))
        if cmd == 1:
            return True
        elif cmd == 2:
            return False
        else:
            "잘못된 입력입니다. 다시 입력하세요"
            return self.isCustomer()

    # 다른 Class로 전달하기 위한 계정 정보
    def accountInfo(self, id):  # if = str
        login_df = pd.read_csv("../../login/Commerce6_login.csv", encoding="UTF-8")

        info = login_df.loc[
            login_df["id"] == id
        ]  # 열을 돌면서 True, False를 반환 (Name : id, dtype : bool)
        print("\t", type(info))
        return info  # series


W = Welcome()
W.accountInfo("문재인")
