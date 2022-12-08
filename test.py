#Example#


test = {
    2020 : {1 : "gaming", 2 : "2gaming" },

    2021 : {1 : "chess", 2 : "2chess"}
    }

#Goes through years
for year in test:
    #Goes through each month
    for month in test[year]:

        print(test[year][month])