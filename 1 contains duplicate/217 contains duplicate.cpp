#include<iostream>
#include<vector>
#include<unordered_set>
using namespace std;
class Solution {
    public:bool containsDuplicate(vector<int>&nums){
        unordered_set<int> numSet;

        for(int n: nums){
            if(numSet.count(n)){
                return true;
            }
            numSet.insert(n);
        }
        return false;
    }
};

int main(){
    Solution sol;
    vector<int> num1 = {1,2,3,1};
    vector<int> num2 = {1,2,3,4};
    cout << boolalpha;
    cout << "num1 contains duplicate " << sol.containsDuplicate(num1) << endl;
    cout << "contains duplicate " << sol.containsDuplicate(num2) << endl;
}
