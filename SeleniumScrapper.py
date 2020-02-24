#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
import time
import re
import csv
import codecs


def click_botton(url):
    browser.get(url)
    botton_str = "ipl-load-more__button"
    # click all
    js = "let reviewList = document.getElementsByClassName('content'); for(let review of reviewList){review.style['max-height'] = 'none'}"

    # 点击按钮
    # i = 0
    while (True):
        s = browser.find_element_by_class_name(botton_str)
        try:
            s.click()
            time.sleep(3)
            # i = i + 1
        except:
            break

    browser.execute_script(js)


def get_comment():
    all_str = "lister-item-content"
    # 每个影评是一块
    elements = browser.find_elements_by_class_name(all_str)
    headers = ['title', 'rate', 'author', 'date', 'content']

    # 改文件名
    with open('FILE NAME TO SAVE.CSV', 'a+', newline='') as f:
        f_csv = csv.writer(f)
        f_csv.writerow(headers)
    tmp = []
    for div in elements:
        try:
            title = div.find_element_by_class_name('title').text
            rate = div.find_element_by_class_name('ipl-ratings-bar').text
            name = div.find_element_by_class_name('display-name-link').text
            date = div.find_element_by_class_name('review-date').text
            content = div.find_element_by_class_name('content').text
            tmp = [title, rate, name, date, content]
            # 改文件名
            with open('FILE NAME TO SAVE.CSV', 'a+', newline='') as f:
                f_csv = csv.writer(f)
                f_csv.writerow(tmp)
        except:
            pass


if __name__ == "__main__":
    # 这里改webdriver的下载路径
    browser = webdriver.Chrome()

    # 这里改电影影评的url
    url = "IMDB COMMENT PAGE URL HERE"
    click_botton(url)
    get_comment()
