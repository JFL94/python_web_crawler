from playwright.sync_api import sync_playwright
from time import sleep

# print(type(sync_playwright)) 

def main():
    with sync_playwright() as p:
        # print("建立資源檔") # 連線時自動建立資源檔
        
        # 啟動瀏覽器
        browser = p.chromium.launch(headless=False)
        print(type(browser))

        # 開啟新分頁
        page = browser.new_page()

        # 訪問網站
        page.goto("https://www.google.com")

        # 取得網站標題
        print(page.title())

        #
        sleep(5)
        
        # 關閉瀏覽器
        browser.close()

    print("釋放資源檔") # 離線時自動釋放資源檔

if __name__ == "__main__":
    main()