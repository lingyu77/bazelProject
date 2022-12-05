Install [Bazelisk](https://github.com/bazelbuild/bazelisk), a wrapper around `Bazel` that takes care of downloading the correct
version of `Bazel` for you.

### Useful commands
```
bazelisk --version

bazelisk --version
bazelisk build //...

bazelisk test projects/calculator/...
cat /private/vat/tmp/_bazel_xxxxxx/.../projects/calculator_test/test.log

python -m venv .venv
source ./.venv/bin/activate

bazelisk run projects/my-python-app/...

```
