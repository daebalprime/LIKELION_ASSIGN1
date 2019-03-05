  

# tests.py
  

### 작성자

*  **김대연** daebalprime@likelion.org _UNIST_LIKELION 6기 수료, 컴퓨터공학과_,

## 개요

추후 서비스의 크기가 비대해질 때, 자동화된 테스트를 위해 tests.py를 작성하는 방법을 정리했습니다. 단순 저장된 정보를 보여주는 것을 넘어선다면 테스트 자동화가 메리트가 있지 않을까 생각합니다.

## appname/tests.py

    import datetime
    
    from django.test import TestCase
       
    # test에 필요한 모듈과 패키지를 알아서 import
    
    class QuestionModelTests(TestCase):
        def first_test(self):
            # test할 상황을 코드로 작성합니다.
            self.assertIs(테스트를 하고싶은 코드, 올바른 return값)

다음과 같은 구조를 띄고 있으며, 원리는 간단합니다.
특정 함수나 기능들이 작동을 잘 하는지 비교를 하게 되는데, assertIs 메서드는 개발자가 의도한 올바른 결과물과 실제 코드의 return 값을 비교하여 일치 여부를 반환합니다.

테스트 실행은 다음과 같이 입력해주세요.

    python manage.py test <appname>

실행 시 다음과 같은 결과물을 반환합니다. django 공식 튜토리얼에서 가져왔습니다.

> reference : https://docs.djangoproject.com/ko/2.1/intro/tutorial05/

    Creating test database for alias 'default'...
    System check identified no issues (0 silenced).
    F
    ======================================================================
    FAIL: test_was_published_recently_with_future_question (polls.tests.QuestionModelTests)
    ----------------------------------------------------------------------
    Traceback (most recent call last):
      File "/path/to/mysite/polls/tests.py", line 16, in test_was_published_recently_with_future_question
        self.assertIs(future_question.was_published_recently(), False)
    AssertionError: True is not False
    
    ----------------------------------------------------------------------
    Ran 1 test in 0.001s
    
    FAILED (failures=1)
    Destroying test database for alias 'default'...
