from bs4 import BeautifulSoup
import os
import requests

url = "https://www.gutenberg.org/cache/epub/58585/pg58585-images.html"

data = requests.get(url)
print(data.status_code)

soup = BeautifulSoup(data.text, 'html.parser')

try:
    os.mkdir(os.path.join(os.getcwd(), "images"))
except OSError:
    print("Folder already exists")
finally:
    # changing current directory to gutenberg/images so the photos are saved in this directory
    os.chdir(os.path.join(os.getcwd(), "images"))

# get a list of all img tags
images = soup.find_all('img')

for image in images:
    # pick out all 'alt' and 'src' in image tag
    # image['alt']
    file_name = image['src'][7:]
    # print(image['src'][7:])
    img_source = "https://www.gutenberg.org/cache/epub/58585/images/" + image['src'][7:]

    with open(file_name, 'wb') as fp:
        img = requests.get(img_source)
        fp.write(img.content)




#for html 1
# img_source = "https://www.gutenberg.org/cache/epub/394/images/" + image['src'][7:]

#for html 3
#img_source = "https://www.gutenberg.org/files/236/236-h/" + image['src']