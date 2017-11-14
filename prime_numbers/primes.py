# Take a look at this and try to incorporate:
# https://www.khanacademy.org/computing/computer-science/cryptography/comp-number-theory/p/level-4-sieve-of-eratosthenes

class PrimeNumbers():
    def prime_count(self, n):
        '''
        This method will return the number of non-negative prime numbeers that
        are less positive than the given number, 'n'.
        Examples
        ----------------------
        >>>prime_count(13)
        5    # 2, 3, 5, 7, 11
        >>>prime_count(17)
        6    #2, 3, 5, 7, 11, 13
        '''
        primes = list(range(2, n))
        index = 0
        finished = False
        while finished == False:
            prime = primes[index]
            elim_list = list(range(prime**2, n, prime))
            for num in primes:
                if num in elim_list:
                    primes.remove(num)
            index += 1
            if prime**2 >= n:
                finished = True
        return len(primes)

test=PrimeNumbers()
print(test.prime_count(100000))
