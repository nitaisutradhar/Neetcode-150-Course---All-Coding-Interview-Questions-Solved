#include<iostream>
#include<vector>
#include<unordered_set>
#include<algorithm>
using namespace std;

class Solution{
public:
    int longestConsecutive(vector<int>& nums){
        if(nums.empty()) return 0;

        unordered_set<int> numSet(nums.begin(),nums.end());
        int longestSub = 1;

        for(int num:numSet){
            if(numSet.count(num-1)) continue;
            else{
                int currentNum = num;
                int currentSub = 1;
                while(numSet.count(currentNum+1)){
                    currentNum++;
                    currentSub++;
                }
                longestSub = max(longestSub, currentSub);
            }
        }
        return longestSub;
    }
};

int main() {
    Solution sol;

    // Test cases
    vector<vector<int>> testCases = {
        {100, 4, 200, 1, 3, 2},
        {0, 3, 7, 2, 5, 8, 4, 6, 0, 1},
        {},
        {1},
        {1, 2, 3, 4, 5},
        {5,4,3,2,1},
        {1,2,2,3,4,5},
        {1,2,0,1},
        {9,1,4,7,3,-1,0,5,-1,6,-1,1},

    };

    vector<int> expectedResults = {4, 9, 0, 1, 5, 5, 5, 3, 7};

    for (size_t i = 0; i < testCases.size(); ++i) {
        int result = sol.longestConsecutive(testCases[i]);
        cout << "Test Case " << i + 1 << ": ";
        if (result == expectedResults[i]) {
            cout << "Passed. Result: " << result << endl;
        } else {
            cout << "Failed. Expected: " << expectedResults[i] << ", Got: " << result << endl;
        }
    }

    return 0;
}

//Time Complexity: O(n)
//Space Complexity: O(n)
