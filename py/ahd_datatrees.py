import Grasshopper as gh

# Create a GH data tree (note the parentheses and type declaration)

dataTree = gh.DataTree[object]()


# Add the data from the nested list to the datatree

for i, v in enumerate(list):
    for d in v:
        dataTree.Add(d,gh.Kernel.Data.GH_Path(i))

# Add other stuff to the data tree using custom paths

for i in range(10):
    dataTree.Add(i,gh.Kernel.Data.GH_Path(69))
    dataTree.Add(i*5,gh.Kernel.Data.GH_Path(666))

# Return the tree to GH

ghTree = dataTree

####################
