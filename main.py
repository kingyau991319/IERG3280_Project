import fd_recommandation as fr
import json
import numpy as np



# I want to show all person recommandation list on here
if __name__ == "__main__":
    test = fr.fd_rd("friend_test.json")
    # person = {"name" : "test10","age" : 68,"friend" : ["perons6","perons7","perons8"],"shcool" : "school5","interest" : ["interest3","interest4","interest5"]}
    output_data = []
    with open(test.profile) as json_file:
        data = json.load(json_file)
        for k in data:
            output_data = np.append(output_data,test.output_fd(k))
    f = open("output.txt", "w")
    f.write(str(output_data))
    print(output_data)