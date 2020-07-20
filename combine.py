# made by munhyung lee 
# e-mail : moonstar114@naver.com
# program goal : open each csv file and add 

import pandas as pd
import glob
import os
import re

directory_list = list( 
                       filter(\
                         os.path.isdir, 
                         glob.glob(os.getcwd() + "/*")\
                      )) # get all directory
for directory in directory_list:
    file_list = [file for file in os.listdir(directory) if file.endswith(".csv")]
    
    file_count =0
    for file_name in file_list:
      file_name_parse = re.split('[._]', file_name)
      
      CSV_file = pd.read_csv(directory +"/"+file_name)
      CSV_file.columns=['Rank', 'Change','subcategory','App', 'Publisher', 'Price', 'Inapp', 'Date', 'CRScore','URL(Address)']
      
      # ex ) file_name_parse = ['AN','M','KR','FREE', 'TRAVEL', '201901','csv']
      
      CSV_file["Country"]= file_name_parse[2]
      CSV_file["Type"] = file_name_parse[3]
      
      if file_name_parse[0] == "AN":
        CSV_file["OS"] = "AND"
      else :
        CSV_file["OS"] = "IOS"
      
      CSV_file["year"] = int(int(file_name_parse[5]) / 100)
      CSV_file["month"] = int(file_name_parse[5]) % 100
      CSV_file["date type"] = file_name_parse[1]
      CSV_file["Industry"] = ""
      #add 6 columns Country, Type, OS, year, month, date type, Industry
      
      CSV_file[["Country","Type","OS", "year", "month", "date type", \
                "Rank", "Change", "Industry", "subcategory","App","Publisher",\
                "Price", "Inapp", "Date", "CRScore", "URL(Address)"]]\
                .to_csv(directory+"/"+file_name+'_out_v1.csv', index= False)
      
      
      # TODO : have to save in other directory , file collision
      print("modify  " + file_name +  " with "+ str(len(CSV_file))+ " records")
