class ReadFile:
    """ReadFile is a class for reading the lines from a given txt file.
    """
    def __init__(self):
        """Keyword argumnets:
        file_name -- path to the file wished to be read
        """
        try:
            print("Started creation of object type of ReadFile succesfully.")
        except Exception as exc:
            print("Error in creation of object type of ReadFile.")
            print(exc)
        finally:
            print("Ended creation of object type of ReadFile succesfully.\n")

    def read_txt_lines(self, file_name):
        try:
            print("Started succesfully ReadFile: read_txt_lines()")
            url_file = open(file_name, "r")
            lines = url_file.readlines()
            url_file.close()
            return lines
        except Exception as exc:
            print("Error in ReadFile: read_txt_lines()!")
            print(exc)
        finally:
            print("Ended succesfully ReadFile: read_txt_lines()\n")

    def read_from_couple(self, prename):
        try:
            print("Started succesfully ReadFile: read_from_dict()")
            save_dir = prename + "/"
            file_path = prename + ".txt"
            return save_dir, file_path

        except Exception as exc:
            print("Error in ReadFile: read_from_dict()!")
            print(exc)
        finally:
            print("Ended succesfully ReadFile: read_from_dict()\n")

    def create_couples(self, urls_path):
        try:
            print("Started succesfully ReadFile: create_dict()")
            lines = self.read_txt_lines(urls_path)
            couples_list = list()
            for line in lines:
                words = line.split(',')
                if words[1].endswith('\n'): words[1] = words[1].rstrip()
                couples_list.append(words)
            return couples_list
        except Exception as exc:
            print("Error in ReadFile: create_dict()!")
            print(exc)
        finally:
            print("Ended succesfully ReadFile: create_dict()\n")
