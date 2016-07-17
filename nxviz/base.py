import matplotlib.pyplot as plt


class BasePlot(object):
    """BasePlot: the base plotting object that computes the layouts."""
    def __init__(self, nodes, edges,
                 nodecolors=None, edgecolors=None,
                 nodeprops=None, edgeprops=None,
                 figsize=None):
        super(BasePlot, self).__init__()
        self.nodes = nodes
        self.edges = edges

        # Set the node and edge props and colors.
        # These are written with functions because there are type checks that
        # have to take place first, and it would make the __init__ function
        # unwieldy to have them all in here.
        #
        # Later if we support other backends, such as Bokeh, it may be wise to
        # set these as "generic" parameters that we can write translators for
        # to other packages.
        self.set_nodeprops(nodeprops)
        self.set_edgeprops(edgeprops)
        self.set_nodecolors(nodecolors)
        self.set_edgecolors(edgecolors)
        # These functions end up setting the following object attributes:
        # - self.nodeprops
        # - self.edgeprops
        # - self.nodecolors
        # - self.edgecolors

        # Initialize a figure object with an axes subplot.
        # Later on if we support other backends, such as Bokeh, then it would
        # be wise to take this out of the class.
        self.figure = plt.figure(figsize=figsize)
        self.ax = self.figure.add_subplot(1, 1, 1)

        # We have an attribute that stores the x- and y-coordinates of each
        # node. They should be in the same order as self.nodes.
        self.node_coords = None

    def set_nodeprops(self, nodeprops):
        """
        Sets the node properties.
        """
        if nodeprops is not None:
            if isinstance(nodeprops, dict):
                self.nodeprops = nodeprops
            else:
                raise TypeError("nodeprops must be a dictionary")
        else:
            self.nodeprops = {}

    def set_edgeprops(self, edgeprops):
        """
        Sets the edge visualization properties.
        """
        if edgeprops is not None:
            if isinstance(edgeprops, dict):
                self.edgeprops = edgeprops
            else:
                raise TypeError("edgeprops must be a dictionary")
        else:
            self.edgeprops = {}

    def set_nodecolors(self, nodecolors):
        """
        Sets the nodecolors. Priority: nodecolor > nodeprops > default.

        By default, node color is blue.
        """
        if nodecolors is not None:
            self.nodecolors = nodecolors
        elif self.nodeprops:
            try:
                self.nodecolors = self.nodeprops.pop('facecolor')
            except KeyError:
                self.nodecolors = 'blue'
        else:
            self.nodecolors = 'blue'

    def set_edgecolors(self, edgecolors):
        """
        Sets the edge colors. Priority: edgecolor > edgeprops > default.

        By default, edge color is black.
        """
        if edgecolors is not None:
            self.edgecolors = edgecolors
        elif self.edgeprops:
            try:
                self.edgecolors = self.edgeprops.pop('edgecolors')
            except KeyError:
                self.edgecolors = 'black'
        else:
            self.edgecolors = 'black'

    def draw(self):
        self.draw_nodes()
        self.draw_edges()

    def compute_node_positions(self):
        """
        Computes the positions of each node on the plot.

        Needs to be implemented for each plot.
        """
        pass

    def draw_nodes(self):
        """
        Renders the nodes to the plot or screen.

        Needs to be implemented for each plot.
        """
        pass

    def draw_edges(self):
        """
        Renders the nodes to the plot or screen.

        Needs to be implemented for each plot.
        """
        pass