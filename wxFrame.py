import wx

class mainFrame(wx.Frame):
	def __init__(self, *args, **kwargs):
		super(mainFrame, self).__init__(*args, **kwargs)
		self.InitUI()
	
	def InitUI(self):
		menuBar = wx.MenuBar()
		aboutMenu = wx.Menu()
		aitem = aboutMenu.Append(wx.ID_ABOUT, "&About..", "About this program")
		menuBar.Append(aboutMenu, "About")
		self.SetMenuBar(menuBar)
		
		self.Bind(wx.EVT_MENU, self.onAbout, aitem)
		
		self.SetSize((800, 400))
		self.SetTitle("Kancolle Auto Script")
		self.Show(True)
		
	def onAbout(self, e):
		wx.MessageBox('Kancolle Auto Script\nAuthor: Mammothrider', "About", wx.OK | wx.ICON_INFORMATION)


if __name__ == '__main__':

	app = wx.App()
	mainFrame(None)
	app.MainLoop()