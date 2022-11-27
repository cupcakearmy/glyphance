jsonschema:
	rm -rf docs/config
	mkdir -p tmp docs/config
	cat src/assets/config.schema.yaml | python3 -c 'import yaml; import json; import sys; print(json.dumps(yaml.safe_load(sys.stdin)));' > tmp/glyphance.schema.json
	pnpm dlx @adobe/jsonschema2md --input tmp --out docs/config
	rm -r out
	rm -r tmp

docker:
	docker build -t glyphance .
