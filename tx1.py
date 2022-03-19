from PIL import Image

def main():
    im = Image.open('./1.PNG')

    # 显示图片
    #im.show()

    # 获取图片格式
    #print(im.format)

    # 获得图片大小
    #print(im.size)

    # 获得图片高度和宽度
    #print(im.height,im.width)

    # 获得图片某个像素的颜色
    print(im.getpixel((200,50)))

    pass

if __name__ == '__main__':
    main()