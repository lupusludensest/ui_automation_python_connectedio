import os

from dotenv import load_dotenv
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait

from app.application import Application

load_dotenv()


def browser_init(context):
    """
    :param context: Behave context
    """
    options = webdriver.ChromeOptions()
    if os.environ.get("HEADLESS", "").lower() in {"1", "true", "yes"}:
        options.add_argument("--headless=new")
    context.driver = webdriver.Chrome(options=options)

    context.driver.maximize_window()
    context.driver.implicitly_wait(4)
    context.driver.wait = WebDriverWait(context.driver, 15)

    context.app = Application(context.driver)


def before_scenario(context, scenario):
    print('\nStarted scenario: ', scenario.name, '.')
    browser_init(context)


def before_step(context, step):
    print('\nStarted step: ', step, '.')


def after_step(context, step):
    if step.status == 'failed':
        print('\nStep failed: ', step, '.')


def after_scenario(context, feature):
    context.driver.delete_all_cookies()
    context.driver.quit()
    print('\nTest done: ', feature, '!')