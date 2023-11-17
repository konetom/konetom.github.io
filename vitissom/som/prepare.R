#!/usr/bin/env Rscript

# IMPORTANT: If vitisSOM package is not installed yet, it will be
# automatically installed from konetom/vitisSOM repository.
# Log file called "git.log" will be created in som folder.
# Please, do not delete the log file unless you want to reinstall the vitisSOM package.

if (!require("devtools")) {
    install.packages("devtools")}
library(devtools)
install_github("konetom/vitisSOM", force = T, quiet = T)
