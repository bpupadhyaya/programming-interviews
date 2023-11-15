// Given a string path, which is an absolute path (starting with a slash '/') to a file or directory in
// a Unix-style file system, convert it to the simplified canonical path.
//In a Unix-style file system, a period '.' refers to the current directory, a double period '..' refers to
// the directory up a level, and any multiple consecutive slashes (i.e. '//') are treated as a single
// slash '/'. For this problem, any other format of periods such as '...' are treated as file/directory names.
//The canonical path should have the following format:
// -The path starts with a single slash '/'.
// -Any two directories are separated by a single slash '/'.
// -The path does not end with a trailing '/'.
// -The path only contains the directories on the path from the root directory to the target file or
//  directory (i.e., no period '.' or double period '..')
// Return the simplified canonical path.
// Example:
// Input: path = "/home//foo/"
// Output: "/home/foo"
// Explanation: In the canonical path, multiple consecutive slashes are replaced by a single one.
//
// Tag: 53/150
// Tag: 71/2927, R349/2936 (overall frequency ranking)

import java.util.Stack;
class PathSimplification {
    public static void main(String...args) {
        String path = "/home//foo/";
        System.out.println("Simplified path: " + simplifyPath(path));

    }

    static String simplifyPath(String path) {
        Stack<String> stack = new Stack<>();
        String[] directories = path.split("/");
        for (String dir: directories) {
            if (dir.equals(".") || dir.isEmpty()) {
                continue;
            } else if (dir.equals("..")) { // Go one level up for double period '..'
                if (!stack.isEmpty()) {
                    stack.pop();
                }
            } else {
                stack.push(dir); // For any other directory, push it to the stack.
            }
        }

        return "/" + String.join("/", stack); // Join the directories in the stack with '/' adn add a slash at
        // the beginning.
    }
}