import java.util.ArrayDeque;
import java.util.HashMap;

public class JavaParser {
    private HashMap<Character, Character> punctuationPairs;

    public JavaParser() {
        // We will want to look up opening punctuation (value) with closing punctuation
        // (key). We'll initialize this in the constructor.
        punctuationPairs = new HashMap<>();
        punctuationPairs.put(')', '(');
        punctuationPairs.put(']', '[');
        punctuationPairs.put('}', '{');
    }

    /*
     * This method checks whether a string is valid Java syntax with respect to
     * open and closed parentheses, brackets, and braces.
     */
    public boolean hasMatchingPunctuation(String input) {
        ArrayDeque<Character> punctuationStack = new ArrayDeque<>();

        // Loop through each character in the input string by index
        for (int i = 0; i < input.length(); i++) {
            // Get the current character
            char c = input.charAt(i);

            if (c == '(' || c == '[' || c == '{') {
                // We found an opening punctuation. Push it onto the stack.
                punctuationStack.push(c);

            } else if (c == ')' || c == ']' || c == '}') {
                // We found a closing punctuation.
                if (punctuationStack.isEmpty()) {
                    // The closing punctuation does not have a corresponding
                    // opening punctuation: unmatched closing punctuation
                    return false;
                }

                // Get the most recent opening punctuation from the stack.
                char top = punctuationStack.pop();
                if (top != punctuationPairs.get(c)) {
                    // The most recent opening punctuation does not match the
                    // current closing punctuation: mismatched punctuation
                    return false;
                }
            }
        }

        // At this point, we've gone through the entire input string.
        if (!punctuationStack.isEmpty()) {
            // We're done going through the string, but something is
            // left on the stack: unmatched opening punctuation
            return false;
        }

        // If we get here, the syntax is valid. Otherwise we would have returned false.
        return true;
    }
}