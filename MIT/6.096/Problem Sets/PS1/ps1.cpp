#include <iostream>

// int main(){
//     const char* str = "Hello, World!";
//     std::cout << str << std::endl;
// }

// int main(){
//     int n;
//     std::cout << "Enter a nonnegative number: ";
//     std::cin >> n;
//     for (; n-- > 0; ) {
//         std::cout << "Hello, World!" << std::endl;
//     }
    // return 0;
// }

// int main(){
//     int n;
//     std::cout << "Enter a nonnegative number: ";
//     std::cin >> n;
//     while (n-- > 0) {
//         std::cout << "Hello, World!" << std::endl;
//     }
//     return 0;
// }

// int main(){
//     int n;
//     std::cout << "Enter a nonnegative number: ";
//     std::cin >> n;
//     do {
//         std::cout << "Hello, World!" << std::endl;
//     } while (--n > 0);
//     return 0;
// }

// int main(){
//     int N;
//     std::cout << "Enter the number of integers in the list: ";
//     std::cin >> N;

//     int x;
//     std::cin >> x;
    
//     double minVal = x;
//     double maxVal = x;
//     long long sum = x;

//     for (int i = 0; i < N - 1; i++) {
//         std::cin >> x;
//         if (x < minVal) {
//             minVal = x;
//         }
//         if (x > maxVal) {
//             maxVal = x;
//         }
//         sum += x;
//     }

//     std::cout << "Mean: " << sum / N << std::endl;
//     std::cout << "Maximum: " << maxVal << std::endl;
//     std::cout << "Minimum: " << minVal << std::endl;
//     std::cout << "Range: " << maxVal - minVal << std::endl;

//     return 0;
// }

// int main(){
//     int N;
//     std::cin >> N;

//     for (int i = 2; N > 0; ++i) {
//         bool isPrime = true;
//         for (int j = 2; j < i; ++j) {
//             if (i % j == 0) {
//                 isPrime = false;
//                 break;
//             }
//         }
//         if (isPrime) {
//             std::cout << i << std::endl;
//             --N;
//         }
//     }
// }

// int main(){
//     while (true) {
//         int N;
//         std::cin >> N;
//         std::cout << (N >= 0 && N % 5 == 0 ? N / 5 : -1) << std::endl;
//     }
//     return 0;
// }

// int main(){
//     while (true) {
//         int N;
//         std::cin >> N;
//         if (N < 0 || N % 5 != 0) {
//             std::cout << -1 << std::endl;
//             continue;
//         }
//         std::cout << N / 5 << std::endl;
//     }
//     return 0;
// }

int main(){
    while (true) {
        int N;
        std::cin >> N;
        if (N == -1) {
            break;
        }
        if (N < 0 || N % 5 != 0) {
            std::cout << -1 << std::endl;
            continue;
        }
        std::cout << N / 5 << std::endl;
    }
    return 0;
}

