#!/usr/bin/env python
# coding: utf-8

# In[29]:


get_ipython().system('pip install bs4')
get_ipython().system('pip install requests')
get_ipython().system('pip install html5lib')


# In[2]:


Page = requests.get("https://bookpage.com/reviews")
Page


# In[3]:


Page.content


# In[5]:


soup = BeautifulSoup(Page.content)
soup


# In[44]:


first_title=soup.find('div',class_="article-list-left")
first_title


# In[48]:


first_title.text


# In[63]:


first_author=soup.find('div',class_="flex-article-content")
first_author


# In[64]:


first_author.text


# In[123]:


first_genre=soup.find('div',class_="bp-block article-info")
first_genre


# In[66]:


first_genre.text


# In[67]:


first_review=soup.find('div',class_="row-fluid article-row")
first_review


# In[68]:


first_review.text


# In[72]:


titles=soup.find_all('div',class_="article-list-left")
titles


# In[76]:


book_titles=[]
for i in titles:
    book_titles.append (i.text)
book_titles


# In[77]:


book_titles=[]
for i in titles:
    book_titles.append(i.text.replace("\n",''))
book_titles


# In[78]:


len(book_titles)


# In[105]:


authors=soup.find_all('div',class_="flex-article-content")
authors


# In[106]:


book_authors=[]
for i in authors:
    book_authors.append (i.text)
book_authors


# In[107]:


book_authors=[]     
for i in titles:
    book_authors.append(i.text.replace("\n",''))
book_authors     


# In[110]:


len(book_authors)


# In[124]:


genres=soup.find.all('div',class_="bp-block article-info")
genres


# In[112]:


book_genres=[]
for i in titles:
    book_genres.append(i.text.strip())
book_genres


# In[113]:


book_genres=[]
for i in titles:
    book_genres.append(i.text.replace("\n",''))
book_genres


# In[115]:


reviews=soup.find.all('div',class_="row-fluid article-row")
reviews


# review_titles=
# for i in titles:
#     review_titles.append(i.text)
# review_titles

# In[116]:


book_reviews=[]
for i in titles:
    book_reviews.append(i.text.replace("\n",''))
book_reviews


# In[118]:


import pandas as pd
books=pd.DataFrame({})
books['title']=book_titles
books['author']=book_authors
books['genre']=book_genres
books['review']=book_reviews


# In[119]:


books


# In[ ]:




