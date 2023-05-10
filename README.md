# Figure Skating Olympic Medals Project

The aim of this project is to answer the following question: How has the number of U.S. figure skating Olympic medals evolved over the history of the Winter Olympic games?

To answer this question, I used Olympic medalists in figure skating data obtained from Wikipedia. The data was extracted manually and stored in Excel data sheets by skating category (except for the team category, team event data was entered manually since the team event has only been held three times).

The data was cleaned and organized using Python Pandas. The data was cleaned to include only Olympic medals won by USA athletes, the data was organized by medal type (gold, silver, bronze) and skating category (ladies, men, pairs, ice dance, and team). 

Stacked bar charts per Olympic games were designed to show trends of Olympic medals won by both medal type and skating category using Python Matplotlib. A web application was deployed using Streamlit to display overall results, including a summary table and bar chart by medal type and skating category, with the option to interactively display results per Olympic games as well for both medal type and skating category. The web application can be accessed [here](https://preina1-figure-skating-data-project-figskatapp-cq5q8t.streamlit.app/).

Results show an increasing trend in the number of medals won in the early history of the Winter Olympics peaking at the 1956 Olympics, followed by a decrease and subsequent slight increase before stabilizing to an approximate uniform distribution from 1984 to the present day. We can also see that bronze medals have the highest overall medal count followed by silver and gold medals. 

In addition, we can observe how the medal count by skating category has changed over the years. We can see that USA figure skating dominated in the ladies' category up until 2006, experiencing a sharp decrease after that with no Olympic medals won since. On the other hand, the performance in the men's category has been fairly consistent since 1948 with at least one medal won almost every Olympic game with a maximum of a two Olympic games gap between wins. We can also observe that the pairs category has been the weakest over the years as well as the rise of the ice dance and team categories, which were introduced in 1976 and 2014 respectively, with ice dance dominating the medal count since 2006.  

This repository includes the present README file with the project description, the data provided in Excel sheets by skating category, the Python code, and the requirements file needed to deploy the web application.
