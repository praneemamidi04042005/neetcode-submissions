class Solution {
    public double myPow(double x, int n) {
        double pow;
        if(n<0){
            n*=-1;
            pow=1;
            for(int i=0;i<n;i++) pow/=x;
            return pow;
        }
        pow=1;
        for(int i=0;i<n;i++) pow*=x;
        return pow;
    }
}
