from cx_Freeze import setup, Executable

base = None    

executables = [Executable("no_of_prime.py", base=base)]

packages = ["os"]
options = {
    'build_exe': {    
        'packages':packages,
    },    
}

setup(
    name = "<any name>",
    options = options,
    version = "<any number>",
    description = '<any description>',
    executables = executables
)
