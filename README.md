# IERG3280_Project
How Do Social Networks Recommend Friends?

# Introduction
It is the project of IERG3820, for our group work.
I am responsible for some code of part and upload them to github.

Main.py :             use api to output all person data.
connection_graph.py : basic calculations here that we need to use them in project.
fd_recommandation:    main part of the system,
                      it trys to adopt some methods to provide a recommdantaion friendls to you.

# Question
In most of the social networks, 
e.g. Facebook, the system regularly recommends friends for the users. 
Sometimes the reason is that the reommended friends share some common friends with the users. 
Sometimes the reason is that the recommended friend have similar interest as the users. 
Are there any other reasons for such a recommendation? 
Can you design a recommendation algorithm to briefly characterize these factor?

# Packet
Here is the packet that my project have used and installed by pip3,
numpy
pandas
networkx
json

# Simulation 
My simulation only take few factor and make different comparsion to incidate 
which person are highly recommanded to become your firend.

Firstly, we need to take the data from JSON, it is simulation the relationship in one group.
that have few data type, name, school, interests, age and friend

and we need to separate these vlaue and compare them each other
process and compare them throught different methods, that get the output and sort it to determine how to recommand in the list

# person_data
That is my csv file to count and store the data, for reference and monitoring 
The data is simulated by me.

# output.txt
It is the output data file to show the real number
I have not set the threshold for that because that is depend on the limited data set size
