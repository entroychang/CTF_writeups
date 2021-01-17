vaild = '0123456789.!^&|+-*/%()[],'
good = ['abs', 'acos', 'acosh', 'asin', 'asinh', 'atan2', 'atan', 'atanh', 'base_convert', 'bindec', 'ceil', 'cos', 'cosh', 'decbin', 'dechex', 'decoct', 'deg2rad', 'exp', 'floor', 'fmod', 'getrandmax', 'hexdec', 'hypot', 'is_finite', 'is_infinite', 'is_nan', 'lcg_value', 'log10', 'log', 'max', 'min', 'mt_getrandmax', 'mt_rand', 'octdec', 'pi', 'pow', 'rad2deg', 'rand', 'round', 'sin', 'sinh', 'sqrt', 'srand', 'tan', 'tanh', 'ncr', 'npr', 'number_format']
answer = "()"

tmp1, tmp2 = '', ''

for i in answer:
    for j in good:
        for k in good:
            if (j ^ k == ord(i)):
                tmp1 += j
                tmp2 += k
                break
        else:
            continue
        break
print("'" + tmp1 + "'" + '^' + "'" + tmp2 + "'")