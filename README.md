
인스타그램 계정에서 사진을 한번에 다받으려고하는데 구글에서 검색해서 하기 귀찮아서 만든 프로그램입니다.
계정명을 입력하고 다운로드 버튼을 누르면 다운로드가 시작됩니다.
다운로드 위치가 복잡합니다 os.path.join(os.getcwd(), 'downloads')를 사용했습니다.
필요하다면 app.py 파일에서 수정해서 사용하세요.

요즘 Instagram에서 크롤링을 안되게하려 한다고 합니다.
개인의 동의없이 크롤링을하고 상업적으로 이용한는것은 불법이라합니다.

이 프로그램은 본인의 계정의 사진을 백업하기위해서 만든 프로그램이므로 다른 사람의 계정에는 사용하지 마세요.

아.instaloader 라이브러리를 사용했습니다. 저는 사진만 다운받으려고 다른 옵션은 모두 False로 했습니다. 
동영상, 게시글 내용까지 다 받고싶으시면 True로 바꿔주세요.

# Instagram Image Downloader

인스타그램 공개 계정의 이미지를 다운로드하는 웹 애플리케이션입니다.

## 기능
- 공개 계정의 이미지 다운로드
- 실시간 다운로드 진행률 표시
- 간단한 웹 인터페이스

## 설치 방법

1. 저장소 클론

    bash
    git clone https://github.com/your-username/instagram-downloader.git
    cd instagram-downloader

2. 필요한 패키지 설치

    bash
    pip install -r requirements.txt

3. 실행방법

    bash
    python3 app.py

Future Work
- 비공개 계정 다운로드
    :login 기능이 필요할겁니다.
- 웹버전 만들기
    :Flask를 사용해서 웹버전을 만들수있습니다. 

심심할때 만들어보세요.


