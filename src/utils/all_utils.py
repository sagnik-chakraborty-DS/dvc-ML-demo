import yaml
import os

#this function take input as path to yaml file
#and give output in dictionary format what ever written in that yaml
def read_yaml(path_to_yaml:str)->dict:
    
    with open(path_to_yaml) as yaml_file:
        content=yaml.safe_load(yaml_file)
    return content    
    
    
  