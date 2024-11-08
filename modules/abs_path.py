import os 

def abspath(name_file):
    return os.path.abspath(__file__ + f"/../../media/{name_file}")
