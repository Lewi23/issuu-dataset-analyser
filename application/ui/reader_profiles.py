from tkinter import *
from tkinter import ttk
from tkinter.messagebox import showinfo
import logging

from ..analysis import analysis_manager as am
from . import helper_functions

class reader_profiles:
  """Class for getting the top ten document readers in the GUI
  """
  def __init__(self, tab, preprocess):
    self.reader_profiles(tab)
    self.preprocess = preprocess
    self.tab =tab
    
    
  def reader_profiles(self, tab):   
    """Builds the UI for the Task 4 tab

    :param tab: The tab we will attach the UI elements to
    :type tab: ttk tab
    """
         
    test_button = Button(tab, text='Get top 10 readers',bg='#999FA5', command= lambda: self.get_reader_profiles())
    test_button.grid(column=0, row=0, padx=30, pady=30)
    
    
  def get_reader_profiles(self):
    """Gets the top ten reader profiles
    """

    self.file_path = self.preprocess.get_file_path()
    
    if helper_functions.is_pathname_valid(self.file_path):
      try:
        manager = am.analysis_manager(self.file_path)
        manager.process_data(flag='reader_profiles')
        result = manager.reader_profiles.top_ten_readers()      
        self.display_top_ten_readers(result)    
      except:
        logging.error('Error processing reader profile data')
    else:
      showinfo("Error", "No file loaded")
      
  def display_top_ten_readers(self, result):
    """Displays the top ten reader profiles on the GUI

    :param result: the readers to be displayed
    :type result: list
    """
    #Create reader heading for table            
    self.e = Entry(self.tab, width=20, fg='blue')
    self.e.grid(column=0, row=1)
    self.e.insert(END, "Top 10 readers") 
    
    #Create readtime header for table
    self.e = Entry(self.tab, width=20, fg='blue')
    self.e.grid(column=1, row=1)
    self.e.insert(END, "Read Time (ms)") 
    
    total_rows = 10
    total_cols = 2
    
    #Create table entries with top
    for i in range(total_rows): 
          for j in range(total_cols): 
            self.e = Entry(self.tab, width=20, fg='blue')
            self.e.grid(column=j, row=i+2)
            try:  
              self.e.insert(END, result[i][j]) 
            except IndexError:
              self.e.insert(END,'') 