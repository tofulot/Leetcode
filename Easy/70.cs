public class Solution {
    int value = 0;
    public int ClimbStairs(int n) {
        int Path1 = 1;
        int Path2 = 1;
        int value = 1;
        for (int i=2; i <= n; i++) {
            value = Path1 + Path2;
            Path2 = Path1;
            Path1 = value;
        }

        return Path1;
    }
}