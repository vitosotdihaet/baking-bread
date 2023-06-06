from configs.constants import cfg
from app import app

import api.routes.auth.controller
import api.routes.goods.controller
import api.error.error_register


if __name__ == '__main__':
	app.run(host=cfg['server']['HOST'], port=cfg['server']['PORT'])
