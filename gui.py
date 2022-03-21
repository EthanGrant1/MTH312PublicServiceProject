import wx as w

class frame(w.Frame):
	def __init__(self):
		super().__init__(parent=None, title='Placeholder Name')
		self.Show()
def main():
	app = w.App()
	frame = frame()
	app.MainLoop()

if __name__ ==  "__main__":
	main()
