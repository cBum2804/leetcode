class Solution {
    public boolean isPalindrome(int x) {
        if(x<0){
            return false;
        }
        if(x==0){
            return true;
        }

        int reversed= 0;
        int digit =0;
        int temp =x;

        while(temp!=0){
            digit = temp%10;
            reversed = reversed*10+ digit;
            temp/=10;
        }
        return x== reversed;
    }
}