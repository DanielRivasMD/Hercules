# load packages
using DataFrames
using CSV
using Plots

# change directory
cd("/Users/Daniel/Factorem/PUBMEDrecord")

# load Scimago Journal database
scimago = CSV.read("Archive/Source/scimagojrDB.csv")

# replace missing values
scimago.SJR = replace(scimago.SJR, missing => "0")
# scimago[!, :SJR] = replace(scimago[:, :SJR], missing => "0")

# cast to integer
scimago[!, :SJR] = parse.(Float32, replace.(scimago[:, :SJR], "," => "."))

# author
prob = CSV.read("Data/Rivas-Carrillo_SD.csv")

# collect info
# TODO: regex interpolation
prob.Journal[1]

tgex = "Transplant"
rgex = Regex(tgex)
r = scimago[occursin.(rgex, scimago.Title), [:Rank, :Title, :SJR, Symbol("H index")]]
