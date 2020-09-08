from multiprocessing import Pool

all_results = [ ]

pool = Pool()
results = pool.imap(get_mutation_info_from_pdb, all_inputs)

for i, result in enumerate(results):
    all_results.extend(result) # result is a expected to be a list
    sys.stdout.write("\r%6d/%d %s"%(i+1,len(all_inputs),all_inputs[i].ljust(8)))
    sys.stdout.flush()
sys.stdout.write("\n")
