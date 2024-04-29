# Configuring

How to configure your application with "pyunite.json"

## General structure

It's literally just json.

## Input files

Input files are stored under the `files` key as a list of glob patterns.
for example, if you wanted to include some files you'd just add them like this:
```json
{
    "files": [
        "./src/main.py",
        "./src/performanceLowerer.py",
        "./src/magic.py"
    ]
}
```
You could also add all the files in a folder, or just the python files like this:
```json
{
    "files": [
        "./src/**/*.py",
        "./include/*"
    ]
}
```
This will include all files in the `include` folder, And all `.py` files in the `src` folder.

You can also exclude files based of glob patterns, This is how that might look:
```json
{
    "files": [
        "./src/*"
    ],
    "exclude": [
        "./src/test/*"
    ]
}
```
This will include all files from the src folder but will not include the test files in the test directory, even though they are in the src directory.

## Output file

The output file, yes the there can only be one, is defined as the `outputFile` key in the `pyunite.json` file.

## Example

Here's an example of how a `pyunite.json` could realistically look:
```json
{
    "outputFile": "pyunite.py",
    "files": [
        "./src/pyunite/"
    ]
}
```
