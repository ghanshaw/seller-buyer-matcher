# seller-buyer-matcher
Algorithm to match buyers and sellers based on json data (Axial Challenge)


## How to Use
1.  Navigate to the folder containing the three program files (main.py, match.py, adjacency_list.py)

2.  Run main module and pass json file as input

    ```
    python3 main.py < sample_data.json
    ```

3.  Read results in standard output in tabular form. For best results, expand command line window to accomidate table size.

## Description

This is a simple matching algorthm that pairs buyers and
sellers based on provided json data. The assignment was implemented in Python 3 using a dictionary and an adjacency list. The program works as follows:

1. First, I read in the json file from standard input. I preprocess the file by replacing single quotes with double quotes to prepare it for Python's json decoder.

2. I then decided to keep track of each geography/industry pairing. To do this, I use a dictionary of Group objects. The Group class consists of two sets, a buyer set and a seller set. The 'groups' dictionary maps a unique
geography/industry pair (tuple) to all of the sellers and buyers that are associated with both categories.

3. Thirdly, I created a weighted, undirected graph based on the 'groups'
dictionary. I implemented this graph as an adjacency list. Each node is a seller or buyer, and edges are created if a seller and a buyer share both a geography and an industry. The weights of the edges represent the number of geographies and industries that a buyer and seller share.

4. Lastly, the Match class prints matches formatted as a table. The results are organized in alphabetical order by seller id. For each seller, the corresponding buyers are ranked according to the size of the overlap. Ties are broken based on alphabetical order. I also include the ids of the geographies and industries to improve user intelligibility.
