import os;

class GithubUploadService(object):

	mGithubPath = '';

	"""docstring for GithubUploadService"""
	def __init__(self, aGithubPath):
		super(GithubUploadService, self).__init__()
		self.mGithubPath = aGithubPath;

	def upload(self, aCommitMessage):
		aGithubPath = self.mGithubPath;
		os.system('cd $aGithubPath');
		os.system('git pull origin');
		os.system('git add ./');
		os.system('git commit -m "$aCommitMessage"')
		os.system('git push origin master');

		pass
