class Node:
    '''Defines a node in a graph'''
    def __init__(self, name : str, destinations = None, origin = None):
        '''initiates a node with name name and a dict of destinations with {Node1: distance1, Node2: distance2}'''
        self.name = name    #name of node
        self.destinations = destinations    #reachable nodes from node
        self.origin = origin    #previous node (only for path finding)
        self.cost = 0
    
    def get_closest(self):
        '''print the names of the closest nodes in the graph'''
        closest_node = min([distance for distance in self.destinations.values()])
        listOfClosest = [closestNodes.name for closestNodes in self.destinations.keys() if self.destinations[closestNodes] == closest_node]
        return listOfClosest
    
def find_route_fewest_changes(startNode, endNode, maxSteps = -1):
    '''find route with fewest changes'''
    listOfNodes = [startNode]    #list of reachable nodes
    lenOfList = len(listOfNodes)    #number of nodes found
    checkVar = 0    #check number of cycles of while loop
    
    while endNode not in listOfNodes:
        if lenOfList == len(listOfNodes) and checkVar != 0:
            return [Node('Not possible')]    #check if list has grown since last time
        checkVar += 1
        lenOfList = len(listOfNodes)    #reset lenOfList for next loop
        
        if checkVar > maxSteps and maxSteps != -1:    #see if steps exceeds max number
            return [Node('TIMEOUT')]
        
        for i in range(len(listOfNodes)):    #loop over listOfNodes and add destinations to temporary list
            newNodes = list(listOfNodes[i].destinations)
            for j in range(len(newNodes)):    #loop over destinations and add to listOfNodes if not already there
                if newNodes[j] not in listOfNodes:
                    newNodes[j].origin = listOfNodes[i]
                    listOfNodes.append(newNodes[j])
                    if newNodes[j] == endNode:    #if final destination found break
                        break
    
    route = []    #list of nodes in the route
    currentNode = endNode    #start at destination
    
    while currentNode != startNode:
        route.append(currentNode)    #add current node to route
        currentNode = currentNode.origin    #make origin the current node
    route.append(startNode)    #add ultimate origin
    route.reverse()    #correct order for the route
    
    return route

def get_distance(route, retInter = False):
    listOfDist = []    #list of distances between nodes
    for i in range(len(route) - 1):    #loop over destination distances to get list of distances
        listOfDist.append(route[i].destinations[route[i + 1]])
        
    if retInter == False:
        return sum(listOfDist)
    return listOfDist
    

London = Node('London')
Paris = Node('Paris')
Amsterdam = Node('Amsterdam')
Madrid = Node('Madrid')
Lisbon = Node('Lisbon')
Berlin = Node('Berlin')
Brussels = Node('Brussels')
Copenhagen = Node('Copenhagen')
Warsaw = Node('Warsaw')
Rome = Node('Rome')
Bucharest = Node('Bucharest')
Vienna = Node('Vienna')
Budapest = Node('Budapest')
Prague = Node('Prague')
Sofia = Node('Sofia')
Stockholm = Node('Stockholm')
Zagreb = Node('Zagreb')
Athens = Node('Athens')
Helsinki = Node('Helsinki')
Riga = Node('Riga')
Vilnius = Node('Vilnius')
Milan = Node('Milan')

London.destinations = {Paris : 300, Amsterdam : 310}
Paris.destinations = {London : 300, Brussels : 200, Rome : 300}
Amsterdam.destinations = {London : 400, Paris : 400, Berlin : 500, Rome : 900}
Madrid.destinations = {Lisbon : 300, Paris : 400}
Lisbon.destinations = {Madrid : 300, Paris : 500, Copenhagen : 1000}
Berlin.destinations = {Amsterdam : 500, Warsaw : 200, Lisbon : 600}
Brussels.destinations = {Amsterdam : 100, Paris : 200}
Copenhagen.destinations = {Berlin : 400, Stockholm : 100}
Warsaw.destinations = {Paris : 700, Berlin : 300}
Rome.destinations = {Paris : 600, Zagreb : 400, Berlin : 650}
Bucharest.destinations = {Berlin : 600, Warsaw : 700, Athens : 900}
Vienna.destinations = {Berlin : 500, Paris : 600, Amsterdam : 500}
Budapest.destinations = {Bucharest : 300, Sofia : 500, Athens : 300}
Prague.destinations = {Berlin : 500, Zagreb : 300, London : 1200, Helsinki : 1000, Rome : 900}
Sofia.destinations = {Vienna : 200, Copenhagen : 1230, Brussels : 1000}
Stockholm.destinations = {Helsinki : 500, Sofia : 1000}
Zagreb.destinations = {Rome : 600, Budapest : 400, Athens : 600}
Athens.destinations = {Zagreb : 500, Rome : 1000, Sofia : 600, London : 2000}
Helsinki.destinations = {Stockholm : 400, Copenhagen : 600, Paris : 1000}
Riga.destinations = {Vilnius : 100, Berlin : 300, Warsaw : 500, Paris : 1000}
Vilnius.destinations = {Athens : 1500, Helsinki : 100}
Milan.destinations = {Paris : 600}