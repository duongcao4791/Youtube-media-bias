# youtube-media-bias
Python Version: 3.7

## The following steps can be used create a single node system:
```
Note: My project file Strucutre looks like this:
youtube-media-bias
|_ _youtube.py
|- -wrangle.py
|- -dataset.json
```
**1. Create Docker with official Mongo image**
macOS:
```
docker run -d -p 27017:27017 --name nodename mongo
```

**2. Create generated_data.json**
Run generate.py from youtube-media-bias folder
```
python generate.py
```

**3. Copy dataset to Docker container**
```
docker cp generated_data.json nodename:/dataset.json
```

**4. In container nodename, install pymongo**
```
pip3 install pymongo
```

**5. Import dataset to mongoDB**
the following will create a db called youtube, and populates youtube.channel with documents in dataset.json
```
mongoimport --db youtube --collection channel --file dataset.json
```
**6. Run mongo**
```
mongo
```

**7. Test a query**
```
use youtube
db.channel.find({},{"snippet.title":1})
```
## Use the following to run the Python application
**1. Open your project folder in PyCharm and run youtube.py**

Observe the console in pycharm
