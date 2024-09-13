class Solution {
    public int minEatingSpeed(int[] piles, int h) {
       int min_speed = 1;
       int max_speed = 0;

       for(int pile: piles){
        max_speed = Math.max(pile, max_speed);
       }

       while(min_speed < max_speed){
        int mid = min_speed + (max_speed - min_speed)/2;

        if(canEat(piles,h,mid)){
            max_speed = mid;
        }
        else{
            min_speed = mid+1;
        }
       }
        return min_speed;
    }

    public boolean canEat(int [] piles,int h, int speed){
        int hours = 0;
        for(int pile: piles){
            hours += (int) Math.ceil((double)pile/speed); 
        }
        return hours<=h;
    }
}
