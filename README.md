# chorder
Finding the chords of a key

## Deploying the API using Docker

```
docker build -t chorderimage .
docker run -d --name chordcontainer -p 80:80 chorderimage
```

API now running on localhost:

```
>>> import requests
>>> requests.get('http://127.0.0.1/chorder/?root_note=F&scale=minor').json()
{'F minor': ['F minor', 'G dimished', 'G#/Ab major', 'A#/Bb minor', 'C minor', 'C#/Db major', 'D#/Eb major'], 'success': True}
```

To stop deployment:
```
docker container stop chordcontainer
```
