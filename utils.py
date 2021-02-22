import urllib.request
import os


class Utils:
    """Utils is a class for utility functions to change and get names of
    urls. It also has a function to check if a directory exists and create
    one if it does not exist.
    """
    def __init__(self):
        try:
            print("Started creation of object type of Utils succesfully.")
        except Exception as exc:
            print("Error in creation of object type of Utils.")
            print(exc)
        finally:
            print("Ended creation of object type of Utils succesfully.\n")

    def replace_names(self, full_path):
        """This method is to change the related part of the url to
        download true sized images. Otherwise provided urls only refer
        to small sized images. By replacing 64 and 64-1 to DHQ and DHQ-1,
        and replacing Zoom and Small to DefaultHQ one can reach original
        sized images.


        Keyword arguments:
        full_path -- full path of the image url
        """
        try:
            print("Started succesfully Utils: replace_names()")
            if full_path.find('Zoom') != -1:
                return full_path.replace("Zoom", "DefaultHQ")
            elif full_path.find('Small') != -1:
                return full_path.replace("Small", "DefaultHQ")
            elif full_path.find('64.jpg') != -1:
                return full_path.replace("64.jpg", "DHQ.jpg")
            elif full_path.find('64-1.jpg') != -1:
                return full_path.replace("64-1.jpg", "DHQ-1.jpg")
            else:
                return full_path
        except Exception as exc:
            print("Error in Utils: replace_names!")
            print(exc)
        finally:
            print("Ended succesfully Utils: replace_names()\n")

    def get_names(self, full_path, mode="Small"):
        """This method is to get a suitable image name from the
        provided url.


        Keyword arguments:
        full_path -- full path of the image url
        mode -- Mode to get name from different types of urls Small/64
        """
        try:
            print("Started succesfully Utils: get_names()")
            if mode == "Small":
                # In urls which includes Small, DefaultHQ or Zoom
                # keywords have the image name after the first "jpg"
                # encounter in the url. Thus getting the name would
                # require one to take the string after the first "jpg"
                # encounter in the url.
                return full_path[full_path.find("jpg")+3:]
            elif mode == "64":
                # In urls which includes 64 or 64-1 keywords don't
                # have a predefined image name. Thus we take the last
                # 20 characters to name the image. However, this strings
                # include char '/', which implies file should be stored
                # in a nested folder chain. To prevent this, we change
                # all '/' to '_'
                return full_path.replace("/", "_")[-20:]
            elif mode == "Default":
                # Default url mode to get the basename
                return os.path.basename(full_path)
            else:
                raise NameError  # mode not found is a name error
        except NameError:
            print("No mode such as " + mode + "!")
        except Exception as exc:
            print("Error in Utils: get_names!")
            print(exc)
        finally:
            print("Ended succesfully Utils: get_names()\n")

    def make_directory(self, dir_name):
        """Keyword argumnets:
        dir_name -- name of the directory to be created
        """
        try:
            print("Started succesfully Utils: make_directory()")
            if not os.path.exists(dir_name):
                os.makedirs(dir_name)
        except Exception as exc:
            print("Error in Utils: mkdir")
            print(exc)
        finally:
            print("Ended succesfully Utils: make_directory()\n")
