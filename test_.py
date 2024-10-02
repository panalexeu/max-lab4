from utils import (
    str_to_bin,
    bin_to_str,
    format_str,
    xor
)
from file import (
    read,
    write
)

from feistel import (
    feistel_encr,
    feistel_decr,
    get_key
)


def test_str_to_bin_convert():
    str_ = 'hello'
    res = str_to_bin(str_)

    assert res == '0110100001100101011011000110110001101111'


def test_bin_to_str_convert():
    bin_ = '0110100001100101011011000110110001101111'
    res = bin_to_str(bin_)

    assert res == 'hello'


def test_format_str():
    str_ = 'Hello\naLex'
    res = format_str(str_)

    assert res == 'hello alex'


def test_feistel_encr():
    text = read('files/text.txt')
    res = feistel_encr(text)
    write('files/text.encr.txt', res)

    assert res == """vl'l~-4ibhwzflb> }pg(fngogdkmc3/whsk6`f/njb.}'9%lhjkdg1iw`kb8!y&rp'z3r=li{b.`9,hl'ffk|vsyn|}tl8nznjfo5gt`k.p!e$agc.i&k>rl'cqh:hrm'hj,0cum`k{~;e.)=j"-(z"""


def test_feistel_decr():
    text = read('files/text.encr.txt')
    res = feistel_decr(text)

    assert res == 'i have been baptized twice, once in water, once in flame. i will carry the fire of the holy spirit inside until i stand before my lord for judgement. :d'


def test_get_key():
    round1 = get_key(0)
    round29 = get_key(29)
    round30 = get_key(30)

    assert bin_to_str(round1) == 'horc' and bin_to_str(round29) == 'horc' and bin_to_str(round30) == 'orch'


def test_xor():
    bin1 = '10010101'
    bin2 = '10001001'
    res = xor(bin1, bin2, 8)

    assert res == '00011100'


def test_xor_32_bits():
    bin1 = '10010101100101011001010110010101'
    bin2 = '10001001100010011000100110001001'
    res = xor(bin1, bin2, 32)

    assert res == '00011100000111000001110000011100'
