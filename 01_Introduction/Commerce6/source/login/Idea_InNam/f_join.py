import numpy as np
import pandas as pd
# 정규표현식 라이브러리
import re

class join :
    def __init__(self, id, pw) :
        self.id = id
        self.pw = pw

    def join_check(self) :
        # ID 중복 검사 추가, 비밀번호 유효성 추가
        df = pd.read_csv('C:/Users/user/Desktop/new/Commerce/login/Commerce6_login.csv', encoding='euc-kr')

        join_info = ['ID','Password', 'Nickname', 'Location']
        return_info = []

        # ID 중복 검사 후 가입
        while True :
            input_id = input('{}를 입력해주세요 : '.format(join_info[0]))
            if (len(df.loc[(df['id'] == input_id)])) == 0 :
                return_info.append(input_id)
                break
            else :
                print("중복된 아이디가 있습니다. 다시 입력해주세요.")

        # 비밀번호 입력
        while True :
            input_pw = input('{}를 입력해주세요 : '.format(join_info[1]))
            if len(input_pw) > 8 and re.search('[A-Z]',input_pw) and re.search('[0-9]+',input_pw) and re.search('[~!@#$%^&*(),<.>/?]+',input_pw):
                print('사용가능한 비밀번호입니다.')
                break
            else:
                print('비밀번호는 최소 8자 이상, 영문 대문자, 숫자, 특수문자가 포함되어야 합니다.')
        
        # 입력 비밀번호 확인
        while True :
            confirm_pw = input('입력한 {}를 다시 입력해주세요 : '.format(join_info[1]))
            if confirm_pw == input_pw :
                return_info.append(confirm_pw)
                print('입력한 비밀번호와 동일한 것으로 확인되었습니다.')
                break
            else:
                print('입력한 비밀번호와 다릅니다. 다시 입력해주세요.')        

        # nickName 중복 검사 후 가입
        while True :
            input_nick = input('{}를 입력해주세요 : '.format(join_info[2]))
            if (len(df.loc[(df['nickname'] == input_nick)])) == 0 :
                return_info.append(input_nick)
                break
            else :
                print("중복된 닉네임이 있습니다. 다시 입력해주세요.")
        
        input_addr = input('{}를 입력해주세요 : '.format(join_info[3]))
        return_info.append(input_addr)

        return_info = pd.DataFrame(np.array(return_info).reshape(1, -1), columns=join_info)
        
        df = df.append(return_info)
        df.to_csv('C:/Users/user/Desktop/new/Commerce/login/Commerce6_login.csv', index=False, encoding='euc-kr')

        return "회원가입 완료"