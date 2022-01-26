import yaml
import os

#this function take input as path to yaml file
#and give output in dictionary format what ever written in that yaml
def read_yaml(path_to_yaml:str)->dict:
    
    with open(path_to_yaml) as yaml_file:
        content=yaml.safe_load(yaml_file)
    return content    
    
def create_directory(dirs:list):
    #we pass list of directory which we want to create
    for directory_path in dirs:
        os.makedirs(directory_path, exist_ok=True)
        print(f"directory is saved at {directory_path}")    


def save_local_df(data,data_path,index_status=False):
    #to save test train file
    data.to_csv(data_path,index=index_status)
    print(f"data is saved at {data_path}")  