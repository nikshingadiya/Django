from bs4 import BeautifulSoup
import argparse


def automata_href(tag,soup):
  for m in soup.findAll(tag,href=True):
      x=m['href']
      ans=r"{% static '"+x+"' %}"
      m['href']=ans
      print(ans)
  

def automata_src(tag,soup):
  for m in soup.findAll(tag,src=True):
      x=m['src']
      ans=r"{% static '"+x+"' %}"
      m['src']=ans
      print(ans)
  




def modify_link(src_path,dest_path,output_filename=""):
    with open(src_path) as fp:
      soup = BeautifulSoup(fp, 'html.parser')
      print(soup)
    

      list_tag=['link','a','img']

      for tag in list_tag:
        if tag!='img':
          automata_href(tag,soup=soup)
        else:
          print(tag)
          automata_src(tag,soup=soup)
    with open(output_filename, "w", encoding='utf-8') as file:
      file.write(str(soup))








if __name__=="__main__":
  parser=argparse.ArgumentParser()
  parser.add_argument("--source_path",help="source_html_file")
  parser.add_argument("--dest_path",help="destination_of_modify_file")
  parser.add_argument("--output_filename",help="destination_of_modify_file")

  

  args=parser.parse_args()

  get_file_path=args.source_path
 
  destination_path=args.dest_path
  output_filename=args.output_filename

  modify_link(src_path=get_file_path,dest_path=destination_path,output_filename=output_filename)
