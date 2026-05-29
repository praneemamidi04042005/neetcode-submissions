class Solution {
    public int[] maxSlidingWindow(int[] nums, int k) {
        int[] a=new int[nums.length-k+1];

        for(int i=0;i<=nums.length-k;i++){
            int max=Integer.MIN_VALUE;
            for(int j=i;j<i+k;j++){
                if(nums[j]>max) max=nums[j];
            }
            a[i]=max;
        }
        return a;   
    }
}
