import java.nio.file.Files;
import java.nio.file.Paths;
import java.io.IOException;

public class Main {
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

        // This is an improvement over our "okay testing" example because:
        // - The testing functionality is now in its own class.
        // - We have one access point to call all of the tests.
        // - Tests are organized into test "sets".

        /*
         * In summary for our testing series:
         * - ANY testing is better than NO testing!
         * - Decide how to test functionality before writing new code.
         * - Test output should be clear.
         * - Tests should be saved; they are part of your codebase.
         * - Ideally, they should be in their own class or separate file.
         * - Testing libraries and frameworks can come later; start with basic checks!
         */
        TestJavaParser test = new TestJavaParser();
        test.testAll();
    }
}
