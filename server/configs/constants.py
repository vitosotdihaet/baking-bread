from yaml import safe_load


with open('configs/config.yml') as yml_cfg:
	cfg = safe_load(yml_cfg)