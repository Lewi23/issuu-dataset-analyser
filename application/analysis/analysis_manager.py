from alive_progress import alive_bar

from . import views_by_location as vbl
from . import views_by_browser as vbb
from . import reader_profiles as rp
from . import also_likes as al

import fileinput
import json

class analysis_manager:
  """ Controls the tasks that are run for the CLI and GUI 
  """
  def __init__(self, file_path):
    self.views_by_location = vbl.views_by_location()
    self.views_by_browser = vbb.views_by_browser()
    self.reader_profiles = rp.reader_profiles()
    self.also_likes = al.also_likes()
    self.file_path = file_path
    
  
  def process_data(self, document_id=1, flag=None, vistor_uuid=None):
    """ Runs the individual tasks

    :param document_id: document ID for function, defaults to 1
    :type document_id: int, optional
    :param flag: the function to run, defaults to None
    :type flag: string, optional
    :param vistor_uuid: vistor ID for function, defaults to None
    :type vistor_uuid: string, optional
    """
    
    if flag == 'country' or flag == 'continent':
      self.run_process(self.views_by_location.process_json_line, document_id)
    elif flag == 'browser_verbose'or flag == 'browser':
      self.run_process(self.views_by_browser.process_json_line)
    elif flag == 'reader_profiles':
      self.run_process(self.reader_profiles.process_json_line)
    elif flag == 'also_likes':
      self.run_process(self.also_likes.build_document_readers, document_id)
      self.run_process(self.also_likes.build_read_by_visitor, vistor_uuid)
    
  def run_process(self, function, arg1=None, arg2=None):
    """Run a generic function with arguments

    :param function: function to run
    :type function: function
    :param arg1: argument 1 for the function, defaults to None
    :type arg1: arg, optional
    :param arg2: argument 2 for the function, defaults to None
    :type arg2: arg, optional
    """
    
    num_lines = sum(1 for line in open(self.file_path))
    
    with alive_bar(num_lines, title='Processing data file...') as bar:
      finput = fileinput.input(self.file_path)
      for line in finput:
        try:
          json_line = json.loads(line)
          if arg1 is not None:
            function(json_line, arg1)
          elif arg1 is not None and arg2 is not None:
            function(json_line, arg1, arg2)
          else:
            function(json_line)
          bar()
        except:
          pass
      finput.close()