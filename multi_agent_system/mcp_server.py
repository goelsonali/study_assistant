from fastmcp import FastMCP
from typing import Literal, List
import re
import uvicorn

# Initialize the FastMCP server.
# Updated name and instructions to fit the "Student Content Assistant" theme.
mcp = FastMCP(
    name="Student Content Assistant Tools",
    instructions="This server provides utilities for students, including basic math, keyword extraction, and word counting for academic content processing.",
)

@mcp.tool()
def count_words(text: str) -> int:
    """
    Counts the number of words in a given academic or general text input.
    Useful for checking essay length requirements.
    
    Args:
        text: The text block (e.g., an essay paragraph or document) to count.
        
    Returns:
        The total count of words.
    """
    # Simple word count: split by whitespace and filter out empty strings
    words = text.split()
    return len(words)

@mcp.tool()
def extract_keywords(text: str, count: int = 5) -> List[str]:
    """
    Analyzes a block of text and extracts the most relevant keywords.
    (Simulated: In a real system, this would use NLP to find key terms.)
    
    Args:
        text: The text block (e.g., a chapter summary or research abstract).
        count: The maximum number of keywords to return (default is 5).
        
    Returns:
        A list of the most relevant keywords found in the text.
    """
    # Simple simulated keyword extraction:
    # 1. Remove punctuation and normalize whitespace.
    cleaned_text = re.sub(r'[^\w\s]', '', text).lower()
    
    # 2. Get all unique words that are longer than 3 characters (to filter out common small words).
    all_words = cleaned_text.split()
    unique_words = sorted(list(set(w for w in all_words if len(w) > 3)))

    # 3. Return the top 'count' words (simulating relevance).
    selected_keywords = unique_words[:count]
    
    if not selected_keywords and all_words:
        # Fallback for very short texts
        return sorted(list(set(all_words)))[:count]
        
    return selected_keywords

# --- Server Execution ---

if __name__ == "__main__":
    print("Starting FastMCP server for Student Assistant Tools...")
    
    # --- Local Development Options ---
    
    # 1. STDIO Transport (Recommended for local ADK client process)
    # The server runs, outputs the manifest, and waits for stdin input.
    #mcp.run(transport="stdio")
    
    # 2. SSE Transport (For local network testing, accessible at http://127.0.0.1:8000/mcp)
    # To use this, comment out the line above and uncomment the line below:
    #mcp_server.run(transport="sse", port=8000, host="127.0.0.1")
    uvicorn.run(app, host="localhost", port=8001)