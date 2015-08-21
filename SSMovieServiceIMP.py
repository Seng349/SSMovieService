#!/usr/bin/python
# -*- coding: utf-8 -*-
import os, sys

from MovieService.MovieSplit import SSMovieEditor;
from UploadService.GithubUpload import GithubUploadService;
from GUIService.MainInterface import MainInterface;
import os;
import string;

def SplitMoviesStart(aOriginalMoviePath, aStoreMoviePath, aSplitMoviesCount, aMovieType, aGithubFilePath, aGithubCommitMessage):
	if not os.path.exists(aOriginalMoviePath):
		aInterface.showAlertView("The Original Movie Path can't be empty !!!")
		return;

	if not aStoreMoviePath:
		aInterface.showAlertView("The Store Movie Path can't be empty !!!")
		return;

	if aSplitMoviesCount <= 0:
		aInterface.showAlertView("The Split Movies Count can't be negative !!!");
		return;

	if not os.path.exists(aOriginalMoviePath):
		aInterface.showAlertView("The Original Movie Path not exit !!!");
		return;

	if not os.path.exists(aStoreMoviePath):
		os.makedirs(aStoreMoviePath);
		pass


	for aFileName in os.listdir(aOriginalMoviePath):
		aFilePath = ''
		if cmp(aOriginalMoviePath[len(aOriginalMoviePath) - 1:], '/')
			aFilePath = aOriginalMoviePath + aFileName;
			pass
		else:
			aFilePath = aOriginalMoviePath + '/' + aFileName;
			pass;

		aMovieEditor = SSMovieEditor(aFilePath);

		if aMovieEditor.GetIsReadSuccess():
			aMovieEditor.SplitMoviesToFile(aSplitMoviesCount, aMovieType, aStoreMoviePath)
			pass
		pass
	
	if len(aGithubFilePath) > 0:
		if len(aGithubCommitMessage) == 0:
			aInterface.showAlertView("The Github Commit Message can't be empty")
			return
		aGithubService = GithubUploadService(aGithubFilePath);
		aGithubService.upload(aGithubCommitMessage)
		pass


	pass

aInterface = MainInterface();
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