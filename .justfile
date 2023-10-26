####################################################################################################

_default:
  @just --list

####################################################################################################

# print justfile
@show:
  bat .justfile --language make

####################################################################################################

# edit justfile
@edit:
  micro .justfile

####################################################################################################

# aliases

####################################################################################################

# build for OSX
osx:
  #!/bin/bash
  set -euo pipefail

  # declarations
  source .just.sh

  echo "Building..."
  go build -v -o ${hercules}/excalibur/hercules

####################################################################################################

# build for linux
linux OUT:
  #!/bin/bash
  set -euo pipefail

  echo "Building..."
  env GOOS=linux GOARCH=amd64 go build -v -o {{OUT}}

####################################################################################################

# install locally
install:
  #!/bin/bash
  set -euo pipefail

  echo "Install..."
  go install
  mv -v "${HOME}/.go/bin/Hercules" "${HOME}/.go/bin/hercules"

####################################################################################################

# watch changes
watch:
  watchexec --clear --watch cmd -- 'just install; hercules pubmed'

####################################################################################################
