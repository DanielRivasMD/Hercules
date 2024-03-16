#!/bin/bash
####################################################################################################

# declarations
pyapp="hercules"
pkver="0.0.0"
devDir=$(pwd)
libDir="$HOME/.python/lib/${pyapp}"

####################################################################################################

# log
echo "\n\033[1;33mBuilding\033[0;37m...\n=================================================="

# activate development enviroment
source venv/bin/activate

# build package
python -m build

# deactivate development enviroment
deactivate

####################################################################################################

# log
echo "\n\033[1;33mInstalling\033[0;37m...\n=================================================="

# create directory & relocate
[ -d "${libDir}" ] && rm -rf "${libDir}" && mkdir "${libDir}"
cd "${libDir}"

# create & activate python enviroment
python -m venv venv
source venv/bin/activate

# install package
pip install "${devDir}/dist/${pyapp}-${pkver}-py3-none-any.whl"

# deactivate python enviroment
deactivate

####################################################################################################

# log
echo "\n\033[1;33mLinking\033[0;37m...\n=================================================="

# link executable
ln -sf "$HOME/.python/lib/${pyapp}/venv/bin/${pyapp}" "${HOME}/.python/bin"

# relocate
cd "${devDir}"

####################################################################################################
