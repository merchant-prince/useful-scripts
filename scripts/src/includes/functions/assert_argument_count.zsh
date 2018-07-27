# Description:
#   The function asserts the argument count of a script
#   : assert that the provided argument count is <condition> than an expected value :
#
# Usage:
#   assert_argument_count CONDITION EXPECTED-ARGUMENT-COUNT PROVIDED-ARGUMENT-COUNT ERROR-MESSAGE
#
#   CONDITION (string):
#     less | less-equal | equal | greater | greater-equal
#
#   EXPECTED-ARGUMENT-COUNT (integer):
#     the argument count provided by the user / the real assertion count
#
#   PROVIDED-ARGUMENT-COUNT (integer):
#     the argument count provided by the script being run (normally ${#})
#
#   ERROR-MESSAGE (string):
#     the error message in case the assertion failed



function assert_argument_count()
{
  local ARGUMENT_COUNT=4

  # Check the argument count of the function
  if [[ ${#} -ne ${ARGUMENT_COUNT} ]]
  then
    echo ""
    echo "Wrong argument count provided to the assertion: ${0}."
    echo ""

    exit 127
  fi


  # boolean to check for errors
  local ERROR=0

  # message buffer
  local ERROR_MESSAGE=""

  # exit status code in case of error
  local EXIT_ERROR_STATUS=1

  case "${1}" in
    less)
      if ! [[ ${3} -lt ${2} ]];
      then
        ERROR=1
        ERROR_MESSAGE="Expected less than ${2} arguments; ${3} arguments provided."
      fi
      ;;

    less-equal)
      if ! [[ ${3} -le ${2} ]];
      then
        ERROR=1
        ERROR_MESSAGE="Expected less than, or ${2} arguments; ${3} arguments provided."
      fi
      ;;

    equal)
      if ! [[ ${3} -eq ${2} ]];
      then
        ERROR=1
        ERROR_MESSAGE="Expected ${2} arguments; ${3} arguments provided."
      fi
      ;;

    greater-equal)
      if ! [[ ${3} -ge ${2} ]];
      then
        ERROR=1
        ERROR_MESSAGE="Expected greater than, or ${2} arguments; ${3} arguments provided."
      fi
      ;;

    greater)
      if ! [[ ${3} -gt ${2} ]];
      then
        ERROR=1
        ERROR_MESSAGE="Expected greater than ${2} arguments; ${3} arguments provided."
      fi
      ;;

    *)
      echo ""
      echo "Wrong condition provided to the assertion: ${0}."
      echo ""
      ;;
  esac


  # check if any errors occured
  if [[ ${ERROR} -eq 1 ]]
  then
    echo ""
    echo "${ERROR_MESSAGE}"
    echo "${4}"
    echo ""

    exit ${EXIT_ERROR_STATUS}
  fi
}
