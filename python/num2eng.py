#!/usr/bin/env python
import sys
import numpy as np
num_dict={
  0: 'zero',
  1: 'one',
  2: 'two',
  3: 'three',
  4: 'four',
  5: 'five',
  6: 'six',
  7: 'seven',
  8: 'eight',
  9: 'nine',
  10: 'ten',
  11: 'eleven',
  12: 'twelve',
  13: 'thirteen',
  14: 'fourteen',
  15: 'fifteen',
  16: 'sixteen',
  17: 'seventeen',
  18: 'eighteen',
  19: 'nineteen',
  20: 'twenty',
  30: 'thirty',
  40: 'forty',
  50: 'fifty',
  60: 'sixty',
  70: 'seventy',
  80: 'eighty',
  90: 'ninety',
}
dig_dict={
  100: 'hundred',
  1000: 'thousand',
  1000000: 'million',
  1000000000: 'billion',
  1000000000000: 'trillion',
  1000000000000000: 'quadrillion',
  1000000000000000000: 'quintillion',
}

dig_array = np.array(sorted(dig_dict.keys()), dtype=int)

def num2eng(num, level=0):
    if num==0: return ''
    ndig = int(np.floor(np.log10(num)))
    assert(ndig<=18)
    if ndig==0:
        return num_dict[num] if num!=0 or level>0 else ''
    elif ndig==1:
        if num in num_dict:
            return num_dict[num]
        else:
            tens = int(num/10)*10
            rem  = num-tens
            return num_dict[tens]+('-'+num_dict[rem] if rem>0 else '')
    else:
        dig      = 10**ndig
        loc      = np.searchsorted(dig_array, dig, side='right')-1
        dig_act  = dig_array[loc]
        dig_mult = int(num/dig_act)
        rem      = num-dig_mult*dig_act
        return num2eng(dig_mult, level+1) + ' ' + dig_dict[dig_act] + ' ' + num2eng(rem, level+1)



if __name__=='__main__':
    n = int(sys.argv[1])
    e = num2eng(n)
    print n, e
