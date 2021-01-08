# issuu-dataset-analyser




The analyser has multiple features: 

* Displays the views by country for a specific document
* Display the views by continent for a specific document
* Display the amount of views for each individual browser for the complete data set in a verbose manner (The user agent )
* Display the amount of views for each individual browser for the complete data set (displaying only the browser name and version)
* Determine the top ten readers for the complete data set based on time spent reading 
* Provide a recommendation of documents a user might be intrested in based on what other readers of the provided document have read
  * Displayed as a table
  * Displayed using a [dotgraph](https://graphviz.org/doc/info/lang.html)


An example of the JSON data set can be seen [here](https://www2.macs.hw.ac.uk/~ks83/dataset_example.json).


## Usage 

The dataset anaylser can be used either through the command line interface or through the use of a graphical user interface. The command line interface displays the outputs of the anlysis inside the console whereas the GUI makes use of tables and graphs.

### Command line interface 

To use the CLI the following command should be used:

```BASH
python3 analyser.py -t task_id -u user_uuid -d doc_uuid -f file_path
```

The table below shows the anaylsis tasks and associated `task_id` along with the required paramters  for each task:


| **Analysis Tasks** | task_id | user_uuid | doc_uuid  | file_path|
|---|---|---|---|---|
| **Document views by country**| 1                              |❌|✅|✅|
| **Document views by continent** | 2                           |❌|✅|✅|
| **Views by browser verbose (user agent)**|   3                |❌|❌|✅|
| **Views by browser (browser name and version)**|  4           |❌|❌|✅|
| **Reader profiles (top ten readers)**|     5                  |❌|❌|✅|
| **Recommended documents (table)**|   6               |✅|✅|✅|
| **Recommended documents (dotgraph)**  | 7           |✅|✅|✅|

<br />

### Graphical user interface

To run the program using the graphical user interface the following command should be run:

```BASH
python3 analyser.py
```

## Installation

Use the package manager [pip](https://pip.pypa.io/en/stable/) to install this project (a [virtual enviroment](https://docs.python.org/3/tutorial/venv.html) is required):

```python3
pip install -r requirements.txt
```
