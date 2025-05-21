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


(4) 임시저장 취소하기 - reset
$ git reset 파일명
$ git reset .
 
(5) Git 저장하기 - Commit
- 임시저장된 상태만 저장이된다.

$ git commit -m " 커밋 메세지 "


(6) Git 히스토리 확인 - log
- commit 이력을 확인

$ git log

commit efe81f41d36af22a54d03ab4b546620fd2b2a825 (HEAD -> main) <- 고유아이디 앞자리7
Author: sunin <suninhailey1104@gmail.com>
Date:   Wed May 21 23:10:27 2025 +0900

    첫번쨰 커밋



7. 로컬 저장소와 원격저장소 연결 추가 - remote add    
$ git remote add [원격저장소 별명] [원격저장소 주소]
git remote add test https://github.com/sunin1104/git1104.git


8. 원격 저장소 연결 상태 확인 - remote -v
$ git remote -v

9. 원격저장소에 이력 업로드 - push
$ git push [원격저장소별명][브런치]
git push test main
''' 




