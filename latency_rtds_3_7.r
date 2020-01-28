# ---------------------------------------
# R-Script to plot real-time measurements
# Author: Pavan Kumar Paluri
# University of Houston @ RTLAB - 2020
# ----------------------------------------
# Set the working directory 
wd_dir=setwd("/Users/pavankumarpaluri/Documents/RRP_S/tcp_ip_charts")
print(wd_dir)
# prepare for extraction
path_30<-paste(wd_dir,"/rtds_3_7_raw_result/172.23.56.93_0.99_30.log",sep="")
print(path_30)
file_read<-read.table(path_30, sep = ",")
# read the extracted file
print(file_read)

# Preprocessing Phase
# get only the 2nd column values
actual_ddlns<- file_read[, 2:ncol(file_read)]
print(actual_ddlns)

# subtract current ddl with prev ddl to obtain diff in ddl
ddl_subtract_res <- diff(actual_ddlns)
print(ddl_subtract_res)

# omit the non -ve vals from the array
ddl_subtract_res <- ddl_subtract_res[ddl_subtract_res >= 0]
print(ddl_subtract_res)

# Caluculate the latency stats {mean, median}
mean_result <- mean(ddl_subtract_res)
median_result <- median(ddl_subtract_res)
max_res <- max(ddl_subtract_res)

# gather everything into one vector
total_res <- data.frame("Scheduler_name"="rtds", "mean" = mean_result,
                        "median" = median_result, "Max"= max_res)

print(total_res)

# writing to the file
write.table(total_res, file="latency_result.csv", row.names = FALSE, col.names = FALSE, sep = "\t", append = TRUE)

