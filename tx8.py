from PIL import Image
from PIL import ImageEnhance

def main():

    im1 = Image.open('./1.jpg')

    w,h = im1.size
    # 设置新的图片，宽度为3张原图
    image_output = Image.new('RGBA',((3*w),h))
    # 第一个放原图
    image_output.paste(im1,(0,0))

    # 第二个放增强的图
    img_color = ImageEnhance.Color(im1)
    # 把图片增强
    imga = img_color.enhance(1.5)
    image_output.paste(imga,(w,0))

    # 第三个放减弱的图
    imgb = img_color.enhance(0.5)
    image_output.paste(imgb, (2*w, 0))

    image_output.show()

    pass

if __name__ == '__main__':
    main()