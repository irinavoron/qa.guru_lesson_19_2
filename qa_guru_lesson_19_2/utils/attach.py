import allure
from selene import browser
from allure_commons.types import AttachmentType
import requests

from config import config


def add_screenshot():
    png = browser.driver.get_screenshot_as_png()
    allure.attach(
        body=png,
        name='screenshot',
        attachment_type=AttachmentType.PNG,
        extension='.png'
    )


def add_xml():
    xml = browser.driver.page_source
    allure.attach(
        body=xml,
        name='xml',
        attachment_type=AttachmentType.XML,
        extension='.xml'
    )


def add_video(session_id):
    bs_session = requests.get(
        url=f'https://api.browserstack.com/app-automate/sessions/{session_id}.json',
        auth=(config.BS_USER, config.BS_ACCESS_KEY)
    ).json()

    video_url = bs_session['automation_session']['video_url']
    html = "<html><body><video width='100%' height='100%' controls autoplay><source src='" \
           + video_url \
           + "' type='video/mp4'></video></body></html>"
    allure.attach(
        body=html,
        name='video',
        attachment_type=AttachmentType.HTML,
        extension='.html'
    )
