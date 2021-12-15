workspace(name = "grpcio_test")

load("@bazel_tools//tools/build_defs/repo:http.bzl", "http_archive")

http_archive(
    name = "bazel_skylib",
    sha256 = "1c531376ac7e5a180e0237938a2536de0c54d93f5c278634818e0efc952dd56c",
    urls = ["https://github.com/bazelbuild/bazel-skylib/releases/download/1.0.3/bazel-skylib-1.0.3.tar.gz"],
)

load("@bazel_skylib//:workspace.bzl", "bazel_skylib_workspace")

bazel_skylib_workspace()

http_archive(
    name = "rules_python",
    sha256 = "cd6730ed53a002c56ce4e2f396ba3b3be262fd7cb68339f0377a45e8227fe332",
    urls = ["https://github.com/bazelbuild/rules_python/releases/download/0.5.0/rules_python-0.5.0.tar.gz"],
)

load("@rules_python//python:pip.bzl", "pip_install")

PYTHON_INTERPRETER = "python3.7"

pip_install(
    name = "pip_deps",
    requirements = "//:requirements.txt",
    python_interpreter = PYTHON_INTERPRETER,
)