from tkinter import *
from tkinter import ttk
from tkinter.messagebox import showinfo
import logging, heapq

from ..analysis import analysis_manager as am
from . import helper_functions

  #######################################
  #  For this taks I used the user_agent library and when testing with the 10k documents file it returned over
  #  100 browsers. I decided to cut this down in the GUI and only display the ten most popular browsers. 
  #  The CLI usage of this task returns all browsers 
  #######################################
class views_by_browser:
  """Class for getting the views by browser in the GUI
  """
  def __init__(self, tab, preprocess):
    self.views_by_browser(tab)
    self.preprocess = preprocess
    self.tab = tab
    
    
  def views_by_browser(self, tab):
    """Builds the UI for the Task 3b tab

    :param tab: The tab we will attach the UI elements to
    :type tab: ttk tab
    """
    get_browsers = Button(tab, text='Get browsers',bg='#999FA5', command= lambda: self.get_browser_result())
    get_browsers.grid(column=0, row=0, padx=30, pady=30)
    
  
  def build_top_browsers(self):
    """Returns the top 10 browsers for display in the GUI.

    :return: top 10 browsers
    :rtype: dictonary
    """
    browsers = heapq.nlargest(10, self.browser_dict, key=self.browser_dict.get)
    
    top_browsers = {}
    for x in range(len(browsers)):
      top_browsers[browsers[x]]= self.browser_dict[browsers[x]]
    
    return top_browsers
    
  def get_browser_result(self):
    """Get the browsers used to accsess documents in the selected file 
    """

    self.file_path = self.preprocess.get_file_path()
    
    if helper_functions.is_pathname_valid(self.file_path):
      try:
        manager = am.analysis_manager(self.file_path)
        manager.process_data(flag='browser')
        self.browser_dict = manager.views_by_browser.get_views_by_browser_dict()
        
        browsers = self.build_top_browsers()
        
        if len(browsers) != 0:
          helper_functions.build_bar_chart(browsers, self.tab, 'Browsers')
        else:
          showinfo('Alert', 'No browsers found')
      except:
        logging.error('Error processing browser data')
    else:
      showinfo('Error', 'No file loaded')