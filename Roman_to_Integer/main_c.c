#include <stdio.h>
#include <stdlib.h>
#include <string.h>

typedef struct Roman {
    char* roman;
    int value;
}Roman;

Roman romans[7] = {
    {"I", 1},
    {"V", 5},
    {"X", 10},
    {"L", 50},
    {"C", 100},
    {"D", 500},
    {"M", 1000}
};

int romanToInt(char* s) {
    int result = 0;
    int len = strlen(s);
    for (int i = 0; i < len; i++){
        for (int j = 0; j < 7; j++) {
            if (s[i] == romans[j].roman[0]){
                result += romans[j].value;
            }
        }
    }

    return result;
};

int main() {
    const char* s = "MCMXCIV";
    printf("%d\n", romanToInt((char*) s));
    
}