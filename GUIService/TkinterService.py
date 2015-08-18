import Tkinter;
from Tkinter import *;
import tkFileDialog

class TkinterMainInterface(object):
	mInterface       = 0;
	mOriginalPathVar = 0;
	mStorePathVar    = 0;
	mSelectMovieType = 0;

	"""docstring for TkinterMainInterface"""
	def __init__(self):
		super(TkinterMainInterface, self).__init__()
		self.mInterface = Tkinter.Tk();
		self.mInterface.title("SSMovieService")
		self.mInterface.geometry('800x600');

		# A Method: Get a Original Movie File
		def GetOriginalFile():
			self.mOriginalPathVar.set("")
			aOriginalFilePath = tkFileDialog.askdirectory(title = "Choose The Original Movie Path");
			try:
				self.mOriginalPathVar.set(aOriginalFilePath)
			except Exception, e:
				raise e
			pass

		def GetStoreFile():
			self.mStorePathVar.set("")
			aStoreFilePath = tkFileDialog.askdirectory(title = "Choose The Store Split Movies Path")
			try:
				self.mStorePathVar.set(aStoreFilePath)
			except Exception, e:
				raise e
			pass

		# First Line
		aFirstLineFrame        = Frame(self.mInterface);
		aFirstLineLabel        = Label(aFirstLineFrame, text = "The Movie File: ")
		self.mOriginalPathVar  = StringVar();
		aOriginalEntry         = Entry(aFirstLineFrame, bd = 5, textvariable = self.mOriginalPathVar);
		aGetOriginalFileButton = Button(aFirstLineFrame, text = "select", command = GetOriginalFile);
		aFirstLineLabel.pack(side = LEFT);
		aOriginalEntry.pack(fill = BOTH);
		aGetOriginalFileButton.pack(fill = BOTH);

		# Second Line
		aSecondLineFrame    = Frame(self.mInterface);
		aSecondLineLabel    = Label(aSecondLineFrame, text = "The Store File: ");
		self.mStorePathVar  = StringVar();
		aStoreEntry         = Entry(aSecondLineFrame, bd = 5, textvariable = self.mStorePathVar);
		aGetStoreFileButton = Button(aSecondLineFrame, text = "select", command = GetStoreFile)
		aSecondLineLabel.pack(side = LEFT);
		aStoreEntry.pack(fill = BOTH)
		aGetStoreFileButton.pack(fill = BOTH)

		# Third Line
		aThirdLineFrame       = Frame(self.mInterface);
		aThirdLineLabel       = Label(aThirdLineFrame, text = 'The Movie Type:');
		self.mSelectMovieType = StringVar();
		self.mSelectMovieType.set("mp4");
		aMovieOptionMenu      = OptionMenu(aThirdLineFrame, self.mSelectMovieType, "mp4", "avi", "ogv", "webm")
		aThirdLineLabel.pack(side = LEFT);
		aMovieOptionMenu.pack(fill = BOTH);

		aFirstLineFrame.pack(side = TOP, fill = BOTH)
		aSecondLineFrame.pack(side = TOP, fill = BOTH)
		aThirdLineFrame.pack(side = TOP, fill = BOTH)

	def show(self):
		self.mInterface.mainloop();
		pass


aInterface = TkinterMainInterface();
aInterface.show();