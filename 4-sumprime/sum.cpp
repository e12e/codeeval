#include "prime.hpp"
#include <sstream>

int main(int argc, char* argv[])
{
    using std::cerr;
    using std::cout;
    using std::endl;
    using std::istringstream;

    unsigned int n = 10;

    if (argc == 2)
    {
        istringstream ss(argv[1]);
        if(!(ss >> n))
        {
            cerr << "Invalid number: " << argv[1] << endl;
            exit(1);
        }
    }

    unsigned int sum = sum_primes(n);

    cout << sum << endl;
}
