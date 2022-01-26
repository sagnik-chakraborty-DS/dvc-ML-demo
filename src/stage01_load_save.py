from src.utils.all_utils import read_yaml,create_directory
import argparse
import pandas as pd
import os


def get_data(config_path):
    config = read_yaml(config_path)
    #print(config)
    
    remote_data_path = config["data_source"]
    df = pd.read_csv(remote_data_path,sep=";")
    #print(df.head)#read data from data source wich is mention inside config.yaml
    artifacts_dir = config["artifacts"]['artifacts_dir']
    raw_local_dir = config["artifacts"]['raw_local_dir']
    raw_local_file = config["artifacts"]['raw_local_file']
    
    raw_local_dir_path = os.path.join(artifacts_dir, raw_local_dir)
    raw_local_file_path = os.path.join(raw_local_dir_path, raw_local_file)
    
    #print(raw_local_dir_path)#output-->artifacts\raw_local_dir
    #print(raw_local_file_path)#output-->artifacts\raw_local_dir\data.csv
     
    #now we create directory
    create_directory(dirs= [raw_local_dir_path])
    
    df.to_csv(raw_local_file_path, sep=",", index=False)#save data in artifacts\raw_local_dir\data.csv
    #we use index= false because we dont want any separate index 

   


if __name__ == '__main__':
    args = argparse.ArgumentParser()

    args.add_argument("--config", "-c", default="config/config.yaml")#this will give path to a file
    #here default path is config/config.yaml

    parsed_args = args.parse_args()

    get_data(config_path=parsed_args.config)