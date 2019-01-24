
# LIKELION 7기 운영진 교육 1차 보고서

### 작성자
* **김대연** daebalprime@likelion.org _UNIST_LIKELION 6기 수료, 컴퓨터공학과_, 
 
> 과제 데드라인까지 벤쿠버에서 머물고 있어서 내용이 다소 부실한 점 죄송합니다. 다음 과제부터 열심히 하도록 하겠습니다.

## 개요
강의보다 한 걸음 더! VSCODE 내의 bash 등을 이용하여 git과 django, python등을 사용하는데
저는 보유중인 Windows 노트북에서 리눅스를 실행할 수 있게 해주는 Windows Subsystem Linux(이하 WSL)을 이용하여 이 모든 작업을 우분투에서 진행하였습니다.

### 대상?
* 리눅스를 사용해본 적이 없는 분
* Windows 10 노트북 사용자 
* 추후 프로그래머로 일하고 싶은 비전공자
* 그냥 멋있어 보여서 써보고 싶으신 분

#### To do list
* 필수 
  * Windows 10 업데이트를 최신 상태로 유지
  * https://webdir.tistory.com/541 (WSL 본격설치)
  * https://studyforus.tistory.com/223 (root 계정 암호 설정)
  * 파이썬 설치하기
  `sudo apt-get update`
  `sudo apt-get install python3`
  `sudo apt-get install python3-pip`
  `cd /mnt/c`
  

	> 현재 위치는 사용중인 윈도우의 C드라이브입니다. 
	> 명령어 ll로 현재 위치에 어떤 폴더와 파일이 존재하는지 확인합니다.   
	> 명령어 cd (폴더이름) 으로 원하는 위치까지 이동합니다.  
    > 가상환경 생성 및 activate까지는 강의에서 배우신 명령어와 동일합니다. 
    > 가상환경 생성 이후 명령어는 다음과 같습니다.

  `source bin/activate`
  `pip3 install django`
* 옵션
  * https://webdir.tistory.com/546 (WSL 터미널 색 변경)
  * https://mnpk.github.io/2017/11/03/bash_on_ubuntu_on_windows.html (WSL 터미널 폰트변경)
  * https://nolboo.kim/blog/2015/08/21/oh-my-zsh/ (Oh My ZSH)

* 공부합시다
	* http://www.ciokorea.com/news/29239 (리눅스 필수 명령어)

* 당장 필요한 상식:
	* Ubuntu는 Windows 내에서 구동되는 또 하나의 운영체제, 컴퓨터라고 생각하시면 편합니다.
	* Ubuntu에서 Windows의 파일에 접근이 가능하지만, 그 반대는 귀찮은 과정이 필요합니다.
	* Ubuntu에서 Windows 파일 위치( /mnt/c/....) 에 접근하여 작업하시는 것을 권장합니다.

