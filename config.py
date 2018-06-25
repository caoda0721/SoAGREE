'''
Created on Nov 10, 2017
Store parameters

@author: Lianhai Miao
'''

class Config(object):
    def __init__(self):
        self.path = './data/MaFengWo/'
        self.user_dataset = self.path + 'userRating'
        self.group_dataset = self.path + 'groupRating'
        self.user_in_group_path = "./data/MaFengWo/groupMember.txt"
        self.follow_in_user_path = "./data/MaFengWo/userFollow.txt"
        self.embedding_size = 32
        self.epoch = 100
        self.num_negatives = 6
        self.batch_size = 1024
        self.lr = [0.000001, 0.000001, 0.0000005]
        self.drop_ratio = 0.2
        self.topK = 5
        self.num_follow = 13096
        self.balance = 6
