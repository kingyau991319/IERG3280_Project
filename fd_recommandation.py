import numpy as np
import networkx as nx
import connection_graph as cg
import json

msg = '''
    What I need to do?
    1. make an aglorithm to simulate the friend recommandation
    2. combine the common function here
    3. process with the simulated file? and output the result?
'''

class fd_rd:

    '''
        for personal input
        that is rely on only a person but also can make an array to make a list?
    '''
    def __init__(self,profile,keyfactor="fd"):
        self.profile = profile
        self.closeness = []
    # use JSON file to store and add_connection
    
    # function that I need : add_person
    # output the fd_recommandation
    # find the close relationship

    def output_fd(self, person_name):

        # data: for the whole json file
        # target_data: for only one that need to input with
        # output_data: sorting and list the output
        data = None
        target_data = None
        output_data = None

        with open(self.profile) as json_file:
            data = json.load(json_file)
            target_data = data[person_name]

        data_len = len(data)
        #build a ajancy matrix
        label = []
        interest = target_data['interest']
        output_data = {}
        interest_count = {}
        school_count = {}

        for k in data:
            label.append(k)
            interest_count[k] = 0
            school_count[k] = 0
            output_data[k] = 0

        person_process = cg.model(data_len,cg.modes.Adjacency,cg.graphType.undirected,label)
        for i in label:

            # for closeness
            if len(self.closeness) == 0:
                firstNode = int(i.split("person")[1]) - 1
                for fd in data[i]["friend"]:
                    secondNode = int(fd.split("person")[1]) - 1
                    person_process.add_connection(firstNode,secondNode)

            # for interest
            for k in interest:
                if k in data[i]["interest"]:
                    interest_count[i] = interest_count[i] + 1
            if target_data["school"] == data[i]["school"]:
                school_count[i] = 1

        # this is most close to this group one, for compare to the relationship
        if len(self.closeness) == 0:
            closeness = person_process.closeness()
        else:
            closeness = self.closeness

        output_data = interest_count
        index = 0
        for k in output_data:
            output_data[k] = interest_count[k] + school_count[i]
            output_data[k] = round(output_data[k]/2 + closeness[index],4)
            index = index + 1

        # sorting
        output_data = {k: v for k, v in sorted(output_data.items(), key=lambda item: item[1],reverse=True)}
        del output_data[person_name]
        self.closeness = closeness

        return output_data

    # todo, this is too.... simple and have not any considration
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