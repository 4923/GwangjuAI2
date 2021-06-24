# import module
import pandas as pd 
import numpy as np

# import customed modules
from account import Account


def main():
    print("--------------------------------------")
    print("\tModule Check\t")
    print("--------------------------------------")

    # user input
    columns = ['id', 'pw', 'nickname', 'location']    
    
    login_dict = {}   # dict로 받아서 df로 변환하는
    for column in columns:
        login_dict[column] = input(f"{column} : ")
    login_df = pd.DataFrame([login_dict])
    print(login_df)
    print()

    USER = Account(id, login_df)
    print(USER.pw)
    print(len(USER.pw))
    # print(USER)

main()