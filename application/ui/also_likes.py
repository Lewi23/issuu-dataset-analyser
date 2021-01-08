from tkinter import *
from tkinter import ttk
from tkinter.messagebox import showinfo
import logging, heapq

from ..analysis import analysis_manager as am
from . import helper_functions

class also_likes:
  """Class for getting the views by country of the provided document in the GUI
  """
  def __init__(self, tab, preprocess):
    self.also_likes(tab)
    self.preprocess = preprocess
    self.tab = tab
    
  def also_likes(self, tab):
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

    also_likes_btn = Button(tab, text='Get top ten also liked documents',bg='#999FA5', 
      command= lambda: self.get_also_likes(helper_functions.get_generic_value(document_id), 
                                           helper_functions.get_generic_value(user_id)))
    also_likes_btn.grid(column=0, row=3, padx=30, pady=30)
    
          
  def get_also_likes(self, doc_id,user_id):
    """Gets the top ten also liked documents

    :param doc_id: The document id to use to check for top ten also liked documents
    :type doc_id: string
    :param user_id: The user id to cehck for top ten also liked documents
    :type user_id: string
    """
  
    # get current file path
    self.file_path = self.preprocess.get_file_path()
    
    if helper_functions.is_pathname_valid(self.file_path):
      try:
        manager = am.analysis_manager(self.file_path)
        manager.process_data(doc_id ,flag='also_likes',vistor_uuid=user_id)
        self.readers_dict = manager.also_likes.get_document_readers_dict()
        self.also_likes_dict = manager.also_likes.get_read_by_vistor_dict(manager.also_likes.top_ten)
        
        list_of_docs = manager.also_likes.top_ten()
        self.display_top_ten_also_likes(list_of_docs)
      
      except:
        logging.error('Error processing browser data')
    else:
      showinfo('Error', 'No file loaded')
      
  def display_top_ten_also_likes(self,list_of_docs):
    """Displays the top ten also liked documents on the GUI

    :param list_of_docs: also liked documents
    :type list_of_docs: list
    """
    #Create readtime header for table
    self.e = Entry(self.tab, width=45, fg='blue')
    self.e.grid(column=1, row=4)
    self.e.insert(END, "Top ten also liked documents") 
      
    total_rows = 10
    total_cols = 1
    
    #Create table entries with top
    for i in range(total_rows): 
          for j in range(total_cols): 
                
              self.e = Entry(self.tab, width=45, fg='blue')
              self.e.grid(column=j+1, row=i+5)
              try:  
                self.e.insert(END, list_of_docs[i]) 
              except IndexError:
                self.e.insert(END,'') 
        