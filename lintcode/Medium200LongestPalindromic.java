package lintcode;

import java.util.Arrays;

public class Medium200LongestPalindromic {
    /**
     * @param s: input string
     * @return: a string as the longest palindromic substring
     */
    //中心扩展1
    public static String longestPalindromeMid1(String s) {
        String res  = "";
        for (int i = 0; i < s.length(); i++) {
            int left = i;
            int right = i;
            // iterate until s[right]!=s[left] and start extend left and right
            while (right<s.length() && s.charAt(left)==s.charAt(right)) {
                right ++;
            }
            if(right-left+1>res.length()){
                res = s.substring(left,right);
            }
            // extend left and right to search longest palindrome string with s[i] as center
            while(left>=0 && right<=s.length()){
                if(isPalindrome(s.substring(left,right))){
                    if(right-left+1>res.length()){
                        res= s.substring(left,right );
                    }
                    left--;
                    right++;
                }else{
                    break;
                }
            }

        }

        return res;
    }

    // 中心扩展2
    public static String longestPalindromeMid2(String s){
        if(s==null || s.length() <=1){
            return s;
        }
        int start = 0, len = 0, longest = 0;
        for (int i = 0; i < s.length(); i++) {
            // mid is 2 num
            if(i<s.length()-1 && s.charAt(i) ==s.charAt(i+1)){
                len = findLongestPalindromeFrom(s,i,i+1);
                if(len>longest){
                    longest = len;
                    start = i- len/2 +1;
                }
            }else{
                // mid is 1 num
                len = findLongestPalindromeFrom(s, i, i);
                if (len > longest) {
                    longest = len;
                    start = i - len / 2;
                }

            }

        }
        return s.substring(start, start+longest);
    }

    // dp
    public static String longestPalindromeDP(String s){
        int [][] dp = new int[s.length()][s.length()];
        for (int i = 0; i < dp.length; i++) {
            dp[i][i] = 1;
            if(i<dp.length - 1 && s.charAt(i) ==s.charAt(i+1)){
                dp[i][i+1] =1;
            }
        }

        for(int i = dp.length-1; i >=0; i--){
            for (int j = i+1; j <dp.length; j++) {
                if(s.charAt(i) == s.charAt(j) && dp[i+1][j-1]==1){
                    dp[i][j] = 1;
                }
            }
        }
        String res  ="";
        for (int i =0;i<dp.length;i++){
            for (int j = i; j < dp.length; j++) {
                if(dp[i][j] ==1 && j-i+1>res.length()){
                    res = s.substring(i,j+1);
                }
            }
        }

        return  res;
    }



    public static int findLongestPalindromeFrom(String s, int left, int right) {
        int len = 0;
        while(left>=0 && right<s.length()){
            if(s.charAt(left) != s.charAt(right)){
                break;
            }
            len += left==right ? 1 : 2;
            left --;
            right ++;
        }
        return len;
    }


    public static boolean isPalindrome(String s){
        int front = 0;
        int end = s.length()-1;
        while(front<=end){
            if(s.charAt(front) !=s.charAt(end)){
                return false;
            }
            front ++;
            end --;
        }
        return true;
    }

    public static void main(String[] args) {
        String s = "";
        System.out.println(longestPalindromeDP(s));
    }
}
