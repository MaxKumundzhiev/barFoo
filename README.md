# barFoo
The crawler module stands for recursive interface for `calculating page rank for a particular page (presneted by URL)`, whereas `recursive` parameter stands for `statically linked pages` to the original url.


## System Usage
```bash
usage: main.py -u URL [-d DEPTH] [--help] [--version]

optional arguments:
  -u URL, --url URL     url address to crawle (type:str required=True)
  -d DEPTH, --depth DEPTH
                        recursion depth to crawle statically linked pages (by default, only the root URL will be processed)
                        (type:ConstrainedIntValue default:1)
  --help                Print Help and Exit
  --version             show program's version number and exit
```