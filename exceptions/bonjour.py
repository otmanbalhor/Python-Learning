import json


class FileNotJsonFormatError(Exception):
    
    def __init__(self):
        self.message = "Vous ne pouvez mettre que des fichiers json"
        


def read_json_file(file_name):
    try:
        if not file_name.endswith('.json'):
            raise FileNotJsonFormatError
        file = open(file_name)
        print(json.load(file))
        file.close()
    except FileNotJsonFormatError as e:
        print(e.message)
    except FileNotFoundError:
        print("Attention erreur fatale")
    finally:
        print("Terminé")

read_json_file('data.json')