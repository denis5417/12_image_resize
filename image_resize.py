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


def is_invalid_args(result_width, result_height, result_scale):
    is_args_conflicts = ((result_width and result_height) or (result_width or result_height)) and result_scale
    is_no_args = result_width is None and result_height is None and result_scale is None
    return is_args_conflicts or is_no_args

if __name__ == '__main__':
    args = parse_args()
    if is_invalid_args(args.width, args.height, args.scale):
        exit("Укажите только ширину / высоту / ширину и высоту / масштаб! И хотя бы одно из этих значений!")
    img = load_image(args.input)
    if not img:
        exit("Такого файла не существует")
    img = resize.resize_image(img, args.width, args.height, args.scale)
    if not img:
        exit("Неправильные параметры. Смотрите справку")
    if args.output:
        img.save(args.output)
    else:
        input_split = path.splitext(args.input)
        img.save("{}__{}x{}{}".format(input_split[0], img.size[0], img.size[1], input_split[1]))
    print("Размер новго изображения – {}x{}".format(img.size[0], img.size[1]))
