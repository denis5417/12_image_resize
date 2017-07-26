from os import path
from PIL import Image
import resize
import argparse


def load_image(path_to_original):
    if not path.exists(path_to_original):
        return None
    else:
        return Image.open(path_to_original)


def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument("input", type=str, help="Путь к исходному изображению")
    parser.add_argument("-w", "--width", type=int, help="Ширина нового изображения (положительное число)")
    parser.add_argument("-he", "--height", type=int, help="Высота нового изображения (положительное число)")
    parser.add_argument("-s", "--scale", type=int, help="Масштаб нового изображения (не может быть равно 0)")
    parser.add_argument("-o", "--output", type=str, help="Название нового файла (положительное число)")
    return parser.parse_args()


if __name__ == '__main__':
    result_width = parse_args().width
    result_height = parse_args().height
    result_scale = parse_args().scale
    if ((result_width and result_height) or (result_width or result_height)) and result_scale:
        exit("Вы можете указать только ширину / высоту / ширину и высоту / масштаб!")
    elif result_width is None and result_height is None and result_scale is None:
        exit("Укажите хотя бы одно значение!")
    img = load_image(parse_args().input)
    if not img:
        exit("Такого файла не существует")
    img = resize.resize_image(img, result_width, result_height)
    if not img:
        exit("Неправильные параметры. Смотрите справку")
    if parse_args().output:
        img.save(parse_args().output)
    else:
        input_split = path.splitext(parse_args().input)
        img.save("{}__{}x{}{}".format(input_split[0], img.size[0], img.size[1], input_split[1]))
    print("Размер новго изображения – {}x{}".format(img.size[0], img.size[1]))
