from bs4.element import SoupStrainer
import requests
from bs4 import BeautifulSoup as bs

def get_profile_img(username):
    url = f"http://github.com/{username}"
    res = requests.get(url)
    soup = bs(res.content, 'lxml')
    profile_img = soup.select('img.avatar.avatar-user')[0]['src']
    return profile_img

if __name__ == '__main__':
    github_username = input("Enter GutHub username: ")
    print(get_profile_img(github_username))