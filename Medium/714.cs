public class Solution {
    public int MaxProfit(int[] prices, int fee) {
        int prof = 0; int buy = prices[0]+fee;
        for (int i=1; i < prices.Length; ++i) {
            prof = Math.Max(prof, prices[i]-buy);
            buy = Math.Min(buy, prices[i]+fee-prof);
        }
        return prof;
    }
}