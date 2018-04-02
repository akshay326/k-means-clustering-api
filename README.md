# k-means-clustering-api
Sample Python API using flask, uses PyTorch to cluster image vectors. Originally forked [from here](https://github.com/christiansafka/img2vec)

# How to use
Just make a __PUT__ request [here](http://beard-app.herokuapp.com) with base64 encoded image data using www-form-encoding. 
 
In python
```python
import http.client

conn = http.client.HTTPConnection("beard-app,herokuapp,com")

payload = "data=%2F9j%...%2F%2FZ" # This is base64 encoded

headers = {
    'Content-Type': "application/x-www-form-urlencoded"
    }

conn.request("PUT", "image_clustering", payload, headers)

res = conn.getresponse()
data = res.read()

print(data.decode("utf-8"))
```

In Javascript/AJAX
```javascript
var settings = {
  "async": true,
  "crossDomain": true,
  "url": "https://beard-app.herokuapp.com/image_clustering",
  "method": "PUT",
  "headers": {
    "Content-Type": "application/x-www-form-urlencoded"
  },
  "data": {
    "data": "/9j/4A....NpI//Z"   // This is base64 encoded
  }
}

$.ajax(settings).done(function (response) {
  console.log(response);
});
```

## Sample Result
Sample Image 

![Image of a cat](cat.jpg)

```json
[
  [
    0.8155140106062471, 
    "https://www.googleapis.com/download/storage/v1/b/python-clustering-api.appspot.com/o/images%2FFace%2F124.jpg?generation=1522585329188523&alt=media"
  ], 
  [
    0.8145577585207011, 
    "https://www.googleapis.com/download/storage/v1/b/python-clustering-api.appspot.com/o/images%2FFace%2F242.jpg?generation=1522585299229997&alt=media"
  ], 
  [
    0.7914929138145477, 
    "https://www.googleapis.com/download/storage/v1/b/python-clustering-api.appspot.com/o/images%2FFace%2F212.jpg?generation=1522584727478100&alt=media"
  ], 
  [
    0.7806927914191767, 
    "https://www.googleapis.com/download/storage/v1/b/python-clustering-api.appspot.com/o/images%2FFace%2F099.jpg?generation=1522585251917855&alt=media"
  ], 
  [
    0.6948463995381056, 
    "https://www.googleapis.com/download/storage/v1/b/python-clustering-api.appspot.com/o/images%2FFace%2F119.jpg?generation=1522584693369035&alt=media"
  ]
]
```

