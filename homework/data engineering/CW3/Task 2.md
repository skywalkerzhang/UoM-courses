### Task 2

First, analyze the task. It is required to find the traffic volume of the North lanes at 9 am on Tuesday.

**There should be 12 numbers in the resulting traffic volume. Because we have four Tuesdays in February 2018 (to be found later), and three lanes are pointing to the north. The volume can be divided into 12 groups, and 12 numbers are obtained.**

**However, the teacher said there should be 4 numbers(Only group by Days). Therefore, I wrote the process of two answers.**

The label 'Direction,' 'Flags,' 'Lanes', and 'Hours' (used to record the hours of a day) can accomplish this task.

The label 'Flags' has been gotten in task 1, which identifies the day of the week. Besides, the 'DataFrame' in pandas can be used to process the data.

* **The first step** is creating the label we needed.

  Creating a new label called Hours to extract the data at 9 am. Besides, to distinguish which day of February the data came from, I created the label 'Day_of _the_month.'

  For convenience, the library 'datetime' is used to deal with the label 'Date.'
  
  ```python
  dataset['Hours'] = dataset['Date'].apply(lambda s : datetime.strptime(s[:19], "%Y-%m-%d %H:%M:%S").hour)
dataset['Day_of_the_month'] = dataset['Date'].apply(lambda s : datetime.strptime(s[:19], "%Y-%m-%d %H:%M:%S").day)
  ```
  
  'Hours' refers to the hours of a day, and 'Day_of_the_month' refers to February's date. For example, in data '2018-02-09 10:01:58.050000', 'Hours' is 0, and 'Day_of_the_month' is 9.
  
  The function head() can be used to show it.
  
  ![image-20201108122225993](C:\Users\16778\AppData\Roaming\Typora\typora-user-images\image-20201108122225993.png)
  
  
  
* **The second step** is calculating the volume.

  In pandas, it is easy to access a group of rows and columns using the function loc, especially under some special conditions, and the function groupby() can be used to group data and compute operations on these groups.

  **If the data is divided into 12 groups, then the code is as follows:**

  ```python
  tmp = dataset.loc[dataset["Flags"] == 2] # Get data on Tuesday
  tmp = tmp.loc[dataset['Hours'] == 9] # Get data on Tuesday at 9 am
  tmp = tmp.loc[dataset['Direction'] == 1] # Get data on Tuesday at 9 am, and the direction is north
  traffic_volume_for_Tue = tmp.groupby(['Day_of_the_month','Lane']).size() 
  ```

  ![image-20201108123246993](C:\Users\16778\AppData\Roaming\Typora\typora-user-images\image-20201108123246993.png)

  **If the data is divided into 4 groups, then the code is as follows:**

  ```python
  tmp = dataset.loc[dataset["Flags"] == 2]
  tmp = tmp.loc[dataset['Hours'] == 9]
  tmp = tmp.loc[dataset['Direction'] == 1]
  traffic_volume_for_Tue = tmp.groupby(['Day_of_the_month']).size()
  ```

  ![image-20201109111559006](C:\Users\16778\AppData\Roaming\Typora\typora-user-images\image-20201109111559006.png)

  The variable traffic_volume_for_Tue stands for the North lanes' traffic volume on Tuesday at 9 am and use the function size() to obtain the traffic volume through the number of eligible rows.

  The data can be grouped by 'Day_of_the_month' and 'Lane.'

* **The third step** is getting Range, 1st Quartile, 2nd Quartile, 3rd Quartile, Interquartile range.

  There are 2 ways to get them.

  The first one is to use dataframe.describe()

  **If the data is divided into 12 groups:**
  
  ```python
traffic_volume_for_Tue.describe()
  ```

  ![image-20201108053548532](C:\Users\16778\AppData\Roaming\Typora\typora-user-images\image-20201108053548532.png)

  The 1st Quartile, 2nd Quartile, 3rd Quartile have been gotten. Then, calculate the Range by using the maximal value - minimal value 915 - 682 = 233. We also can use the 3rd Quartile - 1st Quartile to get the Interquartile range 861.75 - 770.75 = 91.00. We can subtract them directly since we already got them.
  
  The second one is to use the function quantile() to get the quantiles.
  
  ```python
  volume_range = max(traffic_volume_for_Tue) - min(traffic_volume_for_Tue)
  interquartile_range = traffic_volume_for_Tue.quantile(0.75) - traffic_volume_for_Tue.quantile(0.25)
  ```
  
  **If the data is divided into 4 groups:**
  
  ```python
  traffic_volume_for_Tue
  ```
  
  ![image-20201109112105393](C:\Users\16778\AppData\Roaming\Typora\typora-user-images\image-20201109112105393.png)
  
  In the same way, we can get the Range 226, and the Interquartile range 72.25.
  
* **The final result** :

  * **If the data is divided into 12 groups:**

    range = 233.00

    1st Quartile = 770.75

    2nd Quartile = 819.00

    3rd Quartile = 861.75

    Interquartile range = 91.00

  * **If the data is divided into 4 groups:**

    range = 226.00

    1st Quartile = 2397.25

    2nd Quartile = 2436.50

    3rd Quartile = 2469.50

    Interquartile range = 72.25

  * **Interpretation**:

    The Range of a data set could measure the variability, and it is very sensitive to the smallest and largest value.

    The Interquartile range of a data set can also measure the variability, which is middle 50% of the data. Compared to the Range, it overcomes the sensitivity to extreme data values.

    **If the data is divided into 12 groups:** 

    ![image-20201110111115229](C:\Users\16778\AppData\Roaming\Typora\typora-user-images\image-20201110111115229.png)

    The data we got is, as shown above. We can see that the traffic volume on the 6th in lane 3 is the largest, while the traffic volume on the 20th in lane 1 is the largest. The Range is 233, which can be said that the data fluctuates no very large. Besides, the Interquartile range is 91, 91 * 2 = 182 and the range is 233. These two numbers are relatively close. Therefore, maybe there are not many extreme values about the traffic volume of the North lanes at 9 am on Tuesday.

    **If the data is divided into 4 groups:**

    ![image-20201110112624573](C:\Users\16778\AppData\Roaming\Typora\typora-user-images\image-20201110112624573.png)

    The data we got is, as shown above. We can see that the traffic volume on the 6th is the largest, while the traffic volume on the 20th is the largest. We can also see that the Range is 226, which can be said that the data fluctuates no very large. Besides, the Interquartile range is 72.25, 72.25 * 2 = 144.5 and the range is 226. These two numbers are relatively close. Therefore, maybe there are not many extreme values about the traffic volume of the North lanes at 9 am on Tuesday. 

### Task 3

I pick up Tuesday and visualize the average traffic volume for each hour on that day.

* **The first step** is calculating the traffic volume of the north lane and the south lane.

  ```python
  north_volume_per_hour = dataset.loc[dataset['Flags'] == 2].loc[dataset['Direction'] == 1].groupby(['Hours']).size()
  north_volume_per_hour /= 4
  south_volume_per_hour = dataset.loc[dataset['Flags'] == 2].loc[dataset['Direction'] == 2].groupby(['Hours']).size()
  south_volume_per_hour /= 4
  ```

  We get the number of all the rows on Tuesday and group by hours (North and South) and divide 4 to get the average.

* **The second step** is using matplotlib.pyplot to visualize.

  matplotlib is a great module for visualization.  The library seaborn can be used to achieve visualization too.

  ```python
  import matplotlib.pyplot as plt
  %matplotlib notebook
  north_volume_per_hour.plot.bar(x="Hours", title="volume for north")
  ```

  Then, we could use matplotlib.pyplot.text() to add the average number of charts.

  ```python
  for i, v in enumerate(north_volume_per_hour):
      plt.text(i-0.5, v + 1, str(v), fontsize=7)
  plt.tight_layout()
  ```

  ![north](C:\Users\16778\Desktop\north.png)

and use the same way to get the south

![south](C:\Users\16778\Desktop\south.png)

* **Interpretation**:

  From the above two graphs, we can see the average traffic volume for each hour of Tuesday in the south is similar to the direction in the north, and the data at 7 - 9 o'clock and 15 - 17 o'clock are relatively high, while at 0 - 5 o'clock and 22 o'clock, 23 o'clock are relatively low. Besides, in the north, the data peak is 2951.5, which is at 7 o'clock, while in the south the data peak is 3001.25, which is at 16 o'clock. Meanwhile, both in the south and the north, the data are low in February.

### Task 4

I choose Excel as a GUI tool to do visualization and still choose Tuesday. The reason why I choose Excel is the amount of this dataset is not very large. If the data set is very large, just choose another GUI tool (Think about NHS news.)

* **The first step** deals with the label 'Flags.' Change the cell format to date is required.

  1. Select  the 'Date' column, click the right button and select the Format cell.

  ![image-20201108142654878](C:\Users\16778\AppData\Roaming\Typora\typora-user-images\image-20201108142654878.png)

  2. Choose the format shown above. 

     ![image-20201108143024197](C:\Users\16778\AppData\Roaming\Typora\typora-user-images\image-20201108143024197.png)

  3. Use function WEEKDAY to calculate the label 'Flags.'
  
  ​	Select the cell that needs to be deal with, then click fx to insert a function.
  
  ![image-20201108143721949](C:\Users\16778\AppData\Roaming\Typora\typora-user-images\image-20201108143721949.png)
  
  ​	Select category Date & Time, and select WEEKDAY.
  
  ![image-20201108144241344](C:\Users\16778\AppData\Roaming\Typora\typora-user-images\image-20201108144241344.png)
  
   Then, select the Serials number and return type. According to the requirements of this task, 2 should be selected as the return type.

![image-20201108144525620](C:\Users\16778\AppData\Roaming\Typora\typora-user-images\image-20201108144525620.png)

![image-20201108144833803](C:\Users\16778\AppData\Roaming\Typora\typora-user-images\image-20201108144833803.png)

​    	The label 'Flags' has been gotten, and the function WEEKDAY can be applied to the whole column.  First, select the cell just be mentioned, right-click to copy. Second, Select the starting cell, press shift, and then select the ending cell.

​											 ![image-20201108163418750](C:\Users\16778\AppData\Roaming\Typora\typora-user-images\image-20201108163418750.png)

​		

* **The second step** is getting the hours of the day. Created a column named hours and then use function HOUR to get the hours of the day. The step is similar to the first step.

  ![image-20201108164527245](C:\Users\16778\AppData\Roaming\Typora\typora-user-images\image-20201108164527245.png)

  ![image-20201108164609932](C:\Users\16778\AppData\Roaming\Typora\typora-user-images\image-20201108164609932.png)

  ![image-20201108164419678](C:\Users\16778\AppData\Roaming\Typora\typora-user-images\image-20201108164419678.png)



​	

​		The result is:

![image-20201108165212031](C:\Users\16778\AppData\Roaming\Typora\typora-user-images\image-20201108165212031.png)

* **The third step** is getting the total volume(North and South).

  The function COUNTIFS can be used to solve it. The COUNTIFS function applies conditions to cells that span multiple regions, and then counts the number of times all conditions are met.

  1. Create column 'North_avg,' and 'South_avg.' Click fx to insert a function.

     In statistical, select COUNTIFS.

     ![image-20201108173711777](C:\Users\16778\AppData\Roaming\Typora\typora-user-images\image-20201108173711777.png)

  2. Filter by conditions

     ![image-20201108181403676](C:\Users\16778\AppData\Roaming\Typora\typora-user-images\image-20201108181403676.png)

     D is the column 'Direction,' I is the column 'Flags,' K is the column 'Hours.' Criterial1 means Direction = 2, other similarities.

  3. Manually change the conditions of Hours from 0-23.

![image-20201108182207889](C:\Users\16778\AppData\Roaming\Typora\typora-user-images\image-20201108182207889.png)

​			Divide these values by 4(Because there are four Tuesdays in February 2018). Finally, the average number has been gotten.  In the same way, the traffic volume in the south can also be gotten.

![image-20201108183520016](C:\Users\16778\AppData\Roaming\Typora\typora-user-images\image-20201108183520016.png)

* **The final step** is to draw charts with excel.

  Select all the North_avg, and click File - Insert, and choose Bar chart.

  ![image-20201108185131562](C:\Users\16778\AppData\Roaming\Typora\typora-user-images\image-20201108185131562.png)

![image-20201108185330119](C:\Users\16778\Desktop\Picture2.png)

​	Right-click, select add data labels.

​	In the same way, the south volume can also be gotten.

​	![](C:\Users\16778\Desktop\Picture1.png)

* **Assessment of the two technologies**

  * **similarities:**

     * Both Excel and python have many functions to deal with data.

          For example, in this coursework, the required data can be filtered by python's loc method or achieved using  Excel's COUNTIFS.

          Excel and python have many functions with similar functions.

      * Both Excel and Python can realize data visualization.

          The library matplotlib in python can be used for visualization, and Excel also provides the function of generating various charts. 

          In python, the kind of plot to produce: The kind of plot to produce: line, bar, hist, box, pie and so on. In comparison, excel can also generate these charts.

      * Both Excel and Python can deal with CSV file.

     

  * **differences:**

    * Excel

      * Advantage: 

        1. Excel has a graphical interface. When processing data, people only need to use the mouse to select the cell that needs to be processed and follow the instructions to write the conditions. This means that even people who are not programmers can perform some complex operations on the data. For programmers, data selection becomes more intuitive.

           For example, in task 3, we need to process the label 'Direction,' 'Hours,' and 'Flags.' Using Excel is more intuitive and convenient than python. When using python, we need to locate twice and groupby once. 

        2. When people do not know what method to use to process data, sometimes you can get the answer directly through the Excel menu name.

           When I calculated the label 'Flags,' I did not know the WEEKDAY function, but through a series of clicks, I found it without searching online.

      * Limitation:

         1. The amount of data that Excel can handle is smaller than python, and the larger the data, the slower the calculation speed.
         2. Excel can only be used for windows and mac, not for Linux.

    * Python

      * Advantage:

        1. People can code functions to solve the same problem.

        2. 1. When there are many repetitive operations to be done, python can reduce a lot of repetitive operations.
             2. Python is a cross-platform language, can also be used on Linux.
             3. Python has many modules about machine learning and deep learning, which is more convenient to use after python processing data.
             4. Python can integrate SQL statements, making it more convenient to process databases.
             5. Python can handle large amounts of data.

          - Limitation:

          1. Compared with Excel, python is harder to learn. The free and flexible syntax may produce many bugs that are difficult to fix.

             


  ​         In this task, I do not think Excel is worse than python. Even sometimes, Excel is more intuitive in terms of filtering conditions, but Python can do everything Excel can do. Therefore, as a computer student, we still have to learn python well.