#include "prime.hpp"
#include <sstream>

int main(int argc, char* argv[])
{
    using std::cerr;
    using std::endl;
    using std::istringstream;

    int n = 10;

    if (argc == 2)
    {
        istringstream ss(argv[1]);
        if(!(ss >> n))
        {
            cerr << "Invalid number: " << argv[1] << endl;
            exit(1);
        }
    }

    return print_primes(n, std::cout);
}
