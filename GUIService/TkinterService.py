import Tkinter;
from Tkinter import *;
import tkFileDialog

class TkinterMainInterface(object):
	mInterface = 0;

	"""docstring for TkinterMainInterface"""
	def __init__(self):
		super(TkinterMainInterface, self).__init__()
		self.mInterface = Tkinter.Tk();
		self.mInterface.title("SSMovieService")
		self.mInterface.geometry('800x600');

		# A Method: Get a Original Movie File
		def GetOriginalFile():
			aOriginalPathVar.set("")
			aOriginalFilePath = tkFileDialog.askdirectory(title = "Choose The Original Movie Path");
			try:
				aOriginalPathVar.set(aOriginalFilePath)
			except Exception, e:
				raise e
			pass

		def GetStoreFile():
			aStorePathVar.set("")
			aStoreFilePath = tkFileDialog.askdirectory(title = "Choose The Store Split Movies Path")
			try:
				aStorePathVar.set(aStoreFilePath)
			except Exception, e:
				raise e
			pass

		# First Line
		aFirstLineFrame        = Frame(self.mInterface);
		aFirstLineLabel        = Label(aFirstLineFrame, text = "The Movie File: ")
		aOriginalPathVar       = StringVar();
		aOriginalEntry         = Entry(aFirstLineFrame, bd = 5, textvariable = aOriginalPathVar);
		aGetOriginalFileButton = Button(aFirstLineFrame, text = "select", command = GetOriginalFile);
		aFirstLineLabel.pack(side = LEFT);
		aOriginalEntry.pack(fill = BOTH);
		aGetOriginalFileButton.pack(fill = BOTH);

		# Second Line
		aSecondLineFrame    = Frame(self.mInterface);
		aSecondLineLabel    = Label(aSecondLineFrame, text = "The Store File: ");
		aStorePathVar       = StringVar();
		aStoreEntry         = Entry(aSecondLineFrame, bd = 5, textvariable = aStorePathVar);
		aGetStoreFileButton = Button(aSecondLineFrame, text = "select", command = GetStoreFile)
		aSecondLineLabel.pack(side = LEFT);
		aStoreEntry.pack(fill = BOTH)
		aGetStoreFileButton.pack(fill = BOTH)
		
		aFirstLineFrame.pack(side = TOP, fill = BOTH)
		aSecondLineFrame.pack(side = TOP, fill = BOTH)

	def show(self):
		self.mInterface.mainloop();
		pass


aInterface = TkinterMainInterface();
aInterface.show();