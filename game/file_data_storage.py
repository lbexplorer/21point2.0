import json
import os


def file_data(robot, human):
    pwd = os.getcwd()
    robot_data_name = os.path.join(pwd, "robot.txt")
    human_data_name =  os.path.join(pwd, "human.txt")

    with open(robot_data_name,'w', encoding='utf-8') as f1:
        f1.write(json.dumps(robot))
    with open(human_data_name, 'w', encoding='utf-8') as f2:
        f2.write(json.dumps(human))

def file_r():
    pwd = os.getcwd()
    robot_data_name = os.path.join(pwd, "robot.txt")
    human_data_name = os.path.join(pwd, "human.txt")
    with open(human_data_name,'r', encoding='utf-8') as f2:
        data_human = eval(f2.read())
    with open(robot_data_name, 'r', encoding='utf-8') as f3:
        data_robot = eval(f3.read())
    return data_robot,data_human