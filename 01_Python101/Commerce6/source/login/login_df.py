# import module
import pandas as pd

# [Issue] encoding: google drive의 csv 파일 그대로 받으면 어떤 encoding 방법으로도 제대로 된 한글이 출력되지 않아 google spread sheet에서 csv파일 추출 후 utf-8 변환
def login_df():
    return pd.read_csv("../../login/Commerce6_login.csv", encoding="UTF-8")
