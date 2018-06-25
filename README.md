# Social-Enhanced Attentive Group Recommendation

This is our implementation for the paper:

Da Cao, Xiangnan He, Lianhai Miao, Guangyi Xiao, Hao Chen, and Richang Hong. Social-Enhance Attentive Group Recommendation. IEEE Transactions on Knowledge and Data Engineering, 2018.

In order to learn the group interest, we first utilize the social infomation to enchance the representation of individual user. then, we use attention mechanism to learn the aggregation strategy from data in a dynamic way.

**Please cite our paper if you use our codes. Thanks!** 

we will provide the BibTeX soon.


## Environment Settings
We use the framework pytorch. 
- pytorch version:  '0.4.0'
- python version: '3.5'

## Example to run the codes.

Run SoAGREE:

```
python main.py
```

After training process, the value of HR and NDCG in the test dataset will be printed in command window after each optimization iteration.

Output:

```
SoAGREE at embedding size 32, run Iteration:100, NDCG and HR at 5
...
user and group training time is: [975.4 s]
User Iteration 30 [1000.5 s]: HR = 0.6477, NDCG = 0.5583, [25.1 s]
Group Iteration 30 [1141.9 s]: HR = 0.4869, NDCG = 0.3803, [166.4 s]

```


## Parameter Tuning

we put all the papameters in the config.py

## Dataset

We provide one processed dataset: MaFengWo

group(user) train.rating:

* Train file.
* Each Line is a training instance: groupID(userID)\t itemID\t rating\t timestamp (if have)

test.rating:

* group(user) Test file (positive instances).
* Each Line is a testing instance: groupID(userID)\t itemID\t rating\t timestamp (if have)

test.negative

* group(user) Test file (negative instances).
* Each line corresponds to the line of test.rating, containing 100 negative samples.
* Each line is in the format: (groupID(userID),itemID)\t negativeItemID1\t negativeItemID2 ...
