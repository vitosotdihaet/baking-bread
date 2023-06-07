from yaml import safe_load

def server_cfg(config_key):
	# default server configuration
	cfg = {'HOST': '0.0.0.0', 'PORT': '5000'}

	# if there's needed server configuration
	with open('configs/server.yml') as yml_cfg:
		loaded_cfg = safe_load(yml_cfg)

		if config_key in loaded_cfg:
			return loaded_cfg[config_key]

	return cfg