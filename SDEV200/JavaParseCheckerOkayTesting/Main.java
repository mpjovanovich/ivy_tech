import java.nio.file.Files;
import java.nio.file.Paths;
import java.nio.file.Path;
import java.io.IOException;

public class Main {

    /*
     * Test methods
     */
    private static boolean testSingleString(JavaParser parser, String testString, boolean expected) {
        if (parser.hasMatchingPunctuation(testString) == expected) {
            System.out.printf("Test case: %-10s - PASS%n", "\"" + testString + "\"");
            return true;
        } else {
            System.out.printf("Test case: %-10s - FAIL%n", "\"" + testString + "\"");
            return false;
        }
    }

    // This program checks whether a string is valid Java syntax with respect to
    // open and closed parentheses, brackets, and braces.
    public static void main(String[] args) {
        /*
         * Execution
         */

        // // Get the file path from the command line arguments
        // if (args.length != 1) {
        // System.out.println("Usage: java Main <file_path>");
        // return;
        // }

        // try {
        // // Read the file
        // String filePath = args[0];
        // String fileContent = Files.readString(Paths.get(filePath));

        // // Parse the file
        // JavaParser parser = new JavaParser();
        // if (parser.hasMatchingPunctuation(fileContent)) {
        // System.out.println("The file is valid Java syntax.");
        // } else {
        // System.out.println("The file is not valid Java syntax.");
        // }
        // } catch (IOException e) {
        // System.err.println("Error reading file: " + e.getMessage());
        // return;
        // }

        /*
         * TESTING
         */

        // This is an improvement over our "poor testing" example because:
        // - We have moved the testing functionality to its own method.
        // - The test now gives us a useful pass / fail message
        // - We've put deliberate thought into which test cases to include in order
        // to cover relevant pass/fail scenarios.
        JavaParser parser = new JavaParser();

        // Pass cases - simple pairs
        testSingleString(parser, "{}", true);
        testSingleString(parser, "[]", true);
        testSingleString(parser, "()", true);

        // Pass cases - nested same type
        testSingleString(parser, "{{}}", true);
        testSingleString(parser, "[[]]", true);
        testSingleString(parser, "(())", true);

        // Pass cases - mixed nested
        testSingleString(parser, "({})", true);
        testSingleString(parser, "{[]}", true);
        testSingleString(parser, "[{}]", true);
        testSingleString(parser, "{[()]}", true);

        // Fail cases - unmatched closing
        testSingleString(parser, "(", false);
        testSingleString(parser, "{{}", false);
        testSingleString(parser, "[", false);
        testSingleString(parser, "[[]", false);
        testSingleString(parser, "({}", false);

        // Fail cases - unmatched opening
        testSingleString(parser, ")", false);
        testSingleString(parser, "}", false);
        testSingleString(parser, "]", false);
        testSingleString(parser, "())", false);
    }
}
