from PIL import Image
from sklearn.metrics.pairwise import cosine_similarity
from img_to_vec import Img2Vec
import numpy as np

import os
import csv

# For each test image, we store the filename and vector as key, value in a dictionary
pics = {}


def read_from_csv():
    # reading csv file
    with open("images.csv", 'r') as csvfile:
        # creating a csv reader object
        csvreader = csv.reader(csvfile)

        # extracting each data row one by one
        for row in csvreader:
            # Ignore the first `[` and last `]` in row[1]
            pics[row[0]] = np.fromstring(row[1][1:-1], dtype=np.float_, sep=' ')

        # get total number of rows
        print("Total no. of rows: %d" % (csvreader.line_num))


def add_to_dict(pic_name):
    img2vec = Img2Vec()
    filename = os.fsdecode(pic_name)

    print("Filename is: %s" % filename)
    img = Image.open(os.path.join('.', filename))
    vec = img2vec.get_vec(img)
    pics[filename] = vec


def main():
    read_from_csv()
    pic_name = str(input("Enter relative path of the image to search?\n"))

    add_to_dict(pic_name)

    try:
        sims = {}
        for key in list(pics.keys()):
            if key == pic_name:
                continue

            sims[key] = cosine_similarity(pics[pic_name].reshape((1, -1)), pics[key].reshape((1, -1)))[0][0]

        d_view = [(v, k) for k, v in sims.items()]
        d_view.sort(reverse=True)
        for v, k in d_view[0:10]:
            print(v, k)

    except KeyError as e:
        print('Could not find filename %s' % e)

    except Exception as e:
        print(e)


if __name__ == '__main__':
    main()
