#include <iostream>

int main(){
    int twoDimArray[2][4] = {
        {6, 0, 9, 6},
        {2, 0, 1, 1}
    };

    for (int row = 0; row < 2; ++row){
        for (int col = 0; col < 4; ++col){
            std::cout << twoDimArray[row][col] << ' ';
        }
        std::cout << '\n';
    }
}