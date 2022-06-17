import tabula
import fitz # PyMuPDF
import io
from PIL import Image
import detectron2
import Multi_Type_TD_TSR.google_colab.deskew as deskew
import Multi_Type_TD_TSR.google_colab.table_detection as table_detection
import Multi_Type_TD_TSR.google_colab.table_structure_recognition_all as tsra
import Multi_Type_TD_TSR.google_colab.table_structure_recognition_lines as tsrl
import Multi_Type_TD_TSR.google_colab.table_structure_recognition_wol as tsrwol
import Multi_Type_TD_TSR.google_colab.table_structure_recognition_lines_wol as tsrlwol
import Multi_Type_TD_TSR.google_colab.table_xml as txml
import Multi_Type_TD_TSR.google_colab.table_ocr as tocr
import pandas as pd
import os
import json
import itertools
import random
from detectron2.utils.logger import setup_logger
# import some common libraries
import numpy as np
import cv2
import matplotlib.pyplot as plt
# import some common detectron2 utilities
from detectron2 import model_zoo
from detectron2.engine import DefaultPredictor
from detectron2.config import get_cfg
from detectron2.utils.visualizer import Visualizer
from detectron2.data import MetadataCatalog
from detectron2.data import DatasetCatalog, MetadataCatalog
from google.colab.patches import cv2_imshow
setup_logger()
from pdf2image import convert_from_path
from PIL import Image
import os

##### fonction to extract the table : 

def table_extractor(path) -> list:
    """ retrun a list of dataframes with the data of the tables"""
    return(tabula.read_pdf(path, pages = "all"))

def pdf_as_table(dataframe) -> bool:
    return len(dataframe)>0


def  image_extrator(path):
  """ input : path is the path of the pdf file
      output : a list of names of all the images of the pdf file. Those images 
              have been save in the current folder to be processed buy the ORC 
  """
  pdf_file = fitz.open(path)
  # iterate over PDF pages
  images = []
  list_names = []
  for page_index in range(len(pdf_file)):
      # get the page itself
      page = pdf_file[page_index]
      image_list = page.getImageList()
      # printing number of images found in this page
      #if image_list:
          #print(f"[+] Found a total of {len(image_list)} images in page {page_index}")
      #else:
          #print("[!] No images found on page", page_index)
      images += image_list
      for image_index, img in enumerate(page.getImageList(), start=1):
         
          # get the XREF of the image
          xref = img[0]
          # extract the image bytes
          base_image = pdf_file.extractImage(xref)
          image_bytes = base_image["image"]
          # get the image extension
          image_ext = base_image["ext"]
          # load it to PIL
          image = Image.open(io.BytesIO(image_bytes))
          print(image)
          images.append(image)  
          name_image = f"image{page_index+1}_{image_index}.{image_ext}"
          list_names.append(name_image)
          #save it to local disk
  
          image.save(open(name_image, "wb"))
  return (list_names)

def model_creation(): 
  #create detectron config
  cfg = get_cfg()

  #set yaml
  cfg.merge_from_file('/content/All_X152.yaml')

  #set model weights
  cfg.MODEL.WEIGHTS = '/content/model_final.pth' # Set path model .pth

  predictor = DefaultPredictor(cfg) 
  return (predictor)

def image_is_table (image, model) -> bool: 
    """ imput is the path (name eg cat.png) of an image """
    # calculate the model to see if there are any images
    document_img = cv2.imread(image)
    table_list, table_coords = table_detection.make_prediction(document_img, model)
    # check the dimention of the array
    # if dim not null :
    if len(table_list)> 0   : 
        return True     
    # else if the dim is null the image is not a table    
    return False

def is_pdf ( path):
    if "pdf" in path : 
        return True 
    return False

def is_there_table ( path, model): 
    direct_table = False 
    table_image = False
    number_table_image = 0
    number_table_direct = 0
    names_pages = []
    # in the case we have a pdf file 
    if (is_pdf(path)):
        # etract_table (path)
        direct_table = pdf_as_table(table_extractor(path))

        #extract image 
        list_names  = image_extrator(path)  
        for image in list_names:       
          if image_is_table (image, model):
            table_image = True
            number_table_image+=1
            print("The image is a table")

        for img in list_names: 
            os.remove(img)

       
        if (table_image ==False): # deal with the case of the page 8 , like that we don't use 
                                  # the neural network if it is not necessary 
          images = convert_from_path(path)
          for i, image in enumerate(images):
              fname = 'image'+str(i)+'.png'
              image.save(fname, "PNG")
              names_pages.append(fname)
              if image_is_table (fname, model):
                table_image = True

        for img in names_pages: 
            os.remove(img)
    # in the case the file is directly a png or a jpge
    else :
        if image_is_table (path, model): # here we see if the all page contains tables 
          table_image = True
          number_table_image+=1
          print("There is a table in the document")
    if (table_image or direct_table):
      print("Congratulation you find a table" )
      return (True)
    return (False)
    print("The documents need to be either a pdf of a png or a jpeg")
