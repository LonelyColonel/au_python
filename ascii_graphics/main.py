from PIL import Image


def func_for_splitting(w, h, scale, im):
    sp = []
    for y in range(h // scale):
        y_start, y_end = y * scale, (y + 1) * scale
        for x in range(w // scale):
            x_start, x_end = x * scale, (x + 1) * scale
            sp.append(im.crop((x_start, y_start, x_end, y_end)))
    return sp


def func_average_color_calculation(array_block, scala):
    matrix = []
    for block in array_block:
        new_block = block.convert(mode='L')
        temp = 0
        for y in range(scala):
            for x in range(scala):
                temp += new_block.getpixel((x, y))
        temp_value = round(temp / (scala ** 2))
        matrix.append(round((temp_value * scala) / 255))
    return matrix


def main():
    print('Здравствуйте, данная программа создаёт изображения в ASCII-графике, используя цветное пиксельное '
          'изображение, до которого пользователь укажет путь.\nПрограмма создаст текстовый файл в той же директории, '
          'где находится и сам скрипт.\n')
    while True:
        try:
            user_answer = input('Введите путь до изображения:')
            image = Image.open(user_answer)
            break
        except FileNotFoundError:
            print('Неправильный путь! Указанного файла нет или он повреждён! Попробуйте ещё раз.')
        except PermissionError:
            print('Вы указали путь до папки, но не до самого изображения.')

    w, h = image.size
    # масштаб уменьшения
    temp_scale = 10
    palette = '@&%#*+=-:.'
    sp = []
    for x in range(w):
        for y in range(h):
            sp.append(image.getpixel((x, y)))

    blocks_sp = func_for_splitting(w, h, temp_scale, image)
    res_array = func_average_color_calculation(blocks_sp, temp_scale)
    with open('file.txt', mode='w') as file:
        for i in range(len(res_array)):
            if i % (w // temp_scale) == 0:
                file.write('\n')
            else:
                file.write(palette[int(res_array[i]) - 1])
    print('Изображение в ASCII готово и сохранено в file.txt')


if __name__ == '__main__':
    main()
