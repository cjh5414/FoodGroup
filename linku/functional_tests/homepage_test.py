import sys
import os
from selenium import webdriver
import pytest


@pytest.fixture(scope="module")
def browser():
    if sys.platform == 'darwin':
        project_root = os.path.dirname(os.path.dirname(
            os.path.realpath(__file__)))
        repo_root = os.path.dirname(project_root)
        sys.path.append(os.path.join(repo_root, 'dev'))
        import download_chromedriver
        download_chromedriver.download()
        chrome_path = download_chromedriver.get_chromedriver_path()
        if chrome_path is False:
            raise SystemExit
        driver = webdriver.Chrome(chrome_path)
    else:
        driver = webdriver.Firefox()
    yield driver
    driver.close()


def test_first_page_cards_title(browser):
    # 평소 짱구는 요즘 새로운 사람을 만나고 싶어서 우리 서비스에 접속했다.
    # 서비스에 접속하니
    browser.get("http://localhost:8000")

    # 첫 화면에는 모임에 대한 정보가 보이는 카드들이 보였다.

    # 그 카드 중 하나를 자세히 살펴보니 맨 상단에는 규카츠 먹을래? 제목이 보여졌고,
    assert '규카츠 먹을래?' in browser.page_source

    # 그 아래에는 장선혁(개설자 이름)
    assert '장선혁' in browser.page_source

    # 강남(장소)
    assert '강남' in browser.page_source

    # 02/22 21:52 (시작 시간)
    assert '02/22 21:52' in browser.page_source

    # 규카츠가 맛있게 보이는 사진
    # 고려대학교 10km 이내(가까운 대학교와의 거리)
    assert '고려대학교 10km 이내' in browser.page_source

    # 5,000원~10,000원(가격대)
    assert '5,000원~10,000원' in browser.page_source

    # 그리고 신청하기 버튼이 카드 가장 하단에 있어서,
    # 한번 눌러보고 싶은 충동이 생겼다.

    # 그 바로 하단에는 선이 그어져 있어서 왠지 서로 구분이 되는 느낌이다
    browser.find_element_by_tag_name('hr')

    # 맨 상단에는 호타루에서 우동 먹을래? 제목이 보여졌고,
    assert '호타루에서 우동 먹을래?' in browser.page_source
    # 그 아래에는 최지훈(개설자 이름)
    assert '최지훈' in browser.page_source
    # 이대(장소)
    assert '이대' in browser.page_source
    # 02/22 22:22 (시작 시간)
    assert '02/22 22:22' in browser.page_source
    # 우동이 맛깔스럽게 보이는 사진
    # 이화여자대학교 10km 이내(가까운 대학교와의 거리)
    assert '이화여자대학교 10km 이내' in browser.page_source
    # 5,000원~10,000원(가격대)
    assert '5,000원~10,000원' in browser.page_source
    # 들이 보여졌다.
