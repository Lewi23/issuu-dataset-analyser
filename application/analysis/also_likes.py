from graphviz import Digraph
import heapq

class also_likes():
  """Implements the also likes functionaility to create the data for top ten releated documents and 
     also for the dot graph
  """
  def __init__(self):
    self.list_of_edges = []
    self.our_user = ''
    self.document_readers_dict = {}
    self.read_by_visitor_dict = {}
  
  def build_document_readers(self,line, document_UUID):
    """Build the doucment readers dictionary

    :param line: The JSON line to processes
    :type line: JSON
    :param document_UUID: document ID to check agaisnt JSON line to make sure the vistor read the document
    :type document_UUID: string
    """
    try:
      if document_UUID == line['env_doc_id']:
        self.document_readers_dict[line['visitor_uuid']] = 1
    except KeyError:
      pass
    
  def build_read_by_visitor(self, line, visitor_UUID=None):
    """Build the read by visitor dictionary 

    :param line: The JSON line to processes
    :type line: JSON
    :param visitor_UUID: Visitor ID checking they are in our document readers dicitonary (the document we are looking for also likes matches)
    thus are of interset, defaults to None
    :type visitor_UUID: string, optional
    """
  
    our_user = visitor_UUID
   
    # If input reader is given, don't count them
    if our_user != line['visitor_uuid']:
      if line['visitor_uuid'] in self.document_readers_dict and line['event_type'] == 'pageread': 
        try:
          self.read_by_visitor_dict[line['env_doc_id']] += 1
          result = ( line['visitor_uuid'][-4:], line['env_doc_id'][-4:])
        except KeyError:
          self.read_by_visitor_dict[line['env_doc_id']] = 1
          result = (line['visitor_uuid'][-4:], line['env_doc_id'][-4:])
        
        # Create edges for dot graph
        if result not in self.list_of_edges:
          self.list_of_edges.append(result)
      
          
  def get_document_readers_dict(self):
    """ Returns the document readers dict

    :return: document_readers_dict
    :rtype: dictionary
    """
    return self.document_readers_dict
      
  def get_read_by_vistor_dict(self, sorting_function=None):
    """ Returns the read by visitor dict

    :param sorting_function: generic sorting function that can be used on the dictionary, defaults to None
    :type sorting_function: function, optional
    :return: If a sorting function is provided, returns the data provided by the sorting function
             otherwise returns read by visitor dictionary
    :rtype: sorting_function return type / dictionary
    """
    if sorting_function is not None:
      return sorting_function()
    else:
      return self.read_by_visitor_dict
      
  def top_ten(self):
    """ top ten sorting function

    :return: Top 10 also liked documents
    :rtype: list
    """
    return heapq.nlargest(10, self.read_by_visitor_dict, key=self.read_by_visitor_dict.get)  