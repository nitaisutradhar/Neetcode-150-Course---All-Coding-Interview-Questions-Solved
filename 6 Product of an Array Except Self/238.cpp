#include<iostream>
#include<vector>
using namespace std;
class Solution{
public:
    vector<int> productExceptSelf(vector<int>&nums){
        int n = nums.size();
        vector<int> result(n,1); //initialize a vector of a specific size (n in this case) with a default value (1)

        int prefix = 1;
        for(int i =0;i<n;i++){
            result[i] = prefix;
            prefix *= nums[i];
        }

        int postfix = 1;
        for(int i = n-1;i>=0;i--){
            result[i] *= postfix;
            postfix *= nums[i];
        }

        return result;
    }
};
int main()
{
    Solution sol;
    vector<int> nums = {1,2,3,4};
    vector<int> result1= sol.productExceptSelf(nums);
    cout << "test case 1: ";
    for(int i: result1){
        cout<< i << " ";
    }
}

//Time Complexity: O(n)
//Space Complexity: O(1)
