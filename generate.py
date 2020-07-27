# generates approximately 1 GB of data from wrangled.json
# wrangled.json is 801 KB
import json

# opens a json file for writing and the json file to generate data from
with open('generated_data.json', 'a') as out_file, \
        open('wrangled.json', 'r') as in_file:

    for line in in_file:
        # each document in the json file will be modified 1300 times
        # note: in_file is 801KB, 1GB is approximately 801 * 1300
        for i in range(1, 1301):
            channel = json.loads(line)  # convert json string to dict

            # modify the channel
            channel["statistics"]["videoCount"] += i
            channel["statistics"]["subscriberCount"] += i
            channel["statistics"]["viewCount"] += i
            channel["snippet"]["title"] += str(i)
            channel["videos_information"]["videos_count"] += i

            # append the modified channel to a new file
            json.dump(channel, out_file)
            out_file.write("\n")
