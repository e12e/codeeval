#include <iostream>
#include <sstream>
#include <set>
#include <numeric>

std::set<unsigned int> genprimes(unsigned int n);

unsigned int sum_primes(unsigned int n);

std::set<unsigned int> genprimes(unsigned int n)
{
    using std::set;
    set<unsigned int> primes;

    primes.insert(2);
    primes.insert(3);
    for(unsigned int i=3; primes.size() < n; i+=2)
    {
        bool is_prime = false;

        for(auto p: primes)
        {
            is_prime = true;

            if (!(i % p))
            {
               is_prime = false;
               break;
            }
        }
        if (is_prime)
        {
            primes.insert(i);
        }
    }

    return primes;
}


unsigned int sum_primes(unsigned int n)
{
    using std::accumulate;
    using std::set;

    set<unsigned int> primes = genprimes(n);
    unsigned int sum = 0;

    sum = accumulate(primes.begin(),primes.end(),0);

    return sum;
}

int main(int argc, char* argv[])
{
    using std::cout;
    using std::endl;

    unsigned int n = 1000;

    unsigned int sum = sum_primes(n);

    cout << sum << endl;
}
