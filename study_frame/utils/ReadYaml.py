import yaml

class YamlHander:
    def __init__(self, filename=r'D:\dome\newuitest\study_frame\data\data.yml'):
        self.filename = filename

    # def write_yaml(token):
    #     t_data = {"token": token}
    #     with open("../common/token.yml", "w", encoding="utf-8") as f:
    #         yaml.dump(data=t_data, stream=f, allow_unicode=True)

    def read_yaml(self):
        with open(self.filename, 'r', encoding='utf-8') as f:
            result = yaml.load(f.read(), Loader=yaml.FullLoader)
        username1 = result["USERNAME1"]
        password1 = result["PASSWORD1"]
        print(username1)
        print(password1)
        return username1, password1

if __name__ == '__main__':
    YamlHander().read_yaml()