#include <iostream>

int main() {
    int n;
    do {
        std::cout << "Enter a positive integer: ";
        std::cin >> n;
    } while (n <= 0);
    std::cout << "Accepted: " << n << std::endl;
    return 0;
}