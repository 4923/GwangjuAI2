# 로그인 / 회원 DB 처리  #홍예은 #최인남 
# 상품보기 / 상품결제   #전선유 #김세연 #전웅

import pandas as pd
import re   # 정규표현식 라이브러리

# Customed module
from blank_copy_1 import Commerce6_product
from Commerce6_board import board_db

PATH = "C:/Users/wjsdn/Desktop/woong/Commerce6_login.csv"
QUALIFIED_START, QUALIFIED_END = 'id', 'location'   # 빈 열 csv에 저장하지 않도록 임시로 슬라이싱

def load_df(PATH):
    df = pd.read_csv(PATH, encoding = 'euc-kr')
    
    return df       # 해당 반환값을 변수에 지정하여 활용할 것 

def upload(df):     # parameter : type(df) == dataframe 
    df = df.loc[:, QUALIFIED_START:QUALIFIED_END]
    # print('-----------df------------')
    # print(df)
    # print("--------------------------")
    df.to_csv(PATH, encoding = 'euc-kr', index = False)
    # print(df)
    # print("--------------------------")
    return df    # return : 업로드한 csv를 df로 변환한 값

df = load_df(PATH)
df

class Account:
    def info(self, id):      # return : series
      df = load_df(PATH)
      info = df.loc[df['id'] == id]     # 열을 돌면서 True, False를 반환 (Name : id, dtype : bool)
      return info.loc[:, QUALIFIED_START:QUALIFIED_END]   # 해당 값 받아서 account_instance['원하는 값, ex) "nickname"' 등 입력]

class Join :
    def join_check(self) :
        # ID 중복 검사 추가, 비밀번호 유효성 추가
        df = load_df(PATH)

        join_info = ['id','pw', 'nickname', 'location'] # password -> pw
        return_info = {}    # [] -> {}

        # ID 중복 검사 후 가입
        while True :
            input_id = input('{}를 입력해주세요 : '.format(join_info[0]))
            if (len(df.loc[(df['id'] == input_id)])) == 0 :
                return_info[join_info[0]] = input_id    # modified
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
                return_info[join_info[1]] = confirm_pw    # modified
                print('입력한 비밀번호와 동일한 것으로 확인되었습니다.')
                break
            else:
                print('입력한 비밀번호와 다릅니다. 다시 입력해주세요.')        

        # nickName 중복 검사 후 가입
        while True :
            input_nick = input('{}를 입력해주세요 : '.format(join_info[2]))
            if (len(df.loc[(df['nickname'] == input_nick)])) == 0 :
                return_info[join_info[2]] = input_nick    # modified
                break
            else :
                print("중복된 닉네임이 있습니다. 다시 입력해주세요.")
        
        input_addr = input('{}를 입력해주세요 : '.format(join_info[3]))
        return_info[join_info[3]] = input_addr    # modified
        
        df = df.append(return_info, ignore_index = True)
        upload(df)

        return main()

class Login :
    # def __init__(self, id, pw) :
    #     self.id = id
    #     self.pw = pw

    def login_check(self, id, pw):
        df = load_df(PATH)
        print('-----------------')
        try:
            df_to_dict = df.loc[df['id'] == id].iloc[0].to_dict()
            if str(df_to_dict['pw']) == pw:
                print("로그인 성공")
                return True 
        except:
            print("로그인 실패")
            return False



class Delete_account:  # 회원탈퇴, 로그인 한 상황에서만 노출
  def __init__(self, id, pw):
    self.id = id 
    self.pw = pw

  def double_check(self):
    print("확인을 위해 ID 와 PW를 다시 한 번 입력하세요.")
    while True:
      input_id = input("Enter Your [ID] : ")
      if self.id != input_id:
        print(f"{input_id}은/는 잘못된 ID 입니다.")
        status = True
      else: 
        while True:
          input_pw = input("Enter Your [pw] : ")
          if str(self.pw) != input_pw:
            print(f"{input_pw}은/는 잘못된 PW입니다.")

            print("계속하려면 1을, 취소하려면 0을 입력하세요.")
            if int(input("입력 : ")) == 1: return False
          else: 
            return True

  def delete(self):
    print("회원 탈퇴 절차를 진행합니다.")
    df = load_df(PATH)
    cmd = input("정말로 탈퇴하겠습니까? 탈퇴하시려면 y를, 탈퇴하지 않으려면 n을 입력하세요. : ")
    if cmd == 'y': 
      deleted_user = df.loc[df['id'] == self.id].iloc[0].to_dict()
      deleted_user_index = df[ df['id'] == self.id ].index
      df.drop(index = deleted_user_index, inplace=True)
      print(f"{deleted_user['id']}({deleted_user['nickname']})님의 정보가 안전하게 삭제되었습니다.")
      upload(df)
      return True
    elif cmd == 'n':
      print("탈퇴처리를 종료합니다. 고객정보는 유지됩니다.")
      return False



account_instance = Account
join_instance = Join
login_instance = Login
delete_instance = Delete_account

def main():
    '''LOGIN & DB'''
    # 회원여부 확인 -> 로그인
    while True:
        # 회원 전용 기능
        account_check_cmd = input("OOO 쇼핑몰에 오신 것을 환영합니다.\n회원이면 1 비회원이면 2 를 입력하세요 : ")
        if account_check_cmd == '1': # 회원이므로 로그인 기능으로 이동
            user_id = input("로그인을 위해 ID를 입력하세요 : ")
            user_pw = input("로그인을 위해 비밀번호를 입력하세요 : ")
            login_status = login_instance.login_check(login_instance, user_id, user_pw)
            if login_status: 
                info_dict = account_instance.info(account_instance, user_id).iloc[0].to_dict()
                print(f"환영합니다. {str(info_dict['nickname'])}님.")
                ACCOUNT_INFO = account_instance.info(account_instance, user_id)     # update user info

                user_menu_cmd = input("원하시는 메뉴의 번호를 입력해주세요.\n\t1. 쇼핑\n\t2. 커뮤니티\n\t3. 회원탈퇴\n\t")
                while user_menu_cmd:
                    if user_menu_cmd == '1':
                        # PURCHASE & BILL
                        print("----------------------------------------------------")
                        print("쇼핑을 시작합니다.")
                        print("----------------------------------------------------")
                        a = Commerce6_product(ACCOUNT_INFO)
                        # s = Commerece6_purchase(ACCOUNT_INFO)
                        a.product_infomation_resule()
                        a.product_receipt()
                        return  # 임시로 종료
                        break    # 쇼핑기능으로 이동
                    elif user_menu_cmd == '2':
                        print("----------------------------------------------------")
                        print("커뮤니티로 이동합니다.")
                        print("----------------------------------------------------")
                        b = board_db(ACCOUNT_INFO)
                        b.start()
                        return   # 임시로 종료
                        break    # 커뮤니티 기능으로 이동
                    elif user_menu_cmd == '3':
                        if delete_instance(user_id, user_pw).double_check(): 
                            delete_instance(user_id, user_pw).delete()
                            return   # 임시로 종료
                            break
                    else:
                        print("잘못된 입력입니다.")
            else:
                cmd = input("잘못된 계정 정보입니다. 다시 시도하려면 1, 종료하려면 2를 입력하세요 : ")
                if cmd == '1': continue
                elif cmd == '2': break 
                else: cmd = input("잘못된 입력입니다. 다시 시도하려면 1, 종료하려면 2를 입력하세요 : ")

        # 비회원 -> 회원가입 유도
        elif account_check_cmd == '2': # 비회원이므로 회원가입 기능으로 이동
            join_instance.join_check(join_instance)
            break
        else: 
            print("잘못된 입력입니다. 다시 입력하세요")
            continue


# load_df(PATH)

main()

# load_df(PATH)

