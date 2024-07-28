class Solution {
    public int maxArea(int[] height) {
        int left=0;
        int right = height.length-1;
        int max_Area = 0;
        while(left< right){
            int h = Math.min(height[left],height[right]);
            int w = right - left;
            int area = h*w;
            max_Area = Math.max(area, max_Area);

            if(height[left]<height[right]){
                left++;
            }
            else{
                right--;
            }
        }
        return max_Area;

    }
}