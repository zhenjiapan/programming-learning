#include <iostream>

void swapInts(int& a, int& b) {
    int temp = a;
    a = b;
    b = temp;
}

void Error_swapInts(int a, int b) {
    int temp = a;
    a = b;
    b = temp;
}


int main() {
    int x = 5;
    int y = 10;

    std::cout << "Before swap: x = " << x << ", y = " << y << std::endl;
    swapInts(x, y);
    std::cout << "After swap: x = " << x << ", y = " << y << std::endl;

    std::cout << "Error_Before swap: x = " << x << ", y = " << y << std::endl;
    Error_swapInts(x, y);
    std::cout << "Error_After swap: x = " << x << ", y = " << y << std::endl;

    return 0;
}
