import os

import numpy as np

import pandas as pd

# parsing sites

from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor
from scrapy.loader.processors import TakeFirst, Identity
from scrapy.loader import ItemLoader
from scrapy.selector import HtmlXPathSelector, Selector

# here code for parsing

# mydataset analyse

import tensorflow as tf

def load_data(data_directory):
    directories = [d for d in os.listdir(data_directory) 
                   if os.path.isdir(os.path.join(data_directory, d))]
    labels = []
    images = []
    for d in directories:
        label_directory = os.path.join(data_directory, d)
        file_names = [os.path.join(label_directory, f) 
                      for f in os.listdir(label_directory) 
                      if f.endswith(".csv")]
        for f in file_names:
            images.append(skimage.data.imread(f))
            labels.append(int(d))
    return images, labels

ROOT_PATH = "/project/root/path"
train_data_directory = os.path.join(ROOT_PATH, "mydataset/Training")
test_data_directory = os.path.join(ROOT_PATH, "mydataset/Testing")

images, labels = load_data(train_data_directory)

# here code for data analyse

# output data
