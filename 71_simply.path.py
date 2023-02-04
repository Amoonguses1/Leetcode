# Time: O(N)
# Space: O(N)
# N = len(path)


class Solution:
    def simplifyPath(self, path: str) -> str:
        """Function to convert the given absolute path to the canonical path

            Args:
                path(str): the absolute path

            Returns:
                str: the canonical path
        """
        if not isinstance(path, str):
            raise ValueError("Input must be a string.")

        dir_name = []
        for token in path.split("/"):
            if token == "" or token == ".":
                pass
            elif token == "..":
                if dir_name:
                    dir_name.pop()
            else:
                dir_name.append(token)
        return "/" + "/".join(dir_name)
