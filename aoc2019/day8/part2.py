import numpy as np


def get_num_integer_in_layer(i, layer, image):
    return len(np.where(image[layer, ...] == i)[0])


def part2(shape, data):

    img_size = np.prod(shape)
    num_layers = len(data) // img_size

    # Get data as a contiguous array of ints
    i_data = np.asarray([int(s) for s in data], dtype=int)

    # Reshape the data into an array of layers, rows, cols
    image = np.reshape(i_data, newshape=(num_layers,) + shape)

    # Build a new image, for each pixel, find the top-most digit != 2
    output = 2 * np.ones(shape, dtype=int)

    for row in range(shape[0]):
        for col in range(shape[1]):
            if output[row, col] != 2:
                continue
            else:
                for layer in range(num_layers):
                    if image[layer, row, col] != 2:
                        output[row, col] = image[layer, row, col]
                        break

    with np.printoptions(linewidth=1024, edgeitems=1024):
        print(output)

    for row in range(shape[0]):
        print()
        for col in range(shape[1]):
            if output[row, col] == 2:
                print('?', end='')
            elif output[row, col] == 1:
                print('#', end='')
            elif output[row, col] == 0:
                print(' ', end='')




if __name__ == '__main__':

    # # Test data
    # shape = (2, 2)
    # data = '0222112222120000'

    shape = (6, 25)

    with open('input.txt') as f:
        data = f.read()

    part2(shape, data)