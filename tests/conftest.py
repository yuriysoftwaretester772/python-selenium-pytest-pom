import os
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.firefox.service import Service as FirefoxService
from selenium.webdriver.edge.service import Service as EdgeService
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from webdriver_manager.microsoft import EdgeChromiumDriverManager
import allure
from allure_commons.types import AttachmentType
import logging

# Configure logging
logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)

USER_AGENT = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"

def pytest_addoption(parser):
    parser.addoption(
        "--browser", action="store", default="chrome",
        help="Browser to run tests: chrome, firefox, or edge"
    )
    parser.addoption(
        "--headless", action="store_true",
        help="Run browser in headless mode"
    )

@pytest.fixture()
def browser(request):
    logger.debug("Starting browser fixture setup")

    # Defaults and GitHub Actions override
    browser_name = request.config.getoption("--browser") or "chrome"
    headless = request.config.getoption("--headless")
    if os.getenv("GITHUB_ACTIONS") == "true":
        logger.debug("Running in GitHub Actions — forcing headless mode")
        headless = True

    logger.debug(f"Browser: {browser_name}, Headless: {headless}")

    try:
        if browser_name == "chrome":
            options = webdriver.ChromeOptions()
            options.add_argument(f"user-agent={USER_AGENT}")
            options.add_argument("--disable-extensions")
            options.add_argument("--disable-gpu")
            options.add_argument("--no-sandbox")
            options.add_argument("--disable-dev-shm-usage")
            options.add_argument("--disable-notifications")
            options.add_argument("--window-size=1920,1080")
            if headless:
                options.add_argument("--headless=new")

            service = ChromeService(ChromeDriverManager().install())
            driver = webdriver.Chrome(service=service, options=options)
            logger.info("Initialized Chrome browser")

        elif browser_name == "firefox":
            options = webdriver.FirefoxOptions()
            options.set_preference("general.useragent.override", USER_AGENT)
            if headless:
                options.add_argument("--headless")

            service = FirefoxService(GeckoDriverManager().install())
            driver = webdriver.Firefox(service=service, options=options)
            logger.info("Initialized Firefox browser")

        elif browser_name == "edge":
            options = webdriver.EdgeOptions()
            options.add_argument(f"user-agent={USER_AGENT}")
            options.add_argument("--disable-extensions")
            options.add_argument("--disable-gpu")
            options.add_argument("--no-sandbox")
            options.add_argument("--disable-notifications")
            options.add_argument("--window-size=1920,1080")
            if headless:
                options.add_argument("--headless=new")

            service = EdgeService(EdgeChromiumDriverManager().install())
            driver = webdriver.Edge(service=service, options=options)
            logger.info("Initialized Edge browser")

        else:
            raise ValueError(f"Unsupported browser: {browser_name}")

        driver.set_page_load_timeout(30)
        driver.implicitly_wait(5)
        driver.maximize_window()

        yield driver

        try:
            allure.attach(
                driver.get_screenshot_as_png(),
                name="Screenshot",
                attachment_type=AttachmentType.PNG
            )
        except Exception as e:
            logger.warning(f"Failed to capture screenshot: {e}")

        driver.quit()
        logger.info(f"Closed {browser_name} browser")

    except Exception as e:
        logger.error(f"Failed to initialize browser: {e}")
        raise
