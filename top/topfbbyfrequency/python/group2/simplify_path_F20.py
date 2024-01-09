"""
Given a string path, which is an absolute path (starting with a slash '/') to a file or directory in
a Unix-style file system, convert it to the simplified canonical path.
In a Unix-style file system, a period '.' refers to the current directory, a double period '..' refers to
the directory up a level, and any multiple consecutive slashes (i.e. '//') are treated as a single
slash '/'. For this problem, any other format of periods such as '...' are treated as file/directory names.
The canonical path should have the following format:
-The path starts with a single slash '/'.
-Any two directories are separated by a single slash '/'.
-The path does not end with a trailing '/'.
-The path only contains the directories on the path from the root directory to the target file or
 directory (i.e., no period '.' or double period '..')
Return the simplified canonical path.

Example:
Input: path = "/home//foo/"
Output: "/home/foo"
Explanation: In the canonical path, multiple consecutive slashes are replaced by a single one.

Tag: 53/150
Tag: 71/2927, R349/2936 (overall frequency ranking), fb R20/50
"""


def simplify_path(path: str) -> str:
    dir_or_files = []
    path = path.split("/")
    for elem in path:
        if dir_or_files and elem == "..":
            dir_or_files.pop()
        elif elem not in [".", "", ".."]:
            dir_or_files.append(elem)

    return "/" + "/".join(dir_or_files)


def main():
    path = "/home//foo/"
    print(simplify_path(path))


if __name__ == "__main__":
    main()
