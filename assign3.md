
# Render와 Redirect,  Reverse의 차이점

### 작성자
* **김대연** daebalprime@likelion.org _UNIST_LIKELION 6기 수료, 컴퓨터공학과_, 
 
## 개요
예전부터 django를 공부할 때 render와 redirect의 차이가 궁금했는데 이번 스터디 대체과제로 주제를 선정해서 쓰게 되었습니다. 
'r'로 시작하는 단어가 5개가 등장하니, 유의깊게 읽어주시면 감사하겠습니다.

## render?
우리가 알다시파 views.py에서 
return render...
를 이용하여 템플릿을 쏴주는 역할을 하는 것으로 알고있죠. context를 통하여 데이터도 템플릿에 전달할 수 있습니다. 

## HTTP Response Code
멋사 강의에서 배웠듯이 http에는 요청과 응답, request가 있으면 response가 있으며, 상태에 따라 code를 반환합니다. 404와 같이 response의 상태를 나타내죠. 

그중 300번 대의 코드는 redirect 요청, request가 완료되기 위해서는, 서버가 제시해주는 주소로 이동해야 완료됨을 알려주는 코드입니다.  그래서 해당 주소로 이동하여 request를 마무리 짓게 됩니다. 

## 그러나... 

300번 대의 response code, redirect에는 오로지 redirect할 주소만을 담고 있습니다. context를 담을 수 없습니다. render와의 차이죠.

## 정리
render는 템플릿을 지정하여 쏴주고, context를 전달할 수 있습니다.
redirect는  `redirect('/some/url/')`처럼 url을 써도 되고, urls.py에서 맨 마지막에 지정했던 `name = "home"` 과 같이 `redirect('home')` 써도 기똥차게 알아듣습니다.
