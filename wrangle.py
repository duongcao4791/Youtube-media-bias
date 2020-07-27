# Wrangles dataset.json
# Wrangled to remove unnecessary data regarding channel objects

import json

# opens a json file for writing and the json file to wrangle
with open('wrangled.json', 'a') as out_file, open('dataset.json', 'r') as \
        in_file:

    # convert json strings in in_file to dictionaries
    original_data = json.load(in_file)

    for channel in original_data:
        # create a dictionary containing relevant channel data
        modified_channel = {"media": channel["media"],
                            "youtube_id": channel["youtube_id"],
                            "snippet": channel["snippet"],
                            "statistics": channel["statistics"],
                            "topicDetails": channel["topicDetails"],
                            "videos_information": channel["videos_information"],
                            "language_information": channel["language_information"],
                            "bias": channel["bias"],
                            }
        
        # convert dictionary to string and append to out_file
        json.dump(modified_channel, out_file)

        out_file.write("\n")  # append new line to out_file for visuals
