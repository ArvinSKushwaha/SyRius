
# CLASS: Node

# CLASS: LiteralNode extends Node
# ATTRIBUTES
#   literal: any constant value

# CLASS: FunctionalNode extends Node
# ATTRIBUTES
#   label: A unique whole number
#   function: pytorch function or string (to be converted to a function)

# CLASS: FunctionalNodeDirectedAcyclicGraph
# ATTRIBUTES
#   vertices: A list of Node instances
#   edges: A list of tuples containing indices of connected operations