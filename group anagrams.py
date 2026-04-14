import java.util.*;

class Solution {
    public static List<List<String>> groupAnagrams(String[] strs) {
        
        // Step 1: Create HashMap to store grouped anagrams
        HashMap<String, List<String>> map = new HashMap<>();

        // Step 2: Loop through each word
        for (String word : strs) {
            
            // Convert word to character array
            char[] arr = word.toCharArray();
            
            // Sort characters
            Arrays.sort(arr);
            
            // Convert sorted array back to string (key)
            String key = new String(arr);

            // Step 3: If key not present, create new list
            if (!map.containsKey(key)) {
                map.put(key, new ArrayList<>());
            }

            // Step 4: Add word to corresponding list
            map.get(key).add(word);
        }

        // Step 5: Return all grouped anagrams
        return new ArrayList<>(map.values());
    }

    // Main method to test
    public static void main(String[] args) {
        String[] strs = {"eat", "tea", "tan", "ate", "nat", "bat"};

        List<List<String>> result = groupAnagrams(strs);

        System.out.println(result);
    }
}
