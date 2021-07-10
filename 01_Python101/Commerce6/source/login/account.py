# import module
import pandas as pd
import numpy as np


class Account:
    def __init__(self, *login_df):
        self.login = True
        self.id = str(login_df[1]["id"])
        self.pw = str(login_df[1]["pw"])
        self.nickname = login_df[1]["nickname"]
        self.location = login_df[1]["location"]

    def __repr__(self):  # 왜 출력이 안되는지 모르겠다 print(object 하면 나와야하는데)
        if self.authority():
            return f"""
            현재 로그인 중인 사용자는 {self.nickname}입니다.
            -----------------------------------------------
            ID : {id}
            PW : {'*' * len(self.pw)//4*3 + self.pw[len(self.pw)//4:]}
            nickname : {self.nickname}
            location : {self.location}
            -----------------------------------------------
            즐거운 쇼핑 하세요!
            """
        else:
            return "로그인 상태가 아닙니다."

    def authority(self):
        return self.login

    def info(self, id):  # return : series
        login_df = pd.read_csv("../../login/Commerce6_login.csv", encoding="UTF-8")
        info = login_df.loc[
            login_df["id"] == id
        ]  # 열을 돌면서 True, False를 반환 (Name : id, dtype : bool)
        return info


"""
# at main.py
# input user info -> for문으로
id = input()
pw = input()
nickname = input()
location = input()

USER = Account()
"""
