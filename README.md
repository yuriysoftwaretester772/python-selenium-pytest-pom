# pytest_selenium_pom
![Test Status](https://github.com/yuriysoftwaretester772/python-selenium-pytest-pom/actions/workflows/python-tests.yml/badge.svg)

This is a simple example of test scripts written using **Python**, **Selenium WebDriver**, **PyTest**
and **Allure**. 
This framework is utilizing Page Object Model (POM). 
conftest.py includes code to use specific chromedriver version based on your Operating System.
webdriver-manager is used to manage drivers for Chrome, Firefox and Edge.

**Pre-requisites:**

Please make sure you have **Python** installed https://www.python.org/downloads/

Please make sure you have **PyCharm** installed https://www.jetbrains.com/pycharm/download/

Please make sure you have **Git** installed https://git-scm.com/downloads

Please make sure you have **Allure** installed https://docs.qameta.io/allure/
To install **Allure** please use the following steps:

For Windows users:
1. Install scoop https://scoop.sh/
2. Execute **scoop install allure** in the powershell

For mac OS users:
1. Install Homebrew https://brew.sh/
2. Execute **brew install allure** in the terminal

mac OS users: 
Please make sure you have **pip** installed https://pip.pypa.io/en/stable/installing/
1. Right click on get-pip.py and select "save link as". Save get-pip.py somewhere on your computer (for example Downloads folder)
2. Open terminal, navigate to Downloads folder (cd Downloads) and execute **python3 get-pip.py**

**How to Install Dependencies:**

To install all the required dependencies for this project, run the following command in your terminal:

```bash
pip install -r requirements.txt
```

This will ensure that all necessary Python packages and their versions are installed in your environment.

**How to run your tests:**
### How to Run Tests in Different Browsers

You can run the tests in different browsers (Chrome, Firefox, Edge) and in headless mode using the command line or terminal. Below are the instructions:

#### Run Tests in Chrome (Default Browser)
```bash
pytest
```

#### Run Tests in Firefox
```bash
pytest --browser=firefox
```

#### Run Tests in Edge
```bash
pytest --browser=edge
```

#### Run Tests in Headless Mode
To run tests in headless mode, add the `--headless` flag:
- **Chrome (Headless)**:
  ```bash
  pytest --headless
  ```
- **Firefox (Headless)**:
  ```bash
  pytest --browser=firefox --headless
  ```
- **Edge (Headless)**:
  ```bash
  pytest --browser=edge --headless
  ```

#### Run Specific Test Markers
To run tests with specific markers (e.g., `regressiontest`):
```bash
pytest -m regressiontest
```

#### Generate Allure Reports
After running the tests, you can generate and view Allure reports:
```bash
allure serve reports
```

**How to run your tests (alternative):**
 
1. Open your PyCharm
2. Navigate to VCS - Git - Clone and paste repository URL 
3. Select "New Window" option.
4. Click on "Terminal" at the bottom of the page
5. For Windows users, type in **pip install pipenv** and press Enter
6. For mac OS users, type in **pip3 install pipenv** and press Enter
7. Type in **pipenv install selenium** and press Enter
8. Type in **pipenv install pytest** and press Enter
9. Type in **pipenv install allure-pytest** and press Enter

Navigate to "Edit Configurations.." at the top right of the PyCharm

Click on "+" (Add New Configuration). Select pytest as on the screenshot below.

[![Screen-Shot-2020-09-10-at-4-51-00-PM.png](https://i.postimg.cc/MGR6V9QM/Screen-Shot-2020-09-10-at-4-51-00-PM.png)](https://postimg.cc/CZhpVHJS)

Your configuration should look similar to this one (use smoketest OR regressiontest):

[![Screen-Shot-2020-09-10-at-5-28-23-PM.png](https://i.postimg.cc/d3mfRysK/Screen-Shot-2020-09-10-at-5-28-23-PM.png)](https://postimg.cc/Zvnj40vf)

After you will run your test(s). 
To generate Allure reports and open them in the browser:

Windows users please do right click on run_reports_win.bat and run
mac OS users please do right click on run_reports_mac.sh and run

It will automatically execute "allure serve reports" command and your Allure Report will open in the default browser

[![Screen-Shot-2020-09-10-at-5-30-20-PM.png](https://i.postimg.cc/CLrN3N6Q/Screen-Shot-2020-09-10-at-5-30-20-PM.png)](https://postimg.cc/kB8K8xCQ)

To stop executing "allure serve reports" command, press Ctrl + C in your PyCharm terminal.
