#include <iostream>

int divide(int a, int b, int& remainder) {
    if (b == 0) {
        throw std::invalid_argument("Division by zero");
    }
    remainder = a % b;
    return a / b;
}
int main() {
    int a = 10;
    int b = 3;
    int remainder = 0;

    try {
        int result = divide(a, b, remainder);
        std::cout << "Result: " << result << ", Remainder: " << remainder << std::endl;
    } catch (const std::invalid_argument& e) {
        std::cerr << "Error: " << e.what() << std::endl;
    }

    return 0;
}