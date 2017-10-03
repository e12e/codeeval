#ifndef PRIME_H
#define PRIME_H

#include <iostream>
#include <sstream>
#include <set>
#include <numeric>

int print_primes(unsigned int n, std::ostream& strout);

std::set<unsigned int> genprimes(unsigned int n);

unsigned int sum_primes(unsigned int n);

#endif
