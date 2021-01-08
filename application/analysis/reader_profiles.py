import heapq
class reader_profiles:
  """ Impelemnts the logic to build the reader profiles 
  """
  def __init__(self):
    self.reader_profiles = {}
    
  def process_json_line(self, line):
    """Processes a single line of JSON updating the reader profiles dictionary

    :param line: Single line of JSON to be processed
    :type line: JSON
    """
    try:
      # Try to index into dict and add read time to user
      self.reader_profiles[line['visitor_uuid']] += line['event_readtime']
    except KeyError:
      try:
        # User doesn't exist so create record with current read time value
        self.reader_profiles[line['visitor_uuid']] = line['event_readtime']
      except KeyError:
        # Could not procsess the vistor_uuid from the JSON line
        pass
  
  def top_ten_readers(self):
    """ Returns the top ten readers from the file

    :return: Top 10 readers
    :rtype: list
    """
    readers = heapq.nlargest(10, self.reader_profiles, key=self.reader_profiles.get)
    
    top_ten = []
    for x in range(len(readers)):
      top_ten.append((readers[x], self.reader_profiles[readers[x]]))
          
    return top_ten