Title:  collectd_transmission
Date:   2015-09-04 14:39:08
Category: monitoring
Tags: collectd, monitoring, transmission

collectd\_transmission just got version 2.3 released today. This is a small
project I 've create to integrate the collectd monitoring server and
transmission. It allows to monitor the state of a transmission server and get
some interesting info on the usage of it. I am quite exhited about it today
since I 've managed to make it reach 100% code coverage. It is a smallish
project, around 40 lines of actual code, close to 130 including spaces and
documentation but still 100% code coverage was not easy to achieve, mostly due
to the fact that it imports collectd, a on the fly created by collectd Python
module and injected into the namespace. Which meant mock. If you have never
heard about mocking in python, well it's time you do. If you do write any kind
of tests that is. It allows you to mock out all the difficult to reproduce
modules and functionalities allowing you to unit test your own code. That means
you won't escape bugs being introduced by libraries you use, but at
least you will be able to rule out your own code faster.

Link for the coverage report at:
<a
href="https://coveralls.io/github/akosiaris/collectd_transmission">https://coveralls.io/github/akosiaris/collectd_transmission</a>

If you are interested in the project itself:

<a
href="https://pypi.python.org/pypi/collectd_transmission/">collectd_transmission
on PyPi</a>.

Yes it's on PyPI. Developed on github with readthedocs.org,
coveralls.io and travis-ci integrations.

Now getting a useful frontend to collectd might be a tad difficult. If you got
collectd pushing to a graphite instance, probably Grafana[1] is the best. If you
used RRDs and it's a single server, I use jarmon[2] and it's fine albeit slow.
That's mostly due to downloading all RRDs on every update. And it is just for
one server, its design does not allow more than one for sure. So unless it's
your toy server you are talking about, it's not for you.
Facette[3] seems to be a better alternative but it is still young.

[1] <a href="http://grafana.org/">http://grafana.org/</a>

[2] <a href="https://launchpad.net/jarmon">https://launchpad.net/jarmon</a>

[3] <a href="https://github.com/facette/facette">https://github.com/facette/facette</a>
