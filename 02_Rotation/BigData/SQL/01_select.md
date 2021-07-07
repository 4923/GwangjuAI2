# `SELECT`

### 컬럼 호출
1. 모든 컬럼 호출
```sql
SELECT * FROM Country;   -- Country의 모든 컬럼을 호출한다.
```

2. 특정 컬럼 호출
```sql
SELECT Name, Code, Region, Population FROM Country;
```

3. 불러온 컬럼의 이름을 변경하여 출력
```sql
SELECT Name AS Country
```

4. 수식 적용
```sql
SELECT Name As Country, Population / 1000 From Country;
-- Country에서 Name열을 Country라는 이름으로 불러오고 Population을 불러오는데 불러올 때 1000으로 나눈 값을 호출 (Population/1000)
```

### 정렬된 결과 : ORDER BY
1. 기본 정렬 (오름차순)
```sql
SELECT Name FROM Country ORDER BY Name;
-- 이름순으로 정렬
```

2. 내림차순 정렬 : DESC (descending)
```sql
SELECT Name FROM Country ORDER BY Name DESC;
-- 이름순으로 내림차순 정렬
```

3. 오름차순 정렬 : ASC (ascending)
```sql
SELECT Name FROM Country ORDER BY Name ASC;
-- 이름순으로 오름차순 정렬
```

4. 두 가지 이상의 기준으로 정렬
- 우선순위 : 먼저 나오는 컬럼
```sql
SELECT Name, Continent From Country ORDER BY Continent DESC, Name;
-- Continent를 내림차순으로, 그 안에서 이름순으로 (기본 오름차순) 정렬
```

### 필터링 결과 : WHERE, LIKE
1. WHERE ~ BETWEEN ~
- AND, OR, NOT 등의 조건문을 사용할 수 있다.
```sql
SELECT Name, Continent, Population FROM Country WHERE Population < 100000 ORDER BY Population DESC;
-- Country라는 데이터에서 Name, Continent, Population 열을 불러오는데 Population은 100000 미만인 값을 내림차순으로 호출

SELECT Name, Continent, Population FROM Country WHERE Population < 100000 AND Continent = 'Oceania' ORDER BY Population DESC;
-- Country라는 데이터에서 Name, Continent, Population 열을 불러오는데 Population은 100000 미만이고 Continent는 Oceanina인 데이터를 Population 내림차순으로 호출
-- Oceanina의 Population이 100000인 Name을 Population 내림차순으로 호출

SELECT Name, Population FROM Country WHERE Population BETWEEN 1000000 AND 10000000 ORDER BY Population DESC
-- Country라는 데이터에서 Name, Continent, Population 열을 불러오는데 Population이 1000000, 10000000 사이인 데이터를 Population 내림차순으로 호출
```
2. LIKE
- `%` : 불특정 문자**열**
- `_` : 불특정 문자

```sql
SELECT Name, Continent FROM Country WHERE Name LIKE '%island' -- 끝.
SELECT Name, Continent FROM Country WHERE Name LIKE 'island%' -- 시작.
SELECT Name, Continent FROM Country WHERE Name LIKE '%island%' -- 중간.
SELECT Name, Continent FROM Country WHERE Name LIKE '_a%' -- 두번째 문자.
```

- `IN`을 사용하면 멤버쉽 필터링 결과를 호출할 수 있다.
```sql
SELECT Name, Continent FROM Country WHERE Continent IN ( 'Europe', 'Asia' ); 
```

### 출력 결과 이어서 사용
SELECT로 선택한 열을 이어서 볼 수 있는데, 이는 실제로 반영되지 않는 '가상의 테이블'이다.

```sql
SELECT Name FROM (SELECT Code, Name, Continent FROM Country);
-- Country에서 Code, Name, Continent를 선택한 테이블에서 Name을 선택
SELECT COUNT(*) FROM (SELECT DISTINCT CountryCode FROM City);
-- (*) : all
-- DISTINCT : 중복 제거
-- City에서 CountryCode를 중복없이 불러와서 그 개수를 COUNT
```