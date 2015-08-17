import Tkinter;

class TkinterMainInterface(object):
	mInterface = 0;

	"""docstring for TkinterMainInterface"""
	def __init__(self):
		super(TkinterMainInterface, self).__init__()
		self.mInterface = Tkinter.Tk();
		self.mInterface.title("SSMovieService")

	def show(self):
		self.mInterface.mainloop();
		pass


aInterface = TkinterMainInterface();
aInterface.show();