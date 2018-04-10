# -*- coding: utf-8 -*-
"""
Created on Mon Apr  2 14:47:37 2018

@author: hasee
"""
 
 
 
 


class indexer:
    def __init__(self):
        self.dict={}
        self.file_obj=None
        self.query_obj=None
        self.query_list=[]
        self.operate_list=[]
    def read_csv(self,filename):
        self.file_obj=open(filename,encoding='utf-8').read().split('\n') 
    def read_query(self,filename):
        self.query_obj=open(filename,encoding='utf-8').read().split('\n')
        for i in range(len(self.query_obj)):
            split_obj=self.query_obj[i].split(' ')
            q=[]
            operate=None
            for item in split_obj:
                if item!="and" and  item!="or" and item!="not":
#                    jieba.add_word(item)
#                    jieba.suggest_freq(item,True) 
                    q.append(item) 
                else:
                    operate=item
            self.operate_list.append(operate)
            if len(q)>0:
                self.query_list.append(q)
                
                
                
    def add_doc(self):
        for i in range(len(self.file_obj)):
           output=self.file_obj[i].translate(str.maketrans(' ',' ',''':!),.:;?]}¢'"、。〉》」』】〕〗〞︰︱︳﹐､﹒﹔﹕%﹖﹗﹚﹜﹞！），．：；？－｜｝︴︶︸︺︼︾﹀﹂﹄﹏､～￠々‖•·ˇˉ―--′’”([{£¥'"‵〈《「『【〔〖（［｛￡￥〝︵︷︹︻︽︿﹁﹃﹙﹛﹝（｛“‘-—_…'''))
#           seg_list = jieba.cut_for_search(output)
#
#            x1=[output[]]
           x1=[]
           x2=[]
           x3=[]
           alphastr=None
           for j in range(len(output)-1):
               
               x1.append(output[j:j+2])
               x2.append(output[j:j+3])
               
               char=output[j]
               if (char>='a' and char<='z' ) or (char>='A' and char<='Z'):
                   if alphastr is None:
                       alphastr=char
                   else:
                       alphastr=alphastr+char
               else:
                   if alphastr is not None:
                       x3.append(alphastr)
                   alphastr=None
           seg=set(x1)|set(x2)|set(x3)
        
           
         
#           seg=list(seg)
#           seg=seg[1:len(seg)-1]
#           seg=set(seg)
           for word in seg:
              if word not in self.dict:
                   item=set()
                   item.add(i+1)
                   self.dict[word]=item
              else:
                   self.dict[word].add(i+1)
        print('dict created')           
        return self.dict  
        
        
        
    def output_query(self):
        output_list=[]
        print(len(self.query_list))
        print(len(self.operate_list))
        for index in range(len(self.query_list)):
            operate=self.operate_list[index]
            output=None
            for item in self.query_list[index]:
                if operate=='and':
                    if output==None:
                        output=self.dict[item]
                        
                    else:
                        output=output & self.dict[item]
                if operate=='or':
                    if output==None:
                        output=self.dict[item]
                    else:
                        output=output | self.dict[item]
                if operate=='not':
                    if output==None:
                        output=self.dict[item]
                    else:
                        output=output - self.dict[item]

            if output is not None:
                if len(output)>0:
                    output=sorted(output)
                if len(output)==0:
                    output.add(0)
                output_list.append(list(output))
        return output_list    
                    
                


    





        
if __name__ == '__main__':
    # You should not modify this part.
    
 
    
    import argparse

    parser = argparse.ArgumentParser()
    parser.add_argument('--source',
                       default='source.csv',
                       help='input source data file name')
    parser.add_argument('--query',
                        default='query.txt',
                        help='query file name')
    parser.add_argument('--output',
                        default='output.txt',
                        help='output file name')
    args = parser.parse_args()
    
    # Please implement your algorithm below
    

    
    index=indexer()
    index.read_csv(args.source)
    index.read_query(args.query)
    index_dict=index.add_doc()
    output_list=index.output_query()
   
    thefile = open(args.output, 'w')
    for item in output_list:
        item = ",".join(map(str, item))
        thefile.write("%s\n"%item)
    # TODO load source data, build search engine

    # TODO compute query result
  
    # TODO output result
    
    
    