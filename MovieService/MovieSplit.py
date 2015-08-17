import moviepy.editor as SSMovie;
import os.path;
import os;

class SSMovieEditor(object):
	"""docstring for SSMovieEditor"""
	mMovie    = 0;
	mFileName = '';

	def __init__(self, originalMoviePath):
		super(SSMovieEditor, self).__init__()
		self.mMovie    = SSMovie.VideoFileClip(originalMoviePath);
		self.mFileName = os.path.basename(originalMoviePath);

		pass;

	""" Split Movie to sub Movies """	
	def SplitMoviesToFile(self, splitCount, fileType, storeMoviePath):
		aMovieDuration = self.mMovie.duration;
		aSplitTime     = aMovieDuration / splitCount;
		aFileName      = os.path.splitext(self.mFileName)[0];

		for i in xrange(0,splitCount):
			aBeginTime = i * aSplitTime;
			aEndTime   = 0;

			if i + 1 == splitCount:
				aEndTime = aMovieDuration;
				pass
			else:
				aEndTime = ( i + 1 ) * aSplitTime;
				pass

			aNewFileName = aFileName + '_'+ ('%d'%i);

			self.SubClipToFile(aBeginTime, aEndTime, aNewFileName, fileType, storeMoviePath)

			pass
		pass;

	# Movie Type: mp4 avi ogv webm
	def SubClipToFile(self, beginTime, endTime, subClipFileName, fileType, storeMoviePath):

		# if store file not exit, create it.
		if os.path.exists(storeMoviePath) == False:
			os.makedirs(storeMoviePath);
			pass

		if len(storeMoviePath) > 0 and cmp(storeMoviePath[len(storeMoviePath) - 1:], '/') == 1:
			storeMoviePath += '/';
			pass

		if (cmp(fileType, 'mp4') == 1 and cmp(fileType, 'avi') == 1 and cmp(fileType, 'ogv') == 1 and cmp(fileType, 'webm') == 1):
		   return;

		aMoviePath    = storeMoviePath + subClipFileName + '.' + fileType;
		aSubClipMovie = self.mMovie.subclip(beginTime, endTime);
		aSubClipMovie.write_videofile(aMoviePath);

		pass;
