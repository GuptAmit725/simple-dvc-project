import yaml
import os
import shutil
import logging
import json

#Reading params.yaml

def read_params(config_path:str) -> dict:
    with open(config_path) as yaml_file:
        config = yaml.safe_load(yaml_file)
    logging.info(f"Read the parameters.")
    return config

def clean_prev_dirs_if_exists(dir_path:str):
    if os.path.isdir(dir_path):
        shutil.rmtree(dir_path)
    logging.info(f"Cleaned the existing artifacts.")

def create_dir(dirs:list):
    for dir_path in dirs:
        os.makedirs(dir_path, exist_ok=True)
    logging.info(f"Directory created at {dir_path}.")

def save_local_df(df, df_path, header=False):
    if header:
        new_cols = [col.replace(' ','_') for col in df.columns]
        df.to_csv(df_path, index=False)
        logging.info(f"Df is saved with header at {df_path}.")
    else:
        df.to_csv(df_path, index=False)
        logging.info(f"Df is saved without header at {df_path}.")

def save_reports(file_path:str, report:dict):
    with open(file_path, 'w',encoding='utf-8') as f:
        json.dump(report,f, indent=4)
    logging.info(f"Reports are saved at {file_path}.")


