#include <iostream>
#include <vector>
#include <map>
using namespace std;


// time complexity: O(n)
// space complexity: O(n)
// class Solution {
// public:
//     int majorityElement(vector<int>& nums) {
//         int max_time = nums.size() / 2;
//         map<int, int> count_map;

//         for (int i = 0; i < nums.size(); i++) {
//             if (count_map.find(nums[i]) == count_map.end()) {
//                 count_map[nums[i]] = 1;
//             }
//             else {
//                 count_map[nums[i]]++;
//             }

//             if (count_map[nums[i]] > max_time) {
//                 return nums[i];
//             }
//         }
//         return -1;
//     }
// };


// time complexity: O(n)
// space complexity: O(1)
class Solution {
    public:
    int majorityElement(vector<int>& nums) {
        // Boyer-Moore Voting Algorithm
        int count = 0;
        int candidate = 0;

        for (int i = 0; i < nums.size(); i++) {
            if (count == 0) {
                candidate = nums[i];
            }
            if (candidate == nums[i]) {
                count++;
            }
            else {
                count--;            
            }
        }
        return candidate;
    }
};

int main() {
    Solution s;
    vector <int> nums = {2,2,1,1,1,2,2};
    cout << s.majorityElement(nums) << endl;
}