# Epilogue Crawler

**Epilogue Crawler**는 교보문고 베스트셀러 API를 활용하여 도서 정보를 수집하는 파이썬 크롤러 프로젝트입니다.  
이 프로젝트는 Python **3.9.12** 환경에서 테스트되었으며, 주요 도서 정보(순위, 제목, 저자, 출판사, 출간일, 구매 리뷰 수, 구매 리뷰 평점, 리뷰 감성 키워드, 데이터 수집 시각)를 추출하여 데이터베이스 등에 저장할 수 있도록 설계되었습니다.

---
## 주요 기능

- 교보문고 베스트셀러 API 호출
- 도서 정보 추출:
  - **순위 (book_rank)**
  - **제목 (book_title)**
  - **저자 및 관련 인물 (author)**
  - **출판사 (publisher)**
  - **출간일 (release_date)**
  - **구매 리뷰 수 (review_count)**
  - **구매 리뷰 평점 (review_rating)**
  - **리뷰 감성 키워드 (review_keyword)**
- 데이터 추출 시 현재 날짜와 시간(초까지 포함) 기록

---
## 요구사항

- Python 3.9.12  
- 필요한 패키지: [requests](https://pypi.org/project/requests/), [PyMySQL](https://pypi.org/project/PyMySQL/)

---
## 설치 및 실행 방법

1. **GitHub 저장소 클론:**

   ```bash
   git clone https://github.com/KittyAdventure/Epilogue_Crawler.git
   cd Epilogue_Crawler```

2. 필요한 패키지 설치

    ```bash
    pip install -r requirements.txt
    ```

3. 크롤러 실행: 데이터베이스 연결 정보 등 환경에 맞게 `kyobo_book_crawler.py` 파일을 수정한 후 아래 명령어로 실행합니다.

    ```bash
    python kyobo_book_crawler.py
    ```
---
## 프로젝트 구조

```bash
Epilogue_Crawler/
├── README.md             # 프로젝트 개요 및 사용법
├── requirements.txt      # 필요한 패키지 목록
└── kyobo_book_crawler.py # 크롤러 코드 (DB 저장 기능 포함)
```
```

---
## 라이선스 (License)

이 프로젝트는 **MIT 라이선스**에 따라 자유롭게 사용, 수정, 배포할 수 있습니다.  
자세한 사항은 [`LICENSE`](LICENSE) 파일을 참고하세요.  

---

### MIT License

Copyright (c) 2024 Epilogue Team

본 소프트웨어는 무료로 제공되며, 누구든지 제약 없이 사용할 수 있습니다.
단, 본 소프트웨어의 사용으로 인해 발생하는 어떠한 법적 책임도 개발자에게 귀속되지 않습니다.

This project is licensed under the MIT License, which allows free use, modification, and distribution.
For more details, please check the LICENSE file.
