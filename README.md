# Bazel Project

Install [Bazelisk](https://github.com/bazelbuild/bazelisk), a wrapper around `Bazel` that takes care of downloading the correct
version of `Bazel` for you. Bazel is an open-source build and test tool similar to Make, Maven, and Gradle.

## Install
### Windows
```
# Install chocolatey (Windows package management)
# Powershell (Run as Administrator)
Get-ExecutionPolicy
Set-ExecutionPolicy Bypass -Scope Process
Set-ExecutionPolicy Bypass -Scope Process -Force; iex ((New-Object System.Net.WebClient).DownloadString('https://chocolatey.org/install.ps1'))

# Install Bazelisk
choco install bazelisk
```

### Linux
```
sudo wget https://github.com/bazelbuild/bazelisk/releases/download/v1.15.0/bazelisk-linux-amd64
sudo mv bazelisk-linux-amd64 bazelisk
sudo cp bazelisk /usr/local/bin
```

## Concepts
Workspace: `WORKSPACE` or `WORKSPACE.bazel`. The root of the main repository, also called `@`.
Packages: `BUILD` or `BUILD.bazel`. A collection of related files and a specification of how they can be used to produce output artifacts.
Targets: A package is a container of targets. Most targets are *files* and *rules*.

## Useful Commands
```
bazelisk --version
bazelisk build //...

bazelisk test --test_output=all projects/calculator/...
cat /private/vat/tmp/_bazel_xxxxxx/.../projects/calculator_test/test.log

python -m venv .venv
source ./.venv/bin/activate

bazelisk run projects/my-python-app/...
```
