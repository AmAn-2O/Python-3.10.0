import pandas as pd
students=[
    {"Name":"hermione","House":"gryfindor","Patronous":"otter"},
{"Name":"harry potter","House":"gryfindor","Patronous":"sch"},
{"Name":"ron","House":"gryfindor","Patronous":"jack rume"},
{"Name":"draco","House":"slytherine","Patronous":"none"}
]
df=pd.DataFrame(students)
print(df,df[1:3])

