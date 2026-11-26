#include <iostream>

int arraySum(const int a[], int n){
    int sum = 0;
    for (int i = 0; i < n; ++i) sum += a[i];
    return sum;
}
int main(){
    int values[] = {1, 2, 3, 4, 5};
    std::cout << arraySum(values, 5) << std::endl;
}