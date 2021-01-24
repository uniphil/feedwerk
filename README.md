# feedwerk

[Werkzeug](https://werkzeug.palletsprojects.com/) used to have an Atom/RSS feed
generator, which was pretty great, even if it didn't make the most sense as part
of the Werkzeug package.

This repository is a straight-forward extract of the [atom code](https://github.com/pallets/werkzeug/blob/0.16.1/src/werkzeug/contrib/atom.py)
from Werkzeug version `0.16.1`, including unit tests.

![Test](https://github.com/uniphil/feedwerk/workflows/Test/badge.svg?branch=main)

## install & migrate from werkzeug.contrib.atom

```py
$ pip install feedwerk
```

Rename imports `werkzeug.contrib.atom` → `feedwerk.atom`

```diff
- from werkzeug.contrib.atom import AtomFeed, FeedEntry
+ from feedwerk.atom         import AtomFeed, FeedEntry
```

## bugs & maintenance

This project exists to help kick the can of migrating atom libraries when
upgrading werkzeug, so the only goal is compatibility with `0.16.1` of
`werkzeug.contrib.atom`. No new features will be considered. Bug fixes may be
rejected if they might be relied-on by anyone still using old Werkzeug.

On the other hand, if you like the API that Werkzeug used to have for atom
feeds, please feel free to fork this project and build and improve on it! I
managed (painfully!) to retain the git history for this module and its tests,
so I think it's a good starting place :)


## work on feedwerk

### run tests

```bash
$ python -m pytest
```

### lints

```bash
$ flake8 --max-line-length=100 *.py tests feedwerk
```

---

### Acknowledgements

The atom feed generator was written by Werkzeug developers from 2007–2019. The
project history affecting this code has been retained in version control; see
[contributors](https://github.com/uniphil/feedwerk/graphs/contributors). The
full source and history of Werkzeug is available at
[palletes/werkzeug](https://github.com/pallets/werkzeug). Werkzeug and this
project are free to use under the terms of the
[BSD 3-Clause License](./LICENSE.rst).

This project is not affiliated with Werkzeug.
