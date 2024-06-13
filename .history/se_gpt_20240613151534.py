from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

import subprocess
import time


user_agent = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/113.0.0.0 Safari/537.36"
options = webdriver.ChromeOptions()
# options.add_argument('--headless=new')
options.add_argument("window-size=1920x1080")
options.add_argument(f"user-agent={user_agent}")
driver = webdriver.Chrome(service=Service(
    ChromeDriverManager().install()), options=options)

# 웹사이트 접속
driver.get("https://chatgpt.com/")


wait = WebDriverWait(driver, 10)
# 웹페이지 열기
print("웹페이지 열기 시도 중...")
driver.get("https://chatgpt.com/")
time.sleep(2)  # 페이지 로딩을 위한 대기 시간
print("웹페이지 열림")

prompt = """
https://www.gvg.co.kr/item/349375 인터넷에서 이 상품과 동일한 상품 찾아보고 상품정보와 구매후기를 요약해줘. gvg.co.kr은 제외하고 검색해줘. 요약된 정보를 아래 JSON 형식으로 제공해줘.
### JSON 형식 예시:
{
  "product_info": {
    "product_name": "Example Shirt",
    "brand": "FashionBrand",
    "category": "Shirt"
  },
  "features": {
    "material": "100% Cotton",
    "color": ["White", "Black", "Blue"],
    "size_options": ["S", "M", "L", "XL"],
    "key_features": ["Breathable fabric", "Slim fit", "Easy care"]
  },
  "pricing": {
    "official_price": "$49.99",
    "discounted_price": "$39.99",
    "purchase_links": [
      {
        "vendor": "FashionBrand Store",
        "url": "https://fashionbrand.com/product/FB12345"
      },
      {
        "vendor": "Another Fashion Store",
        "url": "https://anotherfashionstore.com/product/FB12345"
      }
    ]
  },
  "user_reviews": [
    {
      "reviewer": "Alice Johnson",
      "review": "Very comfortable and fits well.",
      "rating": 5,
      "date": "2024-05-15"
    },
    {
      "reviewer": "Bob Smith",
      "review": "Good quality but the size runs a bit small.",
      "rating": 4,
      "date": "2024-05-20"
    }
  ],
  "sources": [
    {
      "source": "Fashion Review Site",
      "url": "https://fashionreview.com/product/FB12345"
    },
    {
      "source": "Official Brand Site",
      "url": "https://fashionbrand.com/product/FB12345"
    }
  ]
}
"""

# 텍스트 입력란 찾기 및 문자열 입력
try:
    print("텍스트 입력란 찾기 시도 중...")
    textarea = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, "prompt-textarea"))
    )
    print("텍스트 입력란 찾기 성공")
    time.sleep(2)  # 입력 전 대기 시간
    textarea.send_keys(prompt)
    time.sleep(5)  # 입력 후 대기 시간
    print("문자열 입력 성공")
except Exception as e:
    print(f"텍스트 입력란을 찾을 수 없습니다: {e}")


# 버튼 클릭
# try:
#     time.sleep(6)  # 입력 후 대기 시간
#     print("버튼 찾기 시도 중...")
#     # 버튼이 클릭 가능할 때까지 대기
#     send_button = WebDriverWait(driver, 100).until(
#         EC.element_to_be_clickable((By.CSS_SELECTOR, ".button[data-testid='fruitjuice-send-button']"))
#     )
#     print("버튼 찾기 성공")
#     time.sleep(2)  # 클릭 전 대기 시간
#     send_button.click()
#     time.sleep(2)  # 클릭 후 대기 시간
#     print("버튼 클릭 성공")
# except Exception as e:
#     print(f"버튼을 클릭할 수 없습니다: {e}")




# # 카페 24 로그인 
# username = driver.find_element(By.ID, 'loginId')  
# password = driver.find_element(By.ID, 'loginPasswd')  
# username.send_keys('gvgurbanstore')
# password.send_keys('iLq-ILS-3pi-ifb')
# print(f'username 로 접속')


# login_button = driver.find_element(By.ID, 'idLoginBtn')  
# login_button.click()
# print(f'login_button 클릭 로그인')

# try:
#     WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, 'iptBtnEm')))
#     pass_btn = driver.find_element(By.ID, 'iptBtnEm')
#     pass_btn.click()
#     print(f'비밀번호 다음에 변경')

#     WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.LINK_TEXT, '백업받기/올리기')))
#     backup_link = driver.find_element(By.LINK_TEXT, '백업받기/올리기')
#     backup_link.click()
#     print(f'{backup_link} 클릭')

#     radio_btn=driver.find_element(By.NAME,'mssqlDbIdx')
#     radio_btn.click()
#     call_DB=driver.find_element(By.ID,'btnBackup')
#     call_DB.click()
#     print(f'{call_DB} 성공')
# except NoSuchElementException:
#     print("iptBtnEm 요소가 없습니다. 백업받기/올리기로 이동합니다.")
#     WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.LINK_TEXT, '백업받기/올리기')))
#     backup_link = driver.find_element(By.LINK_TEXT, '백업받기/올리기')
#     backup_link.click()
#     print(f'{backup_link} 클릭')

#     radio_btn=driver.find_element(By.NAME,'mssqlDbIdx')
#     radio_btn.click()
#     call_DB=driver.find_element(By.ID,'btnBackup')
#     call_DB.click()
#     print(f'{call_DB} 성공')

# # pass_btn = driver.find_element(By.ID, 'iptBtnEm')  
# # pass_btn.click()
# # print(f'{pass_btn} 다음에 변경')

# print(f'20분 대기')
# time.sleep(1000)
# #========================================
# #===============FTP exe 실행=================
# #========================================

# print(f'파일질러 실행')
# subprocess.Popen(["C:\\Program Files\\FileZilla FTP Client\\filezilla.exe"])
