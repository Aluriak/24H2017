"""

usage:
    main.py <method> <data>
    main.py listen

Where <method> should be a method named after the modules find in methods/
And <data> should be a file in data/ directory containing the data
to feed the to method with.

"""

import glob
import docopt

import methods


DATA_DIR = 'data/'


if __name__ == '__main__':
    args = docopt.docopt(__doc__)
    if args['listen']:
        from ball import ball_reader
        ball_reader.laumii_protection_against_times()
        exit()
    else:
        assert '<method>' in args
        assert '<data>' in args

        expected_methods = {
            attr_name: getattr(methods, attr_name)
            for attr_name in dir(methods)
            if not attr_name.startswith('__')
        }
        expected_files = frozenset(glob.glob(DATA_DIR + '*'))
        user_fn = DATA_DIR + args['<data>']

        if args['<method>'] not in expected_methods:
            raise ValueError("It seems that methods subpackage doesn't contains"
                             "the {} submodule. Known internal modules are: {}"
                             "".format(args['<method>'], set(expected_methods.keys())))
        if user_fn not in expected_files:
            raise ValueError("It seems that data file {} does not exists. "
                             "Found data files are: {}"
                             "".format(user_fn, set(expected_files)))

        # open the file, use the method to feed it,
        # print the result
        with open(user_fn) as fd:
            result = expected_methods[args['<method>']].run(fd.read())
            print(result)
