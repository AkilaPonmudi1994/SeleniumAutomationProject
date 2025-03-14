import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options

@pytest.fixture(scope="function", autouse=True)
def setup_function(request):
    print('******Function level setup*****')