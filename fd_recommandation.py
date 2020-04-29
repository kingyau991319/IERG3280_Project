import numpy as np
import networkx as nx
import connection_graph as cg
import json
import math

msg = '''
    What I need to do?
    1. make an aglorithm to simulate the friend recommandation
    2. combine the common function here
    3. process with the simulated file? and output the result?
'''


# that is attached with the algorithm simulation, but not exactly can run ,only a test
# for consideration the simply case and neglecting the possible expanding code here
class fd_rd:

    '''
        for personal input
        that is rely on only a person but also can make an array to make a list?
        @para profile:  for json file that store the information for some fd
                        Maybe its relationship comes from a group.
    '''
    def __init__(self,profile,keyfactor="fd"):
        self.profile = profile
        self.closeness = []
    # use JSON file to store and add_connection
    
    # output the fd_recommandation
    # find the close relationship

    def output_fd(self, person_name,threshold):

        # data: for the whole json file
        # target_data: for only one that need to input with
        # output_data: sorting and list the output
        data = None
        target_data = None
        output_data = None

        with open(self.profile) as json_file:
            data = json.load(json_file)
            target_data = data[person_name]

        #build a ajancy matrix
        # @para label: incidate all list for the header of the json format
        # @para data_len: all person
        # @para interest: show the first person interest here
        # @para output_data: the data that I want to return and output the result
        # @para interest_count: the sum of same interst with target person
        # @para school_count: enable to check whatever is it equal to user
        data_len = len(data)
        label = []
        interest = target_data['interest']
        output_data = {}
        interest_count = {}
        school_count = {}
        age_count = []

        # init statement
        for k in data:
            label.append(k)
            age_count = np.append(age_count,round(math.sqrt(abs(target_data["age"] - data[k]["age"])) / 10,3))
            interest_count[k] = 0
            school_count[k] = 0
            output_data[k] = 0


        # to build a adjacency matrix and make the connection in this part
        person_process = cg.model(data_len,cg.modes.Adjacency,cg.graphType.undirected,label)
        for i in label:

            # for closeness building, if already build, neglect it
            if len(self.closeness) == 0:
                firstNode = int(i.split("person")[1]) - 1
                for fd in data[i]["friend"]:
                    secondNode = int(fd.split("person")[1]) - 1
                    person_process.add_connection(firstNode,secondNode)

            # for interest checking, if interest is same, then add 1
            for k in interest:
                if k in data[i]["interest"]:
                    interest_count[i] = interest_count[i] + data[i]["interest"][k]["like"]
            if target_data["school"] == data[i]["school"]:
                school_count[i] = 1

        # this is most close to this group one, for compare to the relationship
        # if alreadly build, just neglect to set closeness
        if len(self.closeness) == 0:
            closeness = person_process.closeness()
        else:
            closeness = self.closeness

        output_data = interest_count
        index = 0

        for k in label:
            if output_data[k] < threshold or k in target_data["friend"]:
                del output_data[k]

        if person_name in output_data:
            del output_data[person_name]

        # it is bulit by the format...  outputData = (scholl_count + interest_count / 2) + closeness
        for k in output_data:
            output_data[k] = interest_count[k] + school_count[i]
            output_data[k] = round(output_data[k]/2 + closeness[index]- age_count[index],4) 
            index = index + 1

        # sorting, to find the highest relationship
        output_data = {k: v for k, v in sorted(output_data.items(), key=lambda item: item[1],reverse=True)}
        self.closeness = closeness

        # subtract that alreadly is friend and yourselves

        return output_data

    # todo, this is too.... simple and have not any considration
    # no need to do that now
    def add_person(self,person):

        data = 0

        with open(self.profile) as json_file:
            data = json.load(json_file)
            num_of_person = len(data) + 1
            new_index_name = "person" + str(num_of_person)
            data[new_index_name] = person
            fd = person["friend"]
            for k in data:
                for i in fd:
                    if i == k:
                        print(i)
        with open(self.profile,"w+") as json_file:
            json.dump(data, json_file)

if __name__ == "__main__":
    test = fd_rd("friend_test.json")
    # person = {"name" : "test10","age" : 68,"friend" : ["perons6","perons7","perons8"],"shcool" : "school5","interest" : ["interest3","interest4","interest5"]}
    output_data = []
    threshold = 0
    output_data = test.output_fd("person1",threshold)
    print(output_data)