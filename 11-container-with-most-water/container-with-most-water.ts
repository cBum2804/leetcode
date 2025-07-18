function maxArea(height: number[]): number {
    let left: number =0;
    let right: number = height.length-1;
    let maxArea : number =0;
    
    while(left<right){
        let h:number = Math.min(height[left], height[right]);
        let width:number = right- left;
        maxArea = Math.max(maxArea, h*width);

        if(height[left]< height[right]){
           left++; 
        }
        else{
            right--;
        }
    }
    return maxArea;
};