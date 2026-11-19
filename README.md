## Week 1 - Performance Assessment 1.8

**File:** Week1-PA2.py

**Description:**
This Python application connects to a Redis key-value database
and allows users to perform CRUD operations through an interactive
menu. Users can create sets, retrieve set members, update members,
delete individual sets, and clear the database.

**Technologies Used:**
- Python 3
- Redis
- Redis-py library
- Ubuntu Linux


## Week 2 - MongoDB Document Database

### AmazonReviewManager.py

This Python application uses PyMongo to perform CRUD operations on the Amazon MongoDB database and ReviewData collection. It includes an interactive menu that allows users to add reviews, retrieve documents, search by star ratings or keywords, update review fields, delete individual documents, delete all documents, and remove the collection.

**Assignment:** 2.5 Performance Assessment - Python Application Accessing a Document Database



## Week 2 – MongoDB Repository Analysis

### New Feature
- `mongo_repository_analysis.py` imports GitHub Archive repository records into MongoDB and displays the top 10 repositories ranked by watch count.
- Successfully tested with 400,000 repository records.
- Converts `watch_count` values from strings to integers for accurate sorting.

### Dependencies
- Python 3
- MongoDB Community Server
- PyMongo (`pip install pymongo`)

### Technology Requirements
- Windows 11 or compatible operating system
- Local MongoDB server running on port 27017
- GitHubArchive-Dataset, including `Sample_Repos.json`

### How to Run
1. Install Python 3, MongoDB, and PyMongo.
2. Extract the GitHub Archive dataset.
3. Update the `file_path` variable in `mongo_repository_analysis.py` to match the location of `Sample_Repos.json`.
4. Start MongoDB.
5. Run `python mongo_repository_analysis.py`.

### Current Status
The repository watch count analysis has been tested successfully. Group integration and additional CRUD and analysis features are pending.
