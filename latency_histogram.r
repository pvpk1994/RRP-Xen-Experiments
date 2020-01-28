# ---------------------------------------
# R-Script to plot real-time measurements
# Author: Pavan Kumar Paluri
# University of Houston @ RTLAB - 2020
# ----------------------------------------

# Set the working directory 
wd_dir=setwd("/Users/pavankumarpaluri/Documents/RRP_S/tcp_ip_charts")
print(wd_dir)

# extract the csv info
latency_vector <- read.csv(file = "latency_result.csv", header = TRUE, sep = "\t")
print(latency_vector)
head(latency_vector)

# read specific columns only [1:2]
read.csv(file = "latency_result.csv", sep = "\t")[ ,1:2]

# Plotting histogram for Mean columns {RTDS, ARINC, AAF, CREDIT}

library(ggplot2)
library(plyr)
library(reshape2)

# means.barplot <- qplot(x=latency_vector$Scheduler_name,
#                        y=latency_vector$mean, position = "dodge")

# Use a bar plot instead
# pdf(file = "Latency_mean.pdf")

#-------- MEAN VALUES PLOTTING ----------
require(grDevices) # required for rainbow colors
par(mfrow=c(1,1))
barplot(latency_vector$mean, names.arg = latency_vector$Scheduler_name,
        xlab = "Scheduler", ylab = "Time (in ms)", col = rainbow(20),
        main = "Mean Latency for Xen schedulers",axes = FALSE,
        space=c(0.3,0.3,0.3,0.3), width=c(0.001,0.001,0.001,0.001) )
usr <- par("usr")
par(usr=c(usr[1:2], 30, 60))
axis(2, at=seq(30,60,10))
# dev.off()
# --------------------------------------

#------------- MEDIAN VALUE PLOTTING ------------
par(mfrow=c(1,1))
barplot(latency_vector$median, names.arg = latency_vector$Scheduler_name,
        xlab = "Scheduler", ylab = "Time (in ms)", col = rainbow(20),
        main = "Median Latency for Xen schedulers",axes = FALSE,
        space=c(0.3,0.3,0.3,0.3), width=c(0.001,0.001,0.001,0.001) )
usr <- par("usr")
par(usr=c(usr[1:2], 20, 60))
axis(2, at=seq(20,60,20))
# -------------------------------------------

#--------- MAX LATENCY PLOTTING --------------
par(mfrow=c(1,1))
barplot(latency_vector$Max, names.arg = latency_vector$Scheduler_name,
        xlab = "Scheduler", ylab = "Max Latency (in ms)", col = rainbow(20),
        main = "Max Latency for Xen schedulers",axes = FALSE,
        space=c(0.3,0.3,0.3,0.3), width=c(0.001,0.001,0.001,0.001) )
usr <- par("usr")
par(usr=c(usr[1:2], 100, 180))
axis(2, at=seq(100,180,20))
#--------------------------------------------

# print(means.barplot)
