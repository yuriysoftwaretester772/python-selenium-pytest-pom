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
logging.basicConfig(level=logging.DEBUG)  # Change to DEBUG for more verbosity
logger = logging.getLogger(__name__)


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
    browser_name = request.config.getoption("--browser").lower()
    headless = request.config.getoption("--headless")
    logger.debug(f"Browser: {browser_name}, Headless: {headless}")

    try:
        if browser_name == "chrome":
            logger.debug("Setting up Chrome options")
            options = webdriver.ChromeOptions()
            options.add_argument("--disable-extensions")
            options.add_argument("--disable-gpu")
            options.add_argument("--no-sandbox")
            options.add_argument("--disable-dev-shm-usage")
            options.add_argument("--disable-notifications")
            if headless:
                options.add_argument("--headless=new")
            logger.debug("Downloading ChromeDriver")
            service = ChromeService(ChromeDriverManager().install())
            logger.debug("Initializing Chrome WebDriver")
            driver = webdriver.Chrome(service=service, options=options)
            logger.info("Initialized Chrome browser")

        elif browser_name == "firefox":
            logger.debug("Setting up Firefox options")
            options = webdriver.FirefoxOptions()
            options.add_argument("--disable-extensions")
            options.add_argument("--disable-notifications")
            if headless:
                options.add_argument("--headless")
            logger.debug("Downloading GeckoDriver")
            service = FirefoxService(GeckoDriverManager().install())
            logger.debug("Initializing Firefox WebDriver")
            driver = webdriver.Firefox(service=service, options=options)
            logger.info("Initialized Firefox browser")

        elif browser_name == "edge":
            logger.debug("Setting up Edge options")
            options = webdriver.EdgeOptions()
            options.add_argument("--disable-extensions")
            options.add_argument("--disable-gpu")
            options.add_argument("--no-sandbox")
            options.add_argument("--disable-notifications")
            if headless:
                options.add_argument("--headless=new")
            logger.debug("Downloading EdgeDriver")
            service = EdgeService(EdgeChromiumDriverManager().install())
            logger.debug("Initializing Edge WebDriver")
            driver = webdriver.Edge(service=service, options=options)
            logger.info("Initialized Edge browser")

        else:
            logger.error(f"Unsupported browser: {browser_name}")
            raise ValueError(f"Unsupported browser: {browser_name}")

        logger.debug("Setting timeouts")
        driver.set_page_load_timeout(30)
        driver.implicitly_wait(5)

        logger.debug("Maximizing window")
        driver.maximize_window()

        yield driver

        logger.debug("Taking screenshot for Allure")
        try:
            allure.attach(
                driver.get_screenshot_as_png(),
                name="Screenshot",
                attachment_type=AttachmentType.PNG
            )
        except Exception as e:
            logger.warning(f"Failed to capture screenshot: {e}")

        logger.debug("Closing browser")
        try:
            driver.quit()
            logger.info(f"Closed {browser_name} browser")
        except Exception as e:
            logger.error(f"Error closing browser: {e}")

    except Exception as e:
        logger.error(f"Failed to initialize browser: {e}")
        raise