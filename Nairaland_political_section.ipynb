{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "3ab99518",
   "metadata": {},
   "outputs": [],
   "source": [
    "from bs4 import BeautifulSoup\n",
    "import requests\n",
    "import pandas as pd\n",
    "import numpy as np\n",
    "url = \"https://www.nairaland.com/politics\"\n",
    "links = []\n",
    "for i in range(0,10):\n",
    "    if i == 0:\n",
    "        url_page = url\n",
    "    else:\n",
    "        url_page = str(url) + \"/{}\".format(i)\n",
    "    try:\n",
    "        page = requests.get(url_page).text\n",
    "    except:\n",
    "        pass\n",
    "    soup = BeautifulSoup(page,\"lxml\")\n",
    "    # post = soup.find('body')\n",
    "    url_links = soup.find_all('a')\n",
    "    for url in url_links:\n",
    "        if url.has_attr(\"href\") and url[\"href\"].startswith(\"http\"):\n",
    "            links.append(url[\"href\"])\n",
    "posts = []\n",
    "posts_link= []\n",
    "\n",
    "for link in links:\n",
    "    try:\n",
    "        page = requests.get(link).text\n",
    "    except:\n",
    "        pass\n",
    "    soup = BeautifulSoup(page,\"lxml\")\n",
    "\n",
    "    for comment in soup.find_all(\"div\", class_=\"narrow\"):\n",
    "        posts.append(comment.text)\n",
    "        posts_link.append(link)\n",
    "\n",
    "df=pd.DataFrame({\"Comments\": posts, \"links\":posts_link})\n",
    "df.to_csv('Nairaland_df.csv')"
   ]
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.8.8"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
