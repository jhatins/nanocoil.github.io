'''import pyautogui
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
'''
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
    "biophysics", "materials science", "social science"]


'''search_queries = ['Can you use the ozone layer?',
 'Do people learn about blockchain explained?',
 'Do people learn about how internet works?',
 'Do people learn about volcanoes erupting?',
 'Do people learn about what are black holes?',
 'Do people understand photosynthesis?',
 'Do people understand the ozone layer?',
 'Do people understand what is ethical hacking?',
 'Do people use electric circuits?',
 'Do people use how to meditate?',
 'Do people use the history of computers?',
 'How are benefits of reading books?',
 'How are best study methods?',
 'How are brain-computer interface?',
 'How are internet safety tips?',
 'How do how gravity works?',
 'How do top programming languages?',
 'How does recycling process?',
 'How is JEE preparation?',
 'How is electric circuits?',
 'How is online learning platforms?',
 'Is it possible to learn about how GPS works?',
 'Is it possible to learn about renewable energy sources?',
 'Is it possible to learn about why people procrastinate?',
 'Is it possible to understand 5G technology?',
 'Is it possible to understand electric vehicles?',
 'Is it possible to use IPv6 vs IPv4?',
 'Is it possible to use best study methods?',
 'Is it possible to use brain-computer interface?',
 'Is it possible to use cloud computing basics?',
 'Is it possible to use difference between RAM and ROM?',
 'Is it possible to use how to stay motivated?',
 'Is it possible to use photosynthesis?',
 'Should I learn about best study methods?',
 'Should I learn about greenhouse effect?',
 'Should I learn about types of renewable energy?',
 'Should I understand how to meditate?',
 'Should I understand importance of biodiversity?',
 'Should I understand solar system facts?',
 'Should I understand space travel?',
 'Should I use types of renewable energy?',
 'What are IPv6 vs IPv4?',
 'What are climate change impacts in India?',
 'What can recycling process?',
 'What do coding in Python?',
 'What does cloud computing basics?',
 'When are renewable energy sources?',
 'When can artificial organs?',
 'When can history of the Taj Mahal?',
 'When can machine learning applications?',
 'When can recycling process?',
 'When do NCERT solutions?',
 'When do photosynthesis?',
 'When do recycling process?',
 'When do the stock market?',
 'When do why data privacy matters?',
 'When does how does photosynthesis work?',
 'When is most spoken languages in the world?',
 'When is what are black holes?',
 'Where are online learning platforms?',
 'Where are top programming languages?',
 'Where can climate change impacts in India?',
 'Where do JEE preparation?',
 'Where do how climate change occurs?',
 'Where does most spoken languages in the world?',
 'Where does the history of computers?',
 'Where does the metaverse?',
 'Where is coding in Python?',
 'Where is volcanoes erupting?',
 'Why are cloud computing basics?',
 'Why can healthy eating?',
 'Why can recycling process?',
 'Why can the history of computers?',
 'Why do how climate change occurs?',
 'Why do importance of mental health?',
 'Why does the benefits of yoga?',
 'Why does the ozone layer?',
 'Why is AI in education?',
 'Why is best laptops under 60000?',
 'Why is sustainable development?','Can you is it important to know the stock market?',
 'Can you should I learn about what are black holes?',
 'Do people can we understand how internet works?',
 'Do people could I use 5G technology?',
 'Do people could I use importance of digital privacy?',
 'Do people could I use time management for students?',
 'Do people should I learn about cybersecurity threats?',
 'Do people should I learn about quantum physics?',
 'How are online learning platforms?',
 'How can we understand solar system facts?',
 'How could I use blockchain explained?',
 'How could I use the speed of light?',
 'How does brain anatomy?',
 'How does genetically modified foods?',
 'How does importance of digital privacy?',
 'How is best study methods?',
 'Is it possible to can volcanoes erupting?',
 'Is it possible to can why data privacy matters?',
 'Is it possible to could I use career options after 12th?',
 'Is it possible to does cyberbullying awareness?',
 'Is it possible to does why dreams happen?',
 'Should I are cybersecurity threats?',
 'Should I are why dreams happen?',
 'Should I can we understand coding in Python?',
 'Should I could I use blockchain explained?',
 'Should I do AI in education?',
 'Should I do robotics in daily life?',
 'Should I is it important to know healthy eating?',
 'Should I should I learn about quantum physics?',
 'Should I should I learn about the stock market?',
 'What are JEE preparation?',
 'What are cybersecurity threats?',
 'What are time management for students?',
 'What can difference between RAM and ROM?',
 'What can we understand brain-computer interface?',
 'What can we understand online learning platforms?',
 'What could I use smartphones vs feature phones?',
 'What do importance of biodiversity?',
 'What do the speed of light?',
 'What does difference between virus and bacteria?',
 'What does why people procrastinate?',
 'What should I learn about how does photosynthesis work?',
 'What should I learn about how gravity works?',
 'What should I learn about quantum physics?',
 'What should I learn about space travel?',
 'When are online learning platforms?',
 'When can electric vehicles?',
 'When can importance of digital privacy?',
 'When can we understand JEE preparation?',
 'When can we understand nuclear fusion?',
 'When can why data privacy matters?',
 'When could I use data science careers?',
 'When could I use photosynthesis?',
 'When do why sleep is important?',
 'When does how to stay motivated?',
 'When is it important to know history of the Taj Mahal?',
 'Where are 5G technology?',
 'Where are difference between RAM and ROM?',
 'Where are the history of computers?',
 'Where can we understand coding in Python?',
 'Where do sustainable development?',
 'Where do what is ethical hacking?',
 'Where does how internet works?',
 'Where does time travel?',
 'Where is importance of teamwork?',
 'Where is it important to know Newton’s laws of motion?',
 'Where is it important to know most spoken languages in the world?',
 'Where should I learn about electric circuits?',
 'Why are most spoken languages in the world?',
 'Why can genetically modified foods?',
 'Why can sustainable development?',
 'Why can we understand how GPS works?',
 'Why could I use best study methods?',
 'Why do NCERT solutions?',
 'Why does how GPS works?',
 'Why is benefits of reading books?',
 'Why is career options after 12th?',
 'Why is it important to know genetically modified foods?',
 'Why is it important to know why sleep is important?',
 'Why should I learn about artificial organs?']'''



# Function to generate a list of 30 unique random search queries
def generate_search_queries():
    search_list = []
    temp_search_queries = search_queries.copy()  # Create a temporary copy of the list
    for _ in range(20):
        if len(temp_search_queries) == 0:  # If the list is empty, break the loop
            break
        query = random.choice(temp_search_queries)  # Select a random element from the list
        search_list.append(query)  # Add the element to the search list
        temp_search_queries.remove(query)  # Remove the element from the temporary list
    return search_list

def searchAuto(query):
    # Wait for the page to load
    time.sleep(3)
    pyautogui.typewrite("/")
    
    # Perform a search
    pyautogui.typewrite(query)  # Type the search query
   
    pyautogui.press('enter')

    # Wait for the search results to load
    time.sleep(4)

# Open the default browser (make sure Microsoft Edge is set as default)
pyautogui.press('winleft')
pyautogui.typewrite('microsoft edge')
time.sleep(1)
pyautogui.press('enter')

# Wait for the browser to load
time.sleep(5)

# Generate the list of random search queries
random_search_list = generate_search_queries()

# Start the search loop
st = time.time()
for query in random_search_list:  # Iterate through the randomly generated list
    searchAuto(query)
    time.sleep(4)  # Set the time gap between searches (5 seconds)

# Print the time taken to complete all searches
ed = time.time()
print(f"That took {round(ed-st)} seconds")

