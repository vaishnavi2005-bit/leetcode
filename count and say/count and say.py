class Solution:
    def countAndSay(self, n: int) -> str:
        # Base case
        if n == 1:
            return "1"
        
        # Get the previous term
        prev = self.countAndSay(n - 1)
        
        # Generate the current term by "reading" the previous one
        result = []
        i = 0
        while i < len(prev):
            count = 1
            # Count consecutive identical characters
            while i + 1 < len(prev) and prev[i] == prev[i+1]:
                count += 1
                i += 1
            
            # Append "count" followed by "digit"
            result.append(str(count))
            result.append(prev[i])
            i += 1
            
        return "".join(result)
