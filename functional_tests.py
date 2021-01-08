from selenium import webdriver

browser = webdriver.Chrome()
browser.get('http://localhost:8000')

assert 'To-Do' in browser.title

# Invited to enter a to-do item right away

#Types in "Buy peacock feathers" in to a text box

#When she hits enter the page updates and the item is added to the list
# "1. Buy peacock feathers" as an item in the list

# Enters "Use peacock feathers to make a fly"

# The page updates again, and now shows both items on her list

#Unique URL generated for the list

# Vist unique url

browser.quit()