from PIL import Image

def main():

    im1 = Image.open('./1.jpg')
    im2 = Image.open('./2.jpg')

    '''
    # 把每个像素扩大2倍
    Image.eval(im1,lambda i:i*2).show()
    '''

    '''
    # 复制一个图片副本到内存
    copy = im1.copy()
    # 缩放到指定大小
    copy.thumbnail((100,50))
    copy.show()
    '''

    '''
    # 剪切图片
    part1 = im1.crop((5,5,130,130))
    # 粘贴图片
    im2.paste(part1,(30,30))
    im2.show()
    '''

    '''
    # 逆时针90°旋转
    im1.rotate(90).show()
    '''

    '''
    # 左右镜像
    im1.transpose(Image.FLIP_LEFT_RIGHT).show()
    '''

    '''
    # 上下镜像
    im1.transpose(Image.FLIP_TOP_BOTTOM).show()
    '''

    '''
    # 旋转90°
    im1.transpose(Image.ROTATE_90).show()
    '''

    # 颠倒
    im1.transpose(Image.TRANSPOSE).show()

    pass

if __name__ == '__main__':
    main()