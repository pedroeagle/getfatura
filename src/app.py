from flask import Flask, request, render_template, url_for #import main Flask class and request object
from bs4 import BeautifulSoup
import requests
import re
import os
import base64
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time
def create_browser(webdriver_path):
    #create a selenium object that mimics the browser
    browser_options = Options()
    #headless tag created an invisible browser
    browser_options.add_argument("--headless")
    browser_options.add_argument('--no-sandbox')
    print(os.path.abspath(os.path.curdir)+webdriver_path)
    print(str(os.path.isfile(os.path.abspath(os.path.curdir)+webdriver_path)))
    browser = webdriver.Chrome(os.path.abspath(os.path.curdir)+webdriver_path, options=browser_options)
    print("Done Creating Browser")
    return browser

app = Flask(__name__) #create the Flask app
@app.route('/', methods=['GET'])
def get():
    driver = webdriver.Chrome(executable_path=os.path.abspath(os.path.curdir)+'/chromedriver')
    #browser = create_browser('/chromedriver') #DON'T FORGET TO CHANGE THIS AS YOUR DIRECTORY
    return "Teste"



if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port, debug=True)