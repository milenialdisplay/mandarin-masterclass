import requests
from bs4 import BeautifulSoup
import json

def scrape_hsk_grammar():
    """Scrape grammar points from Chinese Grammar Wiki"""
    
    # The grammar points are organized by HSK level[citation:7]
    grammar_by_level = {1: [], 2: [], 3: [], 4: [], 5: [], 6: []}
    
    # Base URL for Chinese Grammar Wiki
    base_url = "https://resources.allsetlearning.com/chinese/grammar/"
    
    # For each HSK level, get the grammar points
    levels = {
        1: "HSK_1",
        2: "HSK_2", 
        3: "HSK_3",
        4: "HSK_4",
        5: "HSK_5",
        6: "HSK_6"
    }
    
    for level, page in levels.items():
        url = f"{base_url}/{page}"
        print(f"Fetching grammar for HSK {level}...")
        
        try:
            response = requests.get(url)
            soup = BeautifulSoup(response.content, 'html.parser')
            
            # Find grammar points on the page
            # (This is a simplified example - actual parsing may need adjustment)
            grammar_tables = soup.find_all('table', class_='wikitable')
            
            for table in grammar_tables:
                rows = table.find_all('tr')
                for row in rows[1:]:  # Skip header row
                    cells = row.find_all('td')
                    if len(cells) >= 2:
                        grammar_point = {
                            'point': cells[0].get_text(strip=True),
                            'pattern': cells[1].get_text(strip=True) if len(cells) > 1 else '',
                            'example': cells[2].get_text(strip=True) if len(cells) > 2 else ''
                        }
                        grammar_by_level[level].append(grammar_point)
                        
        except Exception as e:
            print(f"Error scraping level {level}: {e}")
    
    # Save to JSON file
    with open('hsk_grammar.json', 'w', encoding='utf-8') as f:
        json.dump(grammar_by_level, f, ensure_ascii=False, indent=2)
    
    print(f"Done! Scraped grammar points for HSK levels 1-6")
    return grammar_by_level

if __name__ == "__main__":
    scrape_hsk_grammar()