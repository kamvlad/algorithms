#include <memory>
#include <iostream>
#include <string>

using namespace std;

class Foo {
public:
    Foo(int i) { std::cout << "Foo()" << endl; }
    Foo(const Foo&) { std::cout << "Copyctr Foo" << std::endl; }
    Foo(Foo&&) noexcept { std::cout << "Movectr Foo" << std::endl; }
    Foo& operator= (const Foo&) { std::cout << "Copy Foo" << std::endl; return *this; }
    Foo& operator= (Foo&&) { std::cout << "Move Foo" << std::endl; return *this; }
    ~Foo() { std::cout << "~Foo()" << std::endl; }
};

template<typename T>
class DynamicTable {
public:
    DynamicTable() : data_(nullptr), capacity_(0), elementsCount_(0) {
    }
    
    DynamicTable(const DynamicTable&) = delete;
    DynamicTable& operator=(const DynamicTable&) = delete;
    DynamicTable(DynamicTable&&) = delete;
    DynamicTable& operator=(DynamicTable&&) = delete;
    
    void push(const T& element) {        
        checkCapacity();
        data_[elementsCount_] = element;
        elementsCount_ += 1;      
    }
    
    void push(T&& element) {
        checkCapacity();
        data_[elementsCount_] = std::move(element);
        elementsCount_ += 1;
    }
    
    size_t getCapacity() { return capacity_; }
    size_t getElementsCount() { return elementsCount_; }
    
    ~DynamicTable() {
        if (data_) {
            for (size_t i = 0; i < elementsCount_; ++i) {
                data_[i].~T();
            }
            operator delete[] (data_);
        }
    }
private:
    void checkCapacity() {
        if (capacity_ == 0) {
            data_ = static_cast<T*>(operator new[] (sizeof(T)));
            capacity_ = 1;
        }
        
        if (elementsCount_ == capacity_) {
            T *newData = static_cast<T*>(operator new[] (2 * capacity_ * sizeof(T)));
            
            for (; elementsCount_ > 0; --elementsCount_) {
                int i = elementsCount_ - 1;
                newData[i] = std::move(data_[i]); 
                data_[i].~T();
            }
            
            if (data_) {
                operator delete[] (data_);
            }
            data_ = newData;
            elementsCount_ = capacity_;
            capacity_ = 2 * capacity_;
        }
    }
private:
    T *data_;
    size_t capacity_;
    size_t elementsCount_;
};

int main()
{
    DynamicTable<Foo> dt;

    Foo a(1);
    Foo b(1);
    Foo c(1);
    
    std::cout << dt.getCapacity() << ", " << dt.getElementsCount() << std::endl;
    dt.push(a);
    std::cout << dt.getCapacity() << ", " << dt.getElementsCount() << std::endl;
    dt.push(b);
    std::cout << dt.getCapacity() << ", " << dt.getElementsCount() << std::endl;
    dt.push(c);
    std::cout << dt.getCapacity() << ", " << dt.getElementsCount() << std::endl;
}
