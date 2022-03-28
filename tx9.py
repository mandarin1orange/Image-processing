from PIL import Image
from PIL import ImageEnhance

def main():
    im1 = Image.open('./1.jpg')

    # 亮度调整
    img_color = ImageEnhance.Brightness(im1)
    image1 = img_color.enhance(1.6)
    image1.show()

    pass

if __name__ == '__main__':
    main()