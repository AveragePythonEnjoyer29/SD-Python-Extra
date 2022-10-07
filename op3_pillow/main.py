from PIL import Image, ImageFont, ImageDraw
from os.path import exists

class MyPillow(): # ;)
    def __init__(self, img):
        if not exists(img):
            raise FileNotFoundError

        self.img = Image.open(img)
        self.lettertype = ImageFont.truetype('impact.ttf', 40)
        self.canvas = ImageDraw.Draw(self.img)
    
    def draw_txt(self, msg, font=None, color=(0, 0, 0)):
        if not font:
            font = self.lettertype
        
        txt_width, txt_height = self.canvas.textsize(msg)

        text_x = ((self.img.width - txt_width) / 2) / 2
        text_y = 0 #(self.img.height - txt_height) / 2

        self.canvas.multiline_text(
            (text_x, text_y),
            msg,
            font=font,
            fill=color
        )

if __name__ == '__main__':
    pillow = MyPillow('chad.jpg')

    pillow.draw_txt(
        'Average python programmer',
        color=(255, 255, 255)
    )

    pillow.img.show()
    pillow.img.save('chad.jpg')