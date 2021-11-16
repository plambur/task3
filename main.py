from Device import *


if __name__ == '__main__':
    try:
        device: Device = open_device('/devices/dev3')

        line = int(input())
        write_line(device, line)

        line = int(input())
        write_line(device, line)

        line = int(input())
        write_line(device, line)

        for i in range(3):
            print(read_line(device))


    except Exception as exception:
        print(f'Error: {exception}')

