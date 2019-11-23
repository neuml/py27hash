SCRIPTS_DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"
SRC_DIR=$SCRIPTS_DIR/../src/python
TEST_DIR=$SCRIPTS_DIR/../test/python

export PYTHONPATH=$SRC_DIR:$TEST_DIR:$PYTHONPATH
export PATH=$TEST_DIR:$PATH
export SKIPSLOW=$1

# Discover and run all tests
python3 -m unittest discover -v -s $TEST_DIR
