from webbot import Browser
import time

web = Browser()
web.go_to('https://www.youtube.com/')
web.type('YouThinker' , into='Search' , id='search.ytd-searchbox')
web.press(web.Key.ENTER)
web.click('YOU THINKER')
web.click('CHRISTMAS DAY')
