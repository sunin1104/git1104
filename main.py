'''
버전관리시스템 (VCS, Version control system)
: 파일 변화를 시간에 따라 기록하여 과거 특정 시점의 버전을 다시 불러올 수 있는 시스템


Git 저장소
: Git의 기본요소로 이력을 관리할 저장소가 필요
: 저장소는 말 그대로 파일을 저장하는 장소로, 파일 이력에 따라 저장


Git 동작원리
작업중 -> 임시저장(add) -> 저장(commit) -> push(업로드)
                                   <- pull(다운받기)


<Git 설정>
git config --global user.name "sunin"
git config --global user.email "suninhailey1104@gmail.com"
git config --global core.precomposeunicode true
git config --global core.quotepath false                  

<로컬 저장소>
(1) 로컬 저장소 생성하기
$ git init
- 빨간색 : 아직 저장안함
- 초록색 : 임시 저장할 선택을 하기


(2) 현재 상태 확인
$ git status

(3) 임시저장상태로 변환하기 - add
$ git add 파일명

$ git add .



'''




