from PIL import Image

def main():

    im1 = Image.open('./1.PNG').convert(mode='RGB')
    im2 = Image.new('RGB', im1.size, 'green')

    Image.blend(im1,im2,alpha=0.5).show()

    pass

if __name__ == '__main__':
    main()