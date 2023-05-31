from app import app

import routes.auth.controller
import routes.goods.controller


if __name__ == "__main__":
	app.run(host='0.0.0.0', port=5000)
