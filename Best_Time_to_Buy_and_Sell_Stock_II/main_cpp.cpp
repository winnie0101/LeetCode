#include <iostream>
#include <vector>
using namespace std;

// Greedy Algorithm

class Solution {
public:
    int maxProfit(vector<int>& prices) {
        int profit = 0;
        for (int i=1; i<prices.size(); i++) {
            if (prices[i] > prices[i-1]) {
                profit += prices[i] - prices[i-1];
            }
        }
        return profit;
    }
};

int main() {
    Solution s;
    vector<int> prices = {7, 1, 5, 3, 6, 4};
    cout << s.maxProfit(prices) << endl;
    vector<int> prices2 = {1, 2, 3, 4, 5};
    cout << s.maxProfit(prices2) << endl;
    vector<int> prices3 = {7, 6, 4, 3, 1};
    cout << s.maxProfit(prices3) << endl;
}