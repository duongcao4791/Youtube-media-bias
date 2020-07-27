1. Project Description
This application is intended to be used as a way of checking the media bias of various Youtube channels. To be particular, this application is meant to help users analyze details regarding left and right wing channels, the political bias of the most popular channels, and to allow them to add, delete and update channels in a user friendly manner.
2. Project Successes
● While we ran into a major issue with the original dataset not being uploaded into mongos, we found that it was an issue with a document exceeding 16MB, and were successfully able to wrangle the data to workable size.
● Ran into multiple issues trying to connect a replicated sharded server to the python driver. After multiple attempts to create a replicated sharded server with both AWS and our local machines, we were able to get AWS to work successfully with our application.
● Successfully deployed each function remotely with the AWS server
○ Only one person had to deploy the cluster for it to work for everyone
3. Unexpected Events
● Documents exceeding 16MB
○ Description: Importing the dataset as retrieved failed as some documents
exceeded the 16MB size limit. Upon closer analysis of the data, unnecessary
fields were found (ie. data regarding captioning).
○ Solution: To address this, the original data was wrangled such that documents
contained only data of use to the application. This data is detailed in the
“DataSet” section.
● Wrangled dataset below 1GB
○ Description: The original dataset found was 2.62 GB. After failing to import the file, documents were found to be over 16MB. To address that problem, the data was wrangled but resulted in a 801 KB file.
○ Solution: Each document in the 801 KB file was used to generate 1300 more documents with slight changes to the name, subscriber count, view count, and video count. The process is detailed in the section “DataSet.”
Final Report
● Connecting Amazon AWS to Python driver
○ Description: Instances were not connecting with the python driver, and the issue
had to do with ports and who can connect to them
○ Solution: Altered mongo.conf file within instance, changed BindIp: 127.0.0.1 to
BindIp: 0.0.0.0, and changed instance security settings to accept all incoming ports. When executing servers, added --bind_ip_all to accept all incoming requests.
4. DataSet
Data Source​: ​https://www.kaggle.com/yoandinkov/youtubepoliticalbias
The 2.62 GB dataset contains information regarding youtube channels (subscriber count, video
count, view count etc) and their media bias.
Data was wrangled using the Python library, “json”.
