import pandas as pd

raspologenie_part = pd.DataFrame({'Парты': ['1 парта','2 парта', '3 парта', '4 парта'],
                        '1 Ряд': [[' 1-1',' 1-2'],[' 5-1', ' 5-2'],[' 9-1', ' 9-2'],['13-1', '13-2']], 
                        '2 Ряд': [[' 2-1',' 2-2'],[' 6-1', ' 6-2'],['10-1', '10-2'],['14-1', '14-2']], 
                        '3 Ряд': [[' 3-1',' 3-2'],[' 7-1', ' 7-2'],['11-1', '11-2'],['15-1', '15-2']], 
                        '4 Ряд': [[' 4-1',' 4-2'],[' 8-1', ' 8-2'],['12-1', '12-2'],['16-1', '16-2']]})

print(raspologenie_part)