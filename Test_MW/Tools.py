#import pickle
import os
import string
import random

class TableObjectMaker():
 def conserve(List,path_to_obj):
        file_path=path_to_obj
        if os.path.exists(file_path):
           os.remove(file_path)
        #print(file_path)
        the_file=open(file_path,"w")
        for line in  List:
            the_file.writelines(line)
            #print (line)
        the_file.close()

 def open_conserve(path_to_obj):
        List=[]        
        the_file=open(path_to_obj,'r')
        for line in the_file:
        
          try:List.append(line)             
          except:pass
        the_file.close()
        return List 

class DataGenerator():
    @staticmethod
    def generate_tourist_data():
        return " ".join(random.choice(string.ascii_uppercase + string.ascii_lowercase) for x in range(8))


        
        
    
