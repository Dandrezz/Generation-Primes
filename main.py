from math import sqrt
import time
import numpy as np

def primegen(n):
  prime = np.ones(n,bool)
  prime[4::2]=False
  for p in range( 3, int(sqrt(n)), 2 ):
      if prime[p]:
        prime[p*p::2*p]=False
  return prime

if __name__ == '__main__':
    start = time.time()
    n = 1_000_000_000
    primegen(n)
    end = time.time()
    print(end-start)