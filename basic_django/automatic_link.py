from bs4 import BeautifulSoup
import argparse
import os
import shutil
import glob
def replace_text(m,key):
    x=m[key]
    ans=r"{% static '"+x+"' %}"
    
    m[key]=ans

def url_based_replace(m,key):
     x=m[key]
     x=x.split(".")[0]
     ans=r"{% url '"+x+"' %}"
     m[key]=ans

def automata_href(list_tag,soup,html_file_list):
  html_file_list=[i.split("/")[-1] for i in html_file_list]
  for m in soup.findAll(list_tag):
      
      if m.name in ['a','link']:
          x=m['href']
        
          if x in html_file_list:
             
             url_based_replace(m,'href')
             print("url")
          else:
            replace_text(m,'href')

      if m.name in ['script','img']:
         
         replace_text(m, 'src')


def reset_folder_file_copy(src_rest_fd,dest_rest_fd):
  if os.path.isfile(src_rest_fd):
    shutil.copy(src_rest_fd, dest_rest_fd)
  else:
    shutil.copytree(src_rest_fd,dest_rest_fd)


def modify_link(src_folder_path,dest_path_folder):
    static_str="{% load static %}"
    all_list_file_folder=glob.glob(src_folder_path+"/*")
    list_html_file=glob.glob(src_folder_path+"/*.html")

    rest_file_folder=set(all_list_file_folder)-set(list_html_file)
    for i in list_html_file:
        
        with open(f"{i}") as fp:
          soup = BeautifulSoup(fp, 'html.parser')
      
          list_tag=['link','a','img','script']
          automata_href(list_tag,soup=soup,html_file_list=list_html_file)
    
        with open(dest_path_folder+"/"+i.split("/")[-1], "w", encoding='utf-8') as file:
          file.write(static_str+str(soup))
    
    for i in rest_file_folder:
      file_name=i.split("/")[-1]
      if file_name in os.listdir(dest_path_folder):
          target=dest_path_folder+"/"+file_name
          if os.path.isfile(target):
             os.unlink(target)
          else:
            shutil.rmtree(target)
          
      reset_folder_file_copy(i,dest_path_folder+"/"+file_name)





if __name__=="__main__":
  parser=argparse.ArgumentParser()
  parser.add_argument("--src_folder_path",help="source_html_file")
  parser.add_argument("--dest_folder_path",help="destination_of_modify_file")


  

  args=parser.parse_args()

  get_src_path_folder=args.src_folder_path
 
  get_dest_path_folder=args.dest_folder_path
 

  modify_link(src_folder_path=get_src_path_folder,dest_path_folder=get_dest_path_folder)
