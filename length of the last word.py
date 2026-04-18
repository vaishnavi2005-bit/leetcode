class Solution {
    public int lengthOfLastWord(String s) {
        int length = 0;
        int i = s.length() - 1;

        // 1. கடைசியில் இருக்கும் இடைவெளிகளைத் தவிர்க்க
        while (i >= 0 && s.charAt(i) == ' ') {
            i--;
        }

        // 2. கடைசி வார்த்தையின் எழுத்துக்களை எண்ண
        while (i >= 0 && s.charAt(i) != ' ') {
            length++;
            i--;
        }

        return length;
    }
}
