# made by munhyung lee 
# e-mail : moonstar114@naver.com
# program goal : open each csv file and add 

import pandas as pd
import glob
import os
import re

def add_column(CSV_file , file_name_parse):

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
  
  return CSV_file

directory_list = list( 
                       filter(\
                         os.path.isdir, 
                         glob.glob(os.getcwd() + "/*")\
                      )) # get all directory
for directory in directory_list:
    file_list = [file for file in os.listdir(directory) if file.endswith(".csv")]
    
    print( str(len(file_list)) + " files in " +directory )
    file_count =0
    
    # 20/07/21 10:07 update
    # had to filter _out_v1.csv file
    # print total number of files of each directory
    for file_name in file_list:
      if file_name.endswith("_out_v1.csv"):
          continue

      file_name_parse = re.split('[._]', file_name)
      
      CSV_file = pd.read_csv(directory +"/"+file_name)
      CSV_file.columns=['Rank', 'Change','subcategory','App', 'Publisher', 'Price', 'Inapp', 'Date', 'CRScore','URL(Address)']
      
      # ex ) file_name_parse = ['AN','M','KR','FREE', 'TRAVEL', '201901','csv']
      
      CSV_file = add_column(CSV_file, file_name_parse)
      #add 6 columns Country, Type, OS, year, month, date type, Industry
      
      new_file_name= file_name_parse[0]+"_"+ file_name_parse[1]+"_"+\
                file_name_parse[2]+"_"+ file_name_parse[3]+"_"+ file_name_parse[4]+"_"+\
                file_name_parse[5]+"_out_v1.csv"
      # new file name
      # ex) AN_M_KR_FREE_EDUCATION_201901_out_v1.csv        
      CSV_file[["Country","Type","OS", "year", "month", "date type", \
                "Rank", "Change", "Industry", "subcategory","App","Publisher",\
                "Price", "Inapp", "Date", "CRScore", "URL(Address)"]]\
                .to_csv(directory+"/"+new_file_name, index= False)

      print("modify  " + file_name +  " with "+ str(len(CSV_file))+ " records")
      file_count = file_count +1
    
    print() 
    print("Modify Total "+str(file_count)+ " files in "+directory )
    print("------------------------------------------------------")
print()
print("End Program <Press> Enter")
end = input()
