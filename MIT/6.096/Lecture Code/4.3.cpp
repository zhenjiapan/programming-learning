#include <cctype>
#include <cstring>
#include <iostream>

int main(){
    char text[] = "tjgDGB8245gDG.B8.21B89.gD";
    for (int i = 0; text[i] != '\0'; ++i) {
        unsigned char ch = static_cast<unsigned char>(text[i]);
        if (std::isalpha(ch)){
            std::cout << static_cast<char>(std::tolower(ch));
        } else if (std::ispunct(ch)) {
            std::cout << ' ';
        }
    }
    std::cout << '\n';
}