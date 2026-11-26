#include <iostream>

int raiseToPower(int base, int exponent) {
    int result = 1;
    for (int i = 0; i < exponent; ++i) {
        result *= base;
    }
    return result;
}
int main() {
    int base, exponent;
    std::cout << "Enter base: ";
    std::cin >> base;
    std::cout << "Enter exponent: ";
    std::cin >> exponent;

    int result = raiseToPower(base, exponent);
    std::cout << base << " raised to the power of " << exponent << " is " << result << std::endl;

    return 0;
}