# Amazon-Price-Tracker
A web scraper designed to track Amazon prices and send notifications when there is a price drop.

# How It Works
Let's demonstrate how this works by tracking a sample product from Amazon.

The web page of the product that we want to track is fetched from the web. 

![image](https://user-images.githubusercontent.com/61287560/190400932-3b3ece0a-0a64-498e-8a5a-cf2048d3746b.png)
 


Once the target page has been retrieved by the scraper, it begins to fetch pricing data from the web page and we can view the product's prices scraped every couple of seconds as follows:

![image](https://user-images.githubusercontent.com/61287560/190401069-193fc6ac-4ae1-49fd-b37c-83a9cf05cf35.png)

The retrieved product prices and corresponding timestamps are stored in a CSV file. Here, you can see the price difference during a time period of 1 day in the highlighted records.

![image](https://user-images.githubusercontent.com/61287560/190401786-c38424c7-4365-43d5-8365-d86c9723c6d5.png)

The data from the CSV file is plotted as a live graph.




