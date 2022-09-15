# Amazon-Price-Tracker
This is a web scraper designed to track Amazon prices and send notifications when a price drop is detected.

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




