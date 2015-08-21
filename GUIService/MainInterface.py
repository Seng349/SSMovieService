import Tkinter;
from Tkinter import *;
import tkFileDialog
import string;
import sys;
import tkMessageBox;

# encode
reload(sys)
sys.setdefaultencoding('utf8')

class MainInterface(object):
	mInterface            = 0;
	mOriginalPathVar      = 0;
	mStorePathVar         = 0;
	mSelectMovieType      = 0;
	mSplitMoviesCountVar  = 0;
	mCallBack             = 0;

	"""docstring for MainInterface"""
	def __init__(self):
		super(MainInterface, self).__init__()
		self.mInterface = Tkinter.Tk();
		self.mInterface.title("SSMovieService")
		self.mInterface.geometry('800x600');

		# A Method: Get a File
		def GetFilePath(title, aPathVar):
			aPathVar.set("")
			aFilePath = tkFileDialog.askdirectory(title = title);
			try:
				aPathVar.set(aFilePath);
			except Exception, e:
				raise e
			pass

		def IsSetGithubPath():
			if not cmp(aGithubSetPathCheckBoxVar.get(), "true"):
				aGithubSetPathLabel.config(state = 'normal')
				aGithubSetPathButton.config(state = 'normal')
				aGithubSetPathEntry.config(state = 'normal')
				aGithubCommitMessageLabel.config(state = 'normal')
				aGithubCommitEntry.config(state = 'normal')
				pass
			else:
				aGithubSetPathLabel.config(state = 'disabled')
				aGithubSetPathEntry.config(state = 'disabled')
				aGithubSetPathButton.config(state = 'disabled')
				aGithubCommitMessageLabel.config(state = 'disabled')
				aGithubCommitEntry.config(state = 'disabled')
				pass
			pass

		def ClickStartService():
			if self.mCallBack:
				aOriginalFilePath    = self.mOriginalPathVar.get();
				aStoreFilePath       = self.mStorePathVar.get();
				aSplitMovieCount     = string.atoi(self.mSplitMoviesCountVar.get())
				aSplitMovieType      = self.mSelectMovieType.get()
				aGithubFilePath      = ''
				aGithubCommitMessage = ''

				if not cmp(aGithubSetPathCheckBoxVar.get(), "true"):
					aGithubFilePath      = aGithubSetPathVar.get();
					aGithubCommitMessage = aGithubCommitMessageVar.get()
					pass

				self.mCallBack(aOriginalFilePath, aStoreFilePath, aSplitMovieCount, aSplitMovieType, aGithubFilePath, aGithubCommitMessage);
				pass
			pass

		# First Line
		aFirstLineFrame        = Frame(self.mInterface, bg = "#FF4040");
		aFirstLineLabel        = Label(aFirstLineFrame, text = "The Movie File: ", bg = "#FF4040")
		self.mOriginalPathVar  = StringVar();
		aOriginalEntry         = Entry(aFirstLineFrame, bd = 5, textvariable = self.mOriginalPathVar, bg = "#FF4040");
		aGetOriginalFileButton = Button(aFirstLineFrame, text = "select", command = lambda : GetFilePath("Choose The Original Movie Path", self.mOriginalPathVar), bg = "#FF4040");
		aFirstLineLabel.pack(side = LEFT, fill = X, expand = NO);
		aOriginalEntry.pack(side = LEFT, fill = X, expand = YES);
		aGetOriginalFileButton.pack(side = LEFT, fill = X, expand = NO);

		# Second Line
		aSecondLineFrame    = Frame(self.mInterface, bg = "#FF3366");
		aSecondLineLabel    = Label(aSecondLineFrame, text = "The Store File: ", bg = "#FF3366");
		self.mStorePathVar  = StringVar();
		aStoreEntry         = Entry(aSecondLineFrame, bd = 5, textvariable = self.mStorePathVar, bg = "#FF3366");
		aGetStoreFileButton = Button(aSecondLineFrame, text = "select", command = lambda : GetFilePath("Choose The Store Split Movies Path", self.mStorePathVar), bg = "#FF3366")
		aSecondLineLabel.pack(side = LEFT, fill = X, expand = NO);
		aStoreEntry.pack(side = LEFT, fill = X, expand = YES)
		aGetStoreFileButton.pack(side = LEFT, fill = X, expand = NO)

		# Third Line
		aThirdLineFrame       = Frame(self.mInterface, bg = "#FFCC00");
		aThirdLineLabel       = Label(aThirdLineFrame, text = 'The Movie Type:', bg = "#FFCC00");
		self.mSelectMovieType = StringVar();
		self.mSelectMovieType.set("mp4");
		aMovieOptionMenu      = OptionMenu(aThirdLineFrame, self.mSelectMovieType, "mp4", "avi", "ogv", "webm")
		aMovieOptionMenu.config(bg = "#FFCC00")
		aThirdLineLabel.pack(side = LEFT, fill = X, expand = NO);
		aMovieOptionMenu.pack(side = LEFT, fill = X, expand = YES);

		# Fourth Line
		aFourthLineFrame            = Frame(self.mInterface, bg = "#669900")
		aFourthLineLabel            = Label(aFourthLineFrame, text = "The Split Movies Count: ", bg = "#669900")
		self.mSplitMoviesCountVar   = StringVar();
		aSplitMoviesCountEntry      = Entry(aFourthLineFrame, bd = 5, textvariable = self.mSplitMoviesCountVar, bg = "#669900")
		aSplitMoviesCountOptionMenu = OptionMenu(aFourthLineFrame, self.mSplitMoviesCountVar, "1", "2", "3", "4", "5", "6");
		self.mSplitMoviesCountVar.set("1");
		aFourthLineLabel.pack(side = LEFT, fill = X, expand = NO);
		aSplitMoviesCountEntry.pack(side = LEFT, fill = X, expand = YES);
		aSplitMoviesCountOptionMenu.pack(side = LEFT, fill = X, expand = NO);

		# Fifth Line 
		aFifthLineFrame           = Frame(self.mInterface, bg = "#bed742")
		aGithubSetPathCheckBoxVar = StringVar();		
		aGithubSetPathCheckBoxVar.set("false")
		aGithubSetPathCheckBox    = Checkbutton(aFifthLineFrame, variable = aGithubSetPathCheckBoxVar, text = "Is Using Git to pull the split movies", onvalue = "true", offvalue = "false", command = IsSetGithubPath).grid(row = 0, sticky = W)

		# Six Line
		aSixLineFrame        = Frame(self.mInterface, bg = "#007947")
		aGithubSetPathLabel  = Label(aSixLineFrame, text = "The Git File: ")
		aGithubSetPathVar    = StringVar();
		aGithubSetPathEntry  = Entry(aSixLineFrame, bd = 5, textvariable = aGithubSetPathVar, bg = "#007947")
		aGithubSetPathButton = Button(aSixLineFrame, text = "select", command = lambda : GetFilePath("Choose The Git File", aGithubSetPathVar), bg = "#007947");
		aGithubSetPathLabel.pack(side = LEFT, fill = X, expand = NO)
		aGithubSetPathEntry.pack(side = LEFT, fill = X, expand = YES)
		aGithubSetPathButton.pack(side = LEFT, fill = X, expand = NO)
		aGithubSetPathLabel.config(state = 'disabled')
		aGithubSetPathEntry.config(state = 'disabled')
		aGithubSetPathButton.config(state = 'disabled')

		# Seven Line
		aSevenLineFrame           = Frame(self.mInterface, bg = "#007947")
		aGithubCommitMessageLabel = Label(aSevenLineFrame, text = 'The Git Commit Message:', bg = "#007947")
		aGithubCommitMessageVar   = StringVar();
		aGithubCommitEntry        = Entry(aSevenLineFrame, bd = 5, textvariable = aGithubCommitMessageVar, bg = "#007947")
		aGithubCommitMessageLabel.config(state = 'disabled')
		aGithubCommitEntry.config(state = 'disabled')
		aGithubCommitMessageLabel.pack(side = LEFT, fill = X, expand = NO)
		aGithubCommitEntry.pack(side = LEFT, fill = X, expand = YES)

		# Bottom Line
		aBottomLineFrame    = Frame(self.mInterface, bg = "#00CCFF")
		aStartServiceButton = Button(aBottomLineFrame, text = "Start Service", command = ClickStartService, bg = "#00CCFF")
		aStartServiceButton.pack(fill = BOTH)

		aFirstLineFrame.pack(side = TOP, fill = BOTH)
		aSecondLineFrame.pack(side = TOP, fill = BOTH)
		aThirdLineFrame.pack(side = TOP, fill = BOTH)
		aFourthLineFrame.pack(side = TOP, fill = BOTH)
		aFifthLineFrame.pack(side = TOP, fill = BOTH)
		aSixLineFrame.pack(side = TOP, fill = BOTH)
		aSevenLineFrame.pack(side = TOP, fill = BOTH)
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

