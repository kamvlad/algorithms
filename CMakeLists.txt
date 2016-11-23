cmake_minimum_required(VERSION 3.5)
project(algorithms)

set(CMAKE_CXX_FLAGS "${CMAKE_CXX_FLAGS} -std=c++11")

add_executable(randomizedSelect 9_MediansAndSeqStat/randomizedSelect.cpp)
add_executable(permutations 0_Others/permutations.cpp)