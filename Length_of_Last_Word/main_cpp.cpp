#include <iostream>
using namespace std;

class Solution {
public:
    int lengthOfLastWord(string s) {
        // string length =s.size() or s.length();
        int count = 0;
        for (int i = s.size()-1; i>=0; i--) {
            // 使用單引號表示字元，使用雙引號表示字串
            if(s[i] == ' '){
                continue;
            }
            else {
                while(s[i] != ' ' && i >= 0){
                    count++;
                    if (i == 0){
                        break;
                    }
                    i--;
                }
                break;
            }
        }
        return count;
    }
};

int main() {
    Solution s;
    cout << s.lengthOfLastWord("Hello World") << endl;
    cout << s.lengthOfLastWord("   fly me   to   the moon  ") << endl;
    cout << s.lengthOfLastWord("luffy is still joyboy") << endl;
    cout << s.lengthOfLastWord("a") << endl;
}