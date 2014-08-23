import os
import time
import logging
from datetime import datetime

class PyTimelapse():


    def __init__(self):
        logging.basicConfig(filename="timelapse.log", level=logging.DEBUG)
        logging.debug("PyTimelapse log started at " + self.timestamp())

        self.fileIndex = 1
        self.imageWidth = 640 # Max = 2592
        self.imageHeight = 480 # Max = 1944


    def timestamp(self):
        d = datetime.now()
        dateTimeString = "{0:02d}.{1:02d}.{2:04d} {3:02d}:{4:02d}:{5:02d}".format(d.day, d.month, d.year, d.hour, d.minute, d.second)
        return dateTimeString


    def run(self):
        while True:
            fileName = "image%05d.jpg" % self.fileIndex
            os.system("raspistill -w " + str(self.imageWidth) + " -h " + str(self.imageHeight) + " -o " + fileName +  " -sh 40 -awb auto -mm average -v")

            # Write out to log file
            logging.debug("Image '" + fileName + "' saved at " + self.timestamp())

            # Increment file index
            self.fileIndex += 1

            time.sleep(60)


if __name__ == "__main__":
    timelapse = PyTimelapse()
    timelapse.run()
