**Part 1: Preparing the dataset (AKA Cleaning)**

**Step 1: Identifying needed files** 

 The downloaded zip file from gorilla has four files. The two smaller files are the practice rounds, and the two larger files are part 1 and 2 of the task. 

* You will see 4 files, 2 are short practice files and 2 larger files ![][image1]  
*  E.g practice file ![][image2]

* E.g Large file 

  ![][image3]


* Delete the 2 short practice files and download the two larger files.![][image4]

**Step 2:  Combining needed data**

In the 2 large files, there is a variable called task version 

* If variable “Task Version” \= 4, then it’s the first half of the task, where participants have to push the spacebar for the letter P![][image5]  
* If variable “Task Version” \= 3, then it’s the second half of the task, where participants have to push the spacebar for the letter R  
  ![][image6]

* Combine the two spreadsheets into one (copy and paste “Task Version”= 3 into “ Task Version” \= 4 , as they have the same exact variable titles. Name them “Subject ID” (e.g., for participant 383, name the file “383”).![][image7]

![][image8]

* Once combined and the file is labeled, you don’t need “Task Version \= 3” any more ![][image9]


**Step 3: Deleting columns** 

* Gorilla collects several variables about the task that we don’t need, including things like the type of computer used and the position of the display. We need to delete the irrelevant columns.

Delete all columns except:

- Trial Number  
- Reaction Time  
  * RT is in milliseconds, (e.g., 770.8 \= 770.8 ms or .7708 sec)  
- Response  
  * This is what the participant did (GO vs NO GO)  
- Attempt  
  * This is whether the participant pushed spacebar “1” or not (blank)  
- Correct  
  * This is whether the participant got it correct “1” or incorrect “0”  
- Display  
  * This identifies part 1 “P Trials” or part 2 “R Trials”  
- Answer  
  * This is the correct answer  
  * If Response \= Answer, then they got it correct

![][image10]

![][image11]

* Gorilla works by having each piece of the task as a “trial”, even if it’s not part of the task. We have to filter out the trials that are just for starting or ending the tasks.

**Step 4**: **Identifying discrepancies** 

Under display, delete all the rows where “display” DOESN’T  \=  “P Trials” or “R Trials”. ![][image12]

Now that you just have just “display” \=  “P Trials” or “R Trials” we can identify certain trials with discrepancies. There are gonna be some that fall out of a specific range. We can’t just delete any trials that fall out of a specific range (e.g., too slow or too fast) because if the participant doesn’t respond, or responds late, that data is still valuable and can reflect meaningful behavior (e.g., inattention, delayed reaction).

* Sometimes, you’ll see a very fast reaction time (\<120 ms) on one trial

* Since human reaction times rarely go below 150 ms, this pattern is suspicious.  
    
* If you see anything less than 120 ms, mark it as an error (“Correct” \= 0), and we will change nothing else because we will identify the type of error further in the analysis. 

Once all that is done we will focus on the things to keep in mind for when we code with the file 

- Because we have two types of trial labels (“P trials” and “R trials” ) we can’t sort or analyze by trial \# (since both have their own starting point of 1 )   
    
- We already identified which trials were error (RT’s \<120 ms) as missing responses.  
    
-  We then calculate how many trials are missing per participant, if more than 25% of all trials are missing (80 out of 320 ) then that participants data will be excluded. 

**Step 5: Exclusion criteria** 

1. Participants with 80 or more trials (25% of 320 total) where “Correct “= 0 (don’t delete just excluded)   
2. The program that we create should let us know which participants should be excluded 

Example on how we would do this :   

1. Define incorrect trials : correct \= 0   
2. Count total trials, count \# of incorrect trials   
3. calculate the proportion of incorrect trials   
4. Flag (not delete) participant if they have \>25% incorrect trials (80 out of 320\)

**Final summary of data cleaning** 

* Remove practice files; keep large task files only  
* Combine task versions into one dataset  
* Delete unnecessary columns; keep only required variables  
* Filter to keep only “P Trials” and “R Trials”  
* Mark trials as incorrect where reaction time \<120ms  
* Calculate incorrect trials per participant  
* Flag participants with \>25% incorrect trials for exclusion  
* Report excluded participants

**Part 2: Calculating Variables of Interest (AKA Analysis)**

Variables of interest:

* Bezdjian et al., 2009:   
  * (1) correct responses to the target (Go) letter (hits);  
  * (2) errors of omission (misses) to the Go letter;   
  * (3) errors of commission (false alarms) (i.e. responding incorrectly to the NoGo letter); and;   
  * (4) correct rejections to the NoGo letter.   
  * In addition, reaction time (RT) and RT variability to the Go letter was assessed and calculated for each participant.   
  * Go errors are typically considered as an indicator of inattention to the task, while NoGo errors and RT to Go responses are considered as indicators of impulsivity  
* These have to be calculated across the whole task, then for the P trials and R trials separately. 

**Step 1:** Calculate the total accuracy rate. 

- The number of correct trials (“correct” \= 1\) from the total number of trials – should be 320   
  * For coding – have the program check that it’s actually 320, tell us if it’s not.   
- New variable name: “go\_nogo\_accuracy\_t”  
  * t  \= total

**Step 2:** Calculate the number of hits.  

- Count the number of trials where “Answer”  \= Go, “Attempt” \= 1, and “Correct” \= 1  
- New variable name: “go\_nogo\_hits\_t”

**Step 3:** Calculate the omission errors. 

- Count the number of trials where “Answer”  \= Go, “Attempt” \= blank, and “Correct” \= 0  
- AKA Inattention errors  
- New variable name: “go\_nogo\_omission \_t”

**Step 4:** Calculate the commission errors. 

- Count the number of trials where “Answer”  \= No Go, “Attempt” \= 1, and “Correct” \= 0  
- AKA impulsivity errors  
- New variable name: “go\_nogo\_comission \_t”

**Step 5:** Calculate the rejections to the no go letter (e.g., true negatives)

- Count the number of trials where “Answer”  \= No Go, “Attempt” \= blank and “Correct” \= 1  
- New variable name: “go\_nogo\_trueneg\_t”

**Step 6:** Calculate the errors due to reaction time being \<120 ms

- Count the number of trials where reaction time \<120ms  
- New variable name: “go\_nogo\_120ms\_t”

**Step 7:** Repeat Steps 1-6 for parts 1 and 2 of the task separately

- Calculate for trials where the variable “Display” \= P trials  
  * New variable names: “go\_nogo\_accuracy\_p” etc.  
  * p \= P trials  
- Calculate for trials where the variable “Display” \= R trials  
  * New variable names: “go\_nogo\_accuracy\_r” etc.  
  * r \= R trials

**Step 8:** Calculate the mean, median, and standard deviation of reaction time for each participant

- Delete rows where “correct” \= 0\. Then, calculate the mean, median, and standard deviation for variable “Reaction Time”  
  * Mean “go\_nogo\_RTmean\_t”  
  * Median “go\_nogo\_RTmed\_t”  
  * Standard Deviation “go\_nogo\_RTstdev\_t”  
  * calculate across all trials, then for just P trials and just R trials (e.g., step 6\)  
    * New variable names: “go\_nogo\_RTmean\_t”, ““go\_nogo\_RTmean\_p”, “go\_nogo\_RTmean\_r”  
  * For coding – step 7 must be done last

**Part 3: Consolidating the data (AKA Uploading)**

From Part 2, we should have the following variables calculated, and they should be arranged in this order:

- go\_nogo\_accuracy\_t  
- go\_nogo\_hits\_t  
- go\_nogo\_omission \_t  
- go\_nogo\_comission \_t  
- go\_nogo\_trueneg\_t  
- go\_nogo\_120ms\_t  
- go\_nogo\_RTmean\_t  
- go\_nogo\_RTmed\_t  
- go\_nogo\_RTstdev\_t  
- go\_nogo\_accuracy\_p  
- go\_nogo\_hits\_p  
- go\_nogo\_omission \_p  
- go\_nogo\_comission \_p  
- go\_nogo\_trueneg\_p  
- go\_nogo\_120ms\_p  
- go\_nogo\_RTmean\_p  
- go\_nogo\_RTmed\_p  
- go\_nogo\_RTstdev\_p  
- go\_nogo\_accuracy\_r  
- go\_nogo\_hits\_r  
- go\_nogo\_omission \_r  
- go\_nogo\_comission \_r  
- go\_nogo\_trueneg\_r  
- go\_nogo\_120ms\_r  
- go\_nogo\_RTmean\_r  
- go\_nogo\_RTmed\_r  
- go\_nogo\_RTstdev\_r

We want to ultimately consolidate the data from each individual spreadsheet into one spreadsheet. 

**Step 1:** Add one final variable “study\_id” that uses the filename from the individual spreadsheets (e.g., 383\) to label each set of variables that we calculated.

Now, the output should be one spreadsheet with all ANT variables, labelled by study\_id, that can be uploaded to REDCap. 
