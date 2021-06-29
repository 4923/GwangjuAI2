import numpy as np
import pandas as pd
import csv
import os.path
import datetime

class board_db :
    # def __init__(self, id, pw) :
    #     self.id = id
    #     self.pw = pw
    def __init__(self, ACCOUNT_INFO) :
        self.id = ACCOUNT_INFO['id'].to_list()[0]
        self.pw = ACCOUNT_INFO['pw'].to_list()[0]
        self.nickname = ACCOUNT_INFO['nickname'].to_list()[0]
        self.location = ACCOUNT_INFO['location'].to_list()[0]
        header=['product_name','title','content','writer','date']
        path='C:/Users/wjsdn/Desktop/woong/Commerce6_board.csv'
        if os.path.isfile(path):
            print("게시판 DB 파일을 불러옵니다.")
        else:
            with open('C:/Users/wjsdn/Desktop/woong/Commerce6_board.csv','a') as file:
                csv.writer(file).writerow(header)
                print("게시판 DB 파일 생성 완료")
    def start(self) :
        while True :
            state = int(input("항목을 선택해주세요 [ 리뷰보기(1), 리뷰쓰기(2), 리뷰검색(3), 리뷰수정(4), 종료(5) ] :"))
            if state == 1 :
                board_db.read_board(self)
            elif state == 2 :
                board_db.write_board(self)
            elif state == 3 :
                board_db.search_board(self)
            elif state == 4 :
                board_db.edit_board(self)
            elif state == 5 :
                print("종료됩니다.")
                break
    #게시글 입력
    def write_board(self) :
        # pd.set_option('display.max.colwitdh',200)
        product_df = pd.read_csv("C:/Users/wjsdn/Desktop/woong/bestsellers with categories.csv")
        board_df = pd.read_csv('C:/Users/wjsdn/Desktop/woong/Commerce6_board.csv', encoding='euc-kr')
        print(product_df)
        # print(board_df)
        my_post = []
        board_info = ['product_name','title','content','writer','date']
        #게시하기
        for i in range(len(board_info)):
            if i == 0:
                # 책번호 선택
                data = int(input("리뷰할 책 번호를 선택해주세요 : "))
                my_post.append(product_df.loc[data][0])
            elif i == 3:
                # writer(작성자 본인) 로그인한 정보 기준으로 리스트 추가
                data = self.nickname
                my_post.append(data)
            elif i == 4:
                # date(작성 날짜) 현재시각 기준 리스트 추가
                data = datetime.datetime.today().strftime("%Y-%m-%d")
                print(data)
                my_post.append(data)
            else:
                # title(제목), content(내용) 입력
                data = input("{}을 입력해주세요. : ".format(board_info[i]))
                my_post.append(data)
        my_post = pd.DataFrame(np.array(my_post).reshape(1, -1), columns=board_info)
        board_df = board_df.append(my_post)
        board_df.to_csv('C:/Users/wjsdn/Desktop/woong/Commerce6_board.csv', index=False, encoding='euc-kr')
        ### 수정 삭제 비밀번호 입력하기
    # 게시글 보기
    def read_board (self) :
        board_df = pd.read_csv('C:/Users/wjsdn/Desktop/woong/Commerce6_board.csv', encoding='euc-kr')
        print(board_df)
    # 게시글 검색(책이름 기준)
    def search_board (self) :
        board_df = pd.read_csv('C:/Users/wjsdn/Desktop/woong/Commerce6_board.csv', encoding='euc-kr')
        keyword = input("검색어를 입력해주세요. (책 이름 기준 / 대소문자 구별): ")
        find_post = '' # 검색어가 포함된 책이름을 담을 변수 선언
        #검색어가 포함된 책이름 찾기
        for i in range(len(board_df['product_name'])):
            if keyword in board_df['product_name'][i]:
                find_post = board_df['product_name'][i]
        # 검색어가 포함된 책이름과 동일한 책이름 리뷰글 찾기
        result = board_df.loc[board_df['product_name']==find_post]
        print(result)
    # 게시글 수정
    def edit_board (self) :
        board_df = pd.read_csv('C:/Users/wjsdn/Desktop/woong/Commerce6_board.csv', encoding='euc-kr')
        #내가 쓴 글 목록 보여주기
        my_post = board_df.loc[board_df['writer']==self.nickname]
        print(my_post)
        choice_post = ''
        print(board_df.index() not in 3)
        #본인 게시글에서 선택하기
        while True :
            choice_post = int(input("수정/삭제할 게시글 번호를 선택해주세요 : "))
            if  (self.nickname != board_df.loc[choice_post][3]):
                print("본인 글 외에는 접근할 수 없습니다. 다시 확인해주세요.")
            else :
                print(my_post.loc[choice_post])
                break
        board_df.index[choice_post] not in choice_post
        # choice_post = int(input("수정/삭제할 게시글 번호를 선택해주세요 : "))
        while True :
            state = int(input("항목을 선택해주세요 [ 제목수정(1), 내용수정(2), 글 삭제(3), 종료(4)] : "))
            # 제목 수정
            if state == 1:
                edit_post = input("수정할 내용을 입력해주세요 : ")
                board_df.loc[choice_post][1] = edit_post
                if edit_post == board_df.loc[choice_post][1]:
                    print("제목이 수정되었습니다.")
                else :
                    print("실패하였습니다.")
            # 내용 수정
            elif state == 2:
                edit_post = input("수정할 내용을 입력해주세요 : ")
                board_df.loc[choice_post][2] = edit_post
                if edit_post == board_df.loc[choice_post][2]:
                    print("내용이 수정되었습니다.")
                else :
                    print("실패하였습니다.")      
            # 내용 삭제
            elif state == 3:
                del_post = input("정말로 삭제하시겠습니까? (y/n) : ")
                # board_df.iloc[3]
                # board_df.drop(3)
                if del_post=='y':
                    board_df = board_df.drop(choice_post)
                    board_df = board_df.reset_index(drop=True)
                    print(board_df)
                    print("게시글이 삭제되었습니다.")
                elif del_post=='n':
                    print("다시 메뉴로 돌아갑니다.")
                else :
                    print("y 또는 n 만 입력 가능합니다. 다시 시도해주세요")
            else :
                break
        print(board_df)
        #바뀐 내용 반영된 게시물 DB 업로드
        board_df.to_csv('C:/Users/wjsdn/Desktop/woong/Commerce6_board.csv', index=False, encoding='euc-kr')