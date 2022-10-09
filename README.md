# python-namespace-demo-app1

This is a `sub-command` GIT repository called `app1`

Implementation module for sub-command `app1` is `namespace_demo.app1`

**Note 1:** We have `namespace_demo.main_app1.py` to wrap CLI. We are not overwriting base module `namespace_demo.main`.

**Note 2**: main cli is still from base module `demo-cli = "namespace_demo.main_app1:cli"` so that app1 is available as sub-command
