from pytube import YouTube
from PyQt5 import QtWidgets, uic
from PyQt5.QtWidgets import QFileDialog
import sys


class YTVideoDownloader(QtWidgets.QMainWindow):
	def __init__(self):
		super(YTVideoDownloader, self).__init__()
		uic.loadUi('forms/main.ui', self)

		self.download_btn.clicked.connect(self.download) #Download button
		self.FileExplorer_btn.clicked.connect(self.savefile) #File explorer button
		self.Path_text.setEnabled(False) #Disabling the url line edit
		## Adding download options to combo box
		self.options.addItems(["Video + Audio", "Video only", "Audio only"])

		self.show()

	def savefile(self):
		options = QFileDialog.Options()
		options |= QFileDialog.DontUseNativeDialog
		self.path = QFileDialog.getSaveFileName(self,"Save Video","","All Files (*);", options=options)
		if self.path:
			print(self.path[0])
			self.Path_text.setEnabled(True)
			self.Path_text.setText(self.path[0])
			self.Path_text.setEnabled(False)

	def set_options(self):
		option = self.options.currentText()
		return option


	def download(self):
		option = self.set_options()
		#try:
		url_text = self.Url_text.text()
		
		if url_text != '':
			if self.path[0] != "":
				## VIDEO + AUDIO DOWNLOAD 
				if option == "Video + Audio":
						try:
							url = YouTube(str(url_text))
							video = url.streams.get_highest_resolution()
							print("START DOWNLOADING")
							video.download(self.path[0])
							print("DOWNLOAD FINISHED")
							self.status.setText("Download Status: Video Ready!")
						except:
							self.status.setText("Download Status: Error has occurred :(")
					
				## AUDIO ONLY DOWNLOAD
				if option == "Audio only":
					try:
						url = YouTube(str(url_text))
						audio = url.streams.filter(only_audio=True, file_extension="mp4")[0]
						print("START DOWNLOADING")
						audio.download(self.path[0])
						print("DOWNLOAD FINISHED")
						self.status.setText("Download Status: Audio Ready!")
					except:
						self.status.setText("Download Status: Error has occurred :(")

				## VIDEO ONLY DOWNLOAD
				if option == "Video only":
					try:
						url = YouTube(str(url_text))
						video = url.streams.filter(only_video=True)[0]
						print("START DOWNLOADING")
						video.download(self.path[0])
						print("DOWNLOAD FINISHED")
						self.status.setText("Download Status: Video Ready!")
					except:
						self.status.setText("Download Status: Error has occurred :(")

				else:
					self.status.setText("Download Status: Please save the folder in a path!")
		else:
			self.status.setText("Download Status: Please insert the Url of the Video!")


if __name__ == "__main__":
	app = QtWidgets.QApplication(sys.argv)
	window = YTVideoDownloader()
	app.exec_()
