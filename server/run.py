from app import app

import routes.auth
import routes.temp
import routes.goods_management


if __name__ == "__main__":
	app.run(host='0.0.0.0', port=5000)
