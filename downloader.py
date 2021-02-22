import urllib.request
from utils import Utils
from timeout import timeout

class Downloader(Utils):
    """Downloader class is a class for image download related tasks.
    It has a method to make download process verbose. It inherits
    the Utils class to use the get_naems function.
    """
    error_downloads = 0  # Variable to count errors while downloading
    correct_downloads = 0  # Variable to count downloaded images
    all_downloads = 0  # Variable to count all attempts while downloading

    def __init__(self):
        try:
            print("Started creation of object type of Downloader succesfully.")
        except Exception as exc:
            print("Error in creation of object type of Downloader.")
            print(exc)
        finally:
            print("Ended creation of object type of Downloader succesfully.\n")

    def download_info(self, full_path, mode="Small"):
        """Keyword arguments:
        full_path -- full path of the image url
        mode -- Mode to get name from different types of urls Small/64
        """
        try:
            print("Started succesfully Downloader: download_info()")
            print("Downloaded: ", self.get_names(full_path, mode=mode))
        except Exception as exc:
            print("Error in Utils: download_info")
            print(exc)
        finally:
            print("Ended succesfully Downloader: download_info()\n")
    @timeout(5)
    def download_image(self, url, save_name, verbose=True, mode="Small"):
        """Keyword arguments:
        url -- image url fow download
        save_name -- file name of the downloaded image
        verbose -- bool for more information on download
        mode -- Mode to get name from different types of urls Small/64
        """
        try:
            print("Started succesfully Downloader: download_image()")
            if verbose:
                self.download_info(url, mode)
            urllib.request.urlretrieve(url, save_name)
            # These and following incremental lines are to count
            # succesful and failed downloads in a global variable
            Downloader.correct_downloads += 1
            Downloader.all_downloads += 1
        except ValueError:
            print("Utils: download image -> URL not founded!\n", url)
            Downloader.error_downloads += 1
            Downloader.all_downloads += 1
        except Exception as exc:
            print("Error in Utils: download_image!")
            print(exc)
            Downloader.error_downloads += 1
            Downloader.all_downloads += 1
        finally:
            print("Ended succesfully Downloader: download_image()\n")

    def final_info(self):
        try:
            print("Started succesfully Downloader: final_info()")
            print("Finished downloading "
                  + str(Downloader.all_downloads)
                  + " image(s) with "
                  + str(Downloader.correct_downloads)
                  + " succesful download(s) and "
                  + str(Downloader.error_downloads)
                  + " failed download(s)!\n")
        except Exception as exc:
            print("Error in Downloader: final_info()")
            print(exc)
        finally:
            print("Ended succesfully Downloader: final_info()\n")
