from PIL import Image
from PIL import ImageDraw, ImageFont

def main():
    # 创建一个300x250的白色底面图像
    pic = Image.new('RGB', (300, 250), 'white')
    # 选择图片资源取画面
    draw_obj = ImageDraw.Draw(pic)
    # 绘制一个红色矩形
    draw_obj.rectangle((50, 50, 150, 150), fill='blue', outline='red')
    # 绘制文本
    font = ImageFont.truetype('test1.TTF', 20)
    draw_obj.text((100, 100), 'abcdefg', font=font, fill='green')

    # 画一个圆形
    draw_obj.arc((0, 0, 100, 50), 0, 180, fill='blue')

    # 画一条线
    draw_obj.line((0, 0) + pic.size, fill=128, width=5)

    pic.show()

    pass

if __name__ == '__main__':
    main()