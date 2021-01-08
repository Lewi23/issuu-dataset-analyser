from tkinter import *
from tkinter import ttk
from tkinter.filedialog import askopenfilename
import errno, os, sys, re, logging
import matplotlib 
matplotlib.use('TkAgg')
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import matplotlib.pyplot as plt


def get_file_path():
  """Returns the users selected file path

  :return: Selected file path
  :rtype: String
  """
  filename = askopenfilename()
  print(filename)
  return filename
  
  
def get_generic_value(data_entry):
    """ Get the value associated with a tkinter object

    :param data_entry: Generic tkinter object
    :type data_entry: tkinter object
    :return: Tries to call .get() on the tkinter object to get the value associated with it
    :rtype: string
    """
    try:
        return data_entry.get()
    except:
        logging.error('Error getting value from object')

def build_bar_chart(dictonary, tab, label, x_size=10,y_size=5):
    """Builds a bar chart

    :param dictonary: The data to plot
    :type dictonary: dictionary
    :param tab: The tab to add the chart too
    :type tab: ttk tab
    :param label: The label for the chart
    :type label: string
    :param x_size: the size of the x axis, defaults to 10
    :type x_size: int, optional
    :param y_size: the size of the y axis, defaults to 5
    :type y_size: int, optional
    """
    
    # Splt the label after every 10th character
    labels = [re.sub("(.{20})", "\\1\n", label, 0, re.DOTALL) for label in dictonary.keys()]
    print(labels)
    
    # Create spacing between the bars
    x = (range(len(dictonary.keys())))
    new_x = [20*i for i in x]

    fig = plt.figure(figsize=(x_size, y_size))
    plt.title(label)
    plt.bar(new_x, list(dictonary.values()), align='center', width=2)
    
    # Adjust padding
    plt.xticks(new_x, labels,rotation=90)
    plt.gcf().subplots_adjust(bottom=0.5)
    
    # Set background colour
    fig.patch.set_facecolor('xkcd:light grey')
    
    # Draw the figure onto the tab
    canvas = FigureCanvasTkAgg(fig, master=tab)
    canvas.draw()
    canvas.get_tk_widget().grid(row=3, column=0)

  
  
# Soultion taken from :
# https://stackoverflow.com/questions/9532499/check-whether-a-path-is-valid-in-python-without-creating-a-file-at-the-paths-ta

# Sadly, Python fails to provide the following magic number for us.
ERROR_INVALID_NAME = 123
'''
Windows-specific error code indicating an invalid pathname.

See Also
----------
https://docs.microsoft.com/en-us/windows/win32/debug/system-error-codes--0-499-
    Official listing of all such codes.
'''

def is_pathname_valid(pathname: str) -> bool:
    '''
    `True` if the passed pathname is a valid pathname for the current OS;
    `False` otherwise.
    '''
    # If this pathname is either not a string or is but is empty, this pathname
    # is invalid.
    try:
        if not isinstance(pathname, str) or not pathname:
            return False

        # Strip this pathname's Windows-specific drive specifier (e.g., `C:\`)
        # if any. Since Windows prohibits path components from containing `:`
        # characters, failing to strip this `:`-suffixed prefix would
        # erroneously invalidate all valid absolute Windows pathnames.
        _, pathname = os.path.splitdrive(pathname)

        # Directory guaranteed to exist. If the current OS is Windows, this is
        # the drive to which Windows was installed (e.g., the "%HOMEDRIVE%"
        # environment variable); else, the typical root directory.
        root_dirname = os.environ.get('HOMEDRIVE', 'C:') \
            if sys.platform == 'win32' else os.path.sep
        assert os.path.isdir(root_dirname)   # ...Murphy and her ironclad Law

        # Append a path separator to this directory if needed.
        root_dirname = root_dirname.rstrip(os.path.sep) + os.path.sep

        # Test whether each path component split from this pathname is valid or
        # not, ignoring non-existent and non-readable path components.
        for pathname_part in pathname.split(os.path.sep):
            try:
                os.lstat(root_dirname + pathname_part)
            # If an OS-specific exception is raised, its error code
            # indicates whether this pathname is valid or not. Unless this
            # is the case, this exception implies an ignorable kernel or
            # filesystem complaint (e.g., path not found or inaccessible).
            #
            # Only the following exceptions indicate invalid pathnames:
            #
            # * Instances of the Windows-specific "WindowsError" class
            #   defining the "winerror" attribute whose value is
            #   "ERROR_INVALID_NAME". Under Windows, "winerror" is more
            #   fine-grained and hence useful than the generic "errno"
            #   attribute. When a too-long pathname is passed, for example,
            #   "errno" is "ENOENT" (i.e., no such file or directory) rather
            #   than "ENAMETOOLONG" (i.e., file name too long).
            # * Instances of the cross-platform "OSError" class defining the
            #   generic "errno" attribute whose value is either:
            #   * Under most POSIX-compatible OSes, "ENAMETOOLONG".
            #   * Under some edge-case OSes (e.g., SunOS, *BSD), "ERANGE".
            except OSError as exc:
                if hasattr(exc, 'winerror'):
                    if exc.winerror == ERROR_INVALID_NAME:
                        return False
                elif exc.errno in {errno.ENAMETOOLONG, errno.ERANGE}:
                    return False
    # If a "TypeError" exception was raised, it almost certainly has the
    # error message "embedded NUL character" indicating an invalid pathname.
    except TypeError as exc:
        return False
    # If no exception was raised, all path components and hence this
    # pathname itself are valid. (Praise be to the curmudgeonly python.)
    else:
        return True
    # If any other exception was raised, this is an unrelated fatal issue
    # (e.g., a bug). Permit this exception to unwind the call stack.
    #
    # Did we mention this should be shipped with Python already?
    

