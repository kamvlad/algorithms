#include <iostream>
#include <iterator>
#include <vector>

using namespace std;

template<typename InputIterator>
void print(InputIterator first, InputIterator end) {
	ostream_iterator<typename InputIterator::value_type> itOut(cout, ", ");
	std::copy(first, end, itOut);
	cout << endl;
}

template<typename RandomAccessIterator>
RandomAccessIterator randomizedPartion(RandomAccessIterator first, RandomAccessIterator end) {
	auto dist = distance(first, end);
	size_t pivot = rand() % dist;

	--end;
	swap(*(first + pivot), *end);

	auto it = first;

	while ((it != end) && (*it < *end)) {
		it++;
	}

	auto it2 = it + 1;

	while (it2 != end) {
		if (*it2 < *it) {
			swap(*it, *it2);
			it++;
		}
		it2++;
	}

	swap(*it, *it2);
	return it;
}

template<typename RandomAccessIterator>
RandomAccessIterator randomizedSelect(RandomAccessIterator first, RandomAccessIterator end, size_t p) {
	RandomAccessIterator pivot = randomizedPartion(first, end);
	auto d = distance(first, pivot);
	print(first, end);

	if (d == p) {
		return pivot;
	} else if (d > p) {
		return randomizedSelect(first, pivot, d - p);
	} else {
		return randomizedSelect(pivot, end, p - d);
	}
}

int main(int argc, char *argv[]) {
	vector<int> v = {1, 0, -10, 3, 6, 9, -14}; // -14, -10, 0, 1, 3, 6, 9

	cout << *randomizedSelect(v.begin(), v.end(), 4) << endl;

	return 0;
}