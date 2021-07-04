
# -- SQL 기초 문법 I. : SELECT (c`R`ud)
from ./Project/01_SQL_and_DataBase/scripts/script_01.txt

-- "world.db"에 접속하여 다음을 실행해 본다.


### 행 가져오기.
* SELECT 'Hello, World';                                   -- 문자열 출력.  
* SELECT 1 + 2;                                              -- 계산결과 출력.  
* SELECT * FROM Country;                               -- "Country"는 table 이름.  
* SELECT * FROM Country ORDER BY Name;    -- 정렬 적용.  
* SELECT Name, LifeExpectancy AS 'Life Expectancy' FROM Country; -- 이름 바꿈. 
    - 변수에 공백이 있는 경우 따옴표로 감싸 문자열을 만들어야 한다.
* SELECT COUNT(*) FROM Country;                                          -- 행 수 카운팅.  
* SELECT * FROM Country ORDER BY Name LIMIT 5;                 -- 출력 수 한정.  
* SELECT * FROM Country ORDER BY Name LIMIT 5 OFFSET 5;   -- 첫 5개 건너 뜀.  
    - OFFSET : 건너뛴다.
    - ex) 순서대로 10번째 값부터? : SELECT * FROM Country ORDER BY Name OFFSET 9;

### 특정 컬럼 가져오기.
> 열은 선택해서 가져오고, 행은 조건을 걸어 가져온다
* SELECT * FROM Country ORDER BY Code;                                            -- 모든 컬럼.
* SELECT Name, Code, Region, Population FROM Country ORDER BY Code;   -- 특정 컬럼. (Name, Code, Region, Population)
* SELECT Name, Code, Region, Population FROM Country ORDER BY Population;   -- 특정 컬럼.
* SELECT Name, Code, Region, Population FROM Country ORDER BY Population DESC;   -- 특정 컬럼.
* SELECT Name AS Country, Code FROM Country ORDER BY Code;            	    -- 컬럼을 불러와서 이름을 변경하여 출력할 수 있다.
* SELECT Name AS Country, Population / 1000 AS "Pop (1000s)" FROM Country;      -- 간단한 수식을 적용할 수도 있다. 
* SELECT Name AS Country, ROUND(Population/SurfaceArea,0) AS "Population Density" From Country ORDER BY ...
    - ROUND(값, 반올림 할 위치)
    - 특정 컬럼을 가져올 때 연산할 수 있다 : **파생변수 생성 가능**

### * SELECT + ORDER BY를 사용해서 정렬된 결과를 보여줄 수 있다. 
* SELECT Name FROM Country;                              -- 정렬되지 않음.
* SELECT Name FROM Country ORDER BY Name;     -- 오름차순 정렬 (Default). 
* SELECT Name FROM Country ORDER BY Name DESC;   -- 내림차순 정렬.
    - DESCending
* SELECT Name FROM Country ORDER BY Name ASC;     -- 오름차순 정렬.
    - ASCending
* SELECT Name, Continent FROM Country ORDER **BY Continent, Name**;         -- 두 개 이상의 컬럼으로 정렬.
    - 대륙 안에서 이름순으로
* SELECT Name, Continent FROM Country ORDER BY **Continent DESC**, Name;  -- 먼저 나오는 컬럼을 우선해서 정렬
    - 특정 컬럼의 특정 행 (조건에 맞는 행)

### * SELECT + <u>WHERE</u> 를 사용해서 필터링 결과를 보여줄 수 있다. 
### AND, OR 등으로 조건문을 연결할 수 있다.
### BETWEEN n1 AND n2로 n1~n2 레인지에 속하는 값만 필터링 할 수 있다.  
* SELECT Name, Continent, Population FROM Country WHERE Population < 100000 ORDER BY Population DESC;
* SELECT Name, Continent, Population FROM Country WHERE Population < 100000 AND Continent = 'Oceania' ORDER BY Population DESC;
* SELECT Name, Population FROM Country WHERE Population BETWEEN 1000000 AND 10000000 ORDER BY Population DESC;
* SELECT Name, Population FROM Country WHERE Population NOT BETWEEN 1000000 AND 10000000 ORDER BY Population DESC;

### * SELECT + WHERE + LIKE을 사용해서 필터링 결과를 보여줄 수 있다. 
### '%' 는 불특정 문자열 부분을 의미하고 '_'는 불특정 문자를 의미한다.
* SELECT Name, Continent FROM Country WHERE Name LIKE '%island';   -- 끝.
* SELECT Name, Continent FROM Country WHERE Name LIKE 'island%';   -- 시작.
* SELECT Name, Continent FROM Country WHERE Name LIKE '%island%'; -- 중간.
* SELECT Name, Continent FROM Country WHERE Name LIKE '_a%';  -- 두번째 문자가 'a'.

### * SELECT + WHERE + IN을 사용해서 멤버쉽 필터링 결과를 보여줄 수 있다. 
* SELECT Name, Continent FROM Country WHERE Continent IN ( 'Europe', 'Asia' ); 
* SELECT Name, Continent, Region FROM Country WHERE Region IN ( 'Western Europe', 'Eastern Europe' ) ORDER BY Region; 
* SELECT Name, Continent, Region FROM Country WHERE Region = 'Western Europe' OR Region = 'Eastern Europe' ORDER BY Region;   -- 이전 것과 같은 의미.

### DISTINCT 키워드를 사용해서 중복을 제거하고 출력할 수 있다. 
* SELECT CountryCode, Name FROM City;
* SELECT DISTINCT CountryCode FROM City;			-- 중복없이 국가코드 출력.
* SELECT COUNT(CountryCode) FROM City;			-- 국가코드 수 카운팅.
* SELECT COUNT(DISTINCT CountryCode) FROM City;		-- 중복없이 국가코드 수 카운팅.

### * SELECT로 출력된 결과를 "가상"의 테이블로 사용하여 * SELECT 문을 만들 수 있다. 
* SELECT Name FROM (* SELECT Code, Name, Continent FROM Country);
* SELECT COUNT(*) FROM (* SELECT DISTINCT CountryCode FROM City);

