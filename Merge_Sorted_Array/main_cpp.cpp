#include <iostream>
#include <vector>
using namespace std;

// class Solution {
// public:
//     void merge(vector<int>& nums1, int m, vector<int>& nums2, int n) {
//         cout << "nums1: " << nums1.size() << endl;
//         int current_a = 0;
//         int current_b = 0;
//         vector<int> result = {};
//         while (current_a < m && current_b < n) {
//             if (nums1[current_a] <= nums2[current_b]) {
//                 result.push_back(nums1[current_a]);
//                 current_a++;
//             }
//             else {
//                 result.push_back(nums2[current_b]);
//                 current_b++;
//             }
//         }

//         if (current_a == m) {
//             for (int i = current_b; i < n; i++) {
//                 result.push_back(nums2[i]);
//             }
//         }
//         else {
//             for (int i = current_a; i < m; i++) {
//                 result.push_back(nums1[i]);
//             }
//         }
//         nums1 = result;
//     }
// };

class Solution {
public:
    void merge(vector<int>& nums1, int m, vector<int>& nums2, int n) {
        int current_a = m - 1;
        int current_b = n - 1;
        int max = m + n - 1;
        while (current_a >= 0 && current_b >= 0) {
            if (nums1[current_a] >= nums2[current_b]) {
                nums1[max] = nums1[current_a];
                current_a--;
            } else {
                nums1[max] = nums2[current_b];
                current_b--;
            }
            max--;
        }
        
        while (current_b >= 0) {
            nums1[max] = nums2[current_b];
            current_b--;
            max--;
        }
    }

};

int main() {
    Solution s;
    vector<int> nums1 = {1,2,3,0,0,0};
    vector<int> nums2 = {2,5,6};
    s.merge(nums1, 3, nums2, 3);
    for (int i = 0; i < nums1.size(); i++) {
        cout << nums1[i] << " ";
    }

    vector<int> nums3 = {0};
    vector<int> nums4 = {1};
    s.merge(nums3, 0, nums4, 1);
    for (int i = 0; i < nums3.size(); i++) {
        cout << nums3[i] << " ";
    }

    vector<int> nums5 = {2,0};
    vector<int> nums6 = {1};
    s.merge(nums5, 1, nums6, 1);
    for (int i = 0; i < nums5.size(); i++) {
        cout << nums5[i] << " ";
    }
}