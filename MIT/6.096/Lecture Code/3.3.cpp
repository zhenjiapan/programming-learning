#include <iostream>

int fibonacci(int n){
    if (n == 0 || n == 1){
        return 1;
    }
    return fibonacci(n-1) + fibonacci(n-2);
}
int main(){
    int a;
    std::cout << "Enter an integer:" << std::endl;
    std::cin >> a;
    std::cout << fibonacci(a) << std::endl;
}