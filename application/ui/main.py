from application.analysis import also_likes
from application.ui.preprocess import preprocess
from tkinter import *
from tkinter import ttk

from ..analysis import analysis_manager as am
from . import views_by_country as vbc
from . import views_by_continent as _vbc
from . import views_by_browser as vbb
from . import views_by_browser_verbose as vbbv
from . import reader_profiles as rp
from . import also_likes as al
from . import also_likes_graph as alg
from . import preprocess as pp

class Main:
    """Main class responsible for the creation of the GUI
    """
    def __init__(self, cli_mode, user_uuid, doc_uuid, path):
        self.root = Tk()  
        self.root.title("Document Tracker Data Analysis")
        self.root.protocol("WM_DELETE_WINDOW", self.quit_me)
          
        ### Tab creation
        self.tabControl = ttk.Notebook(self.root)
        self.tabControl.pack(expand=1, fill="both")
        self.build_tabs()
        
        #Create preprocess
        self.preprocess = pp.preprocess(self.tab1)
        #Set the current path
        self.file_path = self.preprocess.get_file_path()
        
        # Build functionality
        self.views_by_country = vbc.views_by_country(self.tab2, self.preprocess)
        self.views_by_continent = _vbc.views_by_continent(self.tab3, self.preprocess)
        self.views_by_browser_verbose = vbbv.views_by_browser_verbose(self.tab4,self.preprocess)
        self.views_by_browser = vbb.views_by_browser(self.tab5,self.preprocess)
        self.reader_profiles = rp.reader_profiles(self.tab6, self.preprocess)
        self.also_likes = al.also_likes(self.tab7, self.preprocess)
        self.also_likes_graph = alg.also_likes_graph(self.tab8,self.preprocess, cli_mode, user_uuid, doc_uuid, path)
        
    def get_current_file_path(self):
        """Returns the file path of the users currently selected file

        :return: Current filepath
        :rtype: string
        """
        return self.preprocess.get_file_path()
    
    def update_file_path(self):
        """ Update the users current file path
        """
        self.file_path = self.preprocess.get_file_path()
        
    def build_tabs(self):
        """Builds the tabs on the GUI
        """
        self.tab1 = ttk.Frame(self.tabControl)
        self.tabControl.add(self.tab1, text='Load Files')
        
        self.tab2 = ttk.Frame(self.tabControl)
        self.tabControl.add(self.tab2, text='Task 2a')
        
        self.tab3 = ttk.Frame(self.tabControl)
        self.tabControl.add(self.tab3, text='Task 2b')
        
        self.tab4 = ttk.Frame(self.tabControl)
        self.tabControl.add(self.tab4, text='Task 3a')
        
        self.tab5 = ttk.Frame(self.tabControl)
        self.tabControl.add(self.tab5, text='Task 3b')
        
        self.tab6 = ttk.Frame(self.tabControl)
        self.tabControl.add(self.tab6, text='Task 4')
        
        self.tab7 = ttk.Frame(self.tabControl)
        self.tabControl.add(self.tab7, text='Task 5d')
        
        self.tab8 = ttk.Frame(self.tabControl)
        self.tabControl.add(self.tab8, text='Task 6')
        
    def quit_me(self):
        """ Safely quit the application
        """
        print('quit')
        self.root.quit()
        self.root.destroy() 
       
    def start(self):
        """ Starts the main loop
        """
        self.root.mainloop()
   
def start_app(cli_mode=None, user_uuid=None, doc_uuid=None, path=None):
    """ Starts the application in either GUI or CLI mode

    :param cli_mode: Running the application in GUI or CLI mode, defaults to None
    :type cli_mode: Boolean, optional
    :param user_uuid: user id used in CLI mode, defaults to None
    :type user_uuid: string, optional
    :param doc_uuid: document id used in CLI mode, defaults to None
    :type doc_uuid: string, optional
    :param path: file path used in CLI mode, defaults to None
    :type path: string, optional
    """
    myWindow = Main(cli_mode, user_uuid, doc_uuid, path)
    myWindow.start()
