#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Aug 15 15:09:15 2017

@author: nima
"""
import dicom
import numpy as np
import matplotlib.pyplot as plt
import sys
import os
sys.path.insert(0,'./voxelcloud/')
from voxelcloud.dicom_util import load_dicom_series_with_new_spacing

#dicom_dir = '/Users/camillezhang/Desktop/camille/100004/1.2.840.113654.2.55.174144834924218414213677353968537663991/1.2.840.113654.2.55.195946682403058845904768502826466194287'
#new_spacing_zyx = [0,0,0]
#series_uid = None
#im = load_dicom_series_with_new_spacing(dicom_dir, new_spacing_zyx, series_uid)[0]
#
#n = int(sys.argv[1])
#
#im_slice = im[n,:,:]
#
#plt.imshow(im_slice, cmap='gray')
#plt.show()
#print(im_slice)

dicom_dir = '/Users/camillezhang/Desktop/camille/100004/1.2.840.113654.2.55.174144834924218414213677353968537663991'

n = int(sys.argv[1])
for filename in os.scandir(dicom_dir):
    if filename.is_dir():
        print("true")
        path = os.path.abspath(filename)
        print(path)
        new_spacing_zyx = [0,0,0]
        series_uid = None
        im = load_dicom_series_with_new_spacing(path, new_spacing_zyx, series_uid)[0]
        im_slice = im[n,:,:]
        plt.figure()
        plt.imshow(im_slice, cmap='gray')
        plt.show()


