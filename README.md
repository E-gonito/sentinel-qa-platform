## Docker Commands

**Test:**

```bash
docker build --target builder --progress=plain .
```

Image will be built if no all tests pass, else pytest will return the FAILURES found during testing in terminal.
