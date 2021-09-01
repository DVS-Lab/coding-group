#!/bin/bash

maindir=/data/projects/istart-data
for i in `ls -1 $maindir/bids/sub-*/func/sub-*_bold.nii.gz` ; do 
	fslstats $i -R 
done