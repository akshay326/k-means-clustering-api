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
