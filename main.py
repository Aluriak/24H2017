"""

usage:

    main.py <method> <data>

Where <method> should be a method named after the modules find in algos/
And <data> should be a file in data/ directory containing the data
to feed the to method with.

"""

import docopt
import glob
import algos

DATA_DIR = 'data/'




if __name__ == '__main__':
    args = docopt.docopt(__doc__)
    assert '<method>' in args
    assert '<data>' in args

    expected_algos = frozenset(
        attr_name: getattr(attr_name)
        for attr_name in dir(algos)
        if not attr_name.startswith('__')
    )
    expected_files = frozenset(glob.glob(DATA_DIR + '*'))

    if args['<method>'] not in expected_algos:
        raise ValueError("It seems that algos subpackage doesn't contains"
                         "the {} submodule. Known internal modules are: {}"
                         "".format(args['<method>'], set(expected_algos.keys())))
    if args['<data>'] not in expected_files:
        raise ValueError("It seems that data file {} does not exists. "
                         "Found data files are: {}"
                         "".format(args['<data>'], set(expected_files)))

    # open the file, use the method to feed it,
    # print the result
    with open(args['<data>']) as fd:
        result = expected_algos[args['<method>']].run(fd.read())
        print(result)
