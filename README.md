## Docker Commands

### Standard Build

Build the image with integrated tests:

```bash
docker build --target builder -t sentinel-qa-platform:test .
```

Tests run automatically during build. The build will fail if tests don't pass.

### View Test Output

To see detailed test output during build:

```bash
docker build --target builder --progress=plain -t sentinel-qa-platform:test .
```

### Run Tests Separately (Development)

For development/debugging, you can run tests in a container:

```bash
# Build without viewing test output
docker build --target builder -t sentinel-qa-platform:test .

# Run tests interactively
docker run --rm sentinel-qa-platform:test uv run pytest -v

# Run with different options
docker run --rm sentinel-qa-platform:test uv run pytest --cov -v
```

### CI/CD

```bash
docker build --target builder --progress=plain -t sentinel-qa-platform:test .
```

The build process will exit with a non-zero code if tests fail.
