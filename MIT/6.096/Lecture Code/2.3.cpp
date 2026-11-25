#include <iostream>

int main() {
    int i = 0;
    int sum = 0;
    while (i < 10) {
        sum += i;
        i++;
    }
    std::cout << "The sum of integers from 0 to 9 is: " << sum << std::endl;
    return 0;
}