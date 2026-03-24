import java.util.HashSet;
import java.util.Set;

public class Solution {
    public int lengthOfLongestSubstring(String s) {
        int start = 0;
        int end = 0;
        int maxLength = 0;
        Set<Character> seenCharacters = new HashSet<>();

        while (end < s.length()) {
            char currentChar = s.charAt(end);
            
            if (seenCharacters.contains(currentChar)) {
                // Remove the character at 'start' and move the left pointer
                seenCharacters.remove(s.charAt(start));
                start++;
            } else {
                seenCharacters.add(currentChar);
                end++;
                maxLength = Math.max(maxLength, seenCharacters.size());
            }
        }
        return maxLength;
    }
}
