import Tkinter;
from Tkinter import *;
import tkFileDialog
import string;
import sys;
import tkMessageBox;

# encode
reload(sys)
sys.setdefaultencoding('utf8')

class TkinterMainInterface(object):
	mInterface            = 0;
	mOriginalPathVar      = 0;
	mOriginalMovieTypeVar = 0;
	mStorePathVar         = 0;
	mSelectMovieType      = 0;
	mSplitMoviesCountVar  = 0;
	mCallBack             = 0;

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

		def ClickStartService():
			if self.mCallBack:
				aOriginalFilePath  = self.mOriginalPathVar.get();
				aStoreFilePath     = self.mStorePathVar.get();
				aSplitMovieCount   = string.atoi(self.mSplitMoviesCountVar.get())
				aSplitMovieType    = self.mSelectMovieType.get()
				aOriginalMovieType = self.mOriginalMovieTypeVar.get();

				print aOriginalFilePath;
				self.mCallBack(aOriginalFilePath, aStoreFilePath, aSplitMovieCount, aSplitMovieType, aOriginalMovieType);
				pass
			pass

		# First Line
		aFirstLineFrame        = Frame(self.mInterface, bg = "#FF4040");
		aFirstLineLabel        = Label(aFirstLineFrame, text = "The Movie File: ", bg = "#FF4040")
		self.mOriginalPathVar  = StringVar();
		aOriginalEntry         = Entry(aFirstLineFrame, bd = 5, textvariable = self.mOriginalPathVar, bg = "#FF4040");
		aGetOriginalFileButton = Button(aFirstLineFrame, text = "select", command = GetOriginalFile, bg = "#FF4040");
		aFirstLineLabel.pack(side = LEFT);
		aOriginalEntry.pack(fill = BOTH);
		aGetOriginalFileButton.pack(fill = BOTH);

		# Second Line
		aSecondLineFrame    = Frame(self.mInterface, bg = "#FF3366");
		aSecondLineLabel    = Label(aSecondLineFrame, text = "The Store File: ", bg = "#FF3366");
		self.mStorePathVar  = StringVar();
		aStoreEntry         = Entry(aSecondLineFrame, bd = 5, textvariable = self.mStorePathVar, bg = "#FF3366");
		aGetStoreFileButton = Button(aSecondLineFrame, text = "select", command = GetStoreFile, bg = "#FF3366")
		aSecondLineLabel.pack(side = LEFT);
		aStoreEntry.pack(fill = BOTH)
		aGetStoreFileButton.pack(fill = BOTH)

		# Third Line
		aThirdLineFrame       = Frame(self.mInterface, bg = "#FFCC00");
		aThirdLineLabel       = Label(aThirdLineFrame, text = 'The Movie Type:', bg = "#FFCC00");
		self.mSelectMovieType = StringVar();
		self.mSelectMovieType.set("mp4");
		aMovieOptionMenu      = OptionMenu(aThirdLineFrame, self.mSelectMovieType, "mp4", "avi", "ogv", "webm")
		aMovieOptionMenu.config(bg = "#FFCC00")
		aThirdLineLabel.pack(side = LEFT);
		aMovieOptionMenu.pack(fill = BOTH);

		# Fourth Line
		aFourthLineFrame            = Frame(self.mInterface, bg = "#669900")
		aFourthLineLabel            = Label(aFourthLineFrame, text = "The Split Movies Count: ", bg = "#669900")
		self.mSplitMoviesCountVar   = StringVar();
		aSplitMoviesCountEntry      = Entry(aFourthLineFrame, bd = 5, textvariable = self.mSplitMoviesCountVar, bg = "#669900")
		aSplitMoviesCountOptionMenu = OptionMenu(aFourthLineFrame, self.mSplitMoviesCountVar, "1", "2", "3", "4", "5", "6");
		self.mSplitMoviesCountVar.set("1");
		aFourthLineLabel.pack(side = LEFT);
		aSplitMoviesCountEntry.pack(fill = BOTH);
		aSplitMoviesCountOptionMenu.pack(fill = BOTH);

		# Fifth Line
		aFifthLineFrame            = Frame(self.mInterface, bg = "#006633");
		aFifthLineLabel            = Label(aFifthLineFrame, text = "The Original Movie Type: ", bg = "#006633")
		self.mOriginalMovieTypeVar = StringVar();
		aOriginalMovieTypeEntry    = Entry(aFifthLineFrame, bd = 5, textvariable = self.mOriginalMovieTypeVar, bg = "#006633")
		self.mOriginalMovieTypeVar.set("");
		aFifthLineLabel.pack(side = LEFT)
		aOriginalMovieTypeEntry.pack(fill = BOTH)

		# Bottom Line
		aBottomLineFrame    = Frame(self.mInterface, bg = "#00CCFF")
		aStartServiceButton = Button(aBottomLineFrame, text = "Start Service", command = ClickStartService, bg = "#00CCFF")
		aStartServiceButton.pack(fill = BOTH)

		aFirstLineFrame.pack(side = TOP, fill = BOTH)
		aSecondLineFrame.pack(side = TOP, fill = BOTH)
		aThirdLineFrame.pack(side = TOP, fill = BOTH)
		aFourthLineFrame.pack(side = TOP, fill = BOTH)
		aFifthLineFrame.pack(side = TOP, fill = BOTH)
		aBottomLineFrame.pack(side = BOTTOM, fill = BOTH)

	def set_callback(self, func_callback):
		self.mCallBack = func_callback;
		pass

	def showAlertView(self, aMessageStr):
		tkMessageBox.showinfo("Warning", aMessageStr);
		pass

	def show(self):
		self.mInterface.mainloop();
		pass

