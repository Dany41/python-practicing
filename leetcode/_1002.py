from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def resolve_tree(traversal, depth, index):
    if index >= len(traversal):
        return None, index
    dashes = traversal[index:(index + depth)]
    if dashes == "-" * depth:
        find_index_maybe = traversal.find('-', index + depth)
        if find_index_maybe == -1:
            find_index = len(traversal)
        else:
            find_index = find_index_maybe
        next_val = traversal[index + depth:find_index]
        (left, new_i) = resolve_tree(traversal, depth + 1, index + depth + len(next_val))
        (right, new_i_2) = resolve_tree(traversal, depth + 1, new_i)
        return TreeNode(int(next_val), left, right), new_i_2
    else:
        return None, index



class Solution:
    def recoverFromPreorder(self, traversal: str) -> Optional[TreeNode]:
        find_index_maybe = traversal.find('-')
        if find_index_maybe == -1:
            find_index = len(traversal)
        else:
            find_index = find_index_maybe
        next_val = traversal[:find_index]
        (left, index) = resolve_tree(traversal, 1, len(next_val))
        root = TreeNode(int(next_val), left, resolve_tree(traversal, 1, index)[0])
        return root


if __name__ == '__main__':
    s = Solution()
    act_n = s.recoverFromPreorder("10-7--8")

