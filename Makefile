.PHONY: jsonschema docker

jsonschema:
	rm -rf docs/config
	mkdir -p tmp docs/config
	cat src/assets/config.schema.yaml | yq > tmp/glyphance.schema.json
	pnpm dlx @adobe/jsonschema2md --input tmp --out docs/config
	rm -r out
	rm -r tmp

docker:
	docker build -t glyphance .
