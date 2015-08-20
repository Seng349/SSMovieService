from MovieService.MovieSplit import SSMovieEditor;
from UploadService.GithubUpload import GithubUploadService;
from GUIService.TkinterService import TkinterMainInterface;
import os;
import string;


def SplitMoviesStart(aOriginalMoviePath, aStoreMoviePath, aSplitMoviesCount, aMovieType, aOriginalMovieType):
	if not os.path.exists(aOriginalMoviePath):
		aInterface.showAlertView("The Original Movie Path can't be empty !!!")
		return;

	if not aStoreMoviePath:
		aInterface.showAlertView("The Store Movie Path can't be empty !!!")
		return;

	if aSplitMoviesCount <= 0:
		aInterface.showAlertView("The Split Movies Count can't be negative !!!");
		return;

	if cmp(aOriginalMovieType, ''):
		aInterface.showAlertView("The Original Movie Type can't be empty !!!")
		return;

	if not os.path.exists(aOriginalMoviePath):
		aInterface.showAlertView("The Original Movie Path not exit !!!");
		return;

	if not os.path.exists(aStoreMoviePath):
		os.makedirs(aStoreMoviePath);
		pass

	

	pass

aInterface = TkinterMainInterface();
aInterface.set_callback(SplitMoviesStart)
aInterface.show();




# aGithubService = GithubUploadService(aStoreMoviePath);
# aGithubService.upload('test Commit');

# for aFileName in os.listdir(aFilePath):

# 	aFileSuffix = os.path.splitext(aFileName)[1][1:]
# 	aStoreFile  = 'splitMovieFile';

# 	if cmp(aFileSuffix, 'mp4') == 0:

# 		aMovieEditor = SSMovieEditor(aFilePath + '/' + aFileName);
# 		aMovieEditor.SplitMoviesToFile(3, 'mp4', aStoreFile);

# 		pass

# 	pass