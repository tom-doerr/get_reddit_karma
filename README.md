
# Get Reddit Karma

Get the current reddit karma for a user from their post page.

## Usage

Get the karma and save it to a csv file:
```
$ python main.py -u https://www.reddit.com/user/<user>/posts -o output.csv
```
You need to replace `<user>` by the username.

## Output

The output is a timestamp and a karma.

```
2020-10-13T13:58:58.619004,702
```
