load("@bazel_tools//tools/build_defs/repo:http.bzl", "http_archive")
http_archive(
    name = "rules_python",
    sha256 = "bc4e59e17c7809a5b373ba359e2c974ed2386c58634819ac5a89c0813c15705c",
    strip_prefix = "rules_python-0.15.1",
    url = "https://github.com/bazelbuild/rules_python/archive/refs/tags/0.15.1.tar.gz",
)

load("@rules_python//python:pip.bzl", "pip_parse")
pip_parse(
   name = "python_deps",
   requirements_lock = "//third_party:requirements.txt",
)

load("@python_deps//:requirements.bzl", "install_deps")
install_deps()
