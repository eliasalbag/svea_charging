import sys
if sys.prefix == '/usr':
    sys.real_prefix = sys.prefix
    sys.prefix = sys.exec_prefix = '/home/eliasalbag/KTH/sveaMasterThesis/svea_charging/install/svea_examples'
