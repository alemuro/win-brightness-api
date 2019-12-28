# win-brightness-api

This repository contains a Python Flask server that exposes an API for 
changing the brightness of a Windows 10 screen (it should work on previous
versions as well).

If the brightness is equal to `0`, then it should turn off the screen.

If the brightness is above `0`, then if should turn on the screen and set the 
desired brigthness value (between 0 and 100).

## Run server

Clone repository and run the ps1 script in PowerShell.
The port listens by default on port 5000.

## API

There are two endpoints.

| Endpoint | Type  | Description                                           |
|----------|-------|-------------------------------------------------------|
| `/`      | `GET` | Acts as a healthcheck. Returns a Hello world message. |
| `/brightness/:brightness` | `GET` | Set the brightness as desired, between 0 and 100. |

## Example

```
$ curl -XGET <IP>:5000/brightness/10
10
```