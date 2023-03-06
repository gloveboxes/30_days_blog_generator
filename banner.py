"""Create a banner image with text and profile image"""

from io import BytesIO
import string
import os
import platform
from PIL import Image, ImageDraw, ImageFont, ImageOps
import requests
import oyaml as yaml


class BANNER:
    """Load YAML file"""

    def __init__(self, file_path, blog_url):
        self.blog_url = blog_url

        self.font_folder = '/System/Library/Fonts/Supplemental'
        self.font_name = 'Verdana.ttf'
        self.font_bold_name = 'Verdana Bold.ttf'

        if platform.system() == 'Windows':
            self.font_folder = 'C:\\Windows\\Fonts'
            self.font_name = 'verdana.ttf'
            self.font_bold_name = 'verdanab.ttf'

        if platform.system() == 'Linux':
            self.font_folder = '/usr/share/fonts/truetype/dejavu'
            self.font_name = 'DejaVuSans.ttf'
            self.font_bold_name = 'DejaVuSans-Bold.ttf'

        with open(file_path, "r", encoding="utf8") as f:
            self.authors = yaml.load(f, Loader=yaml.Loader)

    def __get_image_circle(self, url):
        """Get image from URL and convert to circle"""

        try:
            response = requests.get(url, timeout=10)
            response.raise_for_status()  # Raise an HTTPError if status code >= 400
        except BaseException as error:
            raise Exception("Failed to fetch image: " + str(error))

        image = Image.open(BytesIO(response.content))

        size = image.size
        mask = Image.new('L', size, 0)
        draw = ImageDraw.Draw(mask)
        draw.ellipse((0, 0) + size, fill=255)
        output = ImageOps.fit(image, mask.size, centering=(0.5, 0.5))
        output.putalpha(mask)

        # # Resize image to 100x100 px
        return output.resize((60, 60))

    def __add_banner_text(self, draw, audience, title, day):
        """Add text to the banner image"""
        # Define the font size and font type
        font = ImageFont.truetype(os.path.join(self.font_folder, self.font_bold_name), 40)
        
        printable = set(string.printable)
        audience = ''.join(filter(lambda x: x in printable, audience))
        title = ''.join(filter(lambda x: x in printable, title))

        # Draw the text on the image
        draw.text((130, 60), audience, font=font, fill=(127, 127, 127))
        draw.text((36, 76), "{:2d}".format(day), font=font, fill=(127, 127, 127))
        draw.text((100, 74), "|", font=font, fill=(127, 127, 127))

        font = ImageFont.truetype(os.path.join(self.font_folder, self.font_bold_name), 24)
        draw.text((130, 112), title, font=font, fill=(111, 61, 212))

        font = ImageFont.truetype(os.path.join(self.font_folder, self.font_name), 14)
        draw.text((640, 6), self.blog_url, font=font, fill=(127, 127, 127))

    def __add_profile_image(self, img, draw, item, name, tag, image_url):
        """Add profile image to the banner image"""
        name_loc = [(204, 170), (204, 240)]
        tag_loc = [(204, 190), (204, 260)]
        image_loc = [(130, 160), (130, 230)]

        if item > len(name_loc) - 1:
            return

        font = ImageFont.truetype(os.path.join(self.font_folder, self.font_name), 15)
        draw.text(name_loc[item], name, font=font, fill=(127, 127, 127))
        draw.text(tag_loc[item], tag, font=font, fill=(127, 127, 127))

        try:
            output = self.__get_image_circle(image_url)
            img.paste(output, image_loc[item], output)
        except BaseException as e:
            print(e)

    def __add_keyword_image(self, img, draw, keywords):
        """Add keyword image to the banner image"""
        keyword_loc = [(450, 160), (530, 160), (610, 160), (690, 160), (450, 230), (530, 230), (610, 230), (690, 230)]
        keyword_count = 0
        for keyword in keywords:

            if keyword_count > len(keyword_loc) - 1:
                break

            filename = 'assets/icons/' + keyword + '.png'
            if os.path.exists(filename):
                keyword_img = Image.open(filename)
                img.paste(keyword_img, keyword_loc[keyword_count], keyword_img)
                keyword_count += 1 
            else:
                print("Keyword image not found: " + filename)


    def create_banner(self, banner_definition):
        """Create the banner image"""

        img = Image.open('assets/banner.png')
        draw = ImageDraw.Draw(img)
        item = 0

        self.__add_banner_text(draw, banner_definition["audience"], banner_definition["title"], banner_definition["day"])
        self.__add_keyword_image(img, draw, banner_definition["keywords"])
        for author in banner_definition["authors"]:
            author_item = self.authors.get(author)

            if not author_item:
                continue

            self.__add_profile_image(img, draw, item, author_item["name"], author_item["tag"], author_item["image_url"])
            item += 1

        filename = os.path.join(banner_definition["folder"], 'banner.png')
        img.save(filename)
