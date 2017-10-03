#define BOOST_TEST_MAIN
#include <boost/test/included/unit_test.hpp>
#include "prime.hpp"

BOOST_AUTO_TEST_CASE(print_n_first_primes)
{
    std::ostringstream dest;

    print_primes(4, dest);

    std::ostringstream expected;

    expected << "Found primes 4 primes:" << std::endl
             << "2 3 5 7 " << std::endl;

    BOOST_REQUIRE_EQUAL(expected.str(), dest.str());
}

BOOST_AUTO_TEST_CASE(sum_n_first_primes)
{
    unsigned sum = sum_primes(4);

    BOOST_REQUIRE_EQUAL(sum, 2+3+5+7);
}
/*
#include <boost/test/included/prg_exec_monitor.hpp>
int cpp_main(int, char*[])
{
    cout << "Hello, World!" << endl;
    return 0;
}

*/
