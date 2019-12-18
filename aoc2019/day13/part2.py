import multiprocessing as mp
import numpy as np
from matplotlib import pyplot as plt
from matplotlib import animation
import time
import os
import shutil

from aoc2019.intcode_computer import IntCodeComputer

# Map of tile_id to color
color_map = {0: [0, 0, 0],
             1: [1, 0, 0],
             2: [0, 1, 1],
             3: [0, 1, 0],
             4: [1, 1, 1]}

def initialize_screen(screen_dict, draw_queue):

    data = []
    while True:
        try:
            data.append(draw_queue.get(timeout=0.1))
        except:
            break
    data = np.reshape(data, newshape=(len(data)//3, 3))

    for tile_id in [0, 1, 2, 3, 4]:
        # Draw the walls
        rows = np.where(data[:, 2] == tile_id)[0]

        for i in rows:
            x = data[i, 0]
            y = data[i, 1]
            screen_dict[y, x] = color_map[tile_id]

    # Convert the screen dict to an image
    screen = np.zeros((20, 37, 3), dtype=int)

    for i in range(20):
        for j in range(37):
            screen[i, j, :] = screen_dict[i, j]

    im = plt.imshow(screen, interpolation='none', origin='upper')
    np.save('screen_data', screen)


def save_screen(frame_idx, screen_dict):
    # Display the screen
    # fig = plt.figure()
    # Convert the screen dict to an image
    screen = np.zeros((20, 37, 3), dtype=np.float)
    for i in range(20):
        for j in range(37):
            screen[i, j, :] = screen_dict[i, j]
    im = plt.imshow(screen, interpolation='none', origin='upper')
    plt.savefig(f'frames/frame_{frame_idx:000d}.png')


def display2(screen_dict, animate=True):

    # First set up the figure, the axis, and the plot element we want to animate
    fig = plt.figure()

    # Convert the screen dict to an image
    screen = np.zeros((20, 37, 3), dtype=np.float)

    for i in range(20):
        for j in range(37):
            screen[i, j, :] = screen_dict[i, j]

    im = plt.imshow(screen, interpolation='none', origin='upper')

    # initialization function: plot the background of each frame
    def init():
        # Convert the screen dict to an image
        screen = np.zeros((20, 37, 3), dtype=np.float)

        for i in range(20):
            for j in range(37):
                screen[i, j, :] = screen_dict[i, j]

        # Get all initial data for the game board
        im.set_data(screen)
        return [im]

    # animation function.  This is called sequentially
    def animate(i):
        # Convert the screen dict to an image
        screen = np.zeros((20, 37, 3), dtype=np.float)

        for i in range(20):
            for j in range(37):
                screen[i, j, :] = screen_dict[i, j]

        im.set_array(screen)
        return [im]

    anim = animation.FuncAnimation(fig, animate, init_func=init, interval=100, blit=True)

    plt.show()


def play_the_game(draw_queue, game_input_queue, ball_impact_history, screen_dict):
    ball_pos = np.array([17, 16], dtype=int)
    ball_vel = np.array([-1, -1], dtype=int)
    paddle_pos = np.array([19, 18], dtype=int)

    with open('scoring.txt', 'w') as score_file:


        for i in range(1_000_000_000):
            print(f'\n\nBEGIN FRAME {i}')

            # Get all awaiting data from the output queue
            data = []
            while True:
                try:
                    for j in range(3):
                        data.append(draw_queue.get(timeout=0.1))
                    if data[-1] == 4:
                        break
                except mp.queues.Empty:
                    break

            data = np.reshape(data, newshape=(len(data) // 3, 3))

            for row in data:
                x, y, tile_id = row

                # Add the information to the screen dictionary for visualization
                if x >= 0:
                    screen_dict[y, x] = color_map[tile_id]

                # If given information on the paddle, save its position
                if tile_id == 3:
                    paddle_pos[:] = [x, y]
                    print('paddle pos', paddle_pos)

                # If given information on the ball, save its position
                if tile_id == 4:
                    ball_vel[:] = np.asarray([x, y]) - ball_pos
                    ball_pos[:] = [x, y]
                    print('ball pos', ball_pos, 'ball_vel', ball_vel)

                if x == -1:
                    if tile_id == 0:
                        print('GAME OVER, MAN!')
                        return
                    else:
                        print('SCORE:', tile_id)
                        blocks_remaining = len([v for v in screen_dict.values() if tuple(v) == (0, 1, 1)])
                        print('BLOCKS REMAINING', blocks_remaining)
                        print(blocks_remaining, tile_id, file=score_file)
                        if blocks_remaining == 0:
                            return

            # save_screen(i, screen_dict)

            # # Find the next impact time in the ball impact history keys
            future_impacts = [t for t in ball_impact_history.keys() if t > i]

            command = 0
            if future_impacts:
                next_t = min(future_impacts)
                next_x = ball_impact_history[min(future_impacts)]
                print(f'next impact at {next_t} {next_x}')
                if next_x > paddle_pos[0]:
                    command = 1
                elif next_x < paddle_pos[0]:
                    command = -1
            else:
                # Flying blind, if impact occurs add its location and time to the history
                if ball_pos[1] == (paddle_pos[1]) and ball_vel[1] > 0:
                    print(f'new impact at t={i} x={x}')
                    ball_impact_history[i] = x
                else:
                    if paddle_pos[0] < ball_pos[0]:
                        command = 1
                    elif paddle_pos[0] > ball_pos[0]:
                        command = -1
                    else:
                        command = 0

            # print('Current pos:', paddle_pos[0], 'Target pos:', next_x, 'Command:', command)
            print('command', command)
            game_input_queue.put(command)



"""
1 [18 18  0]
1 [17 18  3]
1 [16 15  0]
1 [17 16  4]

2 [17 18  0]
2 [18 18  3]
2 [17 16  0]
2 [18 17  4]
"""

def part2(program):

    manager = mp.Manager()

    iq = mp.Queue()
    oq = mp.Queue()
    ball_impact_history = manager.dict()

    screen_dict = manager.dict()

    for i in range(20):
        for j in range(37):
            screen_dict[i, j] = [0, 0, 0]

    # comp = IntCodeComputer(stdio=False, relative_base=0)

    # Put two quarters in
    prog = program.split(',')
    prog[0] = '2'

    # display_proc = mp.Process(target=display2, args=(screen_dict,))
    # display_proc.start()

    for i in range(1):
        if os.path.isdir('frames'):
            shutil.rmtree('frames')
        os.mkdir('frames')

        program = ','.join(prog)

        comp = IntCodeComputer(stdio=False, relative_base=0)
        game_proc = mp.Process(target=comp.run_program, args=(program,), kwargs={'mem': 10000,
                                                                                 'input_queue': iq,
                                                                                 'output_queues': [oq]})

        game_proc.start()

        time.sleep(0.1)

        initialize_screen(screen_dict, draw_queue=oq)

        play_proc = mp.Process(target=play_the_game, args=(oq, iq, ball_impact_history, screen_dict))

        play_proc.start()

        game_proc.join()
        play_proc.join()

        print(ball_impact_history)


    # while True:
    #     game_proc = mp.Process(target=comp.run_program, args=(program,), kwargs={'mem': 10000,
    #                                                                              'input_queue': iq,
    #                                                                              'output_queues': [
    #                                                                                  oq]})
    #
    #     game_proc.start()
    #     # Get the initial board data
    #     time.sleep(1.0)
    #     screen = initialize_screen(draw_queue=oq)
    #     game_proc.join()
    #
    # draw_proc.join()

    # # Get all outputs
    # output = []
    # while True:
    #     try:
    #         output.append(oq.get(block=False))
    #     except:
    #         break
    #
    # data = np.reshape(output, (len(output)//3, 3))
    #
    # display(data)


if __name__ == '__main__':
    with open('input.txt') as f:
        inp = f.read()

    part2(inp)

