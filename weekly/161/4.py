class Solution(object):
    def isGoodArray(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """



# class Solution {
# public:
#     int gcd(int a,int b){return b==0?a:gcd(b,a%b);}
#     bool isGoodArray(vector<int>& a) {
#         int g=a[0];
#         for(int i:a) g=gcd(i,g);
#         if(g==1) return 1;
#         return 0;
#     }
# };