from selenium import webdriver
from django.core import management

browser = webdriver.Firefox()
browser.get('http://localhost:8000')


assert 'Django' in browser.title
