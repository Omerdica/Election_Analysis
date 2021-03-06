# Election_Analysis

## Project Overview
  In this challenge we are tasked with helping Seth and Tom to break down the data and complete the election audits on a recent congressional election. We will have to come up with results of the election based on the information provided to us by Tom in a CSV file. 
  
  ## Resources 
- Data Sources: election_results.csv
- software: Pythin 3.9.7, Visual studio code 1.63

## Election Results
  One of the first tasks was to come up with a full count of votes that were collected out of the counties involved. All three counties had a total of 369,711 votes.
 
  ![Code1](Resources/final_vote_count.png)


  ![Code1](Resources/Total_votes.png)

  The election consisted of three diffrent counties, as we start to look at each county we will provide the vote count also the percentage of votes.

  First county is Arapahoe with 6.7% of the votes which resulted in 24,801 actual votes.

  ![Code1](Resources/Arapahoe.png)

  Second county is Denver with 82.8% of the votes which resulted in 306,055 actual votes.

  ![Code1](Resources/Denver.png)

  Third county is Jefferson with 10.5% of the votes which resulted in 38,855 actual votes.

  ![Code1](Resources/Jefferson.png) 

  While looking at the data we can see that Denver had the largest number of votes and the highest turnout of voters

  ![Code1](Resources/code_largest_turnout.png) 

  ![Code1](Resources/Largest_Turnout.png) 
  
  Next we look at the candidates who were involved in the election, we will look at each of the candidates votes and percanetage to determine who is the winner of the election

  Charles Casper Stockham had total of 85,213 votes which resulted in 10.5% of the votes counted. 

  ![Code1](Resources/Charles.png) 

  Diana DeGette: had a total of 272,892 votes which resulted in 73.8% of the votes counted

  ![Code1](Resources/Diana.png) 

  Raymon Anthony Doane: had total of 11,606 votes which resulted in 3.1% of the votes counted. 

  ![Code1](Resources/Raymon.png) 

  ![Code1](Resources/Candidate_Code.png)

  When we look at the completed data and complete count of votes we come to a conclusion that Diana DeGette was a winner of the election. Diana had the highest number of votes out of the three candidates. 

  ![Code1](Resources/Winner_Diana.png)

  ## Summary
   We can apply this to any CSV file by changing the code around based on what the CSV file about. One of the first changes has to happen in the importing the file into the VS_Code by assigning os.path where the file is located.

  ![Code1](Resources/Code_CSV_OS.png) 

   We will have to change the names of the variables to make sure they match the new CSV file. 

  ![Code1](Resources/Code_Variables.png) 

  In this next step we focus on For/If loops, as we start creating these loops its very important to make sure when naming you variables not to choose very similar names that you already have in your code. This was a mistakes i made and had hard time figuring out error's as my variables names were one letter off. 

 ![Code1](Resources/For_If_Code_2.png) 


