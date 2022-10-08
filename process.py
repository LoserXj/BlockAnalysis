import os
import pandas as pd

dir1="./钓鱼数据集"
directory1=os.listdir(dir1)
nodeSet=set()
for dir2 in directory1:
  if dir2=='钓鱼一阶节点' or dir2=='非钓鱼一阶节点':
      directory2=os.listdir(os.path.join(dir1,dir2))
      for file in directory2:
          csvData=pd.read_csv(os.path.join(dir1,dir2,file))
          for row in csvData.values:
              nodeSet.add(row[4])
              nodeSet.add(row[5])
  else:
      directory2=os.listdir(os.path.join(dir1,dir2))
      for dir3 in directory2:
          if os.path.isdir(os.path.join(dir1,dir2,dir3)):
              directory3=os.listdir(os.path.join(os.path.join(dir1,dir2,dir3)))
              for file in directory3:
                  csvData=pd.read_csv(os.path.join(dir1,dir2,dir3,file))
                  for row in csvData.values:
                      nodeSet.add(row[4])
                      nodeSet.add(row[5])
print(len(nodeSet))




