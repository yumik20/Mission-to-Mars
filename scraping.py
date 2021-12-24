#!/usr/bin/env python
# coding: utf-8

# In[23]:


from splinter import Browser
from bs4 import BeautifulSoup as soup
import pandas as pd
from webdriver_manager.chrome import ChromeDriverManager


# In[2]:


# Set up Splinter
executable_path = {'executable_path': ChromeDriverManager().install()}
browser = Browser('chrome', **executable_path, headless=False)


# In[3]:


# Visit the Quotes to Scrape site
url = 'http://quotes.toscrape.com'
browser.visit(url)


# In[4]:


# Parse the HTML
html = browser.html
html_soup = soup(html, 'html.parser')


# In[5]:


# Scrape the Title
title = html_soup.find('h2').text
title


# In[6]:


# Scrape the top ten tags
tag_box = html_soup.find('div', class_='tags-box')
# tag_box
tags = tag_box.find_all('a', class_='tag')

for tag in tags:
    word = tag.text
    print(word)


# In[7]:


# Import Splinter and BeautifulSoup
from splinter import Browser
from bs4 import BeautifulSoup as soup
from webdriver_manager.chrome import ChromeDriverManager


# In[8]:


executable_path = {'executable_path': ChromeDriverManager().install()}
browser = Browser('chrome', **executable_path, headless=False)


# In[9]:


# Visit the mars nasa news site
url = 'https://redplanetscience.com'
browser.visit(url)
# Optional delay for loading the page
browser.is_element_present_by_css('div.list_text', wait_time=1)


# In[10]:


html = browser.html
news_soup = soup(html, 'html.parser')
slide_elem = news_soup.select_one('div.list_text')
slide_elem.find('div', class_='content_title')


# In[11]:


# Use the parent element to find the first `a` tag and save it as `news_title`
news_title = slide_elem.find('div', class_='content_title').get_text()
news_title


# In[12]:


# Use the parent element to find the paragraph text
news_p = slide_elem.find('div', class_='article_teaser_body').get_text()
news_p


# In[13]:


# Visit URL
url = 'https://spaceimages-mars.com'
browser.visit(url)


# In[14]:


# Find and click the full image button
full_image_elem = browser.find_by_tag('button')[1]
full_image_elem.click()


# In[15]:


# Parse the resulting html with soup
html = browser.html
img_soup = soup(html, 'html.parser')


# In[16]:


# Find the relative image url
img_url_rel = img_soup.find('img', class_='fancybox-image').get('src')
img_url_rel


# In[17]:


# Use the base URL to create an absolute URL
img_url = f'https://spaceimages-mars.com/{img_url_rel}'
img_url


# In[24]:


df = pd.read_html('https://galaxyfacts-mars.com')[0]
df.head()


# In[25]:


df.columns=['description', 'Mars', 'Earth']
df.set_index('description', inplace=True)
df


# In[26]:


df.to_html()


# In[27]:


browser.quit()


# In[ ]:




