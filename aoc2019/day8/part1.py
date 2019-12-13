import numpy as np


def get_num_integer_in_layer(i, layer, image):
    return len(np.where(image[layer, ...] == i)[0])


def part1(shape, data):

    img_size = np.prod(shape)
    num_layers = len(data) // img_size

    # Get data as a contiguous array of ints
    i_data = np.asarray([int(s) for s in data], dtype=int)

    # Reshape the data into an array of layers, rows, cols
    image = np.reshape(i_data, newshape=(num_layers,) + shape)

    # Find the layer with the fewest zeros
    zero_counts = {}
    for layer in range(num_layers):
        zero_counts[layer] = get_num_integer_in_layer(0, layer, image)

    best_layer = min(zero_counts, key=zero_counts.get)

    number_of_1s = get_num_integer_in_layer(1, best_layer, image)
    number_of_2s = get_num_integer_in_layer(2, best_layer, image)

    print(number_of_1s * number_of_2s)


if __name__ == '__main__':

    ## Test data
    # shape = (2, 3)
    # data = '123456789012'

    shape = (6, 25)

    with open('input.txt') as f:
        data = f.read()

    part1(shape, data)