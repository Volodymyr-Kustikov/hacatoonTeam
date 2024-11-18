import pandas as pd
from dataset import load_dataset
direct = load_dataset()
from dataset import take_question as stivensFunc


print(direct)

user1 = input("User1 Pick ur name")
user2 = input("User2 Pick ur name")

points_user1 = [user1, 0]
points_user2 = [user2, 0]

records = [points_user1, points_user2]

def user_data():
  file_path = './file.csv'
  d = pd.read_csv(file_path)
  categories = d['Category'].unique()[:-1]
  levels = d['Difficulty'].unique()[:-1]
  categories_list = categories.tolist()
  levels_list = levels.tolist()
  
  counter = 0
  while(counter < 6):

    user1_topic= input(f'Pick one of these topics: {categories_list} ')
    user_difficult = input(f'Pick one of these lvl: {levels_list} ')
  
    stivensFunc(user1_topic, user_difficult, direct, points_user1, points_user2)
    counter+=1
    
    if(counter == 5):
      if(points_user1[1] > points_user2[1]):
        print(f"Winner winner chicken dinner! {user1} is winner")
      elif(points_user1[1] < points_user2[1]):
        print(f"Winner winner chicken dinner! {user2} is winner")
      

    
    
user_data()

