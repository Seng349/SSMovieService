import Tkinter;
from Tkinter import *;

class TkinterMainInterface(object):
	mInterface = 0;

	"""docstring for TkinterMainInterface"""
	def __init__(self):
		super(TkinterMainInterface, self).__init__()
		self.mInterface = Tkinter.Tk();
		self.mInterface.title("SSMovieService")
		self.mInterface.geometry('800x600');

		# First Line
		aFirstLineFrame = Frame(self.mInterface);
		aFirstLineLabel = Label(aFirstLineFrame, text = "The Movie File: ", height = 60)
		aFirstLineLabel.pack(side = LEFT);
		
		aFirstLineFrame.pack(fill = BOTH)

	def show(self):
		self.mInterface.mainloop();
		pass


aInterface = TkinterMainInterface();
aInterface.show();