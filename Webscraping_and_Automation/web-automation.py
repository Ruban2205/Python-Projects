from webbot import Browser
import time

web = Browser()
web.go_to('https://www.rubangino.in/')
web.click('ABOUT')
web.click('SKILLS')
web.click('PORTFOLIO')
web.go_to('https://www.rubangino.in/android-app.html')
