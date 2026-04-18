class Solution {
    private int count = 0;

    public int totalNQueens(int n) {
        // செங்குத்து கோடு (Columns), குறுக்கு கோடுகள் (Diagonals) ஆகியவற்றை கண்காணிக்க
        boolean[] cols = new boolean[n];
        boolean[] diag1 = new boolean[2 * n]; // இடமிருந்து வலமாக செல்லும் விட்டம் (row - col)
        boolean[] diag2 = new boolean[2 * n]; // வலமிருந்து இடமாக செல்லும் விட்டம் (row + col)
        
        backtrack(0, n, cols, diag1, diag2);
        return count;
    }

    private void backtrack(int row, int n, boolean[] cols, boolean[] diag1, boolean[] diag2) {
        // பேஸ் கேஸ்: எல்லா ராணிகளையும் வைத்தாகிவிட்டது என்றால், ஒரு தீர்வு கிடைத்துவிட்டது
        if (row == n) {
            count++;
            return;
        }

        for (int col = 0; col < n; col++) {
            int d1 = row - col + n; // Negative index வராமல் இருக்க +n செய்கிறோம்
            int d2 = row + col;

            // இந்த இடத்தில் ராணியை வைப்பது பாதுகாப்பானதா என்று பார்க்கிறோம்
            if (!cols[col] && !diag1[d1] && !diag2[d2]) {
                
                // ராணியை வைக்கிறோம் (Place)
                cols[col] = diag1[d1] = diag2[d2] = true;
                
                // அடுத்த வரிசைக்குச் செல்கிறோம் (Explore)
                backtrack(row + 1, n, cols, diag1, diag2);
                
                // வைத்த ராணியை எடுக்கிறோம் (Backtrack - மீண்டும் பழைய நிலைக்கு வருதல்)
                cols[col] = diag1[d1] = diag2[d2] = false;
            }
        }
    }
}
