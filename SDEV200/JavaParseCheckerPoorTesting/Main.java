import java.nio.file.Files;
import java.nio.file.Paths;
import java.nio.file.Path;
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
        // For development, this is our main way to get feedback on whether the parser
        // is working correctly.

        JavaParser parser = new JavaParser();

        // This is not a great testing strategy because:
        // - Our test cases are relatively arbitrary
        // - We have not covered all scenarios or edge cases
        // - The tests are just lumped in with the main code
        // - The output gives us no useful information
        System.out.println(parser.hasMatchingPunctuation("{my test}"));
        System.out.println(parser.hasMatchingPunctuation("{my test}}"));
        System.out.println(parser.hasMatchingPunctuation("{other test]"));
    }
}
