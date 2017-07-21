from adjacency_list import Graph

# Group class stores sets buyers and sellers
class Group():

    def __init__(self):
        self.seller = set()
        self.buyer = set()
    
    def __str__(self):
        return "Sellers: {} \nBuyers: {}".format(self.seller, self.buyer)

# Match class implements matching algorithm
class Match():

    def __init__(self, data):
        self.data = data

        # Dictionary of Group objects that map geography/industry
        # sets of buyers and sellers
        self.groups = {}

        # Directed graph from sellers to buyers
        self.graph = Graph()

    # Store data in 'groups' dictionary
    def processInput(self):

        # Read json data into groups dictionary
        for d in self.data:
            dType = d['type']
            dId = d['id']
            geography = d['details']['geography_ids']
            industry = d['details']['industry_ids']

            for g in geography:
                for i in industry:

                    gi = (g, i)
                    if gi not in self.groups:
                        self.groups[gi] = Group()
                    
                    if dType == 'seller':
                        self.groups[gi].seller.add(dId)
                    else:
                        self.groups[gi].buyer.add(dId)

    # Create graph based on mapping
    def createGraph(self):

        # Populate undirected graph
        for tup in self.groups:
            geo = tup[0]
            ind = tup[1]

            group = self.groups[tup]
            for s in group.seller:
                for b in group.buyer:
                    self.graph.addEdge(s, b, geo, ind)


    # Print matching buyers for each seller
    def printMatches(self):

        spacing = [40, 40, 25, 20, 10, 10]

        # Print table heading
        heading = ['Seller Id', 'Buyer Id', 'Geographies', 'Industries', 'Overlap', 'Rank']
        
        # Python adds 1 additional space between each print statement automatically
        divider = '-' * ( sum(spacing) + len(heading)-1 )

        print(
            heading[0].center(spacing[0]), 
            heading[1].center(spacing[1]), 
            heading[2].center(spacing[2]),
            heading[3].center(spacing[3]),
            heading[4].center(spacing[4]),
            heading[5].center(spacing[5])
        )

        print(divider.center(sum(spacing)))

        # Print matches in order
        for node in self.graph.getNodes(): 

            # Only print seller id on first row of corresponding matches
            firstRow = True     
            
            if node.type == 'seller':

                edges = self.graph.getSortedEdges(node)
                rank = 1

                for edge in edges:

                    if firstRow:
                        seller_id = node.id
                        firstRow = False
                    else:
                        seller_id = ''

                    buyer_id = edge.u
                    geo = str(edge.geography)
                    ind = str(edge.industry)      
                    weight = str(edge.weight)   

                    print(
                        seller_id.center(spacing[0]), 
                        buyer_id.center(spacing[1]), 
                        geo.center(spacing[2]),
                        ind.center(spacing[3]),
                        weight.center(spacing[4]),
                        str(rank).center(spacing[5])
                    ) 

                    rank += 1
                
                print(divider.center(sum(spacing)))


    
    