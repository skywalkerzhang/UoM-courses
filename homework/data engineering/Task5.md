### Task5

* **Task5.1**

  To get the Column Completeness, the data need to be filtered out according to the conditions. Because the conditions of 'Headway(s)' and 'Gap(s)' are the same, they can be filtered together.

  ```python
  # use a dictionary to store the Column Completeness.
  Column_Completeness = {}
  
  # get all data on Tuesday. 'Flags' refers to the day of the week, which has been gotten in task 1.
  condition = dataset.loc[dataset['Flags'] == 2]
  
  # Extract the time from 7:00 to 19:00. 'Hours' refers to the hours of a day.
  condition = condition.loc[(condition['Hours'] >= 7) & (condition['Hours'] < 19)]
  
  # get the quality assessment of the level of completeness of the 'Gaps(s).'
  # condition['Gap (s)'].count() is used for calculating the non-empty value of 'Gap (s)'
  # condition['Gap (s)'].size is used for getting number of the cells.
  Column_Completeness['Gap (s)'] = condition['Gap (s)'].count() * 100 / condition['Gap (s)'].size
  
  # get the quality assessment of the level of completeness of the 'Headways(s).' 'Hours' refers to the hours of a day, which I defined in task 2.
  # condition['Headway (s)'].icount() is used for calculating the non-empty value of 'Headway (s)'
  # condition['Headway (s)'].size is used for getting number of the cells.
  Column_Completeness['Headway (s)'] = condition['Headway (s)'].count() * 100 / condition['Headway (s)'].size
  
  # show the result
  Column_Completeness
  ```

  Then the **final result** is as following:

  ![image-20201112102709482](C:\Users\16778\AppData\Roaming\Typora\typora-user-images\image-20201112102709482.png)

  **interpretation：** 

  Completeness is one of the characteristics of data quality. In this task, it can be seen that in the 'Gap (s)' column, 98.04% of the data is non-empty. Besides, in the 'Headway (s)' column, 98.97% of the data is non-empty. I think the level of completeness for 'Gap (s)' and 'Headway (s)' is very high, but not 100, that means there are still some data is empty.

  Therefore, it would be better for us to do data cleaning to improve data quality. 

* **Task5.2**

  * **The first step:** Get median.

    ```python
    # get the lane named NB_MID
    NB_MID = dataset.loc[dataset['Lane Name'] == 'NB_MID']
    
    # get Tuesday
    NB_MID = NB_MID.loc[NB_MID['Flags'] == 2]
    
    # get the median between 7:00 - 19:00
    NB_MID_median = NB_MID.loc[(NB_MID['Hours'] >= 7) & (NB_MID['Hours'] < 19)].groupby(['Hours']).median()
    NB_MID_median
    ```

    ![image-20201112201425481](C:\Users\16778\AppData\Roaming\Typora\typora-user-images\image-20201112201425481.png)

    From the picture above,  'Gap (s)' and 'Headways' can be seen.

    **The medians of 'Gap (s)' and 'Headway (s)' are as following**:

    | Hours | Gap(s) | Headway(s) |
    | ----- | ------ | ---------- |
    | 7     | 1.8340 | 2.7220     |
    | 8     | 2.1020 | 3.1910     |
    | 9     | 2.0800 | 2.7200     |
    | 10    | 2.5835 | 3.0000     |
    | 11    | 2.7785 | 3.2100     |
    | 12    | 2.7950 | 3.1600     |
    | 13    | 2.7560 | 3.1020     |
    | 14    | 2.8050 | 3.1330     |
    | 15    | 2.5770 | 2.9200     |
    | 16    | 2.3225 | 2.8530     |
    | 17    | 2.1870 | 2.9065     |
    | 18    | 2.2280 | 2.7900     |

  * **The second step:**  

    Write a function to fill the median of  'Gap (s)' and 'Headway (s)'.

    In the description of this task, it is said that we can get the median by sorting, but there is no need for sorting steps, because I use pandas.

    Function to fill the median of  'Gap (s)' :

    ```python
    # function to fill median of 'Gap (s),' x represents each row in the dataset.
    def fill_median_of_gaps(x):
        
        # If the name of the road is not 'NB_MID' or 'Gap(s)' is not a null value or the time is not in 7:00-19:00, return to the original value.
        if x['Lane Name'] != 'NB_MID' or not pd.isna(x['Gap (s)']) or x['Hours'] >= 19 or x['Hours'] < 7:
            return x
        
        # else use the median to fill the missing data.
        # use NB_MID_median.loc[int(x['Hours'])] to get the Hours of x, and find the median of the corresponding 'Gap(s).'
        x['Gap (s)'] = NB_MID_median.loc[int(x['Hours'])]['Gap (s)']
        return x
    
    # assign to dataset. Now the empty columns of 'Gap (s)' is filled with median.
    dataset = dataset.apply(fill_median_of_gaps, axis=1)
    ```

    In the same way, function to fill the median of  'Headway (s)' are as followed:

    ```python
    # function to fill median of 'Headway (s),' x represents each row in the dataset.
    def fill_median_of_headways(x):
        
         # If the name of the road is not 'NB_MID' or 'Headway (s)' is not a null value or the time is not in 7:00-19:00, return to the original value.
        if x['Lane Name'] != 'NB_MID' or not pd.isna(x['Headway (s)']) or x['Hours'] >= 19 or x['Hours'] < 7:
            return x
        
        # else use the median to fill the missing data.
        # use NB_MID_median.loc[int(x['Hours'])] to get the Hours of x, and find the median of the corresponding # else use median to fill the missing data.
        # use NB_MID_median.loc[int(x['Hours'])] to get the Hours of x, and find the median of the corresponding 'Gap(s).'
        x['Headway (s)'] = NB_MID_median.loc[int(x['Hours'])]['Headway (s)']
        return x
    
    # assign to dataset. Now the empty columns of 'Gap (s)' is filled with median.
    dataset = dataset.apply(fill_median_of_headways, axis=1)
    ```

    In order to judge whether the code is correct, there are two snapshots below, one stands for some data before executing these two functions, and another stands for the same data after executing these two functions. By doing this, a comparison can be made.

    **Before executing:**

    I selected all the data at 7 o’clock, and the lane name called NB_MID and Gap(s) and Headway(s) are missing.

    ```python
    dataset.loc[(dataset['Hours'] == 7) & (dataset['Lane Name'] == 'NB_MID') & (pd.isna(dataset['Gap (s)'])) & (pd.isna(dataset['Headway (s)']))]
    ```

    We can see the part of these data

    ![image-20201112165324015](C:\Users\16778\AppData\Roaming\Typora\typora-user-images\image-20201112165324015.png)

    We could also choose some data at 9 o’clock, and the lane name called NB_MID and Gap(s) and Headway(s) are missing.

    ![image-20201112165714266](C:\Users\16778\AppData\Roaming\Typora\typora-user-images\image-20201112165714266.png)

    

    **After executing:**

    Compared to the average that we got, we can say that we got the correct answer.

    Hours = 7:

    ![image-20201112202018410](C:\Users\16778\AppData\Roaming\Typora\typora-user-images\image-20201112202018410.png)

    Hours = 9:

    ![image-20201112201727872](C:\Users\16778\AppData\Roaming\Typora\typora-user-images\image-20201112201727872.png)

* **interpretation：** 
  
    Filling in empty values with median is a common data processing method, we can also use mean or mode to fill it. What we are doing now is called data cleaning, which can improve data quality. 
  
    For the final result, if we do not want 'Hours' and 'Day_of_the_month.' We could use del to delete it, and this helps to improve data quality because these two columns are actually redundant data. For the convenience of processing data later, I have not deleted it temporarily, but it should be deleted when the data is stored.

### Task6

* **The first step:** Get the average speed at 17:00 on Fridays that the direction is north. 

  In file 1083, the code is as following:

  ```python
  # find the data on Friday
  condition_for_avg_speed = dataset.loc[dataset['Flags'] == 5]
  
  # find the data that between 17:00 - 18:00
  condition_for_avg_speed = condition_for_avg_speed.loc[dataset['Hours'] == 17]
  
  # find the data that direction is north
  condition_for_avg_speed = condition_for_avg_speed.loc[dataset['Direction'] == 1]
  
  # get the average speed of 1083 
  avg_1083 = condition_for_avg_speed.groupby(['Lane']).mean()
  ```

  The answer is as followed：

  ![image-20201112202501376](C:\Users\16778\AppData\Roaming\Typora\typora-user-images\image-20201112202501376.png)

  It can be seen that the averages of each lane, and it can be used by using `avg_1083['Speed (mph)']`

  In the file 1415, the data should be put in pandas first.

  ```python
  data_1415 = pd.read_csv("rawpvr_2018-02-01_28d_1415 TueFri.csv", index_col = False)
  dataset.head()
  ```

  ![image-20201112185257557](C:\Users\16778\AppData\Roaming\Typora\typora-user-images\image-20201112185257557.png)

  Then, get the average number of speed, it can be seen that Direction = 2 stands for the Direction is north.

  Besides, the label 'Flags' and the label 'Hours'(the hours of a day) should be gotten first.

  ```python
  # create a column to describe hour
  data_1415['Hours'] = data_1415['Date'].apply(lambda s : datetime.strptime(s[:19], "%Y-%m-%d %H:%M:%S").hour)
  
  # get the Flags
  data_1415['Flags'] = data_1415['Date'].apply(lambda s : datetime.strptime(s[:19], "%Y-%m-%d %H:%M:%S").weekday()+1)
  ```

  Then, select qualified data.

  ```python
  # find the data on Friday
  condition_for_avg_speed = data_1415.loc[dataset['Flags'] == 5]
  
  # find the data that between 17:00 - 18:00
  condition_for_avg_speed = condition_for_avg_speed.loc[dataset['Hours'] == 17]
  
  # find the data that direction is north
  condition_for_avg_speed = condition_for_avg_speed.loc[dataset['Direction'] == 1]
  
  # get the average speed of 1083 
  avg_1415 = condition_for_avg_speed.groupby(['Lane']).mean()
  ```

  We get the result.

  ![image-20201112202612174](C:\Users\16778\AppData\Roaming\Typora\typora-user-images\image-20201112202612174.png)

  Finally, calculate the average of the five lanes.

  ```python
  # /5 is because we got 5 speed.
  avg_speed = (avg_1083['Speed (mph)'].sum() + avg_1415['Speed (mph)'].sum()) / 5
  
  # convert to mph -> km/h
  avg_speed *= 1.6
  ```

  The result is

  ![image-20201112202921594](C:\Users\16778\AppData\Roaming\Typora\typora-user-images\image-20201112202921594.png)

* **The second step:** Calculate the time.

  ```python
  # distance is given in task
  distance = 4.86
  
  time = distance / avg_speed
  
  # get the result in minutes
  time *= 60
  ```

  So, the answer is 

  ![image-20201112202934928](C:\Users\16778\AppData\Roaming\Typora\typora-user-images\image-20201112202934928.png)

  Convert to two decimal places is 6.75 (min.)


* **interpretation：**

  In this task, we use average to describe the journey time for the north lanes between site 1083 and site 1415 between 17:00 and 18:00.

  The average can describe the general level of the object. Through the average value, we can see where the data is concentrated. It can be used to get general information.

### Task7

* **part1:**

  An analogy to Task 5, I suggest 2 formula:

  The **first** one is:

  `Rows_Completeness = (number_of_non-empty_cells_for_each_row x 100) / number_of_cells` 

  The **second** one is:

  `Another_Rows_Completeness = (number_of_non-empty_rows x 100) / number_of_row` 

  I personally understand row completeness from two different perspectives. The first one is focusing on each specific row, measure the completeness of each specific row and express it by an average value, and the second is to treat each row as a unit to get the row completeness from the whole.

  Since I have created two labels before, I need to delete them ('Hours,' 'Day_of_the_month'). 

  ```python
  # del the label 'Hours' and 'Day_of_the_month'
  tmp = condition.drop(['Hours', 'Day_of_the_month'], axis=1)
  ```

  

  ![image-20201113135040181](C:\Users\16778\AppData\Roaming\Typora\typora-user-images\image-20201113135040181.png)

  It should be noticed that we should use the data before task 6 because task 6 has changed the data we deal with.  Besides, I have created the variable 'condition' before, which is as followed.  

  ![image-20201113141027400](C:\Users\16778\AppData\Roaming\Typora\typora-user-images\image-20201113141027400.png)

  According to the task description, we will only focus on 'Speed (mph)' and 'Headways (s).' Therefore, it does not matter whether the 'Flags' and 'Flag Text' are empty (the initial data is empty but during the tasks, it changed, so it became non-empty ), and there is no need to process them separately. Besides, if the 'Flags' and 'Flag Text' are not empty, the only two empty labels are Speed (mph)' and 'Headways (s),' that is what we needed.

  We could use this condition to get completeness.

  **The first one is**

  ```python
  # row.isna() means the cells that are missing (In this case, only highway and speed could be missing). 
  # So len(row) - row.isna().sum() stands for the non-empty cells.
  # len(row) can get all the cells in one row.
  Rows_Completeness = tmp.apply(lambda row: (len(row) - row.isna().sum()) * 100 / len(row), axis=1)
  Rows_Completeness
  ```

  Then, all the rows completeness have been gotten.

  ![image-20201113142318962](C:\Users\16778\AppData\Roaming\Typora\typora-user-images\image-20201113142318962.png)

  Get the mean of these completeness.

  ```python
  Rows_Completeness.mean()
  ```

  ![image-20201113142636571](C:\Users\16778\AppData\Roaming\Typora\typora-user-images\image-20201113142636571.png)

  The result is 99.70 (2 Decimal)

  **The second one is:**

  ```python
  # rows_empty stands for the row contains the empty cell.
  # tmp.isnull().any(axis=1) can get the rows that are empty. axis = 1 stands for low.
  rows_empty = tmp.loc[tmp.isnull().any(axis=1)]
  
  # len(tmp) - len(non_empty) Represents rows without any empty cells.
  Another_Rows_Completeness = (len(tmp) - len(non_empty)) * 100 / len(tmp)
  Another_Rows_Completeness
  ```

  The answer is :

  ![image-20201119002230650](C:\Users\16778\AppData\Roaming\Typora\typora-user-images\image-20201119002230650.png)

  The values obtained by both methods are very high, close to one hundred. We could infer that the completeness of the data is high. Besides, according to the formula in task 5 and task 7, it is not hard to find that if we divided these formulae by 100, we would get a percentage, which is the proportion of non-empty values in the total data.

  I think this might be a good way to measure the completeness of the data. (Actually, I think divided by 100 change it to percentage will be more intuitive.)

* **part2:**

  I use Excel as my second tool to do task 6.

  * **The first step:** calculate the  average speed at 17:00 on Fridays on each lane.

    1. Open the file `'rawpvr_2018-02-01_28d_1083 TueFri.csv'`, and the file `rawpvr_2018-02-01_28d_1415 TueFri`

    2. Change the format of the date cell.

       In file 1013, select the cell, right-click and choose format cell.

       ![image-20201114074134405](C:\Users\16778\AppData\Roaming\Typora\typora-user-images\image-20201114074134405.png)

       Then, the result is as following:

       ![image-20201114074325114](C:\Users\16778\AppData\Roaming\Typora\typora-user-images\image-20201114074325114.png)

       Use the same method to process files 1415.

       ![image-20201114074632320](C:\Users\16778\AppData\Roaming\Typora\typora-user-images\image-20201114074632320.png)

    3. Use function WEEKDAY to calculate the label 'Flags.' Select the cell that needs to be deal with, then click ![image-20201114075456787](C:\Users\16778\AppData\Roaming\Typora\typora-user-images\image-20201114075456787.png) to insert a function.

       ![image-20201114081743679](C:\Users\16778\AppData\Roaming\Typora\typora-user-images\image-20201114081743679.png)

       Select category Date & Time, and select WEEKDAY.

       ![image-20201108144241344](C:\Users\16778\AppData\Roaming\Typora\typora-user-images\image-20201108144241344.png)

        Then, select the Serials number and return type. According to the requirements of this task, 2 should be selected as the return type.

       ![image-20201108144525620](C:\Users\16778\AppData\Roaming\Typora\typora-user-images\image-20201108144525620.png)

       ![image-20201108144833803](C:\Users\16778\AppData\Roaming\Typora\typora-user-images\image-20201108144833803.png)

       The label 'Flags' has been gotten, and the function WEEKDAY can be applied to the whole column.  First, select the cell just be mentioned, right-click to copy. Second, Select the starting cell, press shift, and then select the ending cell.

       ![image-20201114082448151](C:\Users\16778\AppData\Roaming\Typora\typora-user-images\image-20201114082448151.png)

    4. Create the label 'Hours' to get the hours of a day. In the same way, the label 'Hours' could be gotten.

       ![image-20201108164527245](C:\Users\16778\AppData\Roaming\Typora\typora-user-images\image-20201108164527245.png)

       ![image-20201108164609932](C:\Users\16778\AppData\Roaming\Typora\typora-user-images\image-20201108164609932.png)

       ![image-20201108164419678](C:\Users\16778\AppData\Roaming\Typora\typora-user-images\image-20201108164419678.png)

       

       ​		The result is:

       

       ![image-20201108165212031](C:\Users\16778\AppData\Roaming\Typora\typora-user-images\image-20201108165212031.png)

       The same method can be applied to the file 1415 to get the label 'Flags' and create the label 'Hours.' 

       The result is as following:

       ![image-20201114083954936](C:\Users\16778\AppData\Roaming\Typora\typora-user-images\image-20201114083954936.png)

    5. Calculate average speed by using the function AVERAGEIFS

       1. Select a cell to put average.

       2. Click ![image-20201114075456787](C:\Users\16778\AppData\Roaming\Typora\typora-user-images\image-20201114075456787.png) to use a function.

       3. Find AVERAGEIFS, and click OK.

          ![image-20201114075549900](C:\Users\16778\AppData\Roaming\Typora\typora-user-images\image-20201114075549900.png)

          The following interface will be displayed:

          ![image-20201114075822236](C:\Users\16778\AppData\Roaming\Typora\typora-user-images\image-20201114075822236.png)

          'Speed' is used to find the average, so select speed.

          ![image-20201114080449517](C:\Users\16778\AppData\Roaming\Typora\typora-user-images\image-20201114080449517.png)

          It can be seen that F is 'Speed.'

       4. Get the average speed of each lane one by one.

          Filter out the lane to the north in these two files. It can be seen that the lanes' number are 1, 2, 3 in file 1083 and 1, 2 in file 1415.

          ![image-20201114085116080](C:\Users\16778\AppData\Roaming\Typora\typora-user-images\image-20201114085116080.png)

          ​	It can be checked in the way that is shown below.

          ![deal1](C:\Users\16778\AppData\Roaming\Typora\typora-user-images\deal1.png)

          Calculate the **lane 1 in file 1083** first:

          Select 'Direction Name.' 

          ![image-20201114080748485](C:\Users\16778\AppData\Roaming\Typora\typora-user-images\image-20201114080748485.png)

          It can be seen that E is 'Direction Name,' and fill the 'Criteria1.' In this case, the Direction is North, so fill '= North.'

          Then, we can use the same way to select 'Hours,' 'Flags' and 'Lane.'

          ![image-20201114091853399](C:\Users\16778\AppData\Roaming\Typora\typora-user-images\image-20201114091853399.png)

          ![image-20201114091918287](C:\Users\16778\AppData\Roaming\Typora\typora-user-images\image-20201114091918287.png)

          ![image-20201114091937691](C:\Users\16778\AppData\Roaming\Typora\typora-user-images\image-20201114091937691.png)

          ![image-20201114091955813](C:\Users\16778\AppData\Roaming\Typora\typora-user-images\image-20201114091955813.png)

          Then, the average speed of lane 1 has been gotten.

          ![image-20201114092020798](C:\Users\16778\AppData\Roaming\Typora\typora-user-images\image-20201114092020798.png)

          In the same way, we can also get the average speed of **lane 2, 3 in file 1083**

          ![image-20201114092048387](C:\Users\16778\AppData\Roaming\Typora\typora-user-images\image-20201114092048387.png)

          we can also get the average speed of **lane 1, 2 in file 1415**

          ![image-20201114093852836](C:\Users\16778\AppData\Roaming\Typora\typora-user-images\image-20201114093852836.png)

          Then, calculate the final average speed.

          Copy(only values) the two speed in file 1415 to 1083, then use function AVERAGE calculate(Actually, Excel supports averaging across files, just for intuitiveness.)

          ![image-20201114093804512](C:\Users\16778\AppData\Roaming\Typora\typora-user-images\image-20201114093804512.png)

          The **the average of the five lanes** is ![image-20201114093831124](C:\Users\16778\AppData\Roaming\Typora\typora-user-images\image-20201114093831124.png), and we need to covert it from mph into km/h by times 1.6.

          It is![image-20201114093915283](C:\Users\16778\AppData\Roaming\Typora\typora-user-images\image-20201114093915283.png)
       
          The average is different, because of **accuracy issues**.

  * **The second step:**  get the average time 

    Using distance 4.86km divide the average speed and times 60 to get the average time(min.)

    ![image-20201114093946799](C:\Users\16778\AppData\Roaming\Typora\typora-user-images\image-20201114093946799.png)

    ![image-20201114094007592](C:\Users\16778\AppData\Roaming\Typora\typora-user-images\image-20201114094007592.png)

    Therefore the final answer is 6.707965, is different from task 5, might be a loss of accuracy.


  **Assessment of the two technologies**

  * **similarities:**

    * Both Excel and python have many functions to deal with data.

      For example, in this coursework, the required data can be filtered by python's loc method or achieved using  Excel's COUNTIFS, or could use AVERAGEIFS.

      Excel and python have many functions with similar functions.

     * Both Excel and Python can deal with CSV file.

    

  * **differences:**

    * Excel

      * Advantage: 

        1. Excel has a graphical interface. When processing data, people only need to use the mouse to select the cell that needs to be processed and follow the instructions to write the conditions. This means that even people who are not programmers can perform some complex operations on the data. For programmers, data selection becomes more intuitive.

           For example, in task 6,  we need to deal with the label 'Direction,' 'Hours,' and 'Flags.' Using Excel is more intuitive and convenient than python. 

        2. When people do not know what method to use to process data, sometimes people can get the answer directly through the Excel menu name.

           For example, when I calculated the label 'Flags,' I did not know the WEEKDAY function, but through a series of clicks, I found it without searching online.

      * Limitation:

        1. The amount of data that Excel can handle is smaller than python, and the larger the data, the slower the calculation speed.
        2. Excel can only be used for windows and mac, not for Linux.
        3. Excel is hard to deal with the loop!

    * Python

      * Advantage:

        1. People can code functions to solve the same problem.

           When faced with complex tasks, python can write complex tasks in a function, which can be easily called. Excel can only repeat this process manually.

        2. Python is a cross-platform language, can also be used on Linux.

        3. Python has many modules about machine learning and deep learning, which is more convenient to use after python processing data.

        4. Python can integrate SQL statements, making it more convenient to process databases.

        5. Python can handle large amounts of data.

      * Limitation:

        1. Compared with Excel, python is harder to learn. The free and flexible syntax may produce many bugs that are difficult to fix.

           


  In this task, I think excel is more challenging to deal with conditions than python. Besides, it’s difficult for others to reproduce the results, people must read a lengthy document, and python only needs to run the code.