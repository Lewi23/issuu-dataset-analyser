# issuu-dataset-analyser


The analyser has multiple features: 

* Displays the views by country for a specific document
* Display the views by continent for a specific document
* Display the amount of views for each individual browser for the complete data set in a verbose manner (The full useragent string)
* Display the amount of views for each individual browser for the complete data set (displaying only the browser name and version)
* Determine the top ren readers for the complete data set based on time spent reading 
* Provide a recommendation of documents a user might also like


## Usage 

The dataset anaylser can be used either through the command line interface or through the use of a graphical user interface. The command line interface displays the outputs of the anlysis inside the console whereas the GUI makes use of tables and graphs.

### Command line interface 

To use the CLI the following command should be used:

```BASH
python3 analyser -t task -u user_uuid -d doc_uuid -f file_path
```

The table below shows the paramters required for each task:


task_id | user_uuid | doc_uuid  | file_path
--- | --- | --- | --- | ---
views_by_country                      |❌     | ✅ | ✅ |  
views_by_continent                    |❌     | ✅ | ✅ |  
views_by_browser_verbose (verbose)            |❌    | ❌    | ✅|  
views_by_browser (browser name and version)  | ❌    |❌     | ✅ |  
reader_profiles (top ten readers)     |❌   | ❌ | ✅|
also_likes (suggested documents)      | ✅   | ✅  | ✅ |  

<br />

### Graphical user interface

To run the program using the graphical user interface the following command should be ran:

```BASH
python3 analyser
```

## Installation

Use the package manager [pip](https://pip.pypa.io/en/stable/) to install this project (a [virtual enviroment](https://docs.python.org/3/tutorial/venv.html) is required):

```python3
pip install -r requirements.txt
```