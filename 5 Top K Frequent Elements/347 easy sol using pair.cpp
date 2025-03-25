#include<iostream>
#include<vector>
#include<unordered_map>
#include<queue>
#include<algorithm>
using namespace std;
class Solution{
public:
    vector<int> topKFrequent(vector<int>& nums, int k){
        unordered_map<int,int> m;
        for(int num: nums){
            m[num]++;
        }
        vector<int>res;

        priority_queue<pair<int,int>>pq;
        for(auto it= m.begin();it != m.end();it++){
            pq.push(make_pair(it->second, it->first));

            if(pq.size() > (int)m.size()-k){
                res.push_back(pq.top().second);
                pq.pop();
            }
        }
        return res;
    }
};
int main(){
    Solution sol;
    vector<int> num1 = {1,1,1,1,2,2,2,3};
    int k1 = 2;
    vector<int> result1= sol.topKFrequent(num1,k1);
    cout << "test case 1: ";
    for(int i: result1){
        cout<< i << " ";
    }

}
