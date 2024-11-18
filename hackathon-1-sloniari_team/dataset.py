import pandas as pd
import random
def load_dataset():
    path = ".\data\Values_main.csv"

    file = pd.read_csv(path)


    category = file["Category"].unique()
    direct = {}
    for i in range(len(category) - 1):
        temp_type = file[file["Category"] == category[i]]
        direct[category[i]] = {"Easy": temp_type[temp_type["Difficulty"] == "Easy"], 
                        "Medium": temp_type[temp_type["Difficulty"] == "Medium"] , 
                        "Hard": temp_type[temp_type["Difficulty"] == "Hard"]}
    return direct
    # dir = {"History" : {"Easy" "Medium" "Hard"}
    #        "Politics" : {"Easy" "Medium" "Hard"}
    #        "Technology" : {"Easy" "Medium" "Hard"}
    #        "Movies" : {"Easy" "Medium" "Hard"}
    #        "Science" : {"Easy" "Medium" "Hard"},            
    #         } dased on Values_main.csv

def take_question(topic, level, direct, user_1, user_2):
    quan = len(direct[topic][level])
    rand_num = random.randint(1, quan)
    question_dir = direct[topic][level][rand_num - 1:rand_num]
    question_answer = int(question_dir["Answer"])
    print(str(question_dir["Question"]))
    
    user_1_input = int(input(f"{user_1[0]} - Plz, Enter answer: "))
    user_2_input = int(input(f"{user_2[0]} - Plz, Enter answer: "))
    
    if abs(question_answer - user_1_input) < abs(question_answer - user_2_input):
        print(f"Point go to {user_1[0]}")
        user_1[1] += 1

    elif abs(question_answer - user_1_input) > abs(question_answer - user_2_input):
        print(f"Point go to {user_2[0]}")
        user_2[1] += 1

    else:
        print("draw")
        user_2[1] += 1
        user_1[1] += 1
