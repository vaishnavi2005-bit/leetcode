import java.util.ArrayList;
import java.util.List;

class Solution {
    public String convert(String s, int numRows) {
        // Edge case: If there's only one row or string is too short, return as is
        if (numRows == 1 || s.length() <= numRows) {
            return s;
        }

        // Initialize a list of StringBuilders, one for each row
        List<StringBuilder> rows = new ArrayList<>();
        for (int i = 0; i < Math.min(numRows, s.length()); i++) {
            rows.add(new StringBuilder());
        }

        int currentRow = 0;
        boolean goingDown = false;

        // Iterate through each character in the input string
        for (char c : s.toCharArray()) {
            rows.get(currentRow).append(c);

            // Change direction when hitting the top (0) or bottom (numRows - 1)
            if (currentRow == 0 || currentRow == numRows - 1) {
                goingDown = !goingDown;
            }

            // Move pointer up or down
            currentRow += goingDown ? 1 : -1;
        }

        // Combine all rows into a single string
        StringBuilder result = new StringBuilder();
        for (StringBuilder row : rows) {
            result.append(row);
        }

        return result.toString();
    }
}

        
