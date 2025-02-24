/*
 * This is our dedicated test class for the JavaParser class.
 */
public class TestJavaParser {
    // We'll use this in many places within this class, so it's
    // better to create it once as a class variable.
    JavaParser parser = new JavaParser();

    /*
     * TEST CASES
     */
    String[] passCasesSinglePair = {
            "()",
            "[]",
            "{}"
    };

    String[] passCasesNestedSameType = {
            "(())",
            "[[]]",
            "{{}}"
    };

    String[] passCasesMixedNested = {
            "({})",
            "{[]}",
            "[{}]",
            "{[()]}"
    };

    String[] failCasesUnmatchedClosing = {
            "(",
            "{{}",
            "[",
            "[[]",
            "({}",
            "(}",
    };
    String[] failCasesUnmatchedOpening = {
            ")",
            "}",
            "]",
            "())",
    };

    /*
     * Runs all test cases.
     */
    // Only this should be called from Main, so it's the only public method.
    public void testAll() {
        System.out.println("RUNNING TEST SUITE: Pass case, single pair");
        testSet(passCasesSinglePair, true);
        System.out.println("RUNNING TEST SUITE: Pass case, nested same type");
        testSet(passCasesNestedSameType, true);
        System.out.println("RUNNING TEST SUITE: Pass case, mixed nested");
        testSet(passCasesMixedNested, true);
        System.out.println("RUNNING TEST SUITE: Fail case, unmatched closing");
        testSet(failCasesUnmatchedClosing, false);
        System.out.println("RUNNING TEST SUITE: Fail case, unmatched opening");
        testSet(failCasesUnmatchedOpening, false);
    }

    /*
     * Runs all test cases in the given set.
     */
    private void testSet(String[] testSet, boolean expected) {
        for (String testString : testSet) {
            testSingleString(testString, expected);
        }
    }

    /*
     * Prints the output of the test case.
     * Returns true if the test case passes, false otherwise.
     */
    private boolean testSingleString(String testString, boolean expected) {
        // This is the actual "did the test case pass" check.
        if (parser.hasMatchingPunctuation(testString) == expected) {
            System.out.printf("Test case: %-10s - PASS%n", "\"" + testString + "\"");
            return true;
        } else {
            System.out.printf("Test case: %-10s - FAIL%n", "\"" + testString + "\"");
            return false;
        }
    }
}
