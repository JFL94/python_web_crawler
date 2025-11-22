from playwright.sync_api import sync_playwright
# from time import sleep # 通用作業系統服務模組 sleep()函式
import os

# print(type(sync_playwright)) 

def main():
    with sync_playwright() as p:
        # print("建立資源檔") # 連線時自動建立資源檔
        
        # 啟動瀏覽器
        browser = p.chromium.launch(headless=False,slow_mo=500)
        # print(type(browser))    

        # 開啟新分頁
        page = browser.new_page()

        # 取得當前html檔案的絕對路徑
        current_dir=os.path.dirname(os.path.abspath(__file__))    
        html_file=os.path.join(current_dir,"login_demo.html")
        
        # print(f"file://{html_file}")
        
        # 訪問網站
        page.goto(f"file://{html_file}")

        # 自動填寫表單
        page.fill("#username","admin")     # 操作網頁中<input>輸入框填寫
        page.fill("#password","password")  # 操作網頁中<input>輸入框填寫
        page.click("#login-button")
        page.wait_for_load_state("networkidle")
        
        page.wait_for_timeout(5000) #取代 time的sleep()

        # #指定秒數內暫停執行
        # sleep(3)
        
        # 關閉瀏覽器
        browser.close()

    # print("釋放資源檔") # 離線時自動釋放資源檔

if __name__ == "__main__":
    main()