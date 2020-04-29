import numpy as np
from enum import Enum, unique
import networkx as nx

msg = '''

    title: How Do Social Networks Recommend Friends?

    msg: In most of the social networks, 
    e.g. Facebook, the system regularly recommends friends for the users. 
    Sometimes the reason is that the reommended friends share some common friends with the users. 
    Sometimes the reason is that the recommended friend have similar interest as the users. 
    Are there any other reasons for such a recommendation? 
    Can you design a recommendation algorithm to briefly characterize these factor?

    '''

# What I need to do?
# 1. input martix and connection
# store as two mode -> Adjacency Matrix, Incidence Matrix
# store as Undirected Graph, Directed Graph 
@unique
class modes(Enum):
    Adjacency = 0
    Incidence = 1


@unique
class graphType(Enum):
    directed = 0
    undirected = 1


class model:

    #   mode = Adjacency Matrix
    #   mode = Incidence Matrix
    #   for init the statement

    def __init__(self,size,modes,graphType,label):
        self.size = size
        self.modes = modes
        self.graphType = graphType
        self.connectionCount = 0
        self.connection = []
        self.label = np.array(label)
        if modes == 0 or self.modes == modes.Adjacency:
            temp = (size,size)
            self.martix = np.zeros(temp)
        else:
            self.martix = np.zeros((size,1))
        if(len(label) != size):
            raise Exception('label must relate with size. Now the label and size is {},{}',len(label),size)

    #   step1: check error 
    #   step2: distingusih what type are
    #   step3: choose that and follow the rule to connect
    #   step4: done and return or print message? (if need, i need to do test case)

    # first Node point to seconNode (if directed)
    def add_connection(self,firstNode,secondNode):

        self.connection.append((firstNode,secondNode,1))

        if(firstNode > self.size or secondNode > self.size):
            print("error: Node > size, plz input again")
            exit()

        martix = self.martix
        # 4 cases
        # Adjacency Matrix -> directed
        # Adjacency Matrix -> undirected
        # Incidence Matrix -> directed
        # Incidence Matrix -> undirected

        if (modes == 0 and graphType == 0) or (self.modes == modes.Adjacency and self.graphType == graphType.directed):
            martix[secondNode][firstNode] = 1

        # Incidence Matrix -> undirected
        if (modes == 0 and graphType == 1) or (self.modes == modes.Adjacency and self.graphType == graphType.undirected):
            martix[firstNode][secondNode] = 1
            martix[secondNode][firstNode] = 1

        if (modes == 1 and graphType == 0) or (self.modes == modes.Incidence and self.graphType == graphType.directed):
            size = (1,self.size)
            if(self.connectionCount == 1):
                martix[firstNode][0] = 1
                martix[secondNode][0] = -1

            else:
                tempMatrix = np.zeros((self.size,1))
                tempMatrix[firstNode][0] = 1
                tempMatrix[secondNode][0] = -1
                martix = np.append(martix,tempMatrix,axis=1)

        if (modes == 1 and graphType == 1) or (self.modes == modes.Incidence and self.graphType == graphType.undirected):
            size = (1,self.size)

            if(self.connectionCount == 1):
                martix[firstNode][0] = 1
                martix[secondNode][0] = 1
            else:
                tempMatrix = np.zeros((self.size,1))
                tempMatrix[firstNode][0] = 1
                tempMatrix[secondNode][0] = 1
                martix = np.append(martix,tempMatrix,axis=1)

        self.martix = martix
        self.connectionCount = self.connectionCount + 1


    # find the closeness, if the num is highest, 
    # that mean in a group, that is most important and popular person in here
    def closeness(self):

        def distantCount(self,distant,row,count,loopCount):
            for j in range(self.size):
                if row[j] == 1:
                    distant[j] = 1

            count = count + 1

            for i in range(self.size-1):
                for j in range(self.size):
                    if distant[j] == count:
                        for k in range(self.size):
                            if self.martix[j][k] == 1 and distant[k] == 0:
                                distant[k] = distant[k] + count + 1
                count = count + 1

            distant[loopCount] = 0
            return distant

        if (modes == 0 and graphType == 1) or (self.modes == modes.Adjacency and self.graphType == graphType.undirected):
            size = self.size - 1
            loopCount = 0
            closeness = np.zeros(self.size)
            for row in self.martix:
                distant = np.zeros(self.size)
                distant = distantCount(self,distant,row,0,loopCount)
                result = size / np.sum(distant)
                closeness[loopCount] = round(result,4)
                loopCount = loopCount + 1
            return closeness

        else:
            print("mode problem and graphType problem")
            return -1

    # todo
    def betweennessCentrality(self):
        if (modes == 0 and graphType == 1) or (self.modes == modes.Adjacency and self.graphType == graphType.undirected):
            FG = nx.DiGraph()
            FG.add_weighted_edges_from(self.connection)
            result = nx.betweenness_centrality(FG,weight=True,normalized=False)
            return result
        else:
            print("mode problem and graphType problem")
            return -1

    # todo
    def eigenvectorCentrality(self):

        if (modes == 0 and graphType == 1) or (self.modes == modes.Adjacency and self.graphType == graphType.undirected):
            FG = nx.path_graph(self.connection)
            result = nx.eigenvector_centrality(FG)
            for k in result:
                result[k] = round(result[k],4)
            return result
        else:
            print("mode problem and graphType problem")
            return -1

    # for adding and subtracting matrix size
    # it is used for expanding some feature
    def reduce_matrix_size(self,reduce_label):
        index = self.label.tolist().index(reduce_label)
        self.label = np.delete(self.label,index,axis=0)
        self.martix = np.delete(np.delete(self.martix, index, 1), index, 0)

    def add_matrix_size(self,add_label):
        self.martix = np.append(self.martix,np.zeros((self.size,1)),axis=1)
        self.martix = np.append(self.martix,np.zeros(self.size))
        self.martix.resize((self.size+1,self.size+1))
        self.size = self.size + 1
        self.label = np.append(self.label,add_label)
        

# checking code
# if __name__ == "__main__":

#     label = ["test1","test2","test3","test4","test5","test6","test7","test8",]
#     test = model(8,modes.Adjacency,graphType.undirected,label)
#     test.add_connection(0,1)
#     test.add_connection(0,2)
#     test.add_connection(0,3)
#     test.add_connection(1,3)
#     test.add_connection(1,4)
#     test.add_connection(2,6)
#     test.add_connection(2,7)
#     test.add_connection(2,5)
#     test.add_connection(3,4)
#     test.add_connection(5,6)
#     test.add_connection(7,6)
#     # test.closeness()
#     result_between = test.betweennessCentrality()
#     result_eigen = test.eigenvectorCentrality()
#     closeness = test.closeness()
#     print(closeness)
#     print(result_between)
#     print(result_eigen)
#     print(test.martix)
#     # print("test.martix",test.martix)
#     # print("closeness",closeness)
#     # print("result",result_eigen)
#     # print("result_between",result_between)
