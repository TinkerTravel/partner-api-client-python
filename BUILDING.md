# Building this

In order to work around various quirks we use a customized version of
`swagger-codegen`, at https://github.com/wires/swagger-codegen
(branch `fix-`).

After you have check this out, you can use make to build the whole
shebang.

```sh
# build the generator
make dist_build_generator:

# update api definitions
make update_api_definition

# make api
make generate_api
```


