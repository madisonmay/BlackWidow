# BlackWidow
Visualizing Python Project Import Graphs

Installation:
```
sudo pip install blackwidow
```

Demo with:
```
python -m blackwidow.web [package_name]
```

Optionally pass in a list of file patterns to exclude
```
python -m blackwidow.web [package_name] --exclude *test*
```

Sample results:

##### Requests:
![Requests Project Graph](http://i.imgur.com/RdUrRAC.png)

##### Flask:
![Flask Project Graph](http://i.imgur.com/az7huA2.png)

##### BlackWidow: 
![BlackWidow Project Graph](http://i.imgur.com/BroPIu8.png)

