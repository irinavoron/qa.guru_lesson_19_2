from selene import browser, have
from appium.webdriver.common.appiumby import AppiumBy
import allure


def search(article_title):
    with allure.step('Enter a value into the search field'):
        browser.element((AppiumBy.ACCESSIBILITY_ID, "Search Wikipedia")).click()
        browser.element((AppiumBy.ID, "org.wikipedia.alpha:id/search_src_text")).type(article_title)


def test_search():
    search('Guru')

    with allure.step('Verify the search results'):
        results = browser.all((AppiumBy.ID, 'org.wikipedia.alpha:id/page_list_item_title'))
        results.should(have.size_greater_than(0))
        results.first.should(have.text('Guru'))


def test_open_first_article():
    search('Guru')
    with allure.step('Open the first article'):
        browser.all((AppiumBy.ID, 'org.wikipedia.alpha:id/page_list_item_title')).first.click()
