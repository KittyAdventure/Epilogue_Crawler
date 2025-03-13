import requests
import json
import pymysql
import datetime

class KyoboBookCrawler:
    def __init__(self, host, user, password, db, charset='utf8mb4',
                 user_agent=""): # 환경에 맞게 변경
        self.host = host
        self.user = user
        self.password = password
        self.db = db
        self.charset = charset
        self.headers = {"User-Agent": user_agent}
        self.conn = None
        self.cursor = None
        self.insert_sql = """
            INSERT INTO test 
            (book_rank, book_title, author, publisher, release_date, review_count, review_rating, review_keyword, reg_date)
            VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)
        """

    def connect_db(self):
        self.conn = pymysql.connect(
            host=self.host,
            user=self.user,
            password=self.password,
            db=self.db,
            charset=self.charset
        )
        self.cursor = self.conn.cursor()

    def close_db(self):
        if self.conn:
            self.conn.commit()
            self.cursor.close()
            self.conn.close()

    def scrape_and_insert(self, pages=10, period_code="002"):
        # period_code를 "002"로 지정하면 주간 데이터를 가져올 수 있습니다.
        for page in range(1, pages+1):
            url = (f"https://store.kyobobook.co.kr/api/gw/best/best-seller/total?"
                   f"page={page}&per=20&period={period_code}&bsslBksClstCode=A")
            res = requests.get(url, headers=self.headers)
            json_data = json.loads(res.text)
            books = json_data.get("data", {}).get("bestSeller", [])
            
            for book in books:
                prstRnkn = book.get("prstRnkn", None)
                cmdtName = book.get("cmdtName", "")
                chrcName = book.get("chrcName", "")
                pbcmName = book.get("pbcmName", "")
                rlseDate = book.get("rlseDate", "")
                buyRevwNumc = book.get("buyRevwNumc", 0)
                buyRevwRvgr = book.get("buyRevwRvgr", 0.0)
                revwEmtnKywrName = book.get("revwEmtnKywrName", "")
                
                current_dt = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
                
                self.cursor.execute(self.insert_sql, (
                    prstRnkn,
                    cmdtName,
                    chrcName,
                    pbcmName,
                    rlseDate,
                    buyRevwNumc,
                    buyRevwRvgr,
                    revwEmtnKywrName,
                    current_dt
                ))
            print(f"Page {page} 데이터 삽입 완료.")

    def run(self, pages=10, period_code="002"):
        try:
            self.connect_db()
            self.scrape_and_insert(pages, period_code)
        finally:
            self.close_db()
            print("전체 데이터 적재가 완료되었습니다.")

if __name__ == "__main__":
    # 환경에 맞게 접속 정보 입력
    crawler = KyoboBookCrawler(
        host='',
        user='',
        password='',
        db=''
    )
    crawler.run(pages=10, period_code="002")
