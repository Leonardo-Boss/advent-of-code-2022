from collections import deque

def has_repeated_char(x):
    for i, v in enumerate(x):
        for j, w in enumerate(x):
            if w == v and i != j:
                return True
    return False

def find_marker(f, charcount, start=0):
    char = True
    letter_buffer = deque((i for i in f.read(charcount - 1)), maxlen=charcount)
    count = start + charcount - 1
    while char:
        count += 1
        char = f.read(1)
        letter_buffer.append(char)
        if not has_repeated_char(letter_buffer):
            print(letter_buffer)
            break
    return count

if __name__ == "__main__":
    with open('input6.txt') as f:
        packet_count = find_marker(f, 4)
        message_count = find_marker(f, 14, packet_count)
    print('packet_start:', packet_count)
    print('message_start:', message_count)
