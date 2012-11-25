# processing.py experiments #

Get [processing.py here] (https://github.com/jdf/processing.py) to get the processing-2.0 version you should clone the repository and re-compile it on your own machine see my [blog] for details. (http://secondcomingforprocessingpy.blogspot.co.uk/2012/11/getting-started.html)

## What is processing.py ##

processing.py is a port of [processing](http://processing.org) to python based on jython and hence it can access vanilla processing libraries. The [tools folder] (https://github.com/monkstone/processing.py-examples/tree/master/tools) contains some useful [tools](https://github.com/monkstone/processing.py-examples/downloads) for processing.py _for using jEdit as an ide_. Until processing.py gets its own mode in the regular processing ide, even non linux users will find my jEdit tools be handy.  The examples demonstrate the terse syntax of python (_cf java and even regular processing in some instances_).

## Alternatives ##

[pyprocessing](http://code.google.com/p/pyprocessing/) is a pure python based implementation of processing, based on the [pyglet](http://www.pyglet.org/) games engine. I find [Eric5](http://eric-ide.python-projects.org/eric-download.html) to be an excellent ide for pyprocessing. The advantage of the pure python implementation is access to python libraries such as scipy and numpy. But this is more than outweighted by relatively poor performance, the lack of easy access to processing-2.0 features, and java libraries.

