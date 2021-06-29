import numpy as np
import pandas as pd

class login :

    def __init__(self, id, pw) :
        self.id = id
        self.pw = pw

    def login_check(self):
        df = pd.read_csv('C:/Users/user/Desktop/new/Commerce/login/Commerce6_login.csv', encoding='euc-kr')
        #login_check
        
        if len(df.loc[(df['id'] == self.id) & (df['pw'] == self.pw)]) == 1 :
            return "로그인 성공"
        else :
            print(self.id)
            return "로그인 실패"

      

        
    