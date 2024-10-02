def str_to_bin(str_: str) -> str:
    str_to_dec = [ord(ch) for ch in str_]
    dec_to_bin = [format(num, '08b') for num in str_to_dec]

    return ''.join(dec_to_bin)


def bin_to_str(bin_: str) -> str:
    bin_size = 8
    bin_chunks = [bin_[i:i + bin_size] for i in range(0, len(bin_), bin_size)]
    bin_to_dec = [int(chunk, 2) for chunk in bin_chunks]
    dec_to_str = [chr(num) for num in bin_to_dec]

    return ''.join(dec_to_str)


def format_str(str_: str) -> str:
    return str_.lower().replace('\n', ' ')


def xor(bin1: str, bin2: str, bit_size: int) -> str:
    res = int(bin1, 2) ^ int(bin2, 2)

    return format(res, f'0{bit_size}b')
