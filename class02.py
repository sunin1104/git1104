'''
<출력함수>
print()

<변수> 
: 데이터 저장하는 공간
변수이름 = 데이터

<데이터타입>
1. 숫자타입 Number
- ⭐ int() 정수타입
- float() 소수타입
- 연산자 : +,-,*,/,**(제곱), %(나머지), //(몫)

2. 문자열 String ""
: !@#$$%%& ' ', \n 줄바꿈
- 연산자 : +(이어서 붙이기), *(반복해서 이어붙이기)
- str() :문자열로 변환
- ⭐ len(데이터) : 데이터의 길이 
- ⭐ 순서(=인덱스, 0번) 가 존재합니다.
- ⭐ 인덱싱 : 인덱스를 사용해서 값을 추출하는 것 => 문자열변수이름[인덱스번호]
- 슬라이싱 : 인덱스를 활용해서원하는 구간으로 문자를 잘라내기
  => 문자열변수[시 : end] 시작번호부터~ (끝-1)번호까지 자르기

'''

text = "hello world"
print(len(text))

print(1+1)
"1"
# 정수타입으로 변경하기 : int()
print(int("1")+1) # TypeError: can only concatenate str (not "int") to str
# 문자열로 변경하기 str()
print("1"+str(1))

# type() : 타입을 확인하는 함수 <class 'str'>
print(type(text))
print(type(1))

# text에서 0번째 문자를 추출해서 출력해주세요.
print(text[0])
# text에서 3번째 문자를 추출해서 출력해주세요.
print(text[2])
# text에서 마지막 문자를 추출해서 출력해주세요.
# 마지막 인덱스번호 : 길이-1 
# 오른쪽부터 인덱스 셀수있다. :-1
print(text[-1])

# 슬라이싱 : 인덱스를 활용해서원하는 구간으로 문자를 잘라내기
# 문자열변수[시 : end] 시작번호부터~ (끝-1)번호까지 자르기

text = "i love you"
# text변수를 2번째부터 5번째까지 잘라주세요. (까지~라고 하면 다음번호에서 잘라주기)
print(text[2 : 6])

# 문자열변수.find("찾고싶은 단어"), 해당 단어의 위치를 찾을 수가 있어요.
# text변수에서 "love"의 위치를 찾아주세요.
print(text.find("love"))
# 인덱스를 찾아서 "love" 찾아서 추출해보기 슬라이싱 해보기
# - love 시작 위치부터~ e까지를 자르기
x=text.find("love") # 시작번호
# e : 5+1
print(x,x+len("love") )
print(text[x:x+len("love")])


# 문제) "start" "end"단어 사이의 문자열을 찾고싶다. 찾아서 출력해주세요. 
ex ='djhfaheu___wehiehrhlsfhouhewwehr1238364892hrehwfwhelhewlehrle whiorhhf3824863___883@hre93734084fdfhieelwhfhieistart#.redro lacitebahpla yb kcatta trats eW .yti@sr@@evinu,tna@lp rae@@lcun,llam@ gni@@ppoh@s,lla@h@ y@tic,tekr@am kcots,noi@tats eci@l@op,ret@aeht:secalp gniwollof fo eno si tegrat ehT#endhfdhsifohifeifhlk368537djs89hds83e____89fwgafg3dbsjhgdiutwf w823___t93g3%@iu3977e&egd37dheehdgsaioiowi'
# print(ex.find("start"))
# print(ex.find("end"))
s = ex.find("start")
e = ex.find("end")
print(ex[s+len("start"):e])
print("\n")

# 맨앞에서 부터 자르고싶다.
ex[:5]
# 맨뒤까지 부터 자르고싶다.
ex[5:]