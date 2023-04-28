#Constructor
def tree(label, branches=[]):
    for branch in branches:
        assert is_tree(branch)
    return [label] + list(branches)

#Selectors
def label(tree):
    return tree[0]

def branches(tree):
    return tree[1:]

def is_tree(tree):
    if type(tree) != list or len(tree) < 1:
        return False
    return True

def is_leaf(tree):
    return not branches(tree)

#Test Trees
t1 = tree(3, [tree(1), tree(2, [tree(1), tree(1)])])
t2 = tree('A', [tree('B'), tree('C', [tree('D'), tree('E')])])
t3 = tree(8,
          [tree(4,
                [tree(2), tree(3)]),
           tree(3,
                [tree(1), tree(1,
                               [tree(1), tree(1)])])])

def print_tree(t, indent=0):
    """Print a representation of this tree in which each node is
    indented by two spaces times its depth from the root.
    >>> print_tree(tree(1))
    1
    >>> print_tree(tree(1, [tree(2)]))
    1
      2
    >>> numbers = tree(1, [tree(2), tree(3, [tree(4), tree(5)]), tree(6, [tree(7)])])
    >>> print_tree(numbers)
    1
      2
      3
        4
        5
      6
        7
    """
    print('  ' * indent + str(label(t)))
    for b in branches(t):
        print_tree(b, indent + 1)
        
def prune_leaves(t, vals):
    """Return a modified copy of t with all leaves that have a label
    that appears in vals removed.  Return None if the entire tree is
    pruned away.
    >>> t = tree(2)
    >>> print(prune_leaves(t, (1, 2)))
    None
    >>> numbers = tree(1, [tree(2), tree(3, [tree(4), tree(5)]), tree(6, [tree(7)])])
    >>> print_tree(numbers)
    1
      2
      3
        4
        5
      6
        7
    >>> print_tree(prune_leaves(numbers, (3, 4, 6, 7)))
    1
      2
      3
        5
      6
    """
    if is_leaf(t):
        if label(t) in vals:
            return None
        else:
            return t
    pruned = [prune_leaves(b, vals) for b in branches(t)]
    return tree(label(t), [b for b in pruned if b is not None])
