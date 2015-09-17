Title:  Servermon flake8 compliant
Date:   2015-09-17 14:39:08
Category: servermon
Tags: servermon, monitoring, puppet, django

Servermon has almost full flake8 compliance. In a pretty big commit:
<a href="https://github.com/servermon/servermon/commit/b4dfd58a85ab52aaf57a2c360a94ea190065459f">b4dfd58</a>
we 've reached almost full compliance. The one error ignored is E501
(line too long) which did not seem worthy to fight for. So, now
patches/PRs to servermon need to keep code style, pass the tests and
not make code coverage significantly worse to be accepted
