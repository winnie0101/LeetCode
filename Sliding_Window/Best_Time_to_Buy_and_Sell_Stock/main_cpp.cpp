# include <iostream>
# include <vector>
using namespace std;

class Solution {
public:
    int maxProfit(vector<int>& prices) {
        int buy_price = prices[0];
        int profit = 0;
        for (int i=1; i<prices.size(); i++) {
            if (prices[i] < buy_price) {
                buy_price = prices[i];
            }
            else {
                profit = max(profit, prices[i] - buy_price);
            }
        }
        
        return profit;
    }
};

int main() {
    Solution s;
    vector<int> prices = {7, 1, 5, 3, 6, 4};
    cout << s.maxProfit(prices) << endl;
    vector<int> prices2 = {7, 6, 4, 3, 1};
    cout << s.maxProfit(prices2) << endl;
    vector<int> prices3 = {2, 4, 1};
    cout << s.maxProfit(prices3) << endl;
}