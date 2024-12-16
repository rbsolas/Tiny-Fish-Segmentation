# https://youtu.be/SQng3eIEw-k
"""
How to read a COCO JSON file to understand the structure of the data?
"""

import json
from pycocotools.coco import COCO

PATH_TO_TRAIN = "c:/Users/Rohan/datasets/coco/images/train2017" # "c:/Users/Rohan/datasets/coco/images/val2017"
PATH_TO_ANNOT = "c:/Users/Rohan/datasets/coco/annotations/instances_train2017.json" # "c:/Users/Rohan/datasets/coco/annotations/instances_val2017.json"

coco = COCO(PATH_TO_ANNOT)

# Load the JSON file
with open(PATH_TO_ANNOT, 'r') as file:
    data = json.load(file)

# Print out the first few image filenames/paths
for img in data['images'][:10]:  # Adjust the number to print more or fewer paths
    print(img['file_name'])


# Understanding the structure of JSON:
def print_structure(d, indent=0):
    """Print the structure of a dictionary or list."""
    
    # If the input is a dictionary
    if isinstance(d, dict):
        for key, value in d.items():
            print('  ' * indent + str(key))
            print_structure(value, indent+1)
            
    # If the input is a list
    elif isinstance(d, list):
        print('  ' * indent + "[List of length {} containing:]".format(len(d)))
        if d:
            print_structure(d[0], indent+1)  # Only print the structure of the first item for brevity

def get_no_annot(d, indent=0):
    """Print samples with no annotations and save text file of all the ids."""

    # Get all image_ids with annotations from annotations 
    # Turn into set
    # Get all image_ids that are not in this set 

    ids = coco.getImgIds(catIds=[])
    with_annots = []

    for annot in d["annotations"]:
        with_annots.append(annot["image_id"])
    with_annots = set(with_annots)

    no_annots = [id for id in ids if id not in with_annots]
    with open("no_annots.txt", "w") as f:
        for id in no_annots:
            f.write(f"{id}\n")
            print(id)


# print_structure(data)
get_no_annot(data)
