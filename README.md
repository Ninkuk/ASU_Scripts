# ASU Scripts
## What is this?
Random scripts that make tasks on myASU and Canvas faster. The class roster scripts uses crawlers to scrape your Canvas courses and gathers the class rosters in a JSON file.
Then it sorts the people based on the criteria that they appear in more than one of your classes. The class availability script checks if a class become available every 30 minutes (customizable in code)
## Why did I make it?
I had nothing better to do but I also didn't want to do manual work.
## How to run the class roster scripts?
- First import selenium and beautiful soup and make sure you have Firefox Geckodriver
- Run ``` class_roster_main.py ``` first to get the class roster
- Then run the ``` find_homework_friends.py ``` which will print the sorted list on your console

## How to run the class availability script?
- First import selenium and beautiful soup and make sure you have Firefox Geckodriver
- You have manually link the class search URL in code since I don't know how ASU decides the code for different semesters.
- You can customize the interval you want the code to run in (please don't run it too frequently)