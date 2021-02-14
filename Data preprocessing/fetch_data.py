# -*- coding: utf-8 -*-

import os
import zipfile
import urllib.request
import shutil

DOWNLOAD_ROOT = "https://kern.humdrum.org/cgi-bin/ksdata?l=essen/europa/deutschl&format=recursive"
DATASET_PATH = os.path.join("Data preprocessing", "deutschl")

def fetch_melodies_data(melodies_url = DOWNLOAD_ROOT, melodies_path = DATASET_PATH):
  #Create the folder if it doesn't exist
  if not os.path.isdir(melodies_path):
    os.makedirs(melodies_path)
  zip_path = os.path.join(melodies_path, "deutschl.zip")
  # Adding a header allows us to download the dataset because the distant server
  # Verify the user agent header and rejected the urllib request
  opener = urllib.request.URLopener()
  opener.addheader('User-Agent', 'whatever')
  filename, headers = opener.retrieve(melodies_url, zip_path)
  melodies_zip = zipfile.ZipFile(zip_path)
  melodies_zip.extractall(path=melodies_path)
  melodies_zip.close()

# Download the dataset
fetch_melodies_data()

# Manage the Directory
shutil.move('./deutschl/essen/europa/deutschl', './Data preprocessing/Deutschl')