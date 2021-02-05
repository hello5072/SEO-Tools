import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def get_image_title(url):
    # 웹 드라이버 초기화 Change the driver path if necessary
    driver_path = 'C:/Users/brian.yang/Desktop/Brian/chromedriver'
    driver = webdriver.Chrome(driver_path)
    driver.implicitly_wait(5)  # or bigger second

    # 열고자 하는 채널 -> 동영상 목록으로 된 url 페이지를 엶
    driver.get(url)

    # 타이틀 리스트 저장
    title_list = list()
    #  뷰카운트 리스트 저장
    view_list = list ()

    idx = 1
    while True:
        try:
            title_xpath = '/html/body/ytd-app/div/ytd-page-manager/ytd-browse/ytd-two-column-browse-results-renderer/div[1]/ytd-section-list-renderer/div[2]/ytd-item-section-renderer/div[3]/ytd-grid-renderer/div[1]/ytd-grid-video-renderer[' + str(idx) + ']/div[1]/div[1]/div[1]/h3/a'
            view_xpath = '/html/body/ytd-app/div/ytd-page-manager/ytd-browse/ytd-two-column-browse-results-renderer/div[1]/ytd-section-list-renderer/div[2]/ytd-item-section-renderer/div[3]/ytd-grid-renderer/div[1]/ytd-grid-video-renderer[' + str(idx) + ']/div[1]/div[1]/div[1]/div/div[1]/div[2]/span[1]'
            date_xpath = '/html/body/ytd-app/div/ytd-page-manager/ytd-browse/ytd-two-column-browse-results-renderer/div[1]/ytd-section-list-renderer/div[2]/ytd-item-section-renderer/div[3]/ytd-grid-renderer/div[1]/ytd-grid-video-renderer[' + str(idx) + ']/div[1]/div[1]/div[1]/div/div[1]/div[2]/span[2]'

            # 이미지가 곧바로 로드 되지 않을 때, 20초간 강제로 기다림
            # img = WebDriverWait(driver, 15).until(EC.presence_of_all_elements_located((By.XPATH, img_xpath)))

            title_ready = WebDriverWait(driver, 15).until(EC.presence_of_all_elements_located((By.XPATH, title_xpath)))
            if title_ready is None:
                print(idx, 'video not loaded')

            # 한 페이지에 약 8개 불러오는 데, 동영상 목록을 추가 불러오기 위해 스크롤 내림
            if idx % 8 == 0:
                driver.execute_script('window.scrollBy(0, 1080);')
                time.sleep(2)
                driver.execute_script('window.scrollBy(0, 1080);')
                time.sleep(2)
                driver.execute_script('window.scrollBy(0, 1080);')
                time.sleep(2)

            # 타이틀을 리스트에 저장
            title = driver.find_element_by_xpath(title_xpath)
            title_url = title.get_attribute('href')

            # 뷰카운트를 가져오기
            view = driver.find_element_by_xpath(view_xpath)
            view_list.append(view)

            # 업데이트 오래된 정도 가져오기
            date = driver.find_element_by_xpath(date_xpath)

            # 결과물 출력
            print(idx,"\t", title.text,"\t", view.text,"\t", date.text,"\t", title_url)
            title_list.append(title.text)

            idx += 1
        except Exception as e:
            print()
            print(e)
            break
    assert len(view_list) == len(title_list)
    driver.close()
    return view_list, title_list

# url1 = 'https://www.youtube.com/channel/UCSGC87iX0QhnIfUOI_B_Rdg/videos'
url1 = input("type in URL")
image1, title1 = get_image_title(url1)
