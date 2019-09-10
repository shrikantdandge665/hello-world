from cx_Freeze import setup , Executable
setup(name="proj",
	  version= "1.0",
	  description = "project for bank database",
	  executables= [Executable(r"c:\project python\proj.py")]
	  )