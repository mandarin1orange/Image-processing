from PIL import Image

def main():

    im1 = Image.open('./1.jpg')
    im2 = Image.open('./2.jpg')

    im2 = im2.resize(im1.size)

    # 进行rgb分离
    r1,g1,b1,a1 = im1.split()
    r2,g2,b2,a2 = im2.split()

    # 制作合成一个新的图片
    tmp1 = [r1,g2,b1,a2]
    im3 = Image.merge('RGBA',tmp1)
    im3.show()

    pass

if __name__ == '__main__':
    main()