from MovieService.MovieSplit import SSMovieEditor;
from UploadService.GithubUpload import GithubUploadService;
from GUIService.TkinterService import TkinterInterface;
import os;
import string;


aInterface = TkinterInterface();
aInterface.show();

# aOriginalMoviePath   = input("The Original Movie Path:");
# aStoreMoviePath      = input("The Store Split Movies Path:");
# aSplitMoviesCountStr = input('The Split Movies Count:');
# aSplitMovieType      = input('The Split Movies Type(just mp4, avi, ogv, webm)')

# if os.path.exists(aOriginalMoviePath):

# 	# if Store File not Exit, create it
# 	if os.path.exists(aStoreMoviePath):
# 		os.makedirs(aStoreMoviePath);
# 		pass

# 	aSplitMoviesCount = string.atoi(aSplitMoviesCountStr);

# 	pass;


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