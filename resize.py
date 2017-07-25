from PIL import Image


def resize_image_by_width_and_height(img, result_width, result_height):
    try:
        return img.resize((result_width, result_height), Image.ANTIALIAS)
    except ValueError:
        return None


def resize_image_by_scale(img, result_scale):
    try:
        if result_scale > 0:
            return img.resize((img.size[0]*result_scale, img.size[1]*result_scale), Image.ANTIALIAS)
        elif result_scale < 0:
            return img.resize((int(img.size[0] / result_scale*-1), int(img.size[1] / result_scale*-1)), Image.ANTIALIAS)
    except ValueError:
        return None


def resize_image_by_height(img, result_height):
    try:
        hpercent = (result_height / float(img.size[1]))
        result_width = int((float(img.size[0]) * float(hpercent)))
        return img.resize((result_width, result_height), Image.ANTIALIAS)
    except ValueError:
        return None


def resize_image_by_width(img, result_width):
    try:
        wpercent = (result_width / float(img.size[0]))
        result_height = int((float(img.size[1]) * float(wpercent)))
        return img.resize((result_width, result_height), Image.ANTIALIAS)
    except ValueError:
        return None
