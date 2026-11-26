#include <cstring>
#include <iostream>

int main(){
    char fragment1[] = "I'm a s";
    const char fragment2[] = "ring!";
    char finalString[32] = "";
    std::strcpy(finalString, fragment1);
    std::strcat(finalString, fragment2);
    std::cout << finalString << std::endl;
}