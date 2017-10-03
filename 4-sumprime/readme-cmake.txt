For some variations, try:

mkdir build
cd build
cmake -GNinja .. && ninja && ninja test

Or:
cmake .. && make && make test

Test output in:

cat ./Testing/Temporary/LastTest.log


The following not tested on this repo yet!:

# Compile with clang:
cmake -D CMAKE_C_COMPILER=clang ..

# Release or debug builds:

cmake -DCMAKE_BUILD_TYPE=Release ..
cmake -DCMAKE_BUILD_TYPE=Debug ..
