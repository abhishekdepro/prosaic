import operator
# A slightly efficient superset of primes.
def PrimesPlus():
  yield 2
  yield 3
  i = 5
  while True:
    yield i
    if i % 6 == 1:
      i += 2
    i += 2
# Returns a dict d with n = product p ^ d[p]
def GetPrimeDecomp(n):
  d = {}
  fact=[]
  primes = PrimesPlus()
  for p in primes:
    while n % p == 0:
      n /= p
      d[p] = d.setdefault(p, 0) + 1
      fact.append(p)
    if n == 1:
      print d
      print fact
      return d
def NumberOfDivisors(n):
  d = GetPrimeDecomp(n)
  powers_plus = map(lambda x: x+1, d.values())
  print powers_plus
  return reduce(operator.mul, powers_plus, 1)

def primegenerator(limit):
    _set=[]
    for i in range(2,limit):
        if(isPrime(i)==True):
            _set.append(i)
    return _set

def isPrime(num):
    flag=0
    for i in range(2, num-1):
        if num%i==0:
            flag=1
            break
        else:
            continue
    if flag==1:
        return False
    else:
        return True
