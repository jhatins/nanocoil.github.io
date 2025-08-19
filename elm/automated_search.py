import pyautogui
import time
import random

# List of possible search queries
search_queries = [
    "python programming",
    "machine learning",
    "artificial intelligence",
    "datascience",
    "natural language processing",
    "computer vision",
    "algorithms",
    "datast ructures",
    "software engineering",
    "web development",
    "game development",
    "cybersecurity",
    "networking",
    "databasemanagement",
    "operating systems",
    "cloud computing",
    "internet of things",
    "big data",
    "analytics",
    "statistics",
    "mathematics",
    "physics",
    "chemistry",
    "biology",
    "medicine",
    "astronomy",
    "space exploration",
    "environmental science",
    "climate  change",
    "sustainability"
]

# Function to generate a list of 30 unique random search queries
def generate_search_queries():
    if len(search_queries) < 30:
        raise ValueError("Not enough search queries to generate 30 unique queries.")
    return random.sample(search_queries, 30)

# Function to perform a search query
def search_auto(query):
    try:
        # Wait for the page to load
        time.sleep(1)
        
        # Perform a search
        pyautogui.typewrite(query)  # Type the search query
        pyautogui.press('enter')
        
        # Wait for the search results to load
        time.sleep(6)
    except Exception as e:
        print(f"An error occurred while searching for '{query}': {e}")

# Main function to open the browser and start the search loop
def main():
    try:
        # Open the default browser (make sure Microsoft Edge is set as default)
        pyautogui.press('winleft')
        pyautogui.typewrite('microsoft edge')
        time.sleep(1)
        pyautogui.press('enter')
        
        # Wait for the browser to load
        time.sleep(5)
        
        # Generate the list of search queries
        search_list = generate_search_queries()
        print("List of search queries:")
        for i, query in enumerate(search_list, 1):
            print(f"{i}. {query}")
        
        # Start the search loop
        start_time = time.time()
        for query in search_list:
            search_auto(query)
            time.sleep(5)  # Set the time gap between searches (5 seconds)
        
        # Print the time taken to complete all searches
        end_time = time.time()
        print(f"That took {round(end_time - start_time)} seconds")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()
