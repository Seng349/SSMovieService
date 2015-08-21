import os;

class GithubUploadService(object):

	mGithubPath = '';

	"""docstring for GithubUploadService"""
	def __init__(self, aGithubPath):
		super(GithubUploadService, self).__init__()
		self.mGithubPath = aGithubPath;

	def upload(self, aCommitMessage):
		aGithubPath = self.mGithubPath;
		aCommitStr  = "git commit -m " + "'" + aCommitMessage + "'"
		os.system('cd $aGithubPath');
		os.system('git pull origin');
		os.system('git add ./');
		os.system(aCommitStr)
		os.system('git push origin master');

		pass
