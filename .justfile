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

####################################################################################################
# import
####################################################################################################

# config
import '.just/js.conf'

####################################################################################################
# jobs
####################################################################################################

# watch changes
watch:
  # watchexec --clear --watch

####################################################################################################
