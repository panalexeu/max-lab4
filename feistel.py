from rich import print

from utils import (
    format_str,
    str_to_bin,
    bin_to_str,
    xor
)
from file import (
    read,
)


def feistel_encr(text: str, avalanche=False):
    formatted_text = format_str(text)
    bin_text = str_to_bin(formatted_text)

    encoded_chunks = []
    chunk_size, rounds = 64, 16
    for i in range(0, len(bin_text), chunk_size):
        bin_chunk = bin_text[i:i + chunk_size]
        L, R = bin_chunk[0:32], bin_chunk[32:]

        for j in range(rounds):
            prev = L + R  # for avalanche effect printing

            # calculation
            temp_R = R
            key = get_key(j)
            R = xor(L, xor(R, key, 32), 32)
            L = temp_R

            cur = L + R  # for avalanche effect printing
            # avalanche effect printing
            if i == 0 and avalanche:
                avalanche_effect(
                    key,
                    prev,
                    cur,
                    j
                )

        cat_L_R = L + R
        encoded_chunks.append(cat_L_R)

    bin_chunks = ''.join(encoded_chunks)
    str_chunks = bin_to_str(bin_chunks)

    return str_chunks


def feistel_decr(text: str):
    bin_text = str_to_bin(text)

    encoded_chunks = []
    chunk_size, rounds = 64, 15
    for i in range(0, len(bin_text), chunk_size):  # reversed round moving order
        bin_chunk = bin_text[i:i + chunk_size]
        R, L = bin_chunk[0:32], bin_chunk[32:]  # reversed here L => R, R => L

        for j in range(rounds, -1, -1):
            temp_R = R
            key = get_key(j)
            R = xor(L, xor(R, key, 32), 32)
            L = temp_R

        cat_R_L = R + L
        encoded_chunks.append(cat_R_L)

    bin_chunks = ''.join(encoded_chunks)
    str_chunks = bin_to_str(bin_chunks)

    return str_chunks


def get_key(round: int) -> str:
    key = read('files/key.txt')
    round = round % len(key)

    return str_to_bin(key[round:round + 4])


def avalanche_effect(key: str, prev: str, cur: str, round: int):
    changed_bits = xor(prev, cur, 64)
    av_prev, av_cur = '', ''
    for i, bit in enumerate(changed_bits):
        if bit == '1':
            av_prev += f'[bold gold3]{prev[i]}[/bold gold3]'
            av_cur += f'[bold gold3]{cur[i]}[/bold gold3]'
            continue
        av_prev += prev[i]
        av_cur += cur[i]

    print(f'ROUND: {round}')
    if round != 0:
        prev_key = get_key(round - 1)
        changed_bits_in_key = xor(key, prev_key, 32)
        av_key_prev, av_key_cur = '', ''
        for i, bit in enumerate(changed_bits_in_key):
            if bit == '1':
                av_key_prev += f'[bold yellow4]{prev_key[i]}[/bold yellow4]'
                av_key_cur += f'[bold yellow4]{key[i]}[/bold yellow4]'
                continue
            av_key_prev += prev_key[i]
            av_key_cur += key[i]

        print(f'prev key: {av_key_prev} | {bin_to_str(prev_key)}')
        print(f'cur key : {av_key_cur} | {bin_to_str(key)}')
        print(f'amount of changed bits in key: [bold orange_red1]{changed_bits_in_key.count('1')}[/bold orange_red1]')
    else:
        print(f'key: {key} | {bin_to_str(key)}')
    print(f'prev: {av_prev} | {bin_to_str(prev)}')
    print(f'cur : {av_cur} | {bin_to_str(cur)} ')
    print(f'amount of changed bits in text: [bold orange_red1]{changed_bits.count('1')} [/bold orange_red1]')
    print()
