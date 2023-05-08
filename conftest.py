from datetime import datetime
from pathlib import Path

import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager


#UrlMA = "https://www.mercantilandina.com.ar/"
#UrlMA = "https://www.mercantilandina.com.ar/"


@pytest.fixture(scope="class", autouse=True)
def browser_setup(request):
    chrome_options = Options()
    chrome_options.add_argument('--incognito')
    chrome_options.add_argument('--start-maximized')
    request.cls.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=chrome_options)

@pytest.hookimpl(tryfirst=True)
def pytest_configure(config):
    today = datetime.now()
    report_path = Path("report", today.strftime("%Y%m%d"))
    report_path.mkdir(parents=True, exist_ok=True)
    pytest_html = report_path / f"Report_{today.strftime('%Y%m%d%H%M')}.html"
    config.option.htmlpath = pytest_html
    config.option.self_contained_html = True

def pytest_html_report_title(report):
    report.title = "Mercantil Andina Challenge"