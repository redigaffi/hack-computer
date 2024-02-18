def modulo(dividend, divisor):
    quotient = dividend // divisor
    product = quotient * divisor
    remainder = dividend - product
    return remainder

print(modulo(1, 16))
