import requests
import urllib.request
from bs4 import BeautifulSoup

url = "https://solved.ac/profile/march381"
res = requests.get(url)
res.raise_for_status()

soup = BeautifulSoup(res.text, "lxml")
name = soup.find(attrs={"class":"ProfileHeaderCardstyles__UserinfoName-wboshd-2 DZXqi"}).text
rank_img_url = soup.find(attrs={"class":"ClassIconInline__ClassIconStyle-hichg2-0 byIFSy"})["src"]

urllib.request.urlretrieve(rank_img_url, 'rank.svg')

rating = soup.find(attrs={"class":"ProfileRatingCard__AcRatingDisplay-sc-989yd6-0 jaNtBE"})
rating_num = rating.text
rating_tier = rating.next_sibling.text

print(name)
print(rating_num + rating_tier)