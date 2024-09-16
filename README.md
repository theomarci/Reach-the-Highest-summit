<img src=".\src\Banner.png">
<br>
<br>
<div align="center">
  <p>
    This is a little exercise in python that I modified to add a chart with two point displayed on it: the origin point and the highest summit fund point. I'm glad to share with you my work, my research. I know that my code isn't perfect (like my english 😄), I'm learning, But it's so important for me to introduce my learning path to you. The initial exercise comes from the AI learning course of Helsinki (link : <a href="https://www.elementsofai.com/">https://www.elementsofai.com</a>) but I add two python libraries (matplotlib and numpy) to display a chart.<br>
    the goal is to reach the high summit from an initial point and move 10 index to the left or 10 index to the right depending of the high value fund. Then I display a graph with red line taking in abscissa the index num and in ordinate the value of index.
  </p>
</div>
<br>
<br>
<div>
  <h4>Stack :</h4>
  <img src=".\src\icons8-python.gif" alt="just a gif">
  <br>
  <h4>Libraries :</h4>
  <ul>
    <li>Random</li>
    <li>Matplotlib</li>
    <li>Numpy</li>
    <li>Math</li>
  </ul>
</div>
<div>
  <h4>Some result examples</h4>
  <h5>graph :</h5>
  <img src=".\src\courbe python .png">
  <br>
  <img src=".\src\graph.png">
  <br>
  <br>
  <p>
    As you can see, I introduce you three examples displaying a red curved line and two colored points. What does the graph represent ? It's an excellent question that I hasten to answer you now ! First, The red curved line Link all points from my random numbers list calucated with random module and math module, for sin. Then you can see, two points one is blue and the other green. The blue point represents the starting position when I run my code for the first time, it indicated as the first parameter of the main function. The green point, for him, represents the arrival position when my code finish. However, You could observe that my second point isn't in the highest position of the curved line, this is explain by the fact that my function look for the highest point between limited index, in that case 10, to the left or to the right. Then this new point become the new origin point and I recall the function with it. When she didn't found any values superior of the current point then I stop the function and return the highest point found.
  </p>  
  <h3>Thank you so much to read me If you are some feedback I'm open</h3>
</div>
