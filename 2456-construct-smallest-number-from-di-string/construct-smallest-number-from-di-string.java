import java.util.*;

class Solution {
    public String smallestNumber(String pattern) {
        StringBuilder result = new StringBuilder();
        Stack<Integer> stack = new Stack<>();

        // We use numbers 1 to (n+1)
        int num = 1;
        
        for (int i = 0; i <= pattern.length(); i++) {
            stack.push(num++); // Push the current number
            
            // If it's the last iteration or we see 'I', pop the stack
            if (i == pattern.length() || pattern.charAt(i) == 'I') {
                while (!stack.isEmpty()) {
                    result.append(stack.pop()); // Pop elements and append to result
                }
            }
        }
        
        return result.toString();
    }
}
