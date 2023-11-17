#!/usr/bin/env Rscript

## Install packages if missing and load them
if(!require("readr")){install.packages("readr")}
if(!requireNamespace("BiocManager")){install.packages("BiocManager")}
if(!require("stringr")){BiocManager::install("stringr")}
if(!require("biomaRt")){BiocManager::install("biomaRt")}
if(!require("oposSOM")){BiocManager::install("oposSOM")}
library(readr)
library(stringr)
library(biomaRt)
library(oposSOM)

## Read input data
data <- read.csv("input/SOM_input.csv")
rownames(data) <- data$Gene.ID
data <- data[,-which(colnames(data) %in% c("Gene.ID"))]

## Define data group labels:
colnames_splitted <- strsplit(sub("_r", "\01", colnames(data)), "\01")
group_labels <- vector()
for (lab in colnames_splitted){group_labels <- c(group_labels, lab[1])}

# Prepare environment
env <- opossom.new(list(database.dataset="auto",  dim.1stLvlSom="auto", spot.threshold.modules=0.9, spot.threshold.groupmap=0.85))
env$indata <- data
env$group.labels <- group_labels

# Run the analysis
opossom.run(env)
