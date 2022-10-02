# Amazon-Price-Tracker
This is a web scraper designed to track Amazon product prices and send notifications when price drops are detected.

# How It Works
Let's demonstrate how this works by tracking a sample product from Amazon.

The URL of the web page of the product that we want to track is given as input to the scraper. 

![image](https://user-images.githubusercontent.com/61287560/190400932-3b3ece0a-0a64-498e-8a5a-cf2048d3746b.png)
 
Once the target page has been retrieved by the scraper, it begins to fetch pricing data from the web page every couple of seconds as follows:

![image](https://user-images.githubusercontent.com/61287560/190401069-193fc6ac-4ae1-49fd-b37c-83a9cf05cf35.png)

The retrieved product prices and corresponding timestamps are stored in a CSV file. Here, you can see the price difference during a time period of 1 day in the highlighted records.

![image](https://user-images.githubusercontent.com/61287560/190401786-c38424c7-4365-43d5-8365-d86c9723c6d5.png)

The data from the CSV file is plotted as a live graph. This helps in visualizing the pricing variations over a period of time.

![Screenshot (486)](https://user-images.githubusercontent.com/61287560/190405066-74784c4f-da32-475d-89f5-89235b47ae07.png)

It is also possible to track multiple products prices simultaneously using the scraper.

![Screenshot (487)](https://user-images.githubusercontent.com/61287560/190409463-1b96392b-c29e-494c-ac41-35a9508af5f6.png)

When a price drop is detected, we are notified of it via email.

![Screenshot (489)](https://user-images.githubusercontent.com/61287560/190417012-9cc78013-f069-4917-94c6-1030a1ba0362.png)

# Prerequisites

Ensure that you have Python and the following libraries installed:

* requests
* dataclasses
* numpy
* time
* matplotlib
* BeautifulSoup
* pandas
* datetime
* smtplib
* csv
* re
* DictWriter
* random
* count
* threading
* os

To install a library, open Powershell and enter
> pip install < name of the library >

You can use the following command as well, if you are starting fresh.
> pip install -r requirements.txt

# Running The Code

* Download the files named Web Scraper.py and Live Graph.py 
* Place them in a separate folder.
* Create an empty subfolder named 'data' and place it in this folder. Here's where the CSV files will be generated.
* Run the file named Web Scraper.py and then simultaneously run Live Graph.py
* You'll now see the live graph being generated from the CSV file data which was scraped from the web.
* You can track any Amazon product's prices by replacing the links in the code with your own.

# Future Enhancement

* The code can be further expanded to track any number of products.
* A cloud service can be used to run the script 24/7 for more accurate results.



