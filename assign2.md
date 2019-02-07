
# 404 Not Found 꾸미기.

### 작성자
* **김대연** daebalprime@likelion.org _UNIST_LIKELION 6기 수료, 컴퓨터공학과_, 
 
## 개요
404 Error가 무엇인지 간략하게 살펴보고, django에서는 어떻게 404 NF page를 만들 수 있는지 살펴봅니다.

## 404 Not Found = '   '

![\[사진\]](http://ldb.phinf.naver.net/20170109_190/1483942888187uU1yP_JPEG/186059555146313_4.jpeg)

> 404 Not Found라는 카페가 있을 정도입니다. 지금은 망한 것으로 추정됩니다. ~~일종의 행위예술...~~


Microsoft의 페이지뷰(조회수의 개념과 유사합니다) 중 4%가 404 Not Found라는 썰이 있을 정도로 자주 등장합니다. 
프로그래머들 사이에서는 '없다'의 대명사로도 자주 쓰입니다.

이만큼 노출이 잦은 오류 페이지기 때문에 디자인에 굉장히 많은 공을 들이기도 합니다. Google에서 404 design를 검색하면 굉장히 많은 결과물을 보실 수 있습니다.

그러나 지금까지 django를 배우면서 본 우리의 404 Page는 끔찍하기 그지 없습니다. 
![삭막해요....](https://i.stack.imgur.com/V2f7f.jpg)
 이 삭막한 페이지를 바꾸는 것이 이번 강의의 목표입니다. 길지 않고 쉽게 따라오실 수 있으나...

# 주의사항

 1. 처음 Django를 공부하시는 분은 보시지 않기를 권장합니다.
 2. 개발 중인 프로젝트에는 적용하지 마시길 권장합니다. 404 페이지 디자인은 대게 우선순위에서 밀리며, 404 페이지 Customize를 하기 위해 끄는 Debug 모드는 개발 중에 유용하게 쓰이기 때문입니다.




Settings.py 

    Debug = False
    ALLOWED_HOSTS = ['localhost']

Debug 모드를 끕니다. 이 상태에서는 ALLOWED_HOSTS를 직접 지정해 줘야 합니다. 배포 직전의 로컬에서 실행한다면 'localhost'를 추가해주세요.

views.py

    def handler404(request, exception, template_name="404.html"):
        response = render_to_response("404.html")
        response.status_code = 404
        return response

urls.py

    handler404 = 'myapp.views.handler404' 
    handler500 = 'myapp.views.handler500'

django 프로젝트 최상위 폴더에 templates/404.html 작성 후 확인하시면 404 page가 바뀌었음을 확인하실 수 있습니다.

