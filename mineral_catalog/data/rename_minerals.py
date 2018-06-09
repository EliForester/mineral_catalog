import os
import json


class ChangeNames:
    def __init__(self):
        self.img_path = '../assets/images'
        self.data_path = 'minerals.json'
        self.raw_data = json.load(open(self.data_path, encoding='UTF-8'))
        self.all_names = [line['name'] for line in self.raw_data]
        self.all_files = os.listdir(self.img_path)

    def change_names(self):
        for name in self.all_names:
            for filename in self.all_files:
                num_matches = 0
                match_rate = 0
                filename_nojpg = filename.split('.')[0]
                if name != filename_nojpg:
                    if len(name) == len(filename_nojpg):
                            for i in range(len(name)):
                                if name[i] == filename_nojpg[i]:
                                    num_matches += 1
                    match_rate = num_matches/len(name)
                    if match_rate >= 0.9:
                        print('Changing value: {} {} {}'.format(
                            name, filename_nojpg, match_rate))
                        new_filename = name + '.jpg'
                        os.rename(self.img_path + '/' + filename,
                                  self.img_path + '/' + new_filename)


if __name__ == '__main__':
    a = ChangeNames()
    a.change_names()
