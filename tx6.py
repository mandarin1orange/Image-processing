from PIL import Image
from PIL import ImageFilter

def main():

    im1 = Image.open('./1.jpg')

    # 高斯模糊
    im1.filter(ImageFilter.GaussianBlur).show()

    pass

if __name__ == '__main__':
    main()