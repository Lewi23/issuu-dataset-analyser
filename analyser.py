import sys, os
from argparse import ArgumentParser
from application.ui import main
from application.analysis import analysis_manager as am


if not len(sys.argv) > 1:
  #Run GUI
  main.start_app(False)
else:
  #Run CLI

  parser = ArgumentParser()
  # Create arguements
  parser.add_argument("-u", "--user", dest="user_uuid",
                      help="the user ID")
  parser.add_argument("-d", "--doc", dest="doc_uuid",
                      help="the document ID")
  parser.add_argument("-t", "--task", dest="task_id",
                      help="the task id")
  parser.add_argument("-f", "--file", dest="file_path",
                      help="the file path of the data")
  args = parser.parse_args()
  args_dict = vars(args)
  
  # Store values from args
  user_uuid = args_dict['user_uuid']
  doc_uuid = args_dict['doc_uuid']
  task_id = args_dict['task_id']
  file_path = args_dict['file_path']

  # Create file path from input
  path = os.getcwd()
  path = path + file_path
  manager = am.analysis_manager(path)
  
  
  def pretty_print_list(list_to_print):
    """Prints a list containing a tupe (x,y) to the same line split by a '-'

    :param list_to_print: list to be printed
    :type list_to_print: list
    """
    for x in range(len(list_to_print)):
      val1, val2 = list_to_print[x]
      print(str(val1) + ' - ' + str(val2))
      
  
  def print_list(list_to_print):
    """Prints each list element on a new line

    :param list_to_print: list_to_print
    :type list_to_print: list
    """
    for x in range(len(list_to_print)):
      print(list_to_print[x])
    
  
  def pretty_print_dict(dictonary):
    """Print a dictionary, witch each record on a new line

    :param dictonary: dictionary to print
    :type dictonary: dictionary
    """
    output = list(dictonary.items())
    
    for x in range(len(output)):
      val1, val2 = output[x]
      print(str(val1) + ' - ' + str(val2))
      
  # Run and print the results of CLI input
  if(task_id == '1'):
    manager.process_data(doc_uuid, 'country')
    print()
    print('Country - Number of views')
    pretty_print_dict(manager.views_by_location.get_country_dict())  
  elif(task_id == '2'):
    manager.process_data(doc_uuid, 'continent')
    print()
    print('Continent - Number of views')
    pretty_print_dict(manager.views_by_location.get_continent_dict())
  elif(task_id == '3'):
    manager.process_data(flag='browser_verbose')
    print()
    print('Browsers Verbose - Entries')
    pretty_print_dict(manager.views_by_browser.get_view_by_browser_verbose_dict())
  elif(task_id == '4'):
    manager.process_data(flag='browser')
    print()
    print('Browsers - Entries')
    pretty_print_dict(manager.views_by_browser.get_views_by_browser_dict())
  elif(task_id == '5'):
    manager.process_data(flag='reader_profiles')
    print()
    print("Top ten readers - Read time (ms)")
    pretty_print_list(manager.reader_profiles.top_ten_readers())
  elif(task_id == '6'):
    manager.process_data(doc_uuid,flag='also_likes')
    manager.process_data(doc_uuid,flag='vistor_uuid')
    print()
    print('Top ten also liked documents')
    print_list(manager.also_likes.get_read_by_vistor_dict(sorting_function=manager.also_likes.top_ten))
  elif(task_id == '7'):
    main.start_app(True, user_uuid, doc_uuid, path)

    
  
  

      



