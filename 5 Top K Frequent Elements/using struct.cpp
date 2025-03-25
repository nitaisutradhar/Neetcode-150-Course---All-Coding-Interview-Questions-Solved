#include<iostream>
#include<vector>
#include<unordered_map>
#include<queue>
#include<algorithm>
using namespace std;

class Solution{
    struct node{
        int no;
        int freq;
        node(int a, int b) // constructor for value initialization for each node
        {
            no = a;
            freq = b;
        }
    };
    struct compare { // Maintain the MAX-HEAP based on frequency
        bool operator()(node const& a, node const& b)
        {
            return a.freq < b.freq;
        }
    };
public:
    vector<int> topKFrequent(vector<int>& nums, int k){
        unordered_map<int,int> m;
        for(int ele: nums){
            m[ele]+= 1;
        }

        priority_queue<node, vector<node>, compare> heap; // Compare defines a max-heap based on frequency
        for(auto it: m)
            heap.push(node(it.first,it.second));

        vector<int>ans;
        while(k-- > 0 & !heap.empty()){
            node temp = heap.top();
            heap.pop();
            ans.push_back(temp.no);
        }
        return ans;
    }
};
int main(){
    Solution sol;
    vector<int> num1 = {1,1,1,2,2,3};
    int k1 = 2;
    vector<int> result1= sol.topKFrequent(num1,k1);
    int arr[result1.size()];
    copy(result1.begin(),result1.end(),arr);
    cout << "test case 1: ";
    for(int i: arr){
        cout<< i << " ";
    }

}
