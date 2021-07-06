###
# ### 데이터 베이스 & 테이블의 생성과 변경. : UPDATE (cr`U`d)
from ./Project/01_SQL_and_DataBase/scripts/script_03.txt

###

### "scratch.db"에 접속하여 다음을 실행해 본다.

### 테이블은 CREATE로 생성 DROP으로 삭제. 
- CREATE TABLE myTB ( a INT, b TEXT );                       ### 새롭게 테이블 생성 (및 추가).
- SELECT * FROM sqlite_master WHERE TYPE = "table";    ### 테이블 목록 (SQLite).
- INSERT INTO myTB VALUES ( 1, 'foo' );
- SELECT * FROM myTB;
- DROP TABLE myTB;                                                ### 테이블 삭제.

- SELECT * FROM customer;						### "customer"  테이블 출력.
- CREATE TABLE customer2 AS SELECT id, name, zip from customer;		### "customer" 바탕으로 "customer2" 생성.
- SELECT * FROM customer2;						### "customer2"  테이블 출력.
- DROP TABLE customer2;                                             		### 테이블 삭제.

### 테이블 생성시 컬럼의 자료형을 명시할 수 있다. CHAR, VARCHAR = TEXT형.
-  CHAR(n) = 길이 고정적.
-  VARCHAR(n) = 최대 길이가 n까지.
- 차이?
	- 호환성 유지를 위해 다양한 '자료형'을 지원하나 실제 처리되는 자료형은 다섯개다.
		1. NULL: 결측치.
		2. INTEGER: 8바이트까지로표현할수있는정수.
		3. REAL:8바이트로표현할수있는실수.
		4. TEXT:길이에제약이없는문자열.
		5. BLOB:입력된자료를원형그대로저장.
	- 내부적으로는 char와 varchar의 차이가 없다.
- DROP TABLE test;                                                  ### "test" 테이블이 이미 있다면 삭제.
- CREATE TABLE test (                         		        
     		id INTEGER,
 		name VARCHAR(255),                      
    		address VARCHAR(255),
    		city VARCHAR(255),
    		state CHAR(2),                             
    		zip CHAR(10)
		);
- INSERT INTO test VALUES ( 1, "John", "Main St. 123", "Seattle", "WA", 92105);                     ### OK. 
- INSERT INTO test VALUES ( 1, "Jackson", "Broadway Av. 123", "San Diego", "CA", 91910);       ### 중복 id도 OK. 
- INSERT INTO test VALUES ( "A", "John", "Main St. 123", "Seattle", "WA", 92105);     	    ### SQLite에서는 OK.
- SELECT * FROM test;


### 테이블 생성시 컬럼 별 제약을 둘 수도 있다.
- DROP TABLE test;                                                  ### "test" 테이블이 이미 있다면 삭제.
- CREATE TABLE test (
		a INTEGER NOT NULL,              
    		b VARCHAR(255)
		);			        ### "a"에 NULL을 허용하지 않는다.
- INSERT INTO test VALUES ( 1, "John");                       ### OK.
- INSERT INTO test (a,b) VALUES ( 3, "Sally");                 ### OK.
- INSERT INTO test (a,b) VALUES ( NULL, "David");          ### NOT OK.
- INSERT INTO test (b) VALUES ( "Paul");                       ### NOT OK.

- DROP TABLE test;                                                  ### "test" 테이블이 이미 있다면 삭제.
- CREATE TABLE test (
    		a INTEGER NOT NULL DEFAULT 0,       
    		b VARCHAR(255) UNIQUE NOT NULL    
                          );			         ### "a"에는 default 값 설정. "b"에는 중복 허용하지 않음. 
- INSERT INTO test VALUES ( 1, "John");                       ### OK.
- INSERT INTO test (a,b) VALUES ( 3, "Sally");                 ### OK.
- INSERT INTO test (b) VALUES ( "Paul");                       ### OK!
- INSERT INTO test (a,b) VALUES ( NULL, "David");          ### NOT OK!
- INSERT INTO test VALUES ( 4, "John");                       ### NOT OK.

### PRIMARY KEY 설정과 AUTO_INCREMENT
- DROP TABLE test;                                                  ### "test" 테이블이 이미 있다면 삭제.
- CREATE TABLE test (
		id INTEGER PRIMARY KEY AUTOINCREMENT,     
		a VARCHAR(255),
    		b VARCHAR(255)
		);
- INSERT INTO test ( a, b ) VALUES ( 'one', 'two' );          ### id로 1 자동 삽입! 
- INSERT INTO test ( a, b ) VALUES ( 'three', 'four' );         ### id로 자동 삽입! 
- INSERT INTO test VALUES (5,  'five', 'six' );                   
- INSERT INTO test ( a, b ) VALUES ( 'seven', 'eight' );         ### id로 6 자동 삽입! 

### 테이블 생성 후 구조 변경.
### 다음과 같이 컬럼을 추가할 수 있다.
D- ROP TABLE test;                                                  ### "test" 테이블이 이미 있다면 삭제.
- CREATE TABLE test (
		id INTEGER PRIMARY KEY AUTOINCREMENT,       
		a VARCHAR(255),
    		b VARCHAR(255)
		);
- ALTER TABLE test ADD COLUMN c VARCHAR(100);
- INSERT INTO test VALUES ( 1, "John", "Male", "True");
- INSERT INTO test VALUES ( 2, "Mary", "Female", "False");

### SQLite에서는 테이블의 컬럼 전체를 삭제할 수 없다. 
### 대신 다음과 같이 새로운 테이블을 만든다. 
- CREATE TABLE test2 AS SELECT id, a, b FROM test;      ### "c" 컬럼 없는 새로운 테이블.
- DROP TABLE test;                                                ### 기존 테이블 삭제.
- ALTER TABLE test2 RENAME TO test;                        ### 새 테이블 이름 변경.
- SELECT * FROM test;			       ### 내용을 확인해 본다. 

### BOOLEAN 자료형 표현.
### 다음과 같이 0,1 이외의 값은 reject 되도록 정의해 둔다.
- CREATE TABLE myTB (
		aColumn BOOLEAN NOT NULL CHECK (aColumn IN (0,1))
		);
- INSERT INTO myTB VALUES (0);		### OK.
- INSERT INTO myTB VALUES (1);		### OK.
- INSERT INTO myTB VALUES (2);		### NOT OK!

### FOREIGN KEY를 사용하여 테이블 사이의 관계 설정. 
### 일종의 제약 (constraint) 역할을 함.
- CREATE TABLE Franchisee (
  FranchiseeID    INTEGER PRIMARY KEY, 
  FranchiseeName  TEXT NOT NULL
);

- INSERT INTO Franchisee VALUES (111,"John");		### 데이터를 입력해 둔다.
- INSERT INTO Franchisee VALUES (112,"Paul");		### 데이터를 입력해 둔다.
- INSERT INTO Franchisee VALUES (113,"David");		### 데이터를 입력해 둔다.

- CREATE TABLE Store (
  StoreID     INTEGER PRIMARY KEY, 
  StoreName   TEXT NOT NULL,
  FranchiseeID INTEGER NOT NULL,
  FOREIGN KEY(FranchiseeID) REFERENCES Franchisee(FranchiseeID)
);   ### Store 테이블의 FranchiseeID와 Franchisee 테이블의 FranchiseeID 연결.

- INSERT INTO Store VALUES (1,"711 Gangnam", 111);	### OK.
- INSERT INTO Store VALUES (2,"711 Munjeong", 111);	### OK.
- INSERT INTO Store VALUES (3,"711 Suyu", 113);		### OK.
- INSERT INTO Store VALUES (4,"711 Youido", 114);		### FOREIGN KEY constraint failed!
- DROP TABLE Franchisee;                                              ### 먼저 삭제할 수 없다!
- DROP TABLE Store;                                                     ### 먼저 삭제 가능.
 
### 테이블 JOIN.
### 왼쪽 테이블과 오른쪽 테이블의 공통 값으로 INNER JOIN.
- SELECT a.name, b.item_id, b.quantity, b.price FROM customer AS a INNER JOIN sale AS b ON a.id = b.customer_id;

### LEFT JOIN.
- SELECT a.name, b.item_id, b.quantity, b.price FROM customer AS a LEFT  JOIN sale AS b ON a.id = b.customer_id;

### SQLite에서는 RIGHT JOIN과 FULL OUTER JOIN 지원하지 않는다. 

### "world.db"에 접속하여 다음을 실행해 본다.
### VIEW 생성과 삭제

### 다음과 같이 View를 만들어 본다.
- CREATE VIEW myView1 AS SELECT Name AS Country, Population / 1000 AS "Pop (1000s)" FROM Country;
- CREATE VIEW myView2 AS SELECT Name, Continent, Population FROM Country WHERE Population < 100000 ORDER BY Population DESC;
- CREATE VIEW myView3 AS SELECT Name, Continent FROM Country WHERE Name LIKE '_a%';

### 다음과 같이 View를 실행해 본다.
- SELECT * FROM myView1;
- SELECT * FROM myView2;
- SELECT Name as CountryName FROM myView3;

### 다음과 같이 저장해 둔 View를 삭제한다.
- DROP VIEW myView1;
- DROP VIEW myView2;
- DROP VIEW myView3;
