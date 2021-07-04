--
# -- SQL 기초 문법 II. : CREATE (`C`rud)
from ./Project/01_SQL_and_DataBase/scripts/script_02.txt

--

-- "scratch.db"에 접속하여 다음을 실행해 본다.

### CREATE TABLE로 데이터 베이스에 테이블을 추가할 수 있다 . 
- CREATE TABLE test ( a INT, b TEXT, c TEXT );        		              -- "a", "b", "c" 컬럼의 테이블 생성.
- CREATE TABLE IF NOT EXISTS test ( a INT, b TEXT, c TEXT );        	-- "a", "b", "c" 컬럼의 테이블 중복 체크 후 생성.
- SELECT name FROM sqlite_master WHERE TYPE = "table"         	-- 테이블 목록 (SQLite).
- PRAGMA table_info(test)                                                                 -- 특정 테이블에 대한 정보.

### INSERT INTO ~ VALUES로 행을 추가할 수 있다.
- INSERT INTO test VALUES ( 1, 'This', 'Right here!' );            -- 1행 추가.
- INSERT INTO test ( b, c ) VALUES ( 'That', 'Over there!' );     -- "a"는 NULL 상태!
- SELECT * FROM test;			             -- 내용 확인.

### 다른 테이블에서 SELECT로 가져온 결과로 행 추가 가능하다.
- INSERT INTO test ( a, b, c ) SELECT id, name, description FROM item;   -- "item" 테이블에서 가져온 결과로 "test"테이블에 행 추가. 

### UPDATE + SET로 특정 행의 특정 컬럼 값을 변경할 수 있다. 
- UPDATE test SET c = 'Extra funny.' WHERE a = 2;              -- "c" 컬럼의 값 변경.
- SELECT * FROM test;			             -- 내용 확인.
- UPDATE test SET c = NULL WHERE a = 2;                       -- NULL 값으로 변경.
- SELECT * FROM test;			             -- 내용 확인.
- UPDATE test SET (b, c) = ('T-Rex', 'Toy dinosaur')  WHERE a = 2;        -- 값 변경.
- SELECT * FROM test;			             -- 내용 확인.

### DELETE FROM으로 특정 행을 삭제할 수 있다. 
- DELETE FROM test WHERE a = 2;              -- 조건에 맞는 행 삭제.      
- DELETE FROM test WHERE a = 1;              -- 조건에 맞는 행 삭제.
- SELECT * FROM test;	                  -- 내용 확인.
- DELETE FROM test;                                  -- 요주의! 모든 행 삭제! 테이블은 남음.
- SELECT * FROM test;	                   -- 내용 확인.

### DROP TABLE로 특정 테이블을 삭제할 수 있다. 
- DROP TABLE test;                                    -- 데이터 베이스에서 "test" 테이블 삭제!
- DROP TABLE IF EXISTS test;                       -- 존재여부 확인하고 데이터 베이스에서 "test" 테이블 삭제!

### NULL은 값이 아니라 결측치를 의미하며 0 또는 ' ' (공백)과는 다르다. 
- CREATE TABLE test ( a INT, b TEXT, c TEXT );       
- INSERT INTO test ( b, c ) VALUES ( 'This', 'That' );         	  -- "a"에는 NULL을 넣어 줌.
- INSERT INTO test ( a, b, c ) VALUES ( 2, 'These', 'Those' );      -- NULL없이 행 추가.
- SELECT * FROM test;                                                -- NULL 포함 다 보여줌.
- SELECT * FROM test WHERE a = NULL;                        -- 작동 안함. 
- SELECT * FROM test WHERE a IS NULL;                        -- 작동 함.
- SELECT * FROM test WHERE a IS NOT NULL;                  -- 작동 함.
- SELECT COUNT(*) FROM test WHERE a IS NULL;                -- "a" 컬럼의 NULL 수 세어 줌.
- SELECT COUNT(*)-COUNT(a) FROM test;                          -- "a" 컬럼의 NULL 수 세어 줌.
- DELETE FROM test WHERE a IS NULL;                              -- "a" 컬럼에 NULL이 있는 행 삭제.
- UPDATE test SET a = 0 WHERE a IS NULL;                        -- "a" 컬럼의 NULL을 0 값으로 채워 넣음.
