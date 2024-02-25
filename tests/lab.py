import os
from pathlib import Path

id_front = os.path.join(os.getcwd(), '_id_front.jpg')
id_back = os.path.join(os.getcwd(), '_id_back.jpg')
_id_front = Path(__file__).parent.joinpath('_id_front.jpg').resolve()
_id_back = Path('_id_back.jpg').resolve()
abs_id_front = r'C:\Users\admin\PycharmProjects\crawler-lab\tests\_id_front.jpg'
abs_id_back = r'C:\Users\admin\PycharmProjects\crawler-lab\tests\_id_back.jpg'

if __name__ == '__main__':
    print(str(id_front) + "\n" + str(id_back))
    print(str(_id_front) + "\n" + str(_id_back))
    print(abs_id_front + "\n" + abs_id_back)
