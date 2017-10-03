cmake_minimum_required (VERSION 2.8)

project (prime)

SET(CMAKE_COLOR_MAKEFILE ON)
SET(CMAKE_VERBOSE_MAKEFILE ON)

#set (CMAKE_CXX_COMPILER "clang++")
#set (CMAKE_CXX_COMPILER "g++")

list (APPEND CMAKE_CXX_FLAGS "-std=c++11 -Wall -Werror -pedantic")
list (APPEND CMAKE_CXX_FLAGS_RELEASE"-O2 -DNDEBUG -s")

add_executable(sum sum.cpp prime.cpp)
add_executable(demo main.cpp prime.cpp)
add_executable(codeval codeval.cpp)
add_executable(prime_test primeTest.cpp prime.cpp)

set(Boost_USE_STATIC_LIBS ON)
find_package(Boost REQUIRED)

target_link_libraries(prime_test ${Boost_FILESYSTEM_LIBRARY} 
                           ${Boost_SYSTEM_LIBRARY})

enable_testing()
add_test(NAME static_test COMMAND prime_test --log_level=test_suite)


# Leave for later...
# Precompile header(s)
#PCH = prime.hpp
#PCH_FILES = $(PCH:hpp=hpp.gch)

# Precompile header(s)
#$(PCH_FILES):
#	$(CXX) $(CXX_CFLAGS) -x c++-header $(PCH)


