#!/usr/bin/env python
# coding: utf-8

import glob
import pandas as pd
import os
import numpy as np
from datetime import date

# Location of the Raw Data from PsychoPy
raw_data_loc = 'data_raw'

# CSV Templates for RedCap Upload Formatting
cfmt_u_upload = pd.read_csv('upload_templates/cfmt_u_template.csv')
rmie_upload = pd.read_csv('upload_templates/rmie_template.csv')
cfmt_i_upload = pd.read_csv('upload_templates/cfmt_i_template.csv')

# CFMT Upright 
cfmt_u_files = glob.glob(raw_data_loc + "/*CFMT_U*.csv")
for file in cfmt_u_files:
    subj_id = file.split("/")[-1].split("_")[0]
    study_id = int(subj_id[1:4])
    
    df = pd.read_csv(file)
    practice = df['Response.keys'].dropna().tolist()
    learn_df = df.dropna(subset=['Answer.keys'])
    learn_list = learn_df[['Answer.keys', 'Answer_2.keys', 'Answer_3.keys']].values.ravel().tolist()
    novel = df['Answer_4.keys'].dropna().tolist()
    noise = df['Answer_5.keys'].dropna().tolist()
    
    data = [study_id, 'ra_record_keeping_arm_1', subj_id, df['date'].iloc[0].split("_")[0] ] + practice + learn_list + novel + noise + [2]
    cfmt_u_upload.loc[len(cfmt_u_upload)] = data

# RMIE
rmie_files = glob.glob(raw_data_loc + "/*RMIE*.csv")
for file in rmie_files:
    subj_id = file.split("/")[-1].split("_")[0]
    df = pd.read_csv(file)
    date = df['date'].iloc[0].split("_")[0]
    responses = df['key_resp.keys'].dropna().tolist()
    data = [subj_id, date ] + responses + [2]
    rmie_upload.loc[len(rmie_upload)] = data

# CFMT Inverted 
cfmt_i_files = glob.glob(raw_data_loc + "/*CFMT_I*.csv")
for file in cfmt_i_files:
    subj_id = file.split("/")[-1].split("_")[0]
    study_id = int(subj_id[1:4])
    
    df = pd.read_csv(file)
    practice = df['Response.keys'].dropna().tolist()
    learn_df = df.dropna(subset=['Answer.keys'])
    learn_list = learn_df[['Answer.keys', 'Answer_2.keys', 'Answer_3.keys']].values.ravel().tolist()
    novel = df['Answer_4.keys'].dropna().tolist()
    noise = df['Answer_5.keys'].dropna().tolist()
    question = df['key_resp_6.keys'].iloc[63]
    
    data = [ subj_id, df['date'].iloc[0].split("_")[0] ] + practice + learn_list + novel + noise + [question] + [2]
    cfmt_i_upload.loc[len(cfmt_i_upload)] = data

# Export
merged_df = pd.merge(cfmt_u_upload, rmie_upload, left_on='cfmt_a_u_part_id', right_on='rmie_a_part_id')
merged_df = pd.merge(merged_df, cfmt_i_upload, left_on='cfmt_a_u_part_id', right_on='cfmt_a_i_part_id')

merged_df = merged_df.apply(lambda x: x.astype(int) if x.dtype == np.float64 else x)
for_export = merged_df.set_index('studyid')

today = date.today()
date = today.strftime("%Y%m%d")
for_export.to_csv(f'CSV_for_RedCap_Upload_{date}.csv')

source = 'data_raw'
destination = 'uploaded_data'

if not os.path.exists(destination):
    os.makedirs(destination)

allfiles = os.listdir(source)
for file in allfiles:
    src_path = os.path.join(source, file)
    dst_path = os.path.join(destination, file)
    os.rename(src_path, dst_path)