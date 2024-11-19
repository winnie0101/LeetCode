#include <iostream>
#include <string>
#include <array>
#include <unordered_map>
#include <vector>
using namespace std;


// class Solution {
//     public:
//         Solution() {
//             roman_map[1000] = "M";
//             roman_map[500] = "D";
//             roman_map[100] = "C";
//             roman_map[50] = "L";
//             roman_map[10] = "X";
//             roman_map[5] = "V";
//             roman_map[1] = "I";
//         };

//         string intToRoman(int num) {
//         for (int i = 0; i < roman_array.size(); i++) {
//             if (num >= roman_array[i]) {
//                 int count = num / roman_array[i];
//                 int reminder = num % roman_array[i];
//                 int next_count = 0;
//                 if (i+1 < roman_array.size()) {
//                     next_count = reminder / roman_array[i+1];
//                 }

//                 if (count == 4) { // 4
//                     roman += roman_map[roman_array[i]];
//                     roman += roman_map[roman_array[i-1]];
//                     num = reminder;
//                 }
//                 else if (count == 1 && next_count == 4) { // 9
//                     roman += roman_map[roman_array[i+1]];
//                     roman += roman_map[roman_array[i-1]];
//                     num = num % roman_array[i+1];
//                 }
//                 else {
//                     string current_roman = roman_map[roman_array[i]];
//                     for (int j = 0; j < count; j++) {
//                         roman += current_roman;
//                     }
//                     num = reminder;
//                 }
//             }
//         }
//         return roman;
//     }

//     private:
//         unordered_map<int, string> roman_map; 
//         string roman;
//         array<int, 7> roman_array = {1000, 500, 100, 50, 10, 5, 1};

// };

class Solution {
    public:
        string intToRoman(int num) {
            for (auto it = roman_vector.begin(); it != roman_vector.end(); ++it) {
                while(num >= it->first) {
                    roman += it->second;
                    num -= it->first;
                }
            }
            return roman;
        };
    private:
        vector<pair<int, string>> roman_vector = {
            {1000, "M"},
            {900, "CM"},
            {500, "D"},
            {400, "CD"},
            {100, "C"},
            {90, "XC"},
            {50, "L"},
            {40, "XL"},
            {10, "X"},
            {9, "IX"},
            {5, "V"},
            {4, "IV"},
            {1, "I"}
        };
        string roman;

};

int main() {
    Solution s;
    cout << s.intToRoman(58) << endl;
}