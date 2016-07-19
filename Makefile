SWAGGER="swagger-codegen/modules/swagger-codegen-cli/target/swagger-codegen-cli.jar"
DEST="tinker_partner_api/swagger_generated"

# quick build
all: generate_api

dist_build_generator:
	cd swagger-codegen && mvn clean package

rebuild_generator:
	cd swagger-codegen && mvn package -DskipTests=true

update_api_definition:
	curl -Lo partner-api-def.json https://sandbox.tinker.taxi/explorer/swagger.json

generate_api:
	rm -rf  ${DEST}
	java -jar ${SWAGGER} generate -l python -c python.config.json -i partner-api-def.json -o ${DEST}
	touch ${DEST}/__init__.py
	cp ${DEST}/README.md SWAGGER_WRAPPER.md

pip_reinstall:
	pip uninstall tinker-partner-api==0.2.0 ; pip install .

# ful build
dist: dist_build_generator update_api_definition generate_api

# without tests
quick: rebuild_generator update_api_definition generate_api

