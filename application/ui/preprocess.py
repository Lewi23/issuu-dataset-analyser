from tkinter import *
from tkinter import ttk
from tkinter.filedialog import askopenfilename
from tkinter.messagebox import showinfo
import logging

from . import helper_functions

class preprocess:
  """Class for managing the files the user works with in the GUI
  """
  def __init__(self, tab):
    self.tab = tab
    self.file_path = ''
    self.file_name = ''
    self.build_preprocess(tab)
    
  def build_preprocess(self, tab):
    """ Builds the UI for the load files tab
    :param tab: The tab we will attach the UI elements to
    :type tab: ttk tab
    """
    ttk.Label(self.tab,text='Please select a file to work on:').grid(column=0,row=0,padx=30,pady=30)
       
    add_file_button = Button(self.tab, text='Load file',bg='#999FA5', command= self.get_file)
    add_file_button.grid(column=1, row=0, padx=30, pady=30)
    
  def get_file(self):
    """Gets the path of the file the user would like to work with

    :return: the file path of the selected file
    :rtype: string
    """
    try:
      self.file_path = askopenfilename()
      
      if helper_functions.is_pathname_valid(self.file_path):
        self.file_name = self.file_path.rsplit('/', 1)[-1]
        self.create_loaded_files()
        showinfo("Success", 'File ' + self.file_name + ' loaded')
      else:
        showinfo("Warning", "No file loaded")
    except:
      logging.error('Error processing file')
    
    return self.file_path
  
  def create_loaded_files(self):   
    """ Creates the label on the UI once the file has been loaded showing the current file
    """
    ttk.Label(self.tab,text='File loaded: ' + self.file_name).grid(column=0,row=1,padx=30,pady=30)
      
  def get_file_path(self):
    """returns the current file path

    :return: The current file path
    :rtype: string
    """
    return self.file_path
   
  
    
    