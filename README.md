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

Once the visualization is displayed, you can inspect file names by hovering over a node.  

# Sample results:

## Flask:
![Flask Project Graph](http://i.imgur.com/az7huA2.png)

## Django 
![Django Project Graph](http://i.imgur.com/54W6LDu.png)

## Requests:
![Requests Project Graph](http://i.imgur.com/RdUrRAC.png)

## BlackWidow: 
![BlackWidow Project Graph](http://i.imgur.com/BroPIu8.png)
