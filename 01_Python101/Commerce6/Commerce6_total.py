# To add a new cell, type '# %%'
# To add a new markdown cell, type '# %% [markdown]'
# %% [markdown]
# ## README
#
#
# %% [markdown]
# ---
# %% [markdown]
# ## Import Modules

# %%
import numpy as np
import pandas as pd
import re  # 정규표현식 라이브러리

# Customed module
from blank import Commerce6_product, Commerece6_purchase

# %% [markdown]
# ## DB Load, DB Upload
#
# - encoding format : `euc-kr`
# - DB : 상대경로 사용해서 load, upload
# - PATH : 상대경로, 계정정보 저장

# %%
PATH = "./login/Commerce6_login.csv"
QUALIFIED_START, QUALIFIED_END = "id", "location"  # csv로 저장할 열 범위 지정


def load_df(PATH):
    df = pd.read_csv(PATH, encoding="euc-kr")
    return df  # 해당 반환값을 변수에 지정하여 활용할 것


def upload(df):  # parameter : type(df) == dataframe
    df = df.loc[:, QUALIFIED_START:QUALIFIED_END]
    df.to_csv(
        PATH, encoding="euc-kr", index=False
    )  # index = False로 지정해야 데이터만 csv에 입력할 수 있음.
    return df  # return : 업로드한 csv를 df로 변환한 값


# %% [markdown]
# ## User Information

# %%
class Account:  # 현재 로그인한 계정의 정보
    def info(self, id):  # return : series
        df = load_df(PATH)
        info = df.loc[
            df["id"] == id
        ]  # 열을 돌면서 True, False를 반환 (Name : id, dtype : bool)
        return info.loc[
            :, QUALIFIED_START:QUALIFIED_END
        ]  # 해당 값 받아서 account_instance['원하는 값, ex) "nickname"' 등 입력]


# %% [markdown]
# ## Sign Up

# %%
class Join:
    def join_check(self):
        # ID 중복 검사 추가, 비밀번호 유효성 추가
        df = load_df(PATH)

        join_info = ["id", "pw", "nickname", "location"]  # return_info의 key값이 될 정보들
        return_info = {}

        # ID 중복 검사 후 가입
        while True:
            input_id = input("{}를 입력해주세요 : ".format(join_info[0]))
            if (len(df.loc[(df["id"] == input_id)])) == 0:
                return_info[join_info[0]] = input_id  # key값에 해당하는 사용자 입력값 저장
                break
            else:
                print("중복된 아이디가 있습니다. 다시 입력해주세요.")

        # 비밀번호 입력
        while True:
            input_pw = input("{}를 입력해주세요 : ".format(join_info[1]))
            if (
                len(input_pw) > 8
                and re.search("[A-Z]", input_pw)
                and re.search("[0-9]+", input_pw)
                and re.search("[~!@#$%^&*(),<.>/?]+", input_pw)
            ):
                print("사용가능한 비밀번호입니다.")
                break
            else:
                print("비밀번호는 최소 8자 이상, 영문 대문자, 숫자, 특수문자가 포함되어야 합니다.")

        # 입력 비밀번호 확인
        while True:
            confirm_pw = input("입력한 {}를 다시 입력해주세요 : ".format(join_info[1]))
            if confirm_pw == input_pw:
                return_info[join_info[1]] = confirm_pw
                print("입력한 비밀번호와 동일한 것으로 확인되었습니다.")
                break
            else:
                print("입력한 비밀번호와 다릅니다. 다시 입력해주세요.")

        # nickName 중복 검사 후 가입
        while True:
            input_nick = input("{}를 입력해주세요 : ".format(join_info[2]))
            if (len(df.loc[(df["nickname"] == input_nick)])) == 0:
                return_info[join_info[2]] = input_nick
                break
            else:
                print("중복된 닉네임이 있습니다. 다시 입력해주세요.")

        # 주소 입력
        input_addr = input("{}를 입력해주세요 : ".format(join_info[3]))
        return_info[join_info[3]] = input_addr

        # DB에 반영
        df = df.append(
            return_info, ignore_index=True
        )  # dictionary를 df로 변환하려면 ignore_index 속성을 설정해야 함
        upload(df)  # 가입한 정보 csv에 반영

        return "회원가입 완료"


# %% [markdown]
# ## Sign In

# %%
class Login:
    def login_check(self, id, pw):  # 생성자 없이 함수에서 바로 받음
        df = load_df(PATH)

        # try - except : try를 실행해보고 에러가 발생하면 except를 실행
        try:  # 없는 계정정보를 입력하면 에러가 발생하므로 except문에서 예외처리
            df_to_dict = (
                df.loc[df["id"] == id].iloc[0].to_dict()
            )  # id열에서 입력값 id와 같은 값을 찾아 dictionary로 변환
            if str(df_to_dict["pw"]) == pw:  # 비밀번호 일치할 경우 로그인 성공
                print("로그인 성공")
                return True
            else:
                print("로그인 실패. 비밀번호가 틀렸습니다.")  # 비밀번호 오류
                return False
        except:
            print("로그인 실패")
            return False


# %% [markdown]
# ## Delete Account
#
# 회원 탈퇴

# %%
class Delete_account:  # 회원탈퇴, 로그인 한 상황에서만 노출
    def __init__(self, id, pw):
        self.id = id
        self.pw = pw

    def double_check(self):  # 보안을 위해 계정정보 (id, pw) 재확인.
        print("확인을 위해 ID 와 PW를 다시 한 번 입력하세요.")
        while True:
            input_id = input("Enter Your [ID] : ")
            if self.id != input_id:  # [ID check] 올바른 아이디가 아닌가?
                print(f"{input_id}은/는 잘못된 ID 입니다.")
            else:  # [ID check] 아이디가 올바른 경우 비밀번호 확인
                while True:
                    input_pw = input("Enter Your [pw] : ")
                    if str(self.pw) != input_pw:  # [pw check] 비밀번호가 잘못된 경우
                        print(f"{input_pw}은/는 잘못된 PW입니다.")

                        #  틀릴 때 마다 과정 종료하기 위해 질문
                        print("계속하려면 1을, 취소하려면 0을 입력하세요.")
                        if int(input("입력 : ")) == 1:
                            return False
                    else:  # [pw check] 비밀번호가 옳은 경우 True 반환
                        return True

    def delete(self):
        print("회원 탈퇴 절차를 진행합니다.")
        df = load_df(PATH)
        cmd = input("정말로 탈퇴하겠습니까? 탈퇴하시려면 y를, 탈퇴하지 않으려면 n을 입력하세요. : ")
        if cmd == "y":  # 탈퇴 절차
            deleted_user = (
                df.loc[df["id"] == self.id].iloc[0].to_dict()
            )  # 삭제할 고객 정보 : 알림 메시지 출력하기 위해 임시로 저장
            deleted_user_index = df[df["id"] == self.id].index  # 삭제할 고객 정보의 index
            df.drop(
                index=deleted_user_index, inplace=True
            )  # 삭제할 고객 정보의 index로 df에서 고객 정보 삭제
            print(
                f"{deleted_user['id']}({deleted_user['nickname']})님의 정보가 안전하게 삭제되었습니다."
            )  # 알림
            upload(df)  # 바뀐 데이터프레임 csv에 반영
            return True
        elif cmd == "n":  # 탈퇴절차 종료
            print("탈퇴처리를 종료합니다. 고객정보는 유지됩니다.")
            return False


# %% [markdown]
# ## Test Code

# %%
# instance
account_instance = Account
join_instance = Join
login_instance = Login
delete_instance = Delete_account


def main():
    """LOGIN & DB"""
    # 회원여부 확인 -> 로그인
    while True:
        # 회원 전용 기능
        account_check_cmd = input("OOO 쇼핑몰에 오신 것을 환영합니다.\n회원이면 1 비회원이면 2 를 입력하세요 : ")
        if account_check_cmd == "1":  # 회원이므로 로그인 기능으로 이동
            user_id = input("로그인을 위해 ID를 입력하세요 : ")
            user_pw = input("로그인을 위해 비밀번호를 입력하세요 : ")
            login_status = login_instance.login_check(
                login_instance, user_id, user_pw
            )  # 로그인 확인 : 이후에 로그인 했는지 확인하기 위해 분리
            if login_status:  # 로그인한 고객일 경우 메뉴 출력
                # 환영문구
                print(f"환영합니다. {str(info_dict['nickname'])}님.")
                # 현재 로그인 한 사람의 정보 : 구매 프로세스로 넘길 정보
                info_dict = (
                    account_instance.info(account_instance, user_id).iloc[0].to_dict()
                )
                ACCOUNT_INFO = account_instance.info(
                    account_instance, user_id
                )  # update user info

                user_menu_cmd = input(
                    "원하시는 메뉴의 번호를 입력해주세요.\n\t1. 쇼핑\n\t2. 커뮤니티\n\t3. 회원탈퇴"
                )
                while user_menu_cmd in ["1", "2", "3"]:  # 반복문 돌릴때마다 올바른 입력인지 확인
                    if user_menu_cmd == "1":
                        # PURCHASE & BILL
                        print("----------------------------------------------------")
                        print("쇼핑을 시작합니다.")
                        print("----------------------------------------------------")
                        # instance
                        a = Commerce6_product(ACCOUNT_INFO)
                        s = Commerece6_purchase(ACCOUNT_INFO)
                        a.product_infomation_resule()
                        break  # 쇼핑기능으로 이동
                    elif user_menu_cmd == "2":
                        print("----------------------------------------------------")
                        print("커뮤니티로 이동합니다.")
                        print("----------------------------------------------------")
                        return  # 커뮤니티 기능으로 이동 -> 연결 필요
                    elif user_menu_cmd == "3":
                        if delete_instance(user_id, user_pw).double_check():
                            delete_instance(user_id, user_pw).delete()
                            return  # 회원탈퇴시 종료
                    else:
                        print("잘못된 입력입니다.")
            else:  # 잘못된 계정정보일 때
                cmd = input("잘못된 계정 정보입니다. 다시 시도하려면 1, 종료하려면 2를 입력하세요 : ")  # command
                if cmd == "1":
                    continue
                elif cmd == "2":
                    break
                else:
                    cmd = input("잘못된 입력입니다. 다시 시도하려면 1, 종료하려면 2를 입력하세요 : ")

        # 비회원 -> 회원가입 유도
        elif account_check_cmd == "2":  # 비회원이므로 회원가입 기능으로 이동
            join_instance.join_check(join_instance)
            break
        else:
            print("잘못된 입력입니다. 다시 입력하세요")
            continue


# %%
main()

# %% [markdown]
#
