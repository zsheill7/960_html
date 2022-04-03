### 9.60 HTML

For the purpose of creating HTML templates for creating surveys in Mechnical Turk

Current specifications:

** Side note: some hand drawn or digitally drawn pictures of the survey could help

Survey qualifications:
* A human with an MTurk account
* Answers a statistically significant number of questions in Preliminary Art Knowledge survey wrong

Preliminary Art Knowledge survey specifications:
* "Out of these art period options, which art period is
the painting to the right of?"
* 11 options to represent all categories
* 15 questions
* 1 picture per question, random category
* If the user gets too many questions right, stop the survey and do not continue to Main Human Art Survey
* Question: could we just preset like 3 of these surveys to try to control some variability?

Main Human Art Survey specifications:
* 15 questions
* 1 picture per question, random category
* 11 options per question to represent all categories

Total things that require logic (Javascript) in addition to plain HTML
* Shutting down the survey after the Preliminary Art Knowledge if they answer too many questions right
    Potential solution: Use built-in Qualifications functionality (screening)
* Form submission


Potentially useful things from the 960_tutoral_mturk slides:

```
Use the MTurk sandbox for development
MTurk sandbox is functionally identical to MTurk but no money changes hands!
https://requestersandbox.mturk.com/ (Develop experiments here)
https://workersandbox.mturk.com/ (Test your own experiments here)

Once everything looks OK on sandbox mode, copy all HTML code + parameters and post experiment on MTurk to get paid workers
https://requester.mturk.com/ (Post live experiments here)
WARNING: carefully check all payment screens before posting here – money will change hands and it’s easy to get the math wrong

```

```
MTurk experiment tips
Modify premade templates!
If you are not comfortable in Javascript / HTML, limit the amount of logic that happens in the experiment script! (Most of the work can be done when generating stimuli / CSV variable files)
```

```
Additional resources
MTurk tutorial focused on more custom scripts: https://bradylab.ucsd.edu/ttt/ 

Linking a Google form to MTurk: https://blog.mturk.com/tutorial-getting-great-survey-results-from-mturk-and-google-forms-da4993d878df 
```