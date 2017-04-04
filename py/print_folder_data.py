import os, csv


desktop = r'C:\Users\Scott\Desktop'
walk_dir = r'C:\Users\Scott\Dropbox\NBI\Vorticity\OUTPUT\Sim_0\FBXs'

#print('walk_dir = ' + walk_dir)
#print('walk_dir (absolute) = ' + os.path.abspath(walk_dir))

def get_dir_size(root):
    size = 0
    for path, dirs, files in os.walk(root):
        for f in files:
            size +=  os.path.getsize( os.path.join( path, f ) )
    return size

def print_folder_data(dir):
    emptyTimes = []
    for root, subdirs, files in os.walk(walk_dir):
        for subdir in subdirs:
            folder = os.path.join(root, subdir)
            emptyTimes.append([subdir, get_dir_size(folder), "%s files" % len(os.listdir(folder))])

            if len(os.listdir(folder)) < 1:
                print(subdir), 'WARNING! - EMPTY'
                emptyTimes.append(subdir)
    return emptyTimes

def csv_writer(data, path):
    with open(path, "rb") as csv_file:
        writer = csv.writer(csv_file, delimiter=',')
        for line in data:
            writer.writerow(line)

test= [['a','b','c'],['a','b','c'],['a','b','c'],['aasd','sdsb','sd']]

outfile = desktop + '\dataout.csv'

with open(outfile, "wb", buffering=-1) as csv_file:
    writer = csv.writer(csv_file)
    for line in print_folder_data(walk_dir):
       writer.writerow(line)


#csv_writer(print_folder_data(walk_dir), csv)
