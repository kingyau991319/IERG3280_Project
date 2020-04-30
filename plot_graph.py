import fd_recommandation as fr
import json
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

if __name__ == "__main__":

    # source of data
    test = fr.fd_rd("friend_test.json")
    output_data = []
    person = []

    with open(test.profile) as json_file:
        data = json.load(json_file)
        for k in data:
            person.append(k)
            output_data = np.append(output_data,test.output_fd(k,0,to_csv = 0,deloutput=0))

    corr = []
    for k in output_data:
        for j in k:
            corr = np.append(corr,k[j])
    corr = np.resize(corr,(10,10))

    fig, (ax) = plt.subplots(1, 1, figsize=(10,6))
    fig.subplots_adjust(top=0.93)

    hm = sns.heatmap(corr, ax=ax, cmap="coolwarm", annot=True, fmt='.2f', 
                    linewidths=.05,yticklabels = person,xticklabels=person,)

    fig.suptitle('Person value with each others', fontweight='bold')
    fig.savefig('corr.png')