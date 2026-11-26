#include <iostream>

int square(int x) {
    return x * x;
}
void print_square(int x) {
    if (x <= 0) return;
    std::cout << "The square of " << x << " is " << square(x) << std::endl;
}
int main() {
    int number;
    std::cout << "Enter an integer: ";
    std::cin >> number;

    print_square(number);

    return 0;
}