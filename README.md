# issuu-dataset-analyser

This application was built to analyse anonymised datasets from the document publishing website [issuu.com](https://issuu.com/). The dataset features information such as how long the user spent reading a document and the browser they used. Performance considerations were made when designing this application as it was required to efficiently handle files with 3-5 million entries. 



The analyser has multiple features: 

* Displays the views by country for a specific document
* Display the views by continent for a specific document
* Display the amount of views all documents received from each browser in a verbose manner ([User-Agent](https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/User-Agent))
* Display the amount of views all documents received from each browser (displaying only the browser name and version)
* Display the top ten readers of all documents based on the users time spent reading
* Provide a recommendation of documents a user might be interested in based on what other readers of the provided document have read
  * Displayed as a table
  * Displayed using a [dotgraph](https://graphviz.org/doc/info/lang.html)




## Usage 

The dataset anaylser can be used either through the command line interface or through the use of a graphical user interface. The command line interface displays the outputs of the analysis inside the console whereas the graphical user interface makes use of tables and graphs. Datasets used with the application **must** be JSON files, an example of a parital dataset can be seen [here](https://www2.macs.hw.ac.uk/~ks83/dataset_example.json).




### Command line interface 

To use the CLI the following command should be used:

```BASH
python3 analyser.py -t task_id -u user_uuid [optional] -d doc_uuid [optional] -f file_path
```

The table below shows the anaylsis tasks and associated `task_id` along with the required parameters for each task:


| **Analysis Tasks** | task_id | user_uuid | doc_uuid  | file_path|
|---|---|---|---|---|
| **Document views by country**| 1                              |❌|✅|✅|
| **Document views by continent** | 2                           |❌|✅|✅|
| **Views by browser verbose (user agent)**|   3                |❌|❌|✅|
| **Views by browser (browser name and version)**|  4           |❌|❌|✅|
| **Reader profiles (top ten readers)**|     5                  |❌|❌|✅|
| **Recommended documents (table)**|   6                        |✅|✅|✅|
| **Recommended documents (dotgraph)**  | 7                     |✅|✅|✅|

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
