from flask import Flask

import threading

from wheel import Wheel
from .test import main_thread

app = Flask(__name__)

wheel_1 = Wheel(1, '../gen_data/wheel_1.txt')
wheel_2 = Wheel(2, '../gen_data/wheel_2.txt')
wheel_3 = Wheel(3, '../gen_data/wheel_3.txt')
wheel_4 = Wheel(4, '../gen_data/wheel_4.txt')


@app.route("/wheels/<int:id>")
def get_wheel(id):
    wheels = [wheel_1, wheel_2, wheel_3, wheel_4]
    wheel = next((w for w in wheels if w.id == id), None)
    if wheel:
        return wheel.json()
    return {"error": "Wheel not found"}, 404

# > hostname -I
# flask --app main run --host=0.0.0.0
# > ip addr show
if __name__ == "__main__":
    # t = threading.Thread(target=main_thread)
    # t.start()
    app.run(debug=True, host="0.0.0.0")
