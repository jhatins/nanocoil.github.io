import pyautogui
import time
import random

# List of possible search queries
search_queries = [
    "biology", "chemistry", "physics", "astronomy", "geology", "zoology", "botany", "ecology",
    "genetics", "microbiology", "immunology", "anatomy", "physiology", "neuroscience", "biochemistry",
    "biotechnology", "paleontology", "anthropology", "sociology", "psychology", "linguistics",
    "archaeology", "economics", "economy", "politics", "philosophy", "ethics", "logic", "literature",
    "history", "theology", "law", "criminology", "education", "geography", "metallurgy", "mineralogy",
    "oceanography", "climatology", "meteorology", "astrophysics", "cosmology", "seismology",
    "hydrology", "toxicology", "epidemiology", "oncology", "cardiology", "dermatology", "endocrinology",
    "gastroenterology", "hematology", "nephrology", "ophthalmology", "orthopedics", "psychiatry",
    "radiology", "urology", "virology", "entomology", "ornithology", "mycology", "taxonomy", "statistics",
    "calculus", "algebra", "geometry", "trigonometry", "mathematics", "arithmetic", "informatics",
    "cybernetics", "robotics", "engineering", "nanotechnology", "mechanics", "electronics",
    "computer science", "data science", "artificial intelligence", "machine learning", "cryptography",
    "networking", "quantum physics", "nuclear physics", "thermodynamics", "optics", "aerodynamics",
    "biophysics", "materials science", "social science"
]

def generate_search_queries():
    """Generates a list of 20 unique random search queries."""
    search_list = []
    temp_search_queries = search_queries.copy()
    for _ in range(20):
        if not temp_search_queries:
            break
        query = random.choice(temp_search_queries)
        search_list.append(query)
        temp_search_queries.remove(query)
    return search_list

def search_in_new_tab(query):
    """
    Opens a new tab, types the query, and presses enter.
    """
    # Open a new tab (Ctrl+T)
    pyautogui.hotkey('ctrl', 't')
    time.sleep(2) # Give browser time to open new tab

    # Type the search query
    pyautogui.typewrite(query)
    time.sleep(1)

    # Press enter to search
    pyautogui.press('enter')
    time.sleep(4) # Wait for search results to load

def close_current_tab():
    """Closes the current browser tab (Ctrl+W)."""
    pyautogui.hotkey('ctrl', 'w')
    time.sleep(1) # Give browser time to close tab

def main():
    # Open the default browser (make sure Microsoft Edge is set as default)
    print("Opening Microsoft Edge...")
    pyautogui.press('winleft')
    pyautogui.typewrite('microsoft edge')
    time.sleep(1)
    pyautogui.press('enter')
    time.sleep(5) # Wait for the browser to load

    # Generate the list of random search queries
    random_search_list = generate_search_queries()
    print(f"Generated {len(random_search_list)} search queries.")

    # Start the search loop
    st = time.time()
    for i, query in enumerate(random_search_list):
        print(f"Searching for: '{query}' ({i+1}/{len(random_search_list)})")
        search_in_new_tab(query)
        # Optional: Close the tab after each search to keep the browser clean
        # close_current_tab()
        time.sleep(2) # Small delay before the next search

    # Print the time taken to complete all searches
    ed = time.time()
    print(f"All searches completed. That took {round(ed-st)} seconds.")

    # Optional: Close the browser window at the end
    # pyautogui.hotkey('alt', 'f4')

if __name__ == "__main__":
    main()
