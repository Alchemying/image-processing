from PIL import Image
from PIL import ImageFilter
from PIL import ImageEnhance
import os


# 读取函数，用来读取文件夹中的所有函数，输入参数是文件名
def read_directory(directory_name):
    for picture_name in os.listdir(directory_name):
        print(picture_name)  # 读取图片名称及类型

        file_name = directory_name + "/" + picture_name  # 读取文件夹地址+图片名称类型
        print(file_name)

        square = Image.open(file_name)  # 打开指定文件夹图片
        # square.show()

        #squarell = square.convert('RGB') #RGB 转换
        #squarell.show()

        squarel = square.filter(ImageFilter.CONTOUR)  # 进行轮廓效果——素描处理
        squarel.show()  # 进行图片显示

        squarelll = squarel.filter(ImageFilter.SMOOTH)  # 平滑处理
        # squarelll.show()

        squarellll = squarelll.filter(ImageFilter.EDGE_ENHANCE)  # 锐化处理
        # squarellll.show()

        enh_col = ImageEnhance.Color(squarellll)  # 进行对比度处理
        color = 1.5
        squarelllll = enh_col.enhance(color)
        # squarelllll.show()

        square_ll = ImageEnhance.Brightness(squarelllll)
        squarell = square_ll.enhance(0.8)  # 改变亮度
        # squarell.show()



        root = 'data/image output'  # 保存地址
        path = root + "/" + picture_name  # 保存路径

        try:
            squarell.save(path, quality=95)  # quality为图片质量，65为最低，95为最高
            print('图片保存成功，保存在' + root + "\n")
        except:
            print('图片保存失败')


if __name__ == '__main__':  # 主函数入口
    directory_name = "data/image input"  # 这里传入所要读取文件夹的绝对路径，加引号（引号不能省略！）
    read_directory(directory_name)
