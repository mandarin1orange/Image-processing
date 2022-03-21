from PIL import Image

def main():

    im1 = Image.open('./1.PNG')
    im2 = Image.open('./2.PNG')

    # 重新让照片变小
    im2 = im2.resize(im1.size)

    r,g,b,a = im2.split()

    # 遮罩处理
    Image.composite(im2,im1,r).show()

    pass

if __name__ == '__main__':
    main()