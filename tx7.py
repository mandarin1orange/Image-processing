from PIL import Image
from PIL import ImageChops

def main():

    im1 = Image.open('./1.jpg')
    im2 = Image.open('./2.jpg')

    im2 = im2.resize(im1.size)

    # 图片进行加法运算
    #ImageChops.add(im1,im2).show()

    # 图片进行减法运算
    #ImageChops.subtract(im1,im2).show()

    # 图片变暗（图片保留较暗的部分）
    #ImageChops.darker(im1,im2).show()

    # 图片变亮
    #ImageChops.lighter(im1, im2).show()

    # 图片叠加
    #ImageChops.multiply(im1,im2).show()

    # 同时显示到屏幕上
    #ImageChops.screen(im1,im2).show()

    # 图片变成底片
    #ImageChops.invert(im1).show()

    # 图片取不同
    ImageChops.difference(im1,im2).show()

    pass

if __name__ == '__main__':
    main()