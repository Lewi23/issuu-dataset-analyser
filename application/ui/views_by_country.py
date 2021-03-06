from tkinter import *
from tkinter import ttk
from tkinter.messagebox import showinfo
import logging

from ..analysis import analysis_manager as am
from . import helper_functions

class views_by_country:
  """Class for getting the views by country of the provided document in the GUI
  """
  def __init__(self, tab, preprocess):
    self.build_views_by_country(tab)
    self.preprocess = preprocess
    self.tab =tab
    
  def build_views_by_country(self, tab):
    """Builds the UI for the Task 2a tab

    :param tab: The tab we will attach the UI elements to
    :type tab: ttk tab
    """
    
    ttk.Label(tab,text='Document ID:').grid(column=1,row=0)
    document_id = ttk.Entry(tab, width=(45))
    document_id.grid(column=2, row=0, padx=30, pady=30)
        
    get_country = Button(tab, text='Get document reader countries',bg='#999FA5', command= lambda: self.get_country_result(helper_functions.get_generic_value(document_id)))
    get_country.grid(column=0, row=0, padx=30, pady=30)
    
  def get_country_result(self, doc_id):
    """Get the countries of the provided document id

    :param doc_id: The document ID
    :type doc_id: string
    """

    self.file_path = self.preprocess.get_file_path()
    
    if helper_functions.is_pathname_valid(self.file_path):
      try:
        print('inside_func' + self.file_path)
        manager = am.analysis_manager(self.file_path)
        manager.process_data(doc_id, flag='country')
        result = manager.views_by_location.get_country_dict()
      
        if len(result) != 0:
          helper_functions.build_bar_chart(result, self.tab, "Views by country",x_size=4,y_size=3)
        else:
          showinfo("Alert", "No matches found for provided document id")
      except:
        logging.error('Error processing country data')
    else:
      showinfo("Error", "No file loaded")
        