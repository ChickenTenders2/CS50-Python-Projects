    # IMDb Top 250 Movies Chart Web Scraper

    #### Video Demo: https://youtu.be/zQLDqMUZ6m0

    #### Description:

    My final project for CS50 is a Python-based web scraper that extracts and organizes data from IMDb’s Top 250 Movies list. This project demonstrates practical web scraping techniques, JSON parsing, and data manipulation using Python. My project includes 3 key files:

    project.py:

    This file contains the core logic for scraping the IMDb Top 250 Movies list. I used libraries like BeautifulSoup, requests, JSON, and pandas. The scraper fetches details such as movie titles, runtimes, and ratings, and stores the information in a neatly formatted CSV file for easy analysis.

    test_project.py:

    This file contains unit tests written using pytest to ensure that the core functions in project.py function correctly. This testing file helps ensure that each component of the project is functioning as expected and can be safely modified without introducing bugs.

    requirements.txt:

    This file lists the dependencies required for running the project. Running "pip install -r requirements.txt" in the console will install all necessary packages to get the project running.

    Design Choices:

    One of the key design decisions I faced was how to extract the movie data efficiently. IMDb embeds the movie data within a JSON structure inside the HTML, which simplified the process by avoiding the need to scrape individual elements from the DOM (e.g., movie titles, runtime, etc.). This approach made the scraping more resistant to potential changes in the HTML layout.

    For handling missing or incomplete data, I opted to include fallback values like "N/A" for missing fields. This prevents the program from crashing if certain fields are missing or inconsistent, ensuring a smoother user experience. For instance, the JSON structure does not store the year values for each movie, therefore I knew I couldn't extract the year data with the help of the fallback value "N/A". Although when I have more time I do wish to revist the project and eventually figure out how can I access the year value from other areas of the HTML structure.

