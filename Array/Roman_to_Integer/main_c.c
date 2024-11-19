#include <stdio.h>
#include <stdlib.h>
#include <string.h>

// typedef struct Roman {
//     const char* roman;
//     int value;
//     struct Roman* next;
// }Roman;

// Roman romans[7] = {
//     {"I", 1, NULL},
//     {"V", 5, NULL},
//     {"X", 10, NULL},
//     {"L", 50, NULL},
//     {"C", 100, NULL},
//     {"D", 500, NULL},
//     {"M", 1000, NULL}
// };

// void initRoman(Roman* romans){
//     for (int i = 0; i < 6; i++) {
//         romans[i].next = &romans[i + 1];
//     }
// }

// Roman* searchRoman(char roman_s, Roman* romans) {
//     Roman* current_roman = &romans[0];
//     while(current_roman != NULL) {
//         if (roman_s == *current_roman->roman) {
//             return current_roman;
//         }
//         current_roman = current_roman->next;
//     }
//     return NULL;
// }

// int romanToInt(char* s) {
//     initRoman(romans);
//     int result = 0;
//     int len = strlen(s);
//     for (int i = 0; i < len; i++){
//         char current_char = s[i];
//         if (i == len - 1) {
//             Roman* current_roman = searchRoman(current_char, romans);
//             result += current_roman->value;
//             break;
//         }
//         char next_char = s[i + 1];
//         char two_char[3];
//         two_char[0] = current_char;
//         two_char[1] = next_char;
//         two_char[2] = '\0';

//         if(strcmp(two_char, "IV") == 0 || strcmp(two_char, "IX") == 0 || 
//         strcmp(two_char, "XL") == 0 || strcmp(two_char, "XC") == 0 || 
//         strcmp(two_char, "CD") == 0 || strcmp(two_char, "CM") == 0) {
//             Roman* current_roman = searchRoman(current_char, romans);
//             Roman* next_roman = searchRoman(next_char, romans);
//             int value = next_roman->value - current_roman->value;
//             result += (next_roman->value - current_roman->value);
//             i++;
//             continue;
//         }
//         else {
//             Roman* current_roman = searchRoman(current_char, romans);
//             result += current_roman->value;
//         }
        
//     }

//     return result;
// };


int roman_values[128];

void initRomansValue() {
    roman_values['I'] = 1;
    roman_values['V'] = 5;
    roman_values['X'] = 10;
    roman_values['L'] = 50;
    roman_values['C'] = 100;
    roman_values['D'] = 500;
    roman_values['M'] = 1000;
}

int romanToInt(char* s){
    initRomansValue();
    int result = 0;
    int len = strlen(s);

    for(int i = 0; i < len; i++) {
        int current_value = roman_values[s[i]];
        if (i < len - 1 && current_value < roman_values[s[i+1]]) {
            result += roman_values[s[i+1]] - current_value;
            i++;
        }
        else {
            result += current_value;
        }
    }
    return result;
}

int main() {
    const char* s = "MCMXCIV";
    printf("%d\n", romanToInt((char*) s));
    
}