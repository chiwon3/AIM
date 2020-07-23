git 
ls -al
git status
git add . #git이 있는 전체 폴더 git 서버에 추가
git commit -m "이 자리에 수정한 내용 알수있도록 메시지 남겨놓기"
git remote -v #git과 연결된 web 서버 보기
git remote add origin https://~~~ #git remote -v 에서 연결이 안되어있을때 연결시키는 명령어 (origin은 default 이름이라서 바꾸고 싶으면 바꿔도 됨)

git config credential.helper store #aws에서 뒤부터는 비밀번호 안넣어도 되도록 함

git push -u origin master #git push 할때 다음부터 자동으로 origin master로 넘겨줌

-m == message
-u == upstream
-f == force


식당에 비유
정적 Web == 식당에 있는 메뉴만 요리해주는 식당      #EX) 블로그
동적 Web == 유저가 들고간 재료로도 요리해주는 식당  #EX) 커뮤니티

pip -m venv myvenv #가상환경 만들기
. myvenv/bin/activate #가상환경 실행(이 명령어 실행하념 pip list 했을때 가상환경에 설치된것만 보여줌
deactivate #가상환경에서 빠져나오기

rm -r myvenv/ #가상환경 폴더 지우기(앞에 명령어 이용하면 다른 폴더도 지울수 있음)

python manage.py runserver 8080 #따로 입력하지 않으면 로컬에서 동작하는걸로 인식하고 8000으로 서버를 돌리지만 aws에서 동작할때는 8080을 붙여야함

