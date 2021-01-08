from user_agents import parse
from alive_progress import alive_bar

class views_by_browser:
  """ Implements the logic to determine which browser have been used
  """
  def __init__(self):
    self.views_by_browser_verbose = {}
    self.views_by_browser = {}
    
  def process_json_line(self, line):  
    """Processes a single line of the JSON file, adding the result to both browser dictionaries

    :param line: JSON line to processes
    :type line: JSON
    """
    ua = parse(line['visitor_useragent'])
    
    try:
      self.views_by_browser_verbose[ua.browser] += 1
      self.views_by_browser[ua.browser.family] += 1
    except KeyError:
      self.views_by_browser_verbose[ua.browser] = 1
      self.views_by_browser[ua.browser.family] = 1
  
  def get_view_by_browser_verbose_dict(self):
    """Returns the views by browser verbose dictionary

    :return: Views by brwoser verbose dictionary
    :rtype: dictionary
    """
    return self.views_by_browser_verbose
  
  def get_views_by_browser_dict(self):
    """Returns the views by browser dictionary

    :return: Views by brwoser dictionary
    :rtype: dictionary
    """
    return self.views_by_browser