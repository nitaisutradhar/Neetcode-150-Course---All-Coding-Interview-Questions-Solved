#include<iostream>
using namespace std;
class Solution{
public:
    bool isAnagram(string s, string t){
        int c[26] = {0};
        for(char x: s){
            c[x - 'a']++;
        }
        for(char x: t){
            c[x-'a']--;
        }
        for(int val: c){
            if(val!=0){
                return false;
            }
        }
        return true;
    }

};
int main(){
    Solution sol;
    string s = "anagram";
    string t = "nagaram";
    cout << boolalpha << sol.isAnagram(s, t) << endl;
}
