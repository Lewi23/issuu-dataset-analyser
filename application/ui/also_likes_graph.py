from tkinter import *
from tkinter import ttk
from tkinter.messagebox import showinfo
import logging, heapq, os
from graphviz import Digraph
from PIL import ImageTk, Image

from ..analysis import analysis_manager as am
from . import helper_functions


class also_likes_graph:
  """Class for building the dot graph in the GUI
  """
  def __init__(self, tab, preprocess, cli_mode, user_uuid, doc_uuid, path):
    self.also_likes_graph(tab)
    self.preprocess = preprocess
    self.tab = tab
    self.cli_mode = cli_mode
    
    if self.cli_mode:
      self.get_also_likes_graph(doc_uuid, user_uuid, path)
    

  def also_likes_graph(self, tab):
    """Builds the UI for the Task 6 tab

    :param tab: The tab we will attach the UI elements to
    :type tab: ttk tab
    """
    
    ttk.Label(tab,text='Document ID:').grid(column=0,row=0)
    document_id = ttk.Entry(tab, width=(45))
    document_id.grid(column=1, row=0)
 
    ttk.Label(tab,text='User ID:').grid(column=0,row=1)
    user_id = ttk.Entry(tab, width=(45))
    user_id.grid(column=1, row=1)
    
    also_likes_btn = Button(tab, text='Show dot graph',bg='#999FA5', command=
                            lambda: self.get_also_likes_graph(helper_functions.get_generic_value(document_id),
                                                              helper_functions.get_generic_value(user_id)))
    also_likes_btn.grid(column=0, row=2, padx=30, pady=30)
    
    
  def get_also_likes_graph(self, doc_id , user_id, path=None):
    """ Get the also likes data for the provided document ID and user ID

    :param doc_id: document ID used to find other documents
    :type doc_id: string
    :param user_id: user ID to filter out this user
    :type user_id: string
    :param path: file path needed for CLI usage, defaults to None
    :type path: string, optional
    """
    
    # Set the correct path (whether CLI or GUI usuage)
    if self.cli_mode == False:
      self.file_path = self.preprocess.get_file_path()
    else:
      self.file_path = path
    
    if helper_functions.is_pathname_valid(self.file_path):
      try:
        manager = am.analysis_manager(self.file_path)
        manager.process_data(doc_id ,flag='also_likes',vistor_uuid=user_id)
        self.readers_dict = manager.also_likes.get_document_readers_dict()
        self.also_likes_dict = manager.also_likes.get_read_by_vistor_dict(manager.also_likes.top_ten)

        # Generate lists of readers and documents from edges to build dot charts
        documents = [x[1] for x in manager.also_likes.list_of_edges]
        readers = [x[0] for x in  manager.also_likes.list_of_edges]
        self.build_dot_graph(readers, documents,  reader_id=user_id, document_ID=doc_id)
      
      except:
        logging.error('Error creating dot graph')
    else:
      showinfo('Error', 'No file loaded')
      
    # Set CLI mode to false once GUI launches so the user can use the GUI
    self.cli_mode = False
    
      
      
  def build_dot_graph(self, readers, documents, reader_id=None, document_ID=1):
    """Build the dot graph and add it to the tab

    :param readers: List of readers
    :type readers: list
    :param documents: List of documents
    :type documents: list
    :param reader_id: Reader ID of provided document , defaults to None
    :type reader_id: string, optional
    :param document_ID: The document used to filter for other liked documents, defaults to 1
    :type document_ID: int, optional
    """
    
    document_ID = document_ID[-4:]
    reader_id = reader_id[-4:]
    
    graph = Digraph(name="Also likes", format='png')
    graph.attr('graph', ranksep='0.75')
    sub_graph = Digraph()
    
    graph.attr('node',shape='plaintext',fontsize='16', bgcolor='grey')
    graph.edge('Readers', 'Documents')
    
    #The document searched for
    graph.node(document_ID, shape="circle",style="filled",color=".3 .9 .7")
    
    #If the a reader ID has been passed in
    if reader_id != '':
      sub_graph.node(reader_id, shape="box", style="filled",color=".3 .9 .7")
      graph.edge(reader_id, document_ID)
    
    # Create reader squares
    for n in readers:
      sub_graph.node(str(n), shape="box")

    # Create document ciricles
    for n in documents:
      graph.node(str(n), shape="circle")
      
    # Build edges
    for reader, document in zip(readers, documents):
      graph.edge(reader,document)
    
    # Set the path and save the image
    path = os.getcwd()
    path = path + '/application/ui/dot_graph_output/graph.png'
    graph.subgraph(sub_graph)  
    
    # Render the image and add to tab
    graph.render('application/ui/dot_graph_output/graph')  
    image = Image.open(path).convert("RGB")
    image = image.resize((800, 250))
    display = ImageTk.PhotoImage(image)
    
    self.image = display
    ttk.Label(self.tab,image=self.image).grid(column=0,row=4,padx=30,pady=30)
    
   


