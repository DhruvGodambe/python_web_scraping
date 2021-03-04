import requests
from lxml import html
import shutil

webPageLink = "https://unsplash.com/"

page = requests.get(webPageLink)
extractedHtml = html.fromstring(page.content)
imageSrc = extractedHtml.xpath("//img/@src")

for image in imageSrc:
    imageType = image.split(".com/")
    if len(imageType) > 1:
        if imageType[1].find("photo") != -1:
            if len(imageType[1].split("-")) > 1:
                filename = "photo-" + imageType[1].split("-")[1] + '.jpg'
            r = requests.get(image, stream = True)

            if r.status_code == 200:
                r.raw.decode_content = True

                with open(filename, 'wb') as f:
                    shutil.copyfileobj(r.raw, f)

                    print(" Image successfully downloaded ", filename)
            else:
                print("could not download image", filename)