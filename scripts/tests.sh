SRC_DIR=./src/python
TEST_DIR=./test/python

export PYTHONPATH=$SRC_DIR:$TEST_DIR:$PYTHONPATH
export PATH=$TEST_DIR:$PATH
export SKIPSLOW=$1

# Discover and run all tests
coverage run -m unittest discover -v -s $TEST_DIR
