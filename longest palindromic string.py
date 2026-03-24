public class Solution {
    public String longestPalindrome(String s) {
        if (s == null || s.length() < 1) return "";
        
        int start = 0, end = 0;
        for (int i = 0; i < s.length(); i++) {
            // Case 1: Odd length palindrome (center is a single character)
            int len1 = expandAroundCenter(s, i, i);
            // Case 2: Even length palindrome (center is between two characters)
            int len2 = expandAroundCenter(s, i, i + 1);
            
            int maxLen = Math.max(len1, len2);
            
            // Update the start and end pointers if a longer palindrome is found
            if (maxLen > end - start) {
                start = i - (maxLen - 1) / 2;
                end = i + maxLen / 2;
            }
        }
        return s.substring(start, end + 1);
    }

    private int expandAroundCenter(String s, int left, int right) {
        while (left >= 0 && right < s.length() && s.charAt(left) == s.charAt(right)) {
            left--;
            right++;
        }
        // Return the length of the palindrome found
        return right - left - 1;
    }
}
